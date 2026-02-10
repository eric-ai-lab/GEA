+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 25 items

wordy_test.py ...............F........F                                  [100%]

=================================== FAILURES ===================================
_______________________ WordyTest.test_non_math_question _______________________

self = <wordy_test.WordyTest testMethod=test_non_math_question>

    def test_non_math_question(self):
        with self.assertRaises(ValueError) as err:
            answer("Who is the President of the United States?")
        self.assertEqual(type(err.exception), ValueError)
>       self.assertEqual(err.exception.args[0], "unknown operation")
E       AssertionError: 'syntax error' != 'unknown operation'
E       - syntax error
E       + unknown operation

wordy_test.py:68: AssertionError
_______________________ WordyTest.test_unknown_operation _______________________

self = <wordy_test.WordyTest testMethod=test_unknown_operation>

    def test_unknown_operation(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 52 cubed?")
        self.assertEqual(type(err.exception), ValueError)
>       self.assertEqual(err.exception.args[0], "unknown operation")
E       AssertionError: 'syntax error' != 'unknown operation'
E       - syntax error
E       + unknown operation

wordy_test.py:62: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED wordy_test.py::WordyTest::test_addition
PASSED wordy_test.py::WordyTest::test_addition_and_multiplication
PASSED wordy_test.py::WordyTest::test_addition_and_subtraction
PASSED wordy_test.py::WordyTest::test_addition_with_negative_numbers
PASSED wordy_test.py::WordyTest::test_division
PASSED wordy_test.py::WordyTest::test_just_a_number
PASSED wordy_test.py::WordyTest::test_large_addition
PASSED wordy_test.py::WordyTest::test_missing_number
PASSED wordy_test.py::WordyTest::test_missing_operation
PASSED wordy_test.py::WordyTest::test_more_addition
PASSED wordy_test.py::WordyTest::test_multiple_additions
PASSED wordy_test.py::WordyTest::test_multiple_division
PASSED wordy_test.py::WordyTest::test_multiple_multiplication
PASSED wordy_test.py::WordyTest::test_multiple_subtraction
PASSED wordy_test.py::WordyTest::test_multiplication
PASSED wordy_test.py::WordyTest::test_reject_postfix_notation
PASSED wordy_test.py::WordyTest::test_reject_prefix_notation
PASSED wordy_test.py::WordyTest::test_reject_problem_missing_an_operand
PASSED wordy_test.py::WordyTest::test_reject_problem_with_no_operands_or_operators
PASSED wordy_test.py::WordyTest::test_reject_two_numbers_in_a_row
PASSED wordy_test.py::WordyTest::test_reject_two_operations_in_a_row
PASSED wordy_test.py::WordyTest::test_subtraction
PASSED wordy_test.py::WordyTest::test_subtraction_then_addition
FAILED wordy_test.py::WordyTest::test_non_math_question - AssertionError: 'sy...
FAILED wordy_test.py::WordyTest::test_unknown_operation - AssertionError: 'sy...
========================= 2 failed, 23 passed in 0.55s =========================
