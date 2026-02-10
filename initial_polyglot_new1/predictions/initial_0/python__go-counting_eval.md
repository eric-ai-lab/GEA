+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 11 items

go_counting_test.py ...........                                          [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED go_counting_test.py::GoCountingTest::test_a_stone_and_not_a_territory_on_5x5_board
PASSED go_counting_test.py::GoCountingTest::test_black_corner_territory_on_5x5_board
PASSED go_counting_test.py::GoCountingTest::test_invalid_because_x_is_too_high_for_5x5_board
PASSED go_counting_test.py::GoCountingTest::test_invalid_because_x_is_too_low_for_5x5_board
PASSED go_counting_test.py::GoCountingTest::test_invalid_because_y_is_too_high_for_5x5_board
PASSED go_counting_test.py::GoCountingTest::test_invalid_because_y_is_too_low_for_5x5_board
PASSED go_counting_test.py::GoCountingTest::test_one_territory_is_the_whole_board
PASSED go_counting_test.py::GoCountingTest::test_open_corner_territory_on_5x5_board
PASSED go_counting_test.py::GoCountingTest::test_two_region_rectangular_board
PASSED go_counting_test.py::GoCountingTest::test_two_territory_rectangular_board
PASSED go_counting_test.py::GoCountingTest::test_white_center_territory_on_5x5_board
============================== 11 passed in 0.01s ==============================
