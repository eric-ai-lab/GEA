+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 13 items

dominoes_test.py ..FFF....F...                                           [100%]

=================================== FAILURES ===================================
__________________ DominoesTest.test_disconnected_double_loop __________________

self = <dominoes_test.DominoesTest testMethod=test_disconnected_double_loop>

    def test_disconnected_double_loop(self):
        input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)]
        output_chain = can_chain(input_dominoes)
>       self.refute_correct_chain(input_dominoes, output_chain)

dominoes_test.py:51: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_disconnected_double_loop>
input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)]
output_chain = [(1, 2), (2, 1)]

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: [(1, 2), (2, 1)] is not None : There should be no valid chain for [(1, 2), (2, 1), (3, 4), (4, 3)]

dominoes_test.py:132: AssertionError
____________________ DominoesTest.test_disconnected_simple _____________________

self = <dominoes_test.DominoesTest testMethod=test_disconnected_simple>

    def test_disconnected_simple(self):
        input_dominoes = [(1, 1), (2, 2)]
        output_chain = can_chain(input_dominoes)
>       self.refute_correct_chain(input_dominoes, output_chain)

dominoes_test.py:46: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_disconnected_simple>
input_dominoes = [(1, 1), (2, 2)], output_chain = [(1, 1)]

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: [(1, 1)] is not None : There should be no valid chain for [(1, 1), (2, 2)]

dominoes_test.py:132: AssertionError
________________ DominoesTest.test_disconnected_single_isolated ________________

self = <dominoes_test.DominoesTest testMethod=test_disconnected_single_isolated>

    def test_disconnected_single_isolated(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 4)]
        output_chain = can_chain(input_dominoes)
>       self.refute_correct_chain(input_dominoes, output_chain)

dominoes_test.py:56: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_disconnected_single_isolated>
input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 4)]
output_chain = [(1, 3), (3, 2), (2, 1)]

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: [(1, 3), (3, 2), (2, 1)] is not None : There should be no valid chain for [(1, 2), (2, 3), (3, 1), (4, 4)]

dominoes_test.py:132: AssertionError
________________ DominoesTest.test_separate_three_domino_loops _________________

self = <dominoes_test.DominoesTest testMethod=test_separate_three_domino_loops>

    def test_separate_three_domino_loops(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
        output_chain = can_chain(input_dominoes)
>       self.refute_correct_chain(input_dominoes, output_chain)

dominoes_test.py:86: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_separate_three_domino_loops>
input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]
output_chain = [(1, 3), (3, 2), (2, 1)]

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: [(1, 3), (3, 2), (2, 1)] is not None : There should be no valid chain for [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]

dominoes_test.py:132: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED dominoes_test.py::DominoesTest::test_can_reverse_dominoes
PASSED dominoes_test.py::DominoesTest::test_can_t_be_chained
PASSED dominoes_test.py::DominoesTest::test_empty_input_empty_output
PASSED dominoes_test.py::DominoesTest::test_need_backtrack
PASSED dominoes_test.py::DominoesTest::test_nine_elements
PASSED dominoes_test.py::DominoesTest::test_separate_loops
PASSED dominoes_test.py::DominoesTest::test_singleton_input_singleton_output
PASSED dominoes_test.py::DominoesTest::test_singleton_that_can_t_be_chained
PASSED dominoes_test.py::DominoesTest::test_three_elements
FAILED dominoes_test.py::DominoesTest::test_disconnected_double_loop - Assert...
FAILED dominoes_test.py::DominoesTest::test_disconnected_simple - AssertionEr...
FAILED dominoes_test.py::DominoesTest::test_disconnected_single_isolated - As...
FAILED dominoes_test.py::DominoesTest::test_separate_three_domino_loops - Ass...
========================= 4 failed, 9 passed in 0.37s ==========================
