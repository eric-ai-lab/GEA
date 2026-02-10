+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 54 items

forth_test.py FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF     [100%]

=================================== FAILURES ===================================
_________________ ForthTest.test_addition_can_add_two_numbers __________________

self = <forth_test.ForthTest testMethod=test_addition_can_add_two_numbers>

    def test_addition_can_add_two_numbers(self):
>       self.assertEqual(evaluate(["1 2 +"]), [3])

forth_test.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 +']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_______ ForthTest.test_addition_errors_if_there_is_nothing_on_the_stack ________

self = <forth_test.ForthTest testMethod=test_addition_errors_if_there_is_nothing_on_the_stack>

    def test_addition_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["+"])

forth_test.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
____ ForthTest.test_addition_errors_if_there_is_only_one_value_on_the_stack ____

self = <forth_test.ForthTest testMethod=test_addition_errors_if_there_is_only_one_value_on_the_stack>

    def test_addition_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["1 +"])

forth_test.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__________ ForthTest.test_addition_more_than_two_values_on_the_stack ___________

self = <forth_test.ForthTest testMethod=test_addition_more_than_two_values_on_the_stack>

    def test_addition_more_than_two_values_on_the_stack(self):
>       self.assertEqual(evaluate(["1 2 3 +"]), [1, 5])

forth_test.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 3 +']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
______ ForthTest.test_case_insensitivity_definitions_are_case_insensitive ______

self = <forth_test.ForthTest testMethod=test_case_insensitivity_definitions_are_case_insensitive>

    def test_case_insensitivity_definitions_are_case_insensitive(self):
>       self.assertEqual(evaluate([": SWAP DUP Dup dup ;", "1 swap"]), [1, 1, 1, 1])

forth_test.py:263: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': SWAP DUP Dup dup ;', '1 swap']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__________ ForthTest.test_case_insensitivity_drop_is_case_insensitive __________

self = <forth_test.ForthTest testMethod=test_case_insensitivity_drop_is_case_insensitive>

    def test_case_insensitivity_drop_is_case_insensitive(self):
>       self.assertEqual(evaluate(["1 2 3 4 DROP Drop drop"]), [1])

forth_test.py:251: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 3 4 DROP Drop drop']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__________ ForthTest.test_case_insensitivity_dup_is_case_insensitive ___________

self = <forth_test.ForthTest testMethod=test_case_insensitivity_dup_is_case_insensitive>

    def test_case_insensitivity_dup_is_case_insensitive(self):
>       self.assertEqual(evaluate(["1 DUP Dup dup"]), [1, 1, 1, 1])

forth_test.py:248: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 DUP Dup dup']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__________ ForthTest.test_case_insensitivity_over_is_case_insensitive __________

self = <forth_test.ForthTest testMethod=test_case_insensitivity_over_is_case_insensitive>

    def test_case_insensitivity_over_is_case_insensitive(self):
>       self.assertEqual(evaluate(["1 2 OVER Over over"]), [1, 2, 1, 2, 1])

forth_test.py:257: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 OVER Over over']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__________ ForthTest.test_case_insensitivity_swap_is_case_insensitive __________

self = <forth_test.ForthTest testMethod=test_case_insensitivity_swap_is_case_insensitive>

    def test_case_insensitivity_swap_is_case_insensitive(self):
>       self.assertEqual(evaluate(["1 2 SWAP 3 Swap 4 swap"]), [2, 3, 4, 1])

forth_test.py:254: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 SWAP 3 Swap 4 swap']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__ ForthTest.test_case_insensitivity_user_defined_words_are_case_insensitive ___

self = <forth_test.ForthTest testMethod=test_case_insensitivity_user_defined_words_are_case_insensitive>

    def test_case_insensitivity_user_defined_words_are_case_insensitive(self):
>       self.assertEqual(evaluate([": foo dup ;", "1 FOO Foo foo"]), [1, 1, 1, 1])

forth_test.py:260: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': foo dup ;', '1 FOO Foo foo']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
________ ForthTest.test_combined_arithmetic_addition_and_multiplication ________

self = <forth_test.ForthTest testMethod=test_combined_arithmetic_addition_and_multiplication>

    def test_combined_arithmetic_addition_and_multiplication(self):
>       self.assertEqual(evaluate(["1 3 4 + *"]), [7])

forth_test.py:128: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 3 4 + *']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_________ ForthTest.test_combined_arithmetic_addition_and_subtraction __________

self = <forth_test.ForthTest testMethod=test_combined_arithmetic_addition_and_subtraction>

    def test_combined_arithmetic_addition_and_subtraction(self):
>       self.assertEqual(evaluate(["1 2 + 4 -"]), [-1])

forth_test.py:119: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 + 4 -']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
________ ForthTest.test_combined_arithmetic_multiplication_and_addition ________

self = <forth_test.ForthTest testMethod=test_combined_arithmetic_multiplication_and_addition>

    def test_combined_arithmetic_multiplication_and_addition(self):
>       self.assertEqual(evaluate(["1 3 4 * +"]), [13])

forth_test.py:125: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 3 4 * +']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
________ ForthTest.test_combined_arithmetic_multiplication_and_division ________

self = <forth_test.ForthTest testMethod=test_combined_arithmetic_multiplication_and_division>

    def test_combined_arithmetic_multiplication_and_division(self):
>       self.assertEqual(evaluate(["2 4 * 3 /"]), [2])

forth_test.py:122: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['2 4 * 3 /']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
________________ ForthTest.test_division_can_divide_two_numbers ________________

self = <forth_test.ForthTest testMethod=test_division_can_divide_two_numbers>

    def test_division_can_divide_two_numbers(self):
>       self.assertEqual(evaluate(["12 3 /"]), [4])

forth_test.py:87: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['12 3 /']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
______________ ForthTest.test_division_errors_if_dividing_by_zero ______________

self = <forth_test.ForthTest testMethod=test_division_errors_if_dividing_by_zero>

    def test_division_errors_if_dividing_by_zero(self):
        # divide by zero
        with self.assertRaises(ZeroDivisionError) as err:
>           evaluate(["4 0 /"])

forth_test.py:95: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_______ ForthTest.test_division_errors_if_there_is_nothing_on_the_stack ________

self = <forth_test.ForthTest testMethod=test_division_errors_if_there_is_nothing_on_the_stack>

    def test_division_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["/"])

forth_test.py:101: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
____ ForthTest.test_division_errors_if_there_is_only_one_value_on_the_stack ____

self = <forth_test.ForthTest testMethod=test_division_errors_if_there_is_only_one_value_on_the_stack>

    def test_division_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["1 /"])

forth_test.py:109: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__________ ForthTest.test_division_more_than_two_values_on_the_stack ___________

self = <forth_test.ForthTest testMethod=test_division_more_than_two_values_on_the_stack>

    def test_division_more_than_two_values_on_the_stack(self):
>       self.assertEqual(evaluate(["1 12 3 /"]), [1, 4])

forth_test.py:116: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 12 3 /']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
______________ ForthTest.test_division_performs_integer_division _______________

self = <forth_test.ForthTest testMethod=test_division_performs_integer_division>

    def test_division_performs_integer_division(self):
>       self.assertEqual(evaluate(["8 3 /"]), [2])

forth_test.py:90: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['8 3 /']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_________ ForthTest.test_drop_errors_if_there_is_nothing_on_the_stack __________

self = <forth_test.ForthTest testMethod=test_drop_errors_if_there_is_nothing_on_the_stack>

    def test_drop_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["drop"])

forth_test.py:152: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_ ForthTest.test_drop_removes_the_top_value_on_the_stack_if_it_is_not_the_only_one _

self = <forth_test.ForthTest testMethod=test_drop_removes_the_top_value_on_the_stack_if_it_is_not_the_only_one>

    def test_drop_removes_the_top_value_on_the_stack_if_it_is_not_the_only_one(self):
>       self.assertEqual(evaluate(["1 2 drop"]), [1])

forth_test.py:148: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 drop']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_ ForthTest.test_drop_removes_the_top_value_on_the_stack_if_it_is_the_only_one _

self = <forth_test.ForthTest testMethod=test_drop_removes_the_top_value_on_the_stack_if_it_is_the_only_one>

    def test_drop_removes_the_top_value_on_the_stack_if_it_is_the_only_one(self):
>       self.assertEqual(evaluate(["1 drop"]), [])

forth_test.py:145: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 drop']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
________________ ForthTest.test_dup_copies_a_value_on_the_stack ________________

self = <forth_test.ForthTest testMethod=test_dup_copies_a_value_on_the_stack>

    def test_dup_copies_a_value_on_the_stack(self):
>       self.assertEqual(evaluate(["1 dup"]), [1, 1])

forth_test.py:131: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 dup']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_____________ ForthTest.test_dup_copies_the_top_value_on_the_stack _____________

self = <forth_test.ForthTest testMethod=test_dup_copies_the_top_value_on_the_stack>

    def test_dup_copies_the_top_value_on_the_stack(self):
>       self.assertEqual(evaluate(["1 2 dup"]), [1, 2, 2])

forth_test.py:134: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 dup']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__________ ForthTest.test_dup_errors_if_there_is_nothing_on_the_stack __________

self = <forth_test.ForthTest testMethod=test_dup_errors_if_there_is_nothing_on_the_stack>

    def test_dup_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["dup"])

forth_test.py:138: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
____________ ForthTest.test_multiplication_can_multiply_two_numbers ____________

self = <forth_test.ForthTest testMethod=test_multiplication_can_multiply_two_numbers>

    def test_multiplication_can_multiply_two_numbers(self):
>       self.assertEqual(evaluate(["2 4 *"]), [8])

forth_test.py:65: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['2 4 *']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
____ ForthTest.test_multiplication_errors_if_there_is_nothing_on_the_stack _____

self = <forth_test.ForthTest testMethod=test_multiplication_errors_if_there_is_nothing_on_the_stack>

    def test_multiplication_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["*"])

forth_test.py:69: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_ ForthTest.test_multiplication_errors_if_there_is_only_one_value_on_the_stack _

self = <forth_test.ForthTest testMethod=test_multiplication_errors_if_there_is_only_one_value_on_the_stack>

    def test_multiplication_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["1 *"])

forth_test.py:77: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_______ ForthTest.test_multiplication_more_than_two_values_on_the_stack ________

self = <forth_test.ForthTest testMethod=test_multiplication_more_than_two_values_on_the_stack>

    def test_multiplication_more_than_two_values_on_the_stack(self):
>       self.assertEqual(evaluate(["1 2 3 *"]), [1, 6])

forth_test.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 3 *']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
___ ForthTest.test_over_copies_the_second_element_if_there_are_more_than_two ___

self = <forth_test.ForthTest testMethod=test_over_copies_the_second_element_if_there_are_more_than_two>

    def test_over_copies_the_second_element_if_there_are_more_than_two(self):
>       self.assertEqual(evaluate(["1 2 3 over"]), [1, 2, 3, 2])

forth_test.py:186: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 3 over']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_____ ForthTest.test_over_copies_the_second_element_if_there_are_only_two ______

self = <forth_test.ForthTest testMethod=test_over_copies_the_second_element_if_there_are_only_two>

    def test_over_copies_the_second_element_if_there_are_only_two(self):
>       self.assertEqual(evaluate(["1 2 over"]), [1, 2, 1])

forth_test.py:183: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 over']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_________ ForthTest.test_over_errors_if_there_is_nothing_on_the_stack __________

self = <forth_test.ForthTest testMethod=test_over_errors_if_there_is_nothing_on_the_stack>

    def test_over_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["over"])

forth_test.py:190: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
______ ForthTest.test_over_errors_if_there_is_only_one_value_on_the_stack ______

self = <forth_test.ForthTest testMethod=test_over_errors_if_there_is_only_one_value_on_the_stack>

    def test_over_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["1 over"])

forth_test.py:198: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__ ForthTest.test_parsing_and_numbers_numbers_just_get_pushed_onto_the_stack ___

self = <forth_test.ForthTest testMethod=test_parsing_and_numbers_numbers_just_get_pushed_onto_the_stack>

    def test_parsing_and_numbers_numbers_just_get_pushed_onto_the_stack(self):
>       self.assertEqual(evaluate(["1 2 3 4 5"]), [1, 2, 3, 4, 5])

forth_test.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 3 4 5']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__ ForthTest.test_parsing_and_numbers_pushes_negative_numbers_onto_the_stack ___

self = <forth_test.ForthTest testMethod=test_parsing_and_numbers_pushes_negative_numbers_onto_the_stack>

    def test_parsing_and_numbers_pushes_negative_numbers_onto_the_stack(self):
>       self.assertEqual(evaluate(["-1 -2 -3 -4 -5"]), [-1, -2, -3, -4, -5])

forth_test.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['-1 -2 -3 -4 -5']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_____________ ForthTest.test_subtraction_can_subtract_two_numbers ______________

self = <forth_test.ForthTest testMethod=test_subtraction_can_subtract_two_numbers>

    def test_subtraction_can_subtract_two_numbers(self):
>       self.assertEqual(evaluate(["3 4 -"]), [-1])

forth_test.py:43: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['3 4 -']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
______ ForthTest.test_subtraction_errors_if_there_is_nothing_on_the_stack ______

self = <forth_test.ForthTest testMethod=test_subtraction_errors_if_there_is_nothing_on_the_stack>

    def test_subtraction_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["-"])

forth_test.py:47: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__ ForthTest.test_subtraction_errors_if_there_is_only_one_value_on_the_stack ___

self = <forth_test.ForthTest testMethod=test_subtraction_errors_if_there_is_only_one_value_on_the_stack>

    def test_subtraction_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["1 -"])

forth_test.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_________ ForthTest.test_subtraction_more_than_two_values_on_the_stack _________

self = <forth_test.ForthTest testMethod=test_subtraction_more_than_two_values_on_the_stack>

    def test_subtraction_more_than_two_values_on_the_stack(self):
>       self.assertEqual(evaluate(["1 12 3 -"]), [1, 9])

forth_test.py:62: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 12 3 -']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_________ ForthTest.test_swap_errors_if_there_is_nothing_on_the_stack __________

self = <forth_test.ForthTest testMethod=test_swap_errors_if_there_is_nothing_on_the_stack>

    def test_swap_errors_if_there_is_nothing_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["swap"])

forth_test.py:168: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
______ ForthTest.test_swap_errors_if_there_is_only_one_value_on_the_stack ______

self = <forth_test.ForthTest testMethod=test_swap_errors_if_there_is_only_one_value_on_the_stack>

    def test_swap_errors_if_there_is_only_one_value_on_the_stack(self):
        with self.assertRaises(StackUnderflowError) as err:
>           evaluate(["1 swap"])

forth_test.py:176: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_ ForthTest.test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_not_the_only_ones _

self = <forth_test.ForthTest testMethod=test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_not_the_only_ones>

    def test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_not_the_only_ones(
        self,
    ):
>       self.assertEqual(evaluate(["1 2 3 swap"]), [1, 3, 2])

forth_test.py:164: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 3 swap']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_ ForthTest.test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_the_only_ones _

self = <forth_test.ForthTest testMethod=test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_the_only_ones>

    def test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_the_only_ones(self):
>       self.assertEqual(evaluate(["1 2 swap"]), [2, 1])

forth_test.py:159: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = ['1 2 swap']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_______ ForthTest.test_user_defined_words_can_consist_of_built_in_words ________

self = <forth_test.ForthTest testMethod=test_user_defined_words_can_consist_of_built_in_words>

    def test_user_defined_words_can_consist_of_built_in_words(self):
>       self.assertEqual(evaluate([": dup-twice dup dup ;", "1 dup-twice"]), [1, 1, 1])

forth_test.py:205: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': dup-twice dup dup ;', '1 dup-twice']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_ ForthTest.test_user_defined_words_can_define_word_that_uses_word_with_the_same_name _

self = <forth_test.ForthTest testMethod=test_user_defined_words_can_define_word_that_uses_word_with_the_same_name>

    def test_user_defined_words_can_define_word_that_uses_word_with_the_same_name(self):
>       self.assertEqual(evaluate([": foo 10 ;", ": foo foo 1 + ;", "foo"]), [11])

forth_test.py:227: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': foo 10 ;', ': foo foo 1 + ;', 'foo']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
______ ForthTest.test_user_defined_words_can_override_built_in_operators _______

self = <forth_test.ForthTest testMethod=test_user_defined_words_can_override_built_in_operators>

    def test_user_defined_words_can_override_built_in_operators(self):
>       self.assertEqual(evaluate([": + * ;", "3 4 +"]), [12])

forth_test.py:219: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': + * ;', '3 4 +']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
________ ForthTest.test_user_defined_words_can_override_built_in_words _________

self = <forth_test.ForthTest testMethod=test_user_defined_words_can_override_built_in_words>

    def test_user_defined_words_can_override_built_in_words(self):
>       self.assertEqual(evaluate([": swap dup ;", "1 swap"]), [1, 1])

forth_test.py:216: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': swap dup ;', '1 swap']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
___ ForthTest.test_user_defined_words_can_override_other_user_defined_words ____

self = <forth_test.ForthTest testMethod=test_user_defined_words_can_override_other_user_defined_words>

    def test_user_defined_words_can_override_other_user_defined_words(self):
        self.assertEqual(
>           evaluate([": foo dup ;", ": foo dup dup ;", "1 foo"]), [1, 1, 1]
        )

forth_test.py:212: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': foo dup ;', ': foo dup dup ;', '1 foo']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_ ForthTest.test_user_defined_words_can_use_different_words_with_the_same_name _

self = <forth_test.ForthTest testMethod=test_user_defined_words_can_use_different_words_with_the_same_name>

    def test_user_defined_words_can_use_different_words_with_the_same_name(self):
        self.assertEqual(
>           evaluate([": foo 5 ;", ": bar foo ;", ": foo 6 ;", "bar foo"]), [5, 6]
        )

forth_test.py:223: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': foo 5 ;', ': bar foo ;', ': foo 6 ;', 'bar foo']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
______ ForthTest.test_user_defined_words_cannot_redefine_negative_numbers ______

self = <forth_test.ForthTest testMethod=test_user_defined_words_cannot_redefine_negative_numbers>

    def test_user_defined_words_cannot_redefine_negative_numbers(self):
        with self.assertRaises(ValueError) as err:
>           evaluate([": -1 2 ;"])

forth_test.py:237: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
____ ForthTest.test_user_defined_words_cannot_redefine_non_negative_numbers ____

self = <forth_test.ForthTest testMethod=test_user_defined_words_cannot_redefine_non_negative_numbers>

    def test_user_defined_words_cannot_redefine_non_negative_numbers(self):
        with self.assertRaises(ValueError) as err:
>           evaluate([": 1 2 ;"])

forth_test.py:231: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
__ ForthTest.test_user_defined_words_errors_if_executing_a_non_existent_word ___

self = <forth_test.ForthTest testMethod=test_user_defined_words_errors_if_executing_a_non_existent_word>

    def test_user_defined_words_errors_if_executing_a_non_existent_word(self):
        with self.assertRaises(ValueError) as err:
>           evaluate(["foo"])

forth_test.py:243: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
_________ ForthTest.test_user_defined_words_execute_in_the_right_order _________

self = <forth_test.ForthTest testMethod=test_user_defined_words_execute_in_the_right_order>

    def test_user_defined_words_execute_in_the_right_order(self):
>       self.assertEqual(evaluate([": countup 1 2 3 ;", "countup"]), [1, 2, 3])

forth_test.py:208: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_data = [': countup 1 2 3 ;', 'countup']

    def evaluate(input_data):
        """
        Evaluate a string of Forth code and return the stack as a list of integers.
        Supports integer arithmetic, stack manipulation, and custom word definitions.
    
        The following built-in operations are supported:
            +, -, *, /
            DUP, DROP, SWAP, OVER
        New words can be defined via the syntax:
            : word-name definition ;
        Words are case-insensitive.
        """
        # Split the input into tokens. We use simple whitespace splitting.
        # We also convert tokens to lower-case for uniformity (custom words and built-in operations are case-insensitive).
>       tokens = input_data.split()
E       AttributeError: 'list' object has no attribute 'split'

forth.py:23: AttributeError
=========================== short test summary info ============================
FAILED forth_test.py::ForthTest::test_addition_can_add_two_numbers - Attribut...
FAILED forth_test.py::ForthTest::test_addition_errors_if_there_is_nothing_on_the_stack
FAILED forth_test.py::ForthTest::test_addition_errors_if_there_is_only_one_value_on_the_stack
FAILED forth_test.py::ForthTest::test_addition_more_than_two_values_on_the_stack
FAILED forth_test.py::ForthTest::test_case_insensitivity_definitions_are_case_insensitive
FAILED forth_test.py::ForthTest::test_case_insensitivity_drop_is_case_insensitive
FAILED forth_test.py::ForthTest::test_case_insensitivity_dup_is_case_insensitive
FAILED forth_test.py::ForthTest::test_case_insensitivity_over_is_case_insensitive
FAILED forth_test.py::ForthTest::test_case_insensitivity_swap_is_case_insensitive
FAILED forth_test.py::ForthTest::test_case_insensitivity_user_defined_words_are_case_insensitive
FAILED forth_test.py::ForthTest::test_combined_arithmetic_addition_and_multiplication
FAILED forth_test.py::ForthTest::test_combined_arithmetic_addition_and_subtraction
FAILED forth_test.py::ForthTest::test_combined_arithmetic_multiplication_and_addition
FAILED forth_test.py::ForthTest::test_combined_arithmetic_multiplication_and_division
FAILED forth_test.py::ForthTest::test_division_can_divide_two_numbers - Attri...
FAILED forth_test.py::ForthTest::test_division_errors_if_dividing_by_zero - A...
FAILED forth_test.py::ForthTest::test_division_errors_if_there_is_nothing_on_the_stack
FAILED forth_test.py::ForthTest::test_division_errors_if_there_is_only_one_value_on_the_stack
FAILED forth_test.py::ForthTest::test_division_more_than_two_values_on_the_stack
FAILED forth_test.py::ForthTest::test_division_performs_integer_division - At...
FAILED forth_test.py::ForthTest::test_drop_errors_if_there_is_nothing_on_the_stack
FAILED forth_test.py::ForthTest::test_drop_removes_the_top_value_on_the_stack_if_it_is_not_the_only_one
FAILED forth_test.py::ForthTest::test_drop_removes_the_top_value_on_the_stack_if_it_is_the_only_one
FAILED forth_test.py::ForthTest::test_dup_copies_a_value_on_the_stack - Attri...
FAILED forth_test.py::ForthTest::test_dup_copies_the_top_value_on_the_stack
FAILED forth_test.py::ForthTest::test_dup_errors_if_there_is_nothing_on_the_stack
FAILED forth_test.py::ForthTest::test_multiplication_can_multiply_two_numbers
FAILED forth_test.py::ForthTest::test_multiplication_errors_if_there_is_nothing_on_the_stack
FAILED forth_test.py::ForthTest::test_multiplication_errors_if_there_is_only_one_value_on_the_stack
FAILED forth_test.py::ForthTest::test_multiplication_more_than_two_values_on_the_stack
FAILED forth_test.py::ForthTest::test_over_copies_the_second_element_if_there_are_more_than_two
FAILED forth_test.py::ForthTest::test_over_copies_the_second_element_if_there_are_only_two
FAILED forth_test.py::ForthTest::test_over_errors_if_there_is_nothing_on_the_stack
FAILED forth_test.py::ForthTest::test_over_errors_if_there_is_only_one_value_on_the_stack
FAILED forth_test.py::ForthTest::test_parsing_and_numbers_numbers_just_get_pushed_onto_the_stack
FAILED forth_test.py::ForthTest::test_parsing_and_numbers_pushes_negative_numbers_onto_the_stack
FAILED forth_test.py::ForthTest::test_subtraction_can_subtract_two_numbers - ...
FAILED forth_test.py::ForthTest::test_subtraction_errors_if_there_is_nothing_on_the_stack
FAILED forth_test.py::ForthTest::test_subtraction_errors_if_there_is_only_one_value_on_the_stack
FAILED forth_test.py::ForthTest::test_subtraction_more_than_two_values_on_the_stack
FAILED forth_test.py::ForthTest::test_swap_errors_if_there_is_nothing_on_the_stack
FAILED forth_test.py::ForthTest::test_swap_errors_if_there_is_only_one_value_on_the_stack
FAILED forth_test.py::ForthTest::test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_not_the_only_ones
FAILED forth_test.py::ForthTest::test_swap_swaps_the_top_two_values_on_the_stack_if_they_are_the_only_ones
FAILED forth_test.py::ForthTest::test_user_defined_words_can_consist_of_built_in_words
FAILED forth_test.py::ForthTest::test_user_defined_words_can_define_word_that_uses_word_with_the_same_name
FAILED forth_test.py::ForthTest::test_user_defined_words_can_override_built_in_operators
FAILED forth_test.py::ForthTest::test_user_defined_words_can_override_built_in_words
FAILED forth_test.py::ForthTest::test_user_defined_words_can_override_other_user_defined_words
FAILED forth_test.py::ForthTest::test_user_defined_words_can_use_different_words_with_the_same_name
FAILED forth_test.py::ForthTest::test_user_defined_words_cannot_redefine_negative_numbers
FAILED forth_test.py::ForthTest::test_user_defined_words_cannot_redefine_non_negative_numbers
FAILED forth_test.py::ForthTest::test_user_defined_words_errors_if_executing_a_non_existent_word
FAILED forth_test.py::ForthTest::test_user_defined_words_execute_in_the_right_order
============================== 54 failed in 5.78s ==============================
