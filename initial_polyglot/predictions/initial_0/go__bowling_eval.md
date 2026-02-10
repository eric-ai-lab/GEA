+ go test ./...
--- FAIL: TestRoll (0.00s)
    --- FAIL: TestRoll/two_rolls_in_a_frame_cannot_score_more_than_10_points (0.00s)
        bowling_test.go:32: Roll(6) after Previous Rolls: []int{5} expected an error, got nil
            	Explanation: Pin count exceeds pins on the lane
    --- FAIL: TestRoll/two_bonus_rolls_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points (0.00s)
        bowling_test.go:32: Roll(6) after Previous Rolls: []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5} expected an error, got nil
            	Explanation: Pin count exceeds pins on the lane
    --- FAIL: TestRoll/the_second_bonus_rolls_after_a_strike_in_the_last_frame_cannot_be_a_strike_if_the_first_one_is_not_a_strike (0.00s)
        bowling_test.go:32: Roll(10) after Previous Rolls: []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 6} expected an error, got nil
            	Explanation: Pin count exceeds pins on the lane
    --- FAIL: TestRoll/cannot_roll_if_game_already_has_ten_frames (0.00s)
        bowling_test.go:32: Roll(0) after Previous Rolls: []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0} expected an error, got nil
            	Explanation: Cannot roll after game is over
    --- FAIL: TestRoll/cannot_roll_after_bonus_roll_for_spare (0.00s)
        bowling_test.go:32: Roll(2) after Previous Rolls: []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 2} expected an error, got nil
            	Explanation: Cannot roll after game is over
    --- FAIL: TestRoll/cannot_roll_after_bonus_rolls_for_strike (0.00s)
        bowling_test.go:32: Roll(2) after Previous Rolls: []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 3, 2} expected an error, got nil
            	Explanation: Cannot roll after game is over
FAIL
FAIL	bowling	0.059s
FAIL
