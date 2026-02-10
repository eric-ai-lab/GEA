+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 31 items

bowling_test.py ...........................F.F.                          [100%]

=================================== FAILURES ===================================
_ BowlingTest.test_the_second_bonus_rolls_after_a_strike_in_the_last_frame_cannot_be_a_strike_if_the_first_one_is_not_a_strike _

self = <bowling_test.BowlingTest testMethod=test_the_second_bonus_rolls_after_a_strike_in_the_last_frame_cannot_be_a_strike_if_the_first_one_is_not_a_strike>

    def test_the_second_bonus_rolls_after_a_strike_in_the_last_frame_cannot_be_a_strike_if_the_first_one_is_not_a_strike(
        self,
    ):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6]
        game = self.roll_new_game(rolls)
>       with self.assertRaisesWithMessage(Exception):
E       AssertionError: Exception not raised

bowling_test.py:146: AssertionError
_ BowlingTest.test_two_bonus_rolls_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points _

self = <bowling_test.BowlingTest testMethod=test_two_bonus_rolls_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points>

    def test_two_bonus_rolls_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points(
        self,
    ):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5]
        game = self.roll_new_game(rolls)
>       with self.assertRaisesWithMessage(Exception):
E       AssertionError: Exception not raised

bowling_test.py:131: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED bowling_test.py::BowlingTest::test_a_roll_cannot_score_more_than_10_points
PASSED bowling_test.py::BowlingTest::test_a_spare_followed_by_zeros_is_worth_ten_points
PASSED bowling_test.py::BowlingTest::test_a_spare_in_the_last_frame_gets_a_one_roll_bonus_that_is_counted_once
PASSED bowling_test.py::BowlingTest::test_a_strike_earns_ten_points_in_a_frame_with_a_single_roll
PASSED bowling_test.py::BowlingTest::test_a_strike_in_the_last_frame_gets_a_two_roll_bonus_that_is_counted_once
PASSED bowling_test.py::BowlingTest::test_a_strike_with_the_one_roll_bonus_after_a_spare_in_the_last_frame_does_not_get_a_bonus
PASSED bowling_test.py::BowlingTest::test_all_strikes_is_a_perfect_game
PASSED bowling_test.py::BowlingTest::test_an_incomplete_game_cannot_be_scored
PASSED bowling_test.py::BowlingTest::test_an_unstarted_game_cannot_be_scored
PASSED bowling_test.py::BowlingTest::test_bonus_roll_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points
PASSED bowling_test.py::BowlingTest::test_bonus_roll_for_a_spare_in_the_last_frame_must_be_rolled_before_score_can_be_calculated
PASSED bowling_test.py::BowlingTest::test_bonus_rolls_for_a_strike_in_the_last_frame_must_be_rolled_before_score_can_be_calculated
PASSED bowling_test.py::BowlingTest::test_both_bonus_rolls_for_a_strike_in_the_last_frame_must_be_rolled_before_score_can_be_calculated
PASSED bowling_test.py::BowlingTest::test_cannot_roll_after_bonus_roll_for_spare
PASSED bowling_test.py::BowlingTest::test_cannot_roll_after_bonus_rolls_for_strike
PASSED bowling_test.py::BowlingTest::test_cannot_roll_if_game_already_has_ten_frames
PASSED bowling_test.py::BowlingTest::test_consecutive_spares_each_get_a_one_roll_bonus
PASSED bowling_test.py::BowlingTest::test_consecutive_strikes_each_get_the_two_roll_bonus
PASSED bowling_test.py::BowlingTest::test_last_two_strikes_followed_by_only_last_bonus_with_non_strike_points
PASSED bowling_test.py::BowlingTest::test_points_scored_in_the_roll_after_a_spare_are_counted_twice
PASSED bowling_test.py::BowlingTest::test_points_scored_in_the_two_rolls_after_a_strike_are_counted_twice_as_a_bonus
PASSED bowling_test.py::BowlingTest::test_rolling_a_spare_with_the_two_roll_bonus_does_not_get_a_bonus_roll
PASSED bowling_test.py::BowlingTest::test_rolls_cannot_score_negative_points
PASSED bowling_test.py::BowlingTest::test_second_bonus_roll_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points
PASSED bowling_test.py::BowlingTest::test_should_be_able_to_score_a_game_with_all_zeros
PASSED bowling_test.py::BowlingTest::test_should_be_able_to_score_a_game_with_no_strikes_or_spares
PASSED bowling_test.py::BowlingTest::test_strikes_with_the_two_roll_bonus_do_not_get_bonus_rolls
PASSED bowling_test.py::BowlingTest::test_two_bonus_rolls_after_a_strike_in_the_last_frame_can_score_more_than_10_points_if_one_is_a_strike
PASSED bowling_test.py::BowlingTest::test_two_rolls_in_a_frame_cannot_score_more_than_10_points
FAILED bowling_test.py::BowlingTest::test_the_second_bonus_rolls_after_a_strike_in_the_last_frame_cannot_be_a_strike_if_the_first_one_is_not_a_strike
FAILED bowling_test.py::BowlingTest::test_two_bonus_rolls_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points
========================= 2 failed, 29 passed in 0.35s =========================
