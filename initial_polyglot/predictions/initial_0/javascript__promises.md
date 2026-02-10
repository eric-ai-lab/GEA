
========== User Instruction ==========
I have uploaded a code repository in the directory /testbed/. Help solve the following problem.

<problem_description>
# Instructions

The two objectives of this exercise are :

1. Implement a `promisify` function that turns a function using the "callback pattern" into a function that returns a `Promise`. See the example below.

```javascript
function fetchProduct(productId, function(error, data) {
    if (error) {
        // Handle the error
    } else {
        // Make something with your data
    }
})

const fetchProductAsPromise = promisify(fetchProduct);

// Now you got a function `fetchProductAsPromise`
// that returns a promise
fetchProductAsPromise(productId)
    .then((data) => {})
    .catch((error) => {});
```

2. Re-implement the following built-ins `Promise` methods (without using them)

- `all`: takes an array of promises and resolves when _all_ of them are resolved, or rejects when _one_ of them rejects.
- `allSettled`: takes an array of promises and resolves when _all_ of them either resolve or reject.
- `race`: takes an array of promises and resolves or rejects with the value of the _first_ promise that resolves or rejects.
- `any`: takes an array of promises and resolves when _one_ of them resolves, or rejects when _all_ of them reject.


# Introduction

Before the `Promise` class was introduced, there was only one way to deal with asynchronous code : the _callback pattern_.

A callback is a function that is passed as an argument to another function and will be called once some action in that other function has finished. A common pattern for those callback functions is that they accept an "error" as first parameter (see example below).

```javascript
function callback(error, arg2, arg3) {}
```

How is it related to asynchronous code ?

Historically, callbacks have been used in order to allow us to do some work after an asynchronous task was done and without blocking the whole program.

```javascript
fetchProduct(productId, function (error, data) {
  if (error) {
    // Handle the error
  } else {
    // Do some work
  }
});
```

In the example above, the `fetchProduct` function (which is asynchronous), takes a callback as a second argument that decides what to do when the product data has been retrieved.



</problem_description>

Your task is to make changes to the files in the /testbed/ directory to address the <problem_description>. I have already taken care of the required dependencies.


Please analyze the problem description carefully. Then make edits to the code files to complete the instruction.

========== Agent Response ==========
Response(id='resp_681ebc22d048819194d861fdb408af000b2a072090c69a09', created_at=1746844706.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='o3-mini-2025-01-31', object='response', output=[ResponseReasoningItem(id='rs_681ebc23c6288191a430cd40ea112a4d0b2a072090c69a09', summary=[], type='reasoning', encrypted_content=None, status=None), ResponseFunctionToolCall(arguments='{"command": "view", "path": "/testbed/README.md", "file_text": null}', call_id='call_CuA0Bg0B8TMYuDuyXOw5CKga', name='editor', type='function_call', id='fc_681ebc244ccc8191bd94cc47f474593b0b2a072090c69a09', status='completed')], parallel_tool_calls=False, temperature=1.0, tool_choice='auto', tools=[FunctionTool(name='bash', parameters={'type': 'object', 'properties': {'command': {'type': 'string', 'description': 'The bash command to run.'}}, 'required': ['command'], 'additionalProperties': False}, strict=True, type='function', description='Run commands in a bash shell\n\n* When invoking this tool, the contents of the "command" parameter does NOT need to be XML-escaped.\n\n* You don\'t have access to the internet via this tool.\n\n* You do have access to a mirror of common linux and python packages via apt and pip.\n\n* State is persistent across command calls and discussions with the user.\n\n* To inspect a particular line range of a file, e.g. lines 10-25, try \'sed -n 10,25p /path/to/the/file\'.\n\n* Please avoid commands that may produce a very large amount of output.\n\n* Please run long lived commands in the background, e.g. \'sleep 10 &\' or start a server in the background.'), FunctionTool(name='editor', parameters={'type': 'object', 'properties': {'command': {'type': 'string', 'enum': ['view', 'create', 'edit'], 'description': 'The command to run: `view`, `create`, or `edit`.'}, 'path': {'description': 'Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.', 'type': 'string'}, 'file_text': {'description': 'Required parameter of `create` or `edit` command, containing the content for the entire file.', 'type': ['string', 'null']}}, 'required': ['command', 'path', 'file_text'], 'additionalProperties': False}, strict=True, type='function', description='Custom editing tool for viewing, creating, and editing files\n\n* State is persistent across command calls and discussions with the user.\n\n* If `path` is a file, `view` displays the entire file with line numbers. If `path` is a directory, `view` lists non-hidden files and directories up to 2 levels deep.\n\n* The `create` command cannot be used if the specified `path` already exists as a file.\n\n* If a `command` generates a long output, it will be truncated and marked with `<response clipped>`.\n\n* The `edit` command overwrites the entire file with the provided `file_text`.\n\n* No partial/line-range edits or partial viewing are supported.')], top_p=1.0, max_output_tokens=None, previous_response_id=None, reasoning=Reasoning(effort='medium', generate_summary=None, summary=None), service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text')), truncation='disabled', usage=ResponseUsage(input_tokens=1027, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=92, output_tokens_details=OutputTokensDetails(reasoning_tokens=64), total_tokens=1119), user=None, store=True)
{'tool_id': 'call_CuA0Bg0B8TMYuDuyXOw5CKga', 'tool_name': 'editor', 'tool_input': {'command': 'view', 'path': '/testbed/README.md', 'file_text': None}}
Tool Used: editor
Tool Input: {'command': 'view', 'path': '/testbed/README.md', 'file_text': None}
Tool Result: Error: The path /testbed/README.md does not exist.
Tool Response: Response(id='resp_681ebc250fe881919bb73fbd10eece020b2a072090c69a09', created_at=1746844709.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='o3-mini-2025-01-31', object='response', output=[ResponseReasoningItem(id='rs_681ebc25cbcc8191ad6d0263f64b390d0b2a072090c69a09', summary=[], type='reasoning', encrypted_content=None, status=None), ResponseFunctionToolCall(arguments='{"command": "view", "path": "/testbed", "file_text": null}', call_id='call_0YnnVDGcQrHCNY1QQWGkkbX6', name='editor', type='function_call', id='fc_681ebc260480819192e5204a4fc6d8e40b2a072090c69a09', status='completed')], parallel_tool_calls=False, temperature=1.0, tool_choice='auto', tools=[FunctionTool(name='bash', parameters={'type': 'object', 'properties': {'command': {'type': 'string', 'description': 'The bash command to run.'}}, 'required': ['command'], 'additionalProperties': False}, strict=True, type='function', description='Run commands in a bash shell\n\n* When invoking this tool, the contents of the "command" parameter does NOT need to be XML-escaped.\n\n* You don\'t have access to the internet via this tool.\n\n* You do have access to a mirror of common linux and python packages via apt and pip.\n\n* State is persistent across command calls and discussions with the user.\n\n* To inspect a particular line range of a file, e.g. lines 10-25, try \'sed -n 10,25p /path/to/the/file\'.\n\n* Please avoid commands that may produce a very large amount of output.\n\n* Please run long lived commands in the background, e.g. \'sleep 10 &\' or start a server in the background.'), FunctionTool(name='editor', parameters={'type': 'object', 'properties': {'command': {'type': 'string', 'enum': ['view', 'create', 'edit'], 'description': 'The command to run: `view`, `create`, or `edit`.'}, 'path': {'description': 'Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.', 'type': 'string'}, 'file_text': {'description': 'Required parameter of `create` or `edit` command, containing the content for the entire file.', 'type': ['string', 'null']}}, 'required': ['command', 'path', 'file_text'], 'additionalProperties': False}, strict=True, type='function', description='Custom editing tool for viewing, creating, and editing files\n\n* State is persistent across command calls and discussions with the user.\n\n* If `path` is a file, `view` displays the entire file with line numbers. If `path` is a directory, `view` lists non-hidden files and directories up to 2 levels deep.\n\n* The `create` command cannot be used if the specified `path` already exists as a file.\n\n* If a `command` generates a long output, it will be truncated and marked with `<response clipped>`.\n\n* The `edit` command overwrites the entire file with the provided `file_text`.\n\n* No partial/line-range edits or partial viewing are supported.')], top_p=1.0, max_output_tokens=None, previous_response_id=None, reasoning=Reasoning(effort='medium', generate_summary=None, summary=None), service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text')), truncation='disabled', usage=ResponseUsage(input_tokens=1076, input_tokens_details=InputTokensDetails(cached_tokens=958), output_tokens=25, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=1101), user=None, store=True)
Tool Used: editor
Tool Input: {'command': 'view', 'path': '/testbed', 'file_text': None}
Tool Result: Here's the files and directories up to 2 levels deep in /testbed, excluding hidden items:
/testbed
/testbed/promises.js
/testbed/package.json

Tool Response: Response(id='resp_681ebc26eb388191b2e92c3a9b6a82220b2a072090c69a09', created_at=1746844711.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='o3-mini-2025-01-31', object='response', output=[ResponseReasoningItem(id='rs_681ebc27e5b481918a381de0e1a02eab0b2a072090c69a09', summary=[], type='reasoning', encrypted_content=None, status=None), ResponseFunctionToolCall(arguments='{"command": "view", "path": "/testbed/promises.js", "file_text": null}', call_id='call_O3E3KI40OxNL05gGWzgrvc6d', name='editor', type='function_call', id='fc_681ebc28374481918027e603922283e70b2a072090c69a09', status='completed')], parallel_tool_calls=False, temperature=1.0, tool_choice='auto', tools=[FunctionTool(name='bash', parameters={'type': 'object', 'properties': {'command': {'type': 'string', 'description': 'The bash command to run.'}}, 'required': ['command'], 'additionalProperties': False}, strict=True, type='function', description='Run commands in a bash shell\n\n* When invoking this tool, the contents of the "command" parameter does NOT need to be XML-escaped.\n\n* You don\'t have access to the internet via this tool.\n\n* You do have access to a mirror of common linux and python packages via apt and pip.\n\n* State is persistent across command calls and discussions with the user.\n\n* To inspect a particular line range of a file, e.g. lines 10-25, try \'sed -n 10,25p /path/to/the/file\'.\n\n* Please avoid commands that may produce a very large amount of output.\n\n* Please run long lived commands in the background, e.g. \'sleep 10 &\' or start a server in the background.'), FunctionTool(name='editor', parameters={'type': 'object', 'properties': {'command': {'type': 'string', 'enum': ['view', 'create', 'edit'], 'description': 'The command to run: `view`, `create`, or `edit`.'}, 'path': {'description': 'Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.', 'type': 'string'}, 'file_text': {'description': 'Required parameter of `create` or `edit` command, containing the content for the entire file.', 'type': ['string', 'null']}}, 'required': ['command', 'path', 'file_text'], 'additionalProperties': False}, strict=True, type='function', description='Custom editing tool for viewing, creating, and editing files\n\n* State is persistent across command calls and discussions with the user.\n\n* If `path` is a file, `view` displays the entire file with line numbers. If `path` is a directory, `view` lists non-hidden files and directories up to 2 levels deep.\n\n* The `create` command cannot be used if the specified `path` already exists as a file.\n\n* If a `command` generates a long output, it will be truncated and marked with `<response clipped>`.\n\n* The `edit` command overwrites the entire file with the provided `file_text`.\n\n* No partial/line-range edits or partial viewing are supported.')], top_p=1.0, max_output_tokens=None, previous_response_id=None, reasoning=Reasoning(effort='medium', generate_summary=None, summary=None), service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text')), truncation='disabled', usage=ResponseUsage(input_tokens=1142, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=28, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=1170), user=None, store=True)
Tool Used: editor
Tool Input: {'command': 'view', 'path': '/testbed/promises.js', 'file_text': None}
Tool Result: Here's the result of running `cat -n` on /testbed/promises.js:
```
     1	//
     2	// This is only a SKELETON file for the 'Promises' exercise. It's been provided as a
     3	// convenience to get you started writing code faster.
     4	//
     5	
     6	export const promisify = () => {
     7	  throw new Error('Remove this statement and implement this function');
     8	};
     9	
    10	export const all = () => {
    11	  throw new Error('Remove this statement and implement this function');
    12	};
    13	
    14	export const allSettled = () => {
    15	  throw new Error('Remove this statement and implement this function');
    16	};
    17	
    18	export const race = () => {
    19	  throw new Error('Remove this statement and implement this function');
    20	};
    21	
    22	export const any = () => {
    23	  throw new Error('Remove this statement and implement this function');
    24	};
    25	
```

Tool Response: Response(id='resp_681ebc28e9c88191b80c8875a7c234c30b2a072090c69a09', created_at=1746844713.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='o3-mini-2025-01-31', object='response', output=[ResponseReasoningItem(id='rs_681ebc2fde3c8191858f5a996e03854d0b2a072090c69a09', summary=[], type='reasoning', encrypted_content=None, status=None), ResponseFunctionToolCall(arguments='{"command": "edit", "path": "/testbed/promises.js", "file_text": "//\\n// This is only a SKELETON file for the \'Promises\' exercise. It\'s been provided as a\\n// convenience to get you started writing code faster.\\n//\\n\\nexport const promisify = (fn) => {\\n  return (...args) => {\\n    return new Promise((resolve, reject) => {\\n      fn(...args, (error, data) => {\\n        if (error) {\\n          reject(error);\\n        } else {\\n          resolve(data);\\n        }\\n      });\\n    });\\n  };\\n};\\n\\nexport const all = (promises) => {\\n  return new Promise((resolve, reject) => {\\n    if (promises.length === 0) {\\n      return resolve([]);\\n    }\\n    const results = new Array(promises.length);\\n    let completed = 0;\\n    promises.forEach((p, i) => {\\n      Promise.resolve(p)\\n        .then((value) => {\\n          results[i] = value;\\n          completed++;\\n          if (completed === promises.length) {\\n            resolve(results);\\n          }\\n        })\\n        .catch(reject);\\n    });\\n  });\\n};\\n\\nexport const allSettled = (promises) => {\\n  return new Promise((resolve) => {\\n    if (promises.length === 0) {\\n      return resolve([]);\\n    }\\n    const results = new Array(promises.length);\\n    let completed = 0;\\n    promises.forEach((p, i) => {\\n      Promise.resolve(p)\\n        .then((value) => {\\n          results[i] = { status: \'fulfilled\', value };\\n        })\\n        .catch((reason) => {\\n          results[i] = { status: \'rejected\', reason };\\n        })\\n        .finally(() => {\\n          completed++;\\n          if (completed === promises.length) {\\n            resolve(results);\\n          }\\n        });\\n    });\\n  });\\n};\\n\\nexport const race = (promises) => {\\n  return new Promise((resolve, reject) => {\\n    if (promises.length === 0) {\\n      // never resolve or reject if empty\\n      return;\\n    }\\n    promises.forEach((p) => {\\n      Promise.resolve(p).then(resolve, reject);\\n    });\\n  });\\n};\\n\\nexport const any = (promises) => {\\n  return new Promise((resolve, reject) => {\\n    if (promises.length === 0) {\\n      // if no promises, reject immediately with an AggregateError\\n      return reject(new AggregateError([], \'All promises were rejected\'));\\n    }\\n    const errors = [];\\n    let rejectedCount = 0;\\n    promises.forEach((p, i) => {\\n      Promise.resolve(p)\\n        .then(resolve)\\n        .catch((err) => {\\n          errors[i] = err;\\n          rejectedCount++;\\n          if (rejectedCount === promises.length) {\\n            reject(new AggregateError(errors, \'All promises were rejected\'));\\n          }\\n        });\\n    });\\n  });\\n};\\n"}', call_id='call_dCXO7qw4v1LkJSPoABSGYgyl', name='editor', type='function_call', id='fc_681ebc30932c8191a7882386cfce07dd0b2a072090c69a09', status='completed')], parallel_tool_calls=False, temperature=1.0, tool_choice='auto', tools=[FunctionTool(name='bash', parameters={'type': 'object', 'properties': {'command': {'type': 'string', 'description': 'The bash command to run.'}}, 'required': ['command'], 'additionalProperties': False}, strict=True, type='function', description='Run commands in a bash shell\n\n* When invoking this tool, the contents of the "command" parameter does NOT need to be XML-escaped.\n\n* You don\'t have access to the internet via this tool.\n\n* You do have access to a mirror of common linux and python packages via apt and pip.\n\n* State is persistent across command calls and discussions with the user.\n\n* To inspect a particular line range of a file, e.g. lines 10-25, try \'sed -n 10,25p /path/to/the/file\'.\n\n* Please avoid commands that may produce a very large amount of output.\n\n* Please run long lived commands in the background, e.g. \'sleep 10 &\' or start a server in the background.'), FunctionTool(name='editor', parameters={'type': 'object', 'properties': {'command': {'type': 'string', 'enum': ['view', 'create', 'edit'], 'description': 'The command to run: `view`, `create`, or `edit`.'}, 'path': {'description': 'Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.', 'type': 'string'}, 'file_text': {'description': 'Required parameter of `create` or `edit` command, containing the content for the entire file.', 'type': ['string', 'null']}}, 'required': ['command', 'path', 'file_text'], 'additionalProperties': False}, strict=True, type='function', description='Custom editing tool for viewing, creating, and editing files\n\n* State is persistent across command calls and discussions with the user.\n\n* If `path` is a file, `view` displays the entire file with line numbers. If `path` is a directory, `view` lists non-hidden files and directories up to 2 levels deep.\n\n* The `create` command cannot be used if the specified `path` already exists as a file.\n\n* If a `command` generates a long output, it will be truncated and marked with `<response clipped>`.\n\n* The `edit` command overwrites the entire file with the provided `file_text`.\n\n* No partial/line-range edits or partial viewing are supported.')], top_p=1.0, max_output_tokens=None, previous_response_id=None, reasoning=Reasoning(effort='medium', generate_summary=None, summary=None), service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text')), truncation='disabled', usage=ResponseUsage(input_tokens=1432, input_tokens_details=InputTokensDetails(cached_tokens=1086), output_tokens=1635, output_tokens_details=OutputTokensDetails(reasoning_tokens=896), total_tokens=3067), user=None, store=True)
Tool Used: editor
Tool Input: {'command': 'edit', 'path': '/testbed/promises.js', 'file_text': "//\n// This is only a SKELETON file for the 'Promises' exercise. It's been provided as a\n// convenience to get you started writing code faster.\n//\n\nexport const promisify = (fn) => {\n  return (...args) => {\n    return new Promise((resolve, reject) => {\n      fn(...args, (error, data) => {\n        if (error) {\n          reject(error);\n        } else {\n          resolve(data);\n        }\n      });\n    });\n  };\n};\n\nexport const all = (promises) => {\n  return new Promise((resolve, reject) => {\n    if (promises.length === 0) {\n      return resolve([]);\n    }\n    const results = new Array(promises.length);\n    let completed = 0;\n    promises.forEach((p, i) => {\n      Promise.resolve(p)\n        .then((value) => {\n          results[i] = value;\n          completed++;\n          if (completed === promises.length) {\n            resolve(results);\n          }\n        })\n        .catch(reject);\n    });\n  });\n};\n\nexport const allSettled = (promises) => {\n  return new Promise((resolve) => {\n    if (promises.length === 0) {\n      return resolve([]);\n    }\n    const results = new Array(promises.length);\n    let completed = 0;\n    promises.forEach((p, i) => {\n      Promise.resolve(p)\n        .then((value) => {\n          results[i] = { status: 'fulfilled', value };\n        })\n        .catch((reason) => {\n          results[i] = { status: 'rejected', reason };\n        })\n        .finally(() => {\n          completed++;\n          if (completed === promises.length) {\n            resolve(results);\n          }\n        });\n    });\n  });\n};\n\nexport const race = (promises) => {\n  return new Promise((resolve, reject) => {\n    if (promises.length === 0) {\n      // never resolve or reject if empty\n      return;\n    }\n    promises.forEach((p) => {\n      Promise.resolve(p).then(resolve, reject);\n    });\n  });\n};\n\nexport const any = (promises) => {\n  return new Promise((resolve, reject) => {\n    if (promises.length === 0) {\n      // if no promises, reject immediately with an AggregateError\n      return reject(new AggregateError([], 'All promises were rejected'));\n    }\n    const errors = [];\n    let rejectedCount = 0;\n    promises.forEach((p, i) => {\n      Promise.resolve(p)\n        .then(resolve)\n        .catch((err) => {\n          errors[i] = err;\n          rejectedCount++;\n          if (rejectedCount === promises.length) {\n            reject(new AggregateError(errors, 'All promises were rejected'));\n          }\n        });\n    });\n  });\n};\n"}
Tool Result: File at /testbed/promises.js has been overwritten with new content.
