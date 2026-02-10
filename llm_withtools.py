import ast
import json
import os
import re
import time
import anthropic
import backoff
import openai
import copy

from llm import create_client, get_response_from_llm
from prompts.tooluse_prompt import get_tooluse_prompt
from tools import load_all_tools

# Default to Opus 4.5, but can be overridden by environment variable
_DEFAULT_CLAUDE_MODEL_OPUS = 'bedrock/global.anthropic.claude-opus-4-5-20251101-v1:0'
_DEFAULT_CLAUDE_MODEL_HAIKU = 'bedrock/global.anthropic.claude-haiku-4-5-20251001-v1:0'
_DEFAULT_CLAUDE_MODEL_SONNET = 'bedrock/global.anthropic.claude-sonnet-4-5-20250929-v1:0'

def _get_claude_model():
    """Get Claude model from environment variable or use default."""
    env_model = os.getenv('CODING_AGENT_CLAUDE_MODEL')
    if env_model == 'claude_haiku_4.5' or env_model == 'claude-haiku-4-5':
        return _DEFAULT_CLAUDE_MODEL_HAIKU
    elif env_model == 'claude_sonnet_4.5' or env_model == 'claude-sonnet-4-5':
        return _DEFAULT_CLAUDE_MODEL_SONNET
    elif env_model == 'claude_opus_4.5' or env_model == 'claude-opus-4-5':
        return _DEFAULT_CLAUDE_MODEL_OPUS
    elif env_model:
        # If a full model name is provided, use it directly
        return env_model
    else:
        # Default to Opus 4.5
        return _DEFAULT_CLAUDE_MODEL_OPUS

# Use a function to get the model dynamically
# This allows the model to be changed via environment variable at runtime
class _ClaudeModel:
    """Wrapper class to make CLAUDE_MODEL work like a string but read from environment."""
    def __str__(self):
        return _get_claude_model()
    def __repr__(self):
        return f"'{_get_claude_model()}'"
    def __eq__(self, other):
        return str(self) == str(other)
    def __ne__(self, other):
        return str(self) != str(other)
    def __contains__(self, item):
        """Support 'in' operator, e.g., 'claude' in CLAUDE_MODEL"""
        return item in str(self)
    def lower(self):
        """Support .lower() method"""
        return str(self).lower()
    def upper(self):
        """Support .upper() method"""
        return str(self).upper()
    def startswith(self, prefix, start=None, end=None):
        """Support .startswith() method"""
        return str(self).startswith(prefix, start, end)
    def endswith(self, suffix, start=None, end=None):
        """Support .endswith() method"""
        return str(self).endswith(suffix, start, end)
    def split(self, sep=None, maxsplit=-1):
        """Support .split() method"""
        return str(self).split(sep, maxsplit)
    def replace(self, old, new, count=-1):
        """Support .replace() method"""
        return str(self).replace(old, new, count)

CLAUDE_MODEL = _ClaudeModel()
OPENAI_MODEL = 'o3-mini-2025-01-31'
GLM_MODEL = 'glm-4.6'

def process_tool_call(tools_dict, tool_name, tool_input):
    try:
        if tool_name in tools_dict:
            return tools_dict[tool_name]['function'](**tool_input)
        else:
            return f"Error: Tool '{tool_name}' not found"
    except Exception as e:
        return f"Error executing tool '{tool_name}': {str(e)}"

@backoff.on_exception(
    backoff.expo,
    (openai.RateLimitError, openai.APITimeoutError, anthropic.RateLimitError, anthropic.APIStatusError),
    max_time=600,
    max_value=60,
)
def get_response_withtools(
    client, model, messages, tools, tool_choice,
    logging=None, max_retry=3, retry_count=0
):
    """
    Get response from LLM with tools, with improved 429 error handling.
    
    Args:
        client: LLM client instance
        model: Model name
        messages: Message history
        tools: Tools to use
        tool_choice: Tool choice parameter
        logging: Logging function
        max_retry: Maximum number of retries
        retry_count: Current retry count (internal use)
    """
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    model = str(model) if not isinstance(model, str) else model
    
    try:
        if 'claude' in model:
            # Use higher max_tokens for Opus 4.5 to handle longer responses
            # Opus 4.5 is more capable and may need more tokens for complex tool calls
            if 'opus' in model.lower():
                max_tokens = 8192  # Higher limit for Opus 4.5
            else:
                max_tokens = 4096  # Standard limit for Haiku and other models
            
            response = client.messages.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                tool_choice=tool_choice,
                tools=tools,
            )
        elif model.startswith('o3-') or model == 'gpt-5.1-2025-11-13' or model == 'gpt-5.1-codex-mini':
            # o3 models, gpt-5.1-2025-11-13, and gpt-5.1-codex-mini use responses.create API
            response = client.responses.create(
                model=model,
                input=messages,
                tool_choice=tool_choice,
                tools=tools,
                parallel_tool_calls=False
            )
            response = response
        elif model.startswith('glm-'):
            # GLM models support OpenAI-compatible native tool calling
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools,
                tool_choice=tool_choice,
                temperature=0.2,
                max_tokens=4096,
            )
            # Convert OpenAI-style response to a consistent format
            response = response.choices[0].message
        else:
            raise ValueError(f"Unsupported model: {model}")
        return response
    except Exception as e:
        error_str = str(e)
        is_rate_limit = (
            '429' in error_str or 
            'Too many tokens' in error_str or 
            'rate limit' in error_str.lower() or
            'RateLimitError' in error_str or
            isinstance(e, (openai.RateLimitError, anthropic.RateLimitError))
        )
        
        if logging:
            logging(f"Error in get_response_withtools: {error_str}")
        
        # Handle rate limiting (429 errors) with exponential backoff
        if is_rate_limit:
            if retry_count >= max_retry:
                if logging:
                    logging(f"Max retries ({max_retry}) exceeded for rate limit error. Raising exception.")
                raise
            
            # Exponential backoff: wait 2^retry_count seconds, with a max of 120 seconds
            wait_time = min(2 ** retry_count, 120)
            if logging:
                logging(f"Rate limit error (429) detected. Waiting {wait_time} seconds before retry {retry_count + 1}/{max_retry}")
            
            time.sleep(wait_time)
            
            # Retry with incremented retry count
            return get_response_withtools(
                client, model, messages, tools, tool_choice, 
                logging, max_retry, retry_count + 1
            )
        
        # For other errors, use the original retry logic
        if max_retry > 0 and retry_count < max_retry:
            if logging:
                logging(f"Retrying after error (attempt {retry_count + 1}/{max_retry})")
            return get_response_withtools(
                client, model, messages, tools, tool_choice, 
                logging, max_retry - 1, retry_count + 1
            )

        # Hitting the context window limit
        if 'Input is too long for requested model' in error_str:
            if logging:
                logging("Input is too long for requested model. Skipping retry.")
            pass

        raise  # Re-raise the exception after logging

def check_for_tool_use(response, model=''):
    """
    Checks if the response contains a tool call.
    """
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    model = str(model) if not isinstance(model, str) else model
    
    if 'claude' in model:
        # Claude, check for stop_reason in response
        if response.stop_reason == "tool_use":
            tool_use_block = next(block for block in response.content if block.type == "tool_use")
            return {
                'tool_id': tool_use_block.id,
                'tool_name': tool_use_block.name,
                'tool_input': tool_use_block.input,
            }

    elif model.startswith('o3-') or model == 'gpt-5.1-2025-11-13' or model == 'gpt-5.1-codex-mini':
        # OpenAI o3 models, gpt-5.1-2025-11-13, and gpt-5.1-codex-mini, check for tool_calls in response
        tool_call = None
        for tool_call in response.output:
            if tool_call.type == "function_call":
                break

        if tool_call:
            return {
                'tool_id': tool_call.call_id,
                'tool_name': tool_call.name,
                'tool_input': json.loads(tool_call.arguments),
            }

    elif model.startswith('glm-'):
        # GLM models (OpenAI-compatible), check for tool_calls
        if hasattr(response, 'tool_calls') and response.tool_calls:
            # Get the first tool call
            tool_call = response.tool_calls[0]
            try:
                tool_input = json.loads(tool_call.function.arguments)
            except:
                tool_input = tool_call.function.arguments
            return {
                'tool_id': tool_call.id,
                'tool_name': tool_call.function.name,
                'tool_input': tool_input,
            }
        elif hasattr(response, 'content') and isinstance(response.content, str):
            # Fallback to manual tool calling if response is a string
            pattern = r'<tool_use>(.*?)</tool_use>'
            match = re.search(pattern, response.content, re.DOTALL)
            if match:
                tool_use_str = match.group(1).strip()
                try:
                    tool_use_dict = ast.literal_eval(tool_use_str)
                    if isinstance(tool_use_dict, dict) and 'tool_name' in tool_use_dict and 'tool_input' in tool_use_dict:
                        return tool_use_dict
                except Exception:
                    pass

    else:
        # Any other LLM, response is str, check for <tool_use> tag in response
        pattern = r'<tool_use>(.*?)</tool_use>'
        match = re.search(pattern, response, re.DOTALL)
        if match:
            tool_use_str = match.group(1).strip()
            try:
                tool_use_dict = ast.literal_eval(tool_use_str)
                if isinstance(tool_use_dict, dict) and 'tool_name' in tool_use_dict and 'tool_input' in tool_use_dict:
                    return tool_use_dict
            except Exception:
                pass

    # No tool use found
    return None

def convert_tool_info(tool_info, model=None):
    """
    Converts tool_info from Claude format to the given model's format.
    """
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    if model is not None:
        model = str(model) if not isinstance(model, str) else model
    
    if model is None or 'claude' in model:
        # should have no change
        return {
            'name': tool_info['name'],
            'description': tool_info['description'],
            'input_schema': tool_info['input_schema'],
        }
    elif model.startswith('o3-') or model == 'gpt-5.1-2025-11-13' or model == 'gpt-5.1-codex-mini':
        # o3 models, gpt-5.1-2025-11-13, and gpt-5.1-codex-mini use the same tool format
        def add_additional_properties(d):
            if isinstance(d, dict):
                if 'properties' in d:
                    d['additionalProperties'] = False
                for k, v in d.items():
                    add_additional_properties(v)
        add_additional_properties(tool_info['input_schema'])
        for p in tool_info['input_schema']['properties'].keys():
            if not p in tool_info['input_schema']['required']:
                tool_info['input_schema']['required'].append(p)
                t = copy.deepcopy(tool_info['input_schema']['properties'][p]["type"])
                if isinstance(t, str):
                    tool_info['input_schema']['properties'][p]["type"] = [t, "null"]
                elif isinstance(t, list):
                    tool_info['input_schema']['properties'][p]["type"] = t + ["null"]
                
        return {
            'type': 'function',
            'name': tool_info['name'],
            'description': tool_info['description'],
            'parameters': tool_info['input_schema'],
            "strict": True,
        }
    elif model.startswith('glm-'):
        # GLM models use OpenAI-compatible format
        tool_schema = copy.deepcopy(tool_info['input_schema'])
        # Ensure required fields exist
        if 'required' not in tool_schema:
            tool_schema['required'] = []
        
        return {
            'type': 'function',
            'function': {
                'name': tool_info['name'],
                'description': tool_info['description'],
                'parameters': tool_schema,
            }
        }
    else:
        return tool_info

def convert_block_claude(block):
    """
    Convert a single block of content from Claude into a standard format.
    """
    if isinstance(block, dict):
        block_type = block.get('type')
        text = block.get('text')
        tool_name = block.get('name')
        tool_input = block.get('input')
        tool_result = block.get('content')
    else:
        block_type = getattr(block, 'type', None)
        text = getattr(block, 'text', None)
        tool_name = getattr(block, 'name', None)
        tool_input = getattr(block, 'input', None)
        tool_result = getattr(block, 'content', None)

    text = text or ""

    if block_type == "text":
        return {
            "type": "text",
            "text": text
        }
    elif block_type == "tool_use":
        # Convert to the manual tool calling format
        return {
            "type": "text",
            "text": f"<tool_use>\n{{'tool_name': {tool_name}, 'tool_input': {tool_input}}}\n</tool_use>"
        }
    elif block_type == "tool_result":
        return {
            "type": "text",
            "text": f"Tool Result: {tool_result}"
        }
    else:
        # Fallback if we ever encounter an unknown block type
        return {
            "type": "text",
            "text": str(block)
        }

def convert_msg_history_claude(msg_history):
    """
    Convert Claude-style message history into a generic format.
    """
    new_msg_history = []
    for msg in msg_history:
        role = msg.get('role', '')
        content_blocks = msg.get('content', [])
        new_content = []

        for block in content_blocks:
            new_content.append(convert_block_claude(block))

        new_msg_history.append({
            "role": role,
            "content": new_content
        })
    return new_msg_history

def convert_msg_history_openai(msg_history):
    """
    Convert OpenAI-style message history into a generic format.
    """
    new_msg_history = []

    for msg in msg_history:
        if isinstance(msg, dict):
            role = msg.get('role', '')
            content = msg.get('content', '')

            if role == 'tool':
                new_msg = {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Tool Result: {content}",
                        }
                    ],
                }
            else:
                new_msg = {
                    "role": role,
                    "content": content,
                }
        else:
            role = getattr(msg, 'role', None)
            content = getattr(msg, 'content', None)
            tool_calls = getattr(msg, 'tool_calls', None)

            if tool_calls:
                tool_call = tool_calls[0]
                function_name = getattr(tool_call.function, 'name', '')
                function_args = getattr(tool_call.function, 'arguments', '')
                # Convert to the manual tool calling format
                new_msg = {
                    "role": role,
                    "content": [
                        {
                            "type": "text",
                            "text": f"<tool_use>\n{{'tool_name': {function_name}, 'tool_input': {function_args}}}\n</tool_use>",
                        }
                    ],
                }
            else:
                new_msg = {
                    "role": role,
                    "content": [
                        {
                            "type": "text",
                            "text": content,
                        }
                    ],
                }

        new_msg_history.append(new_msg)

    return new_msg_history

def convert_msg_history(msg_history, model=None):
    """
    Convert message history from the model-specific format to a generic format.
    """
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    if model is not None:
        model = str(model) if not isinstance(model, str) else model
    
    if model is None or 'claude' in model:
        return convert_msg_history_claude(msg_history)
    elif model.startswith('o3-') or model == 'gpt-5.1-2025-11-13' or model == 'gpt-5.1-codex-mini':
        return convert_msg_history_openai(msg_history)
    else:
        return msg_history

def chat_with_agent_manualtools(msg, model, msg_history=None, logging=print):
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    model = str(model) if not isinstance(model, str) else model
    
    # Construct message
    if msg_history is None:
        msg_history = []
    system_message = f'You are a coding agent.\n\n{get_tooluse_prompt()}'
    new_msg_history = msg_history

    try:
        # Log that we're using GLM for manual tools
        # if model.startswith('glm-'):
        #     logging(f"这里是llm_withtools.py中的chat_with_agent_manualtools函数")
        #     logging(f"[GLM Self-Modification] Using GLM model: {model} for manual tool calling")
        #     logging(f"[GLM Self-Modification] ZAI_API_KEY present: {bool(os.environ.get('ZAI_API_KEY'))}")
        
        # Load all tools
        all_tools = load_all_tools(logging=logging)
        tools_dict = {tool['info']['name']: tool for tool in all_tools}
        
        # Create client
        # logging(f"[GLM Self-Modification] Creating client for model: {model}")
        client, client_model = create_client(model)
        # logging(f"[GLM Self-Modification] Client created successfully. Client model: {client_model}")

        # Call API
        logging(f"Input: {msg}")
        # if model.startswith('glm-'):
        #     logging(f"[GLM Self-Modification] Making API call to GLM model: {client_model}")
        response, new_msg_history = get_response_from_llm(
            msg=msg,
            client=client,
            model=client_model,
            system_message=system_message,
            print_debug=False,
            msg_history=new_msg_history,
        )
        # if model.startswith('glm-'):
        #     logging(f"[GLM Self-Modification] Received response from GLM. Response length: {len(str(response))} chars")
        logging(f"Output: {response}")

        # Tool use
        tool_use = check_for_tool_use(response, model=client_model)
        while tool_use:
            # Process tool call
            tool_name = tool_use['tool_name']
            tool_input = tool_use['tool_input']
            tool_result = process_tool_call(tools_dict, tool_name, tool_input)

            # Get tool response
            tool_msg = f'Tool Used: {tool_name}\nTool Input: {tool_input}\nTool Result: {tool_result}'
            logging(tool_msg)
            response, new_msg_history = get_response_from_llm(
                msg=tool_msg,
                client=client,
                model=client_model,
                system_message=system_message,
                print_debug=False,
                msg_history=new_msg_history,
            )
            logging(f"Output: {response}")

            # Check for next tool use
            tool_use = check_for_tool_use(response, model=client_model)

    except Exception as e:
        if model.startswith('glm-'):
            logging(f"[GLM Self-Modification] ERROR in chat_with_agent_manualtools: {str(e)}")
            import traceback
            logging(f"[GLM Self-Modification] Traceback: {traceback.format_exc()}")
        raise  # Re-raise to avoid silent failures

    return new_msg_history

def chat_with_agent_glm(
        msg,
        model='glm-4.6',
        msg_history=None,
        logging=print,
    ):
    """
    Chat with GLM model using manual tool calling via text tags.
    GLM models use OpenAI-compatible API but need manual tool calling format.
    """
    # logging(f"这里是llm_withtools.py中的chat_with_agent_glm函数，入口参数msg: {msg}, model: {model}, msg_history长度: {len(msg_history) if msg_history else 0}")
    
    # Construct message
    if msg_history is None:
        msg_history = []
    system_message = f'You are a coding agent.\n\n{get_tooluse_prompt()}'
    new_msg_history = msg_history

    try:
        # Load all tools
        all_tools = load_all_tools(logging=logging)
        tools_dict = {tool['info']['name']: tool for tool in all_tools}
        print(f"这里是llm_withtools.py中的chat_with_agent_glm函数376行，all_tools: {all_tools}"+"\n")
        print(f"这里是llm_withtools.py中的chat_with_agent_glm函数377行，tools_dict: {tools_dict}"+"\n")

        # Create client
        # logging(f"[GLM Self-Modification] Creating client for model: {model}")
        client, client_model = create_client(model)
        # logging(f"[GLM Self-Modification] Client created successfully. Client model: {client_model}")

        # Call API
        print(f"这里是llm_withtools.py中的chat_with_agent_glm函数385行，Input: {msg}"+"\n")
        print(f"[GLM Self-Modification] 这里是llm_withtools.py中的chat_with_agent_glm函数386行,Making API call to GLM model: {client_model}")
        response, new_msg_history = get_response_from_llm(
            msg=msg,
            client=client,
            model=client_model,
            system_message=system_message,
            print_debug=False,
            msg_history=new_msg_history,
        )        

        print(f"这里是llm_withtools.py中的chat_with_agent_glm函数396行，response: {response}"+"\n")
        print(f"这里是llm_withtools.py中的chat_with_agent_glm函数397行，new_msg_history: {new_msg_history}"+"\n")

        # Tool use
        tool_use = check_for_tool_use(response, model=client_model)
        print(f"这里是llm_withtools.py中的chat_with_agent_glm函数402行，tool_use: {tool_use}"+"\n")

        
        while tool_use:
            # Process tool call
            tool_name = tool_use['tool_name']
            tool_input = tool_use['tool_input']
            tool_result = process_tool_call(tools_dict, tool_name, tool_input)
            print(f"这里是llm_withtools.py中的chat_with_agent_glm函数409行，在while tool_use循环中, tool_name: {tool_name}"+"\n")
            print(f"这里是llm_withtools.py中的chat_with_agent_glm函数410行，在while tool_use循环中, tool_input: {tool_input}"+"\n")
            print(f"这里是llm_withtools.py中的chat_with_agent_glm函数409行，在while tool_use循环中, tool_result: {tool_result}"+"\n")

            # Get tool response
            tool_msg = f'Tool Used: {tool_name}\nTool Input: {tool_input}\nTool Result: {tool_result}'
            logging(tool_msg)
            response, new_msg_history = get_response_from_llm(
                msg=tool_msg,
                client=client,
                model=client_model,
                system_message=system_message,
                print_debug=False,
                msg_history=new_msg_history,
            )
            print(f"这里是llm_withtools.py中的chat_with_agent_glm函数424行，在while tool_use循环中, response: {response}"+"\n")

            # Check for next tool use
            tool_use = check_for_tool_use(response, model=client_model)
            print(f"这里是llm_withtools.py中的chat_with_agent_glm函数427行，在while tool_use循环中, tool_use: {tool_use}"+"\n")

    except Exception as e:
        logging(f"[GLM Self-Modification] ERROR in chat_with_agent_glm: {str(e)}")
        import traceback
        logging(f"[GLM Self-Modification] Traceback: {traceback.format_exc()}")
        raise  # Re-raise to avoid silent failures

    print(f"这里是llm_withtools.py中的chat_with_agent_glm函数436行，函数返回值new_msg_history: {new_msg_history}"+"\n")
    return new_msg_history

def chat_with_agent_glm_native(
        msg,
        model='glm-4.6',
        msg_history=None,
        logging=print,
    ):
    """
    Chat with GLM model using native tool calling (OpenAI-compatible).
    GLM-4.6 supports native function calling via OpenAI-compatible API.
    Reference: https://open.bigmodel.cn/dev/api/normal-model/glm-4
    """
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    model = str(model) if not isinstance(model, str) else model
    
    # logging(f"这里是llm_withtools.py中的chat_with_agent_glm_native函数，入口参数msg: {msg}, model: {model}, msg_history长度: {len(msg_history) if msg_history else 0}")
    
    # Construct message
    if msg_history is None:
        msg_history = []
    new_msg_history = [
        {
            "role": "user",
            "content": msg,
        }
    ]
    
    try:
        # Create client
        client, client_model = create_client(model)
        
        # Load all tools
        all_tools = load_all_tools(logging=logging)
        tools_dict = {tool['info']['name']: tool for tool in all_tools}
        tools = [convert_tool_info(tool['info'], model=client_model) for tool in all_tools]
        
        # Call API with native tool calling
        response = get_response_withtools(
            client=client,
            model=client_model,
            messages=msg_history + new_msg_history,
            tool_choice="auto",
            tools=tools,
            logging=logging,
        )
        
        # Check for tool use
        tool_use = check_for_tool_use(response, model=client_model)
        
        while tool_use:
            # Process tool call
            tool_name = tool_use['tool_name']
            tool_input = tool_use['tool_input']
            tool_result = process_tool_call(tools_dict, tool_name, tool_input)
            
            # Add assistant's message with tool calls
            new_msg_history.append({
                "role": "assistant",
                "content": response.content,
                "tool_calls": [
                    {
                        "id": tool_use['tool_id'],
                        "type": "function",
                        "function": {
                            "name": tool_name,
                            "arguments": json.dumps(tool_input),
                        }
                    }
                ] if hasattr(response, 'tool_calls') and response.tool_calls else None,
            })
            
            # Add tool result
            new_msg_history.append({
                "role": "tool",
                "tool_call_id": tool_use['tool_id'],
                "content": str(tool_result),
            })
            
            # Call API again with tool results
            response = get_response_withtools(
                client=client,
                model=client_model,
                messages=msg_history + new_msg_history,
                tool_choice="auto",
                tools=tools,
                logging=logging,
            )
            
            # Check for next tool use
            tool_use = check_for_tool_use(response, model=client_model)
        
        # Add final response
        if hasattr(response, 'content') and response.content:
            new_msg_history.append({
                "role": "assistant",
                "content": response.content,
            })
        
    except Exception as e:
        logging(f"[GLM Self-Modification] ERROR in chat_with_agent_glm_native: {str(e)}")
        import traceback
        logging(f"[GLM Self-Modification] Traceback: {traceback.format_exc()}")
        raise

    return new_msg_history

def chat_with_agent_claude(
        msg,
        model='bedrock/us.anthropic.claude-3-5-sonnet-20241022-v2:0',
        msg_history=None,
        logging=print,
    ):
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    model = str(model) if not isinstance(model, str) else model
    
    # logging(f"这里是llm_withtools.py中的chat_with_agent_claude函数362行，入口参数msg: {msg}, model: {model}, msg_history长度: {len(msg_history) if msg_history else 0}"+"\n")
    # Construct message
    if msg_history is None:
        msg_history = []
    new_msg_history = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": msg,
                }
            ],
        }
    ]

    try:
        # Create client
        client, client_model = create_client(model)

        # Load all tools
        all_tools = load_all_tools(logging=logging)
        tools_dict = {tool['info']['name']: tool for tool in all_tools}
        print(f"这里是llm_withtools.py中的chat_with_agent_claude函数456行，tools_dict: {tools_dict}"+"\n")
        tools = [convert_tool_info(tool['info'], model=client_model) for tool in all_tools]
        print(f"这里是llm_withtools.py中的chat_with_agent_claude函数458行，用完convert_tool_info之后tools: {tools}"+"\n")

        # Call API
        print(f"这里是llm_withtools.py中的chat_with_agent_claude函数461行，入口参数msg_history + new_msg_history: {msg_history + new_msg_history}"+"\n")
        response = get_response_withtools(
            client=client,
            model=client_model,
            messages=msg_history + new_msg_history,
            tool_choice={"type": "auto"},
            tools=tools,
            logging=logging,
        )
        print(f"这里是llm_withtools.py中的chat_with_agent_claude函数470行，response: {response}"+"\n")
        # Check for tool use
        tool_use = check_for_tool_use(response, model=client_model)
        print(f"这里是llm_withtools.py中的chat_with_agent_claude函数473行，tool_use: {tool_use}"+"\n")
        while tool_use:
            # Collect all tool_use blocks from response.content to support parallel tool calls
            # This is needed for models like Opus 4.5 that may return multiple tool_use blocks
            # while Haiku 4.5 typically returns single tool_use blocks (backward compatible)
            tool_use_blocks = []
            if hasattr(response, 'content') and response.content:
                for block in response.content:
                    # Handle both object attributes and dict access
                    block_type = None
                    if hasattr(block, 'type'):
                        block_type = block.type
                    elif isinstance(block, dict):
                        block_type = block.get('type')
                    
                    if block_type == "tool_use":
                        tool_use_blocks.append(block)
            
            # Process all tool_use blocks (supports both single and parallel tool calls)
            tool_results = []
            for tool_use_block in tool_use_blocks:
                # Extract tool information from block (handle both object and dict formats)
                if hasattr(tool_use_block, 'id'):
                    tool_id = tool_use_block.id
                    tool_name = tool_use_block.name
                    tool_input = tool_use_block.input
                elif isinstance(tool_use_block, dict):
                    tool_id = tool_use_block.get('id')
                    tool_name = tool_use_block.get('name')
                    tool_input = tool_use_block.get('input')
                else:
                    # Skip if we can't extract tool info
                    continue
                
            # Process tool call
                tool_result = process_tool_call(tools_dict, tool_name, tool_input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_id,
                    "content": tool_result,
                })
            
            # If no blocks were found, fall back to single tool_use processing (backward compatibility)
            # This handles edge cases where block detection might fail
            if not tool_results:
                tool_name = tool_use['tool_name']
                tool_input = tool_use['tool_input']
                tool_result = process_tool_call(tools_dict, tool_name, tool_input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_use['tool_id'],
                    "content": tool_result,
                })

            # Add assistant's message with tool calls and user's message with tool results
            new_msg_history.append({"role": "assistant", "content": response.content})
            new_msg_history.append({
                "role": "user",
                "content": tool_results,
            })
            
            response = get_response_withtools(
                client=client,
                model=client_model,
                messages=msg_history + new_msg_history,
                tool_choice={"type": "auto"},
                tools=tools,
                logging=logging,
            )

            # Check for next tool use
            print(f"这里是llm_withtools.py中的chat_with_agent_claude函数502行，在while  tool_use循环中, response: {response}"+"\n")
            tool_use = check_for_tool_use(response, model=client_model)
            print(f"这里是llm_withtools.py中的chat_with_agent_claude函数504行，在while  tool_use循环中, tool_use: {tool_use}"+"\n")

        # Get final response
        final_response = next((block.text for block in response.content if hasattr(block, "text")), None)
        print(f"这里是llm_withtools.py中的chat_with_agent_claude函数508行，在while  tool_use循环中, final_response: {final_response}"+"\n")
        new_msg_history.append({
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": final_response,
                }
            ],
        })

    except Exception as e:
        logging(f"Error in chat_with_agent_claude: {e}")
        import traceback
        logging(f"Traceback: {traceback.format_exc()}")
        # Return empty message history on error, but at least log it
        return new_msg_history

    return new_msg_history

def chat_with_agent_openai(
        msg,
        model='o3-mini-2025-01-31',
        msg_history=None,
        logging=print,
    ):
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    model = str(model) if not isinstance(model, str) else model
    
    # Construct message
    if msg_history is None:
        msg_history = []
    new_msg_history = [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": msg,
                }
            ],
        }
    ]
    separator = '=' * 10
    logging(f"\n{separator} User Instruction {separator}\n{msg}")
    try:
        # Create client
        client, client_model = create_client(model)

        # Load all tools
        all_tools = load_all_tools(logging=logging)
        tools_dict = {tool['info']['name']: tool for tool in all_tools}
        tools = [convert_tool_info(tool['info'], model=client_model) for tool in all_tools]

        # Call API
        response = get_response_withtools(
            client=client,
            model=client_model,
            messages=msg_history + new_msg_history,
            tool_choice="auto",
            tools=tools,
            logging=logging,
        )
        logging(f"\n{separator} Agent Response {separator}\n{response}")

        # Check for tool use
        tool_use = check_for_tool_use(response, model=client_model)
        logging(tool_use)
        while tool_use:
            # Process tool call
            tool_name = tool_use['tool_name']
            tool_input = tool_use['tool_input']
            tool_result = process_tool_call(tools_dict, tool_name, tool_input)

            logging(f"Tool Used: {tool_name}")
            logging(f"Tool Input: {tool_input}")
            logging(f"Tool Result: {tool_result}")

            # Get tool response
            for tool_call in response.output:
                if tool_call.type == "function_call":
                    break
            new_msg_history.append(tool_call)
            new_msg_history.append({
                "type": "function_call_output",
                "call_id": tool_use['tool_id'],
                "output": tool_result,
            })
            response = get_response_withtools(
                client=client,
                model=client_model,
                messages=msg_history + new_msg_history,
                tool_choice="auto",
                tools=tools,
                logging=logging,
            )

            # Check for next tool use
            tool_use = check_for_tool_use(response, model=client_model)

            logging(f"Tool Response: {response}")

        # Get final response
        new_msg_history.append(response)

    except Exception:
        pass

    return new_msg_history

def chat_with_agent(
    msg,
    model=str(CLAUDE_MODEL),
    msg_history=None,
    logging=print,
    convert=False,  # Convert the message history to a generic format, so that msg_history can be used across models
):
    # Log function entry parameters using the provided logging function
    # Convert model to string if it's a _ClaudeModel object or other non-string type
    model = str(model) if not isinstance(model, str) else model
    
    msg_str = str(msg)
    msg_preview = msg_str[:200] + "..." if len(msg_str) > 200 else msg_str
    # logging(f"这里是llm_withtools.py中的chat_with_agent函数，入口参数msg: {msg_preview}, model: {model}, msg_history长度: {len(msg_history) if msg_history else 0}, convert: {convert}")
    if msg_history is None:
        msg_history = []

    if 'claude' in model:
        # Claude models - native tool calling
        new_msg_history = chat_with_agent_claude(msg, model=model, msg_history=msg_history, logging=logging)
        # logging(f"这里是llm_withtools.py中的chat_with_agent函数，chat_with_agent_claude函数的返回值new_msg_history是: {new_msg_history}"+"\n")
        conv_msg_history = convert_msg_history(new_msg_history, model=model)
        logging(conv_msg_history)
        if convert:
            new_msg_history = conv_msg_history
        new_msg_history = msg_history + new_msg_history

    elif model.startswith('o3-') or model == 'gpt-5.1-2025-11-13' or model == 'gpt-5.1-codex-mini':
        # OpenAI o3 models, gpt-5.1-2025-11-13, and gpt-5.1-codex-mini
        new_msg_history = chat_with_agent_openai(msg, model=model, msg_history=msg_history, logging=logging)
        # Current version does not support cross-model conversion
        # new_msg_history = convert_msg_history(new_msg_history, model=model)
        new_msg_history = msg_history + new_msg_history

    elif model.startswith('glm-'):
        # GLM models - native tool calling (OpenAI-compatible)
        new_msg_history = chat_with_agent_glm_native(msg, model=model, msg_history=msg_history, logging=logging)
        # logging(f"这里是llm_withtools.py中的chat_with_agent函数，chat_with_agent_glm_native函数的返回值new_msg_history是: {new_msg_history}"+"\n")
        conv_msg_history = convert_msg_history(new_msg_history, model=model)
        # logging(f"这里是llm_withtools.py中的chat_with_agent函数，convert_msg_history函数的返回值conv_msg_history是: {conv_msg_history}"+"\n")
        if convert:
            new_msg_history = conv_msg_history
        # Note: chat_with_agent_glm_native already includes msg_history, so no need to merge again

    else:
        # Other models without in-built tool calling
        new_msg_history = chat_with_agent_manualtools(msg, model=model, msg_history=msg_history, logging=logging)
        conv_msg_history = convert_msg_history(new_msg_history, model=model)
        if convert:
            new_msg_history = conv_msg_history

    return new_msg_history


if __name__ == "__main__":
    # Test the tool calling functionality
    msg = "hello!"
    chat_with_agent(msg)
