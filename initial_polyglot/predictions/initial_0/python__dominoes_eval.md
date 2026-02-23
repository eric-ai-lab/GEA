+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 13 items

dominoes_test.py .............                                           [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED dominoes_test.py::DominoesTest::test_can_reverse_dominoes
PASSED dominoes_test.py::DominoesTest::test_can_t_be_chained
PASSED dominoes_test.py::DominoesTest::test_disconnected_double_loop
PASSED dominoes_test.py::DominoesTest::test_disconnected_simple
PASSED dominoes_test.py::DominoesTest::test_disconnected_single_isolated
PASSED dominoes_test.py::DominoesTest::test_empty_input_empty_output
PASSED dominoes_test.py::DominoesTest::test_need_backtrack
PASSED dominoes_test.py::DominoesTest::test_nine_elements
PASSED dominoes_test.py::DominoesTest::test_separate_loops
PASSED dominoes_test.py::DominoesTest::test_separate_three_domino_loops
PASSED dominoes_test.py::DominoesTest::test_singleton_input_singleton_output
PASSED dominoes_test.py::DominoesTest::test_singleton_that_can_t_be_chained
PASSED dominoes_test.py::DominoesTest::test_three_elements
============================== 13 passed in 0.02s ==============================
