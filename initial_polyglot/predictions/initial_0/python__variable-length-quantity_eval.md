+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 26 items

variable_length_quantity_test.py ..........................              [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_arbitrary_double_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_arbitrary_quadruple_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_arbitrary_quintuple_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_arbitrary_single_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_arbitrary_triple_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_four_bytes
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_incomplete_sequence_causes_error
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_incomplete_sequence_causes_error_even_if_value_is_zero
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_largest_double_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_largest_quadruple_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_largest_single_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_largest_triple_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_many_multi_byte_values
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_maximum_32_bit_integer
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_maximum_32_bit_integer_input
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_multiple_values
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_one_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_smallest_double_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_smallest_quadruple_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_smallest_quintuple_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_smallest_triple_byte
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_three_bytes
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_two_bytes
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_two_multi_byte_values
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_two_single_byte_values
PASSED variable_length_quantity_test.py::VariableLengthQuantityTest::test_zero
============================== 26 passed in 0.22s ==============================
