+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
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
============================== 26 passed in 0.02s ==============================
