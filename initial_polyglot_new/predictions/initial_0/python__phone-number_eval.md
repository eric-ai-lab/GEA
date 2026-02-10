+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 21 items

phone_number_test.py .....................                               [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED phone_number_test.py::PhoneNumberTest::test_area_code
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
PASSED phone_number_test.py::PhoneNumberTest::test_pretty_print
PASSED phone_number_test.py::PhoneNumberTest::test_pretty_print_with_full_us_phone_number
PASSED phone_number_test.py::PhoneNumberTest::test_valid_when_11_digits_and_starting_with_1
PASSED phone_number_test.py::PhoneNumberTest::test_valid_when_11_digits_and_starting_with_1_even_with_punctuation
============================== 21 passed in 0.02s ==============================
