+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
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
============================== 12 passed in 0.02s ==============================
