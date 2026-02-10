+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 21 items

phone_number_test.py F................FF..                               [100%]

=================================== FAILURES ===================================
________________________ PhoneNumberTest.test_area_code ________________________

self = <phone_number_test.PhoneNumberTest testMethod=test_area_code>

    def test_area_code(self):
        number = PhoneNumber("2234567890")
>       self.assertEqual(number.area_code, "223")
E       AttributeError: 'PhoneNumber' object has no attribute 'area_code'

phone_number_test.py:114: AttributeError
______________________ PhoneNumberTest.test_pretty_print _______________________

self = <phone_number_test.PhoneNumberTest testMethod=test_pretty_print>

    def test_pretty_print(self):
        number = PhoneNumber("2234567890")
>       self.assertEqual(number.pretty(), "(223)-456-7890")
E       AssertionError: '(223) 456-7890' != '(223)-456-7890'
E       - (223) 456-7890
E       ?      ^
E       + (223)-456-7890
E       ?      ^

phone_number_test.py:118: AssertionError
_________ PhoneNumberTest.test_pretty_print_with_full_us_phone_number __________

self = <phone_number_test.PhoneNumberTest testMethod=test_pretty_print_with_full_us_phone_number>

    def test_pretty_print_with_full_us_phone_number(self):
        number = PhoneNumber("12234567890")
>       self.assertEqual(number.pretty(), "(223)-456-7890")
E       AssertionError: '(223) 456-7890' != '(223)-456-7890'
E       - (223) 456-7890
E       ?      ^
E       + (223)-456-7890
E       ?      ^

phone_number_test.py:122: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED phone_number_test.py::PhoneNumberTest::test_cleans_numbers_with_dots
PASSED phone_number_test.py::PhoneNumberTest::test_cleans_numbers_with_multiple_spaces
PASSED phone_number_test.py::PhoneNumberTest::test_cleans_the_number
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_if_area_code_starts_with_0
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_if_area_code_starts_with_0_on_valid_11_digit_number
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_if_area_code_starts_with_1
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_if_area_code_starts_with_1_on_valid_11_digit_number
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_if_exchange_code_starts_with_0
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_if_exchange_code_starts_with_0_on_valid_11_digit_number
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_if_exchange_code_starts_with_1
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_if_exchange_code_starts_with_1_on_valid_11_digit_number
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_when_11_digits_does_not_start_with_a_1
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_when_9_digits
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_when_more_than_11_digits
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_with_letters
PASSED phone_number_test.py::PhoneNumberTest::test_invalid_with_punctuations
PASSED phone_number_test.py::PhoneNumberTest::test_valid_when_11_digits_and_starting_with_1
PASSED phone_number_test.py::PhoneNumberTest::test_valid_when_11_digits_and_starting_with_1_even_with_punctuation
FAILED phone_number_test.py::PhoneNumberTest::test_area_code - AttributeError...
FAILED phone_number_test.py::PhoneNumberTest::test_pretty_print - AssertionEr...
FAILED phone_number_test.py::PhoneNumberTest::test_pretty_print_with_full_us_phone_number
========================= 3 failed, 18 passed in 1.07s =========================
