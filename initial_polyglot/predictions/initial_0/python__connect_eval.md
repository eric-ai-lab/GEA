+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items

connect_test.py FFF.FF....                                               [100%]

=================================== FAILURES ===================================
________________ ConnectTest.test_an_empty_board_has_no_winner _________________

self = <connect_test.ConnectTest testMethod=test_an_empty_board_has_no_winner>

    def test_an_empty_board_has_no_winner(self):
        game = ConnectGame(
            """. . . . .
                . . . . .
                 . . . . .
                  . . . . .
                   . . . . ."""
        )
        winner = game.get_winner()
>       self.assertEqual(winner, "")
E       AssertionError: None != ''

connect_test.py:22: AssertionError
___________ ConnectTest.test_illegal_diagonal_does_not_make_a_winner ___________

self = <connect_test.ConnectTest testMethod=test_illegal_diagonal_does_not_make_a_winner>

    def test_illegal_diagonal_does_not_make_a_winner(self):
        game = ConnectGame(
            """X O . .
                O X X X
                 O X O .
                  . O X .
                   X X O O"""
        )
        winner = game.get_winner()
>       self.assertEqual(winner, "")
E       AssertionError: 'X' != ''
E       - X
E       +

connect_test.py:53: AssertionError
____________ ConnectTest.test_nobody_wins_crossing_adjacent_angles _____________

self = <connect_test.ConnectTest testMethod=test_nobody_wins_crossing_adjacent_angles>

    def test_nobody_wins_crossing_adjacent_angles(self):
        game = ConnectGame(
            """X . . .
                . X O .
                 O . X O
                  . O . X
                   . . O ."""
        )
        winner = game.get_winner()
>       self.assertEqual(winner, "")
E       AssertionError: 'X' != ''
E       - X
E       +

connect_test.py:64: AssertionError
_____________ ConnectTest.test_o_wins_crossing_from_top_to_bottom ______________

self = <connect_test.ConnectTest testMethod=test_o_wins_crossing_from_top_to_bottom>

    def test_o_wins_crossing_from_top_to_bottom(self):
        game = ConnectGame(
            """. O . .
                O X X X
                 O O O .
                  X X O X
                   . O X ."""
        )
        winner = game.get_winner()
>       self.assertEqual(winner, "O")
E       AssertionError: 'X' != 'O'
E       - X
E       + O

connect_test.py:86: AssertionError
______________ ConnectTest.test_only_edges_does_not_make_a_winner ______________

self = <connect_test.ConnectTest testMethod=test_only_edges_does_not_make_a_winner>

    def test_only_edges_does_not_make_a_winner(self):
        game = ConnectGame(
            """O O O X
                X . . X
                 X . . X
                  X O O O"""
        )
        winner = game.get_winner()
>       self.assertEqual(winner, "")
E       AssertionError: 'X' != ''
E       - X
E       +

connect_test.py:42: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED connect_test.py::ConnectTest::test_o_can_win_on_a_1x1_board
PASSED connect_test.py::ConnectTest::test_x_can_win_on_a_1x1_board
PASSED connect_test.py::ConnectTest::test_x_wins_crossing_from_left_to_right
PASSED connect_test.py::ConnectTest::test_x_wins_using_a_convoluted_path
PASSED connect_test.py::ConnectTest::test_x_wins_using_a_spiral_path
FAILED connect_test.py::ConnectTest::test_an_empty_board_has_no_winner - Asse...
FAILED connect_test.py::ConnectTest::test_illegal_diagonal_does_not_make_a_winner
FAILED connect_test.py::ConnectTest::test_nobody_wins_crossing_adjacent_angles
FAILED connect_test.py::ConnectTest::test_o_wins_crossing_from_top_to_bottom
FAILED connect_test.py::ConnectTest::test_only_edges_does_not_make_a_winner
========================= 5 failed, 5 passed in 1.99s ==========================
