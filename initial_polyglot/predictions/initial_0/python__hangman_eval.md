+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 7 items

hangman_test.py F.F...F                                                  [100%]

=================================== FAILURES ===================================
_____________ HangmanTests.test_after_10_failures_the_game_is_over _____________

self = <hangman_test.HangmanTests testMethod=test_after_10_failures_the_game_is_over>

    def test_after_10_failures_the_game_is_over(self):
        game = Hangman('foo')
    
        for i in range(10):
            game.guess('x')
    
>       self.assertEqual(game.get_status(), hangman.STATUS_LOSE)
E       AssertionError: 'ongoing' != 'lose'
E       - ongoing
E       + lose

hangman_test.py:26: AssertionError
_____ HangmanTests.test_feeding_a_correct_letter_twice_counts_as_a_failure _____

self = <hangman_test.HangmanTests testMethod=test_feeding_a_correct_letter_twice_counts_as_a_failure>

    def test_feeding_a_correct_letter_twice_counts_as_a_failure(self):
        game = Hangman('foobar')
    
        game.guess('b')
        self.assertEqual(game.get_status(), hangman.STATUS_ONGOING)
        self.assertEqual(game.remaining_guesses, 9)
        self.assertEqual(game.get_masked_word(), '___b__')
    
        game.guess('b')
        self.assertEqual(game.get_status(), hangman.STATUS_ONGOING)
>       self.assertEqual(game.remaining_guesses, 8)
E       AssertionError: 9 != 8

hangman_test.py:55: AssertionError
________ HangmanTests.test_winning_on_last_guess_still_counts_as_a_win _________

self = <hangman_test.HangmanTests testMethod=test_winning_on_last_guess_still_counts_as_a_win>

    def test_winning_on_last_guess_still_counts_as_a_win(self):
        game = Hangman('aaa')
        for ch in 'bcdefghij':
            game.guess(ch)
>       game.guess('a')

hangman_test.py:94: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <hangman.Hangman object at 0x70f80b97b390>, char = 'a'

    def guess(self, char):
        if self.status != STATUS_ONGOING:
>           raise ValueError("The game has already ended.")
E           ValueError: The game has already ended.

hangman.py:17: ValueError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED hangman_test.py::HangmanTests::test_feeding_a_correct_letter_removes_underscores
PASSED hangman_test.py::HangmanTests::test_getting_all_the_letters_right_makes_for_a_win
PASSED hangman_test.py::HangmanTests::test_initially_9_failures_are_allowed
PASSED hangman_test.py::HangmanTests::test_initially_no_letters_are_guessed
FAILED hangman_test.py::HangmanTests::test_after_10_failures_the_game_is_over
FAILED hangman_test.py::HangmanTests::test_feeding_a_correct_letter_twice_counts_as_a_failure
FAILED hangman_test.py::HangmanTests::test_winning_on_last_guess_still_counts_as_a_win
========================= 3 failed, 4 passed in 0.13s ==========================
