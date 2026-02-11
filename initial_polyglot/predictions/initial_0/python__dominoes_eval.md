+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: asyncio-1.3.0, anyio-4.12.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 13 items

dominoes_test.py FFFFFFFFFFFFF                                           [100%]

=================================== FAILURES ===================================
____________________ DominoesTest.test_can_reverse_dominoes ____________________

self = <dominoes_test.DominoesTest testMethod=test_can_reverse_dominoes>

    def test_can_reverse_dominoes(self):
        input_dominoes = [(1, 2), (1, 3), (2, 3)]
        output_chain = can_chain(input_dominoes)
>       self.assert_correct_chain(input_dominoes, output_chain)

dominoes_test.py:36: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_can_reverse_dominoes>
input_dominoes = [(1, 2), (1, 3), (2, 3)], output_chain = True

    def assert_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be a chain for {}".format(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
>       self.assert_same_dominoes(input_dominoes, output_chain)

dominoes_test.py:124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_can_reverse_dominoes>
input_dominoes = [(1, 2), (1, 3), (2, 3)], output_chain = True

    def assert_same_dominoes(self, input_dominoes, output_chain):
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
>       output_normal = self.normalize_dominoes(output_chain)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dominoes_test.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_can_reverse_dominoes>
dominoes = True

    def normalize_dominoes(self, dominoes):
>       return list(sorted(tuple(sorted(domino)) for domino in dominoes))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: 'bool' object is not iterable

dominoes_test.py:91: TypeError
______________________ DominoesTest.test_can_t_be_chained ______________________

self = <dominoes_test.DominoesTest testMethod=test_can_t_be_chained>

    def test_can_t_be_chained(self):
        input_dominoes = [(1, 2), (4, 1), (2, 3)]
        output_chain = can_chain(input_dominoes)
>       self.refute_correct_chain(input_dominoes, output_chain)

dominoes_test.py:41: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_can_t_be_chained>
input_dominoes = [(1, 2), (4, 1), (2, 3)], output_chain = False

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: False is not None : There should be no valid chain for [(1, 2), (4, 1), (2, 3)]

dominoes_test.py:132: AssertionError
__________________ DominoesTest.test_disconnected_double_loop __________________

self = <dominoes_test.DominoesTest testMethod=test_disconnected_double_loop>

    def test_disconnected_double_loop(self):
        input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)]
        output_chain = can_chain(input_dominoes)
>       self.refute_correct_chain(input_dominoes, output_chain)

dominoes_test.py:51: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_disconnected_double_loop>
input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)], output_chain = False

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: False is not None : There should be no valid chain for [(1, 2), (2, 1), (3, 4), (4, 3)]

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
input_dominoes = [(1, 1), (2, 2)], output_chain = False

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: False is not None : There should be no valid chain for [(1, 1), (2, 2)]

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
input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 4)], output_chain = False

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: False is not None : There should be no valid chain for [(1, 2), (2, 3), (3, 1), (4, 4)]

dominoes_test.py:132: AssertionError
__________________ DominoesTest.test_empty_input_empty_output __________________

self = <dominoes_test.DominoesTest testMethod=test_empty_input_empty_output>

    def test_empty_input_empty_output(self):
        input_dominoes = []
        output_chain = can_chain(input_dominoes)
>       self.assert_correct_chain(input_dominoes, output_chain)

dominoes_test.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_empty_input_empty_output>
input_dominoes = [], output_chain = True

    def assert_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be a chain for {}".format(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
>       self.assert_same_dominoes(input_dominoes, output_chain)

dominoes_test.py:124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_empty_input_empty_output>
input_dominoes = [], output_chain = True

    def assert_same_dominoes(self, input_dominoes, output_chain):
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
>       output_normal = self.normalize_dominoes(output_chain)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dominoes_test.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_empty_input_empty_output>
dominoes = True

    def normalize_dominoes(self, dominoes):
>       return list(sorted(tuple(sorted(domino)) for domino in dominoes))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: 'bool' object is not iterable

dominoes_test.py:91: TypeError
_______________________ DominoesTest.test_need_backtrack _______________________

self = <dominoes_test.DominoesTest testMethod=test_need_backtrack>

    def test_need_backtrack(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
        output_chain = can_chain(input_dominoes)
>       self.assert_correct_chain(input_dominoes, output_chain)

dominoes_test.py:61: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_need_backtrack>
input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)], output_chain = True

    def assert_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be a chain for {}".format(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
>       self.assert_same_dominoes(input_dominoes, output_chain)

dominoes_test.py:124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_need_backtrack>
input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)], output_chain = True

    def assert_same_dominoes(self, input_dominoes, output_chain):
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
>       output_normal = self.normalize_dominoes(output_chain)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dominoes_test.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_need_backtrack>
dominoes = True

    def normalize_dominoes(self, dominoes):
>       return list(sorted(tuple(sorted(domino)) for domino in dominoes))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: 'bool' object is not iterable

dominoes_test.py:91: TypeError
_______________________ DominoesTest.test_nine_elements ________________________

self = <dominoes_test.DominoesTest testMethod=test_nine_elements>

    def test_nine_elements(self):
        input_dominoes = [
            (1, 2),
            (5, 3),
            (3, 1),
            (1, 2),
            (2, 4),
            (1, 6),
            (2, 3),
            (3, 4),
            (5, 6),
        ]
        output_chain = can_chain(input_dominoes)
>       self.assert_correct_chain(input_dominoes, output_chain)

dominoes_test.py:81: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_nine_elements>
input_dominoes = [(1, 2), (5, 3), (3, 1), (1, 2), (2, 4), (1, 6), ...]
output_chain = True

    def assert_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be a chain for {}".format(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
>       self.assert_same_dominoes(input_dominoes, output_chain)

dominoes_test.py:124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_nine_elements>
input_dominoes = [(1, 2), (5, 3), (3, 1), (1, 2), (2, 4), (1, 6), ...]
output_chain = True

    def assert_same_dominoes(self, input_dominoes, output_chain):
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
>       output_normal = self.normalize_dominoes(output_chain)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dominoes_test.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_nine_elements>
dominoes = True

    def normalize_dominoes(self, dominoes):
>       return list(sorted(tuple(sorted(domino)) for domino in dominoes))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: 'bool' object is not iterable

dominoes_test.py:91: TypeError
_______________________ DominoesTest.test_separate_loops _______________________

self = <dominoes_test.DominoesTest testMethod=test_separate_loops>

    def test_separate_loops(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
        output_chain = can_chain(input_dominoes)
>       self.assert_correct_chain(input_dominoes, output_chain)

dominoes_test.py:66: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_separate_loops>
input_dominoes = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
output_chain = True

    def assert_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be a chain for {}".format(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
>       self.assert_same_dominoes(input_dominoes, output_chain)

dominoes_test.py:124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_separate_loops>
input_dominoes = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
output_chain = True

    def assert_same_dominoes(self, input_dominoes, output_chain):
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
>       output_normal = self.normalize_dominoes(output_chain)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dominoes_test.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_separate_loops>
dominoes = True

    def normalize_dominoes(self, dominoes):
>       return list(sorted(tuple(sorted(domino)) for domino in dominoes))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: 'bool' object is not iterable

dominoes_test.py:91: TypeError
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
output_chain = False

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: False is not None : There should be no valid chain for [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 4)]

dominoes_test.py:132: AssertionError
______________ DominoesTest.test_singleton_input_singleton_output ______________

self = <dominoes_test.DominoesTest testMethod=test_singleton_input_singleton_output>

    def test_singleton_input_singleton_output(self):
        input_dominoes = [(1, 1)]
        output_chain = can_chain(input_dominoes)
>       self.assert_correct_chain(input_dominoes, output_chain)

dominoes_test.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_singleton_input_singleton_output>
input_dominoes = [(1, 1)], output_chain = True

    def assert_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be a chain for {}".format(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
>       self.assert_same_dominoes(input_dominoes, output_chain)

dominoes_test.py:124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_singleton_input_singleton_output>
input_dominoes = [(1, 1)], output_chain = True

    def assert_same_dominoes(self, input_dominoes, output_chain):
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
>       output_normal = self.normalize_dominoes(output_chain)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dominoes_test.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_singleton_input_singleton_output>
dominoes = True

    def normalize_dominoes(self, dominoes):
>       return list(sorted(tuple(sorted(domino)) for domino in dominoes))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: 'bool' object is not iterable

dominoes_test.py:91: TypeError
______________ DominoesTest.test_singleton_that_can_t_be_chained _______________

self = <dominoes_test.DominoesTest testMethod=test_singleton_that_can_t_be_chained>

    def test_singleton_that_can_t_be_chained(self):
        input_dominoes = [(1, 2)]
        output_chain = can_chain(input_dominoes)
>       self.refute_correct_chain(input_dominoes, output_chain)

dominoes_test.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_singleton_that_can_t_be_chained>
input_dominoes = [(1, 2)], output_chain = False

    def refute_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be no valid chain for {}".format(input_dominoes)
>       self.assertIsNone(output_chain, msg)
E       AssertionError: False is not None : There should be no valid chain for [(1, 2)]

dominoes_test.py:132: AssertionError
_______________________ DominoesTest.test_three_elements _______________________

self = <dominoes_test.DominoesTest testMethod=test_three_elements>

    def test_three_elements(self):
        input_dominoes = [(1, 2), (3, 1), (2, 3)]
        output_chain = can_chain(input_dominoes)
>       self.assert_correct_chain(input_dominoes, output_chain)

dominoes_test.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_three_elements>
input_dominoes = [(1, 2), (3, 1), (2, 3)], output_chain = True

    def assert_correct_chain(self, input_dominoes, output_chain):
        msg = "There should be a chain for {}".format(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
>       self.assert_same_dominoes(input_dominoes, output_chain)

dominoes_test.py:124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_three_elements>
input_dominoes = [(1, 2), (3, 1), (2, 3)], output_chain = True

    def assert_same_dominoes(self, input_dominoes, output_chain):
        msg = (
            "Dominoes used in the output must be the same "
            "as the ones given in the input"
        )
        input_normal = self.normalize_dominoes(input_dominoes)
>       output_normal = self.normalize_dominoes(output_chain)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

dominoes_test.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dominoes_test.DominoesTest testMethod=test_three_elements>
dominoes = True

    def normalize_dominoes(self, dominoes):
>       return list(sorted(tuple(sorted(domino)) for domino in dominoes))
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: 'bool' object is not iterable

dominoes_test.py:91: TypeError
=========================== short test summary info ============================
FAILED dominoes_test.py::DominoesTest::test_can_reverse_dominoes - TypeError:...
FAILED dominoes_test.py::DominoesTest::test_can_t_be_chained - AssertionError...
FAILED dominoes_test.py::DominoesTest::test_disconnected_double_loop - Assert...
FAILED dominoes_test.py::DominoesTest::test_disconnected_simple - AssertionEr...
FAILED dominoes_test.py::DominoesTest::test_disconnected_single_isolated - As...
FAILED dominoes_test.py::DominoesTest::test_empty_input_empty_output - TypeEr...
FAILED dominoes_test.py::DominoesTest::test_need_backtrack - TypeError: 'bool...
FAILED dominoes_test.py::DominoesTest::test_nine_elements - TypeError: 'bool'...
FAILED dominoes_test.py::DominoesTest::test_separate_loops - TypeError: 'bool...
FAILED dominoes_test.py::DominoesTest::test_separate_three_domino_loops - Ass...
FAILED dominoes_test.py::DominoesTest::test_singleton_input_singleton_output
FAILED dominoes_test.py::DominoesTest::test_singleton_that_can_t_be_chained
FAILED dominoes_test.py::DominoesTest::test_three_elements - TypeError: 'bool...
============================== 13 failed in 0.09s ==============================
