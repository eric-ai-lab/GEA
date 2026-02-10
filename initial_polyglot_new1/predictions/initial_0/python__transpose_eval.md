+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 12 items

transpose_test.py ............                                           [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED transpose_test.py::TransposeTest::test_empty_string
PASSED transpose_test.py::TransposeTest::test_first_line_longer_than_second_line
PASSED transpose_test.py::TransposeTest::test_jagged_triangle
PASSED transpose_test.py::TransposeTest::test_mixed_line_length
PASSED transpose_test.py::TransposeTest::test_rectangle
PASSED transpose_test.py::TransposeTest::test_second_line_longer_than_first_line
PASSED transpose_test.py::TransposeTest::test_simple
PASSED transpose_test.py::TransposeTest::test_single_line
PASSED transpose_test.py::TransposeTest::test_square
PASSED transpose_test.py::TransposeTest::test_triangle
PASSED transpose_test.py::TransposeTest::test_two_characters_in_a_column
PASSED transpose_test.py::TransposeTest::test_two_characters_in_a_row
============================== 12 passed in 0.01s ==============================
