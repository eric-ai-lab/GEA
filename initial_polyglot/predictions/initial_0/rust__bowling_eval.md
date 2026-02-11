+ cargo test -- --include-ignored
   Compiling bowling v1.2.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.41s
     Running unittests src/lib.rs (target/debug/deps/bowling-b320769701906fad)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/bowling.rs (target/debug/deps/bowling-a3910bd408639e57)

running 31 tests
test a_game_score_is_none_if_fewer_than_ten_frames_have_been_rolled ... ok
test a_game_score_is_some_if_ten_frames_have_been_rolled ... ok
test a_roll_is_err_if_the_game_is_done ... ok
test a_spare_with_the_two_roll_bonus_does_not_get_a_bonus_roll ... ok
test a_strike_earns_ten_points_in_a_frame_with_a_single_roll ... ok
test a_strike_in_the_last_frame_earns_a_two_roll_bonus_that_is_counted_once ... ok
test a_strike_with_the_one_roll_bonus_after_a_spare_in_the_last_frame_does_not_get_a_bonus ... ok
test all_strikes_is_a_perfect_score_of_300 ... ok
test cannot_roll_after_bonus_roll_for_spare ... ok
test cannot_roll_after_bonus_roll_for_strike ... ok
test consecutive_spares_each_get_a_one_roll_bonus ... ok
test consecutive_strikes_each_get_the_two_roll_bonus ... ok
test first_bonus_ball_after_a_final_strike_cannot_score_an_invalid_number_of_pins ... ok
test if_the_last_frame_is_a_spare_you_cannot_create_a_score_before_extra_roll_is_taken ... ok
test if_the_last_frame_is_a_spare_you_get_one_extra_roll_that_is_scored_once ... ok
test if_the_last_frame_is_a_strike_you_cannot_score_before_the_extra_rolls_are_taken ... ok
test last_two_strikes_followed_by_only_last_bonus_with_non_strike_points ... ok
test points_scored_in_the_roll_after_a_spare_are_counted_twice_as_a_bonus ... ok
test points_scored_in_the_two_rolls_after_a_strike_are_counted_twice_as_a_bonus ... ok
test roll_returns_a_result ... ok
test second_bonus_ball_after_a_final_strike_cannot_score_an_invalid_number_of_pins_even_if_first_is_strike ... ok
test spare_in_the_first_frame_followed_by_zeros ... ok
test strikes_with_the_two_roll_bonus_do_not_get_a_bonus_roll ... ok
test ten_frames_without_a_strike_or_spare ... ok
test the_two_balls_after_a_final_strike_can_be_a_strike_and_non_strike ... ok
test the_two_balls_after_a_final_strike_cannot_be_a_non_strike_followed_by_a_strike ... FAILED
test the_two_balls_after_a_final_strike_cannot_score_an_invalid_number_of_pins ... FAILED
test twenty_zero_pin_rolls_scores_zero ... ok
test you_cannot_roll_more_than_ten_pins_in_a_single_frame ... ok
test you_cannot_roll_more_than_ten_pins_in_a_single_roll ... ok
test you_cannot_score_a_game_with_no_rolls ... ok

failures:

---- the_two_balls_after_a_final_strike_cannot_be_a_non_strike_followed_by_a_strike stdout ----

thread 'the_two_balls_after_a_final_strike_cannot_be_a_non_strike_followed_by_a_strike' (5590) panicked at tests/bowling.rs:343:5:
assertion `left == right` failed
  left: Ok(())
 right: Err(NotEnoughPinsLeft)
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- the_two_balls_after_a_final_strike_cannot_score_an_invalid_number_of_pins stdout ----

thread 'the_two_balls_after_a_final_strike_cannot_score_an_invalid_number_of_pins' (5591) panicked at tests/bowling.rs:313:5:
assertion `left == right` failed
  left: Ok(())
 right: Err(NotEnoughPinsLeft)


failures:
    the_two_balls_after_a_final_strike_cannot_be_a_non_strike_followed_by_a_strike
    the_two_balls_after_a_final_strike_cannot_score_an_invalid_number_of_pins

test result: FAILED. 29 passed; 2 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

error: test failed, to rerun pass `--test bowling`
