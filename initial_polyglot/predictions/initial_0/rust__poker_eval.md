+ cargo test -- --include-ignored
   Compiling poker v1.1.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 1.13s
     Running unittests src/lib.rs (target/debug/deps/poker-f70f1a321c61ee78)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/poker.rs (target/debug/deps/poker-b9f221fc6801a510)

running 37 tests
test a_straight_beats_three_of_a_kind ... ok
test a_tie_has_multiple_winners ... FAILED
test aces_can_end_a_straight_flush_10_j_q_k_a ... FAILED
test aces_can_end_a_straight_10_j_q_k_a ... FAILED
test aces_can_start_a_straight_a_2_3_4_5 ... ok
test aces_can_start_a_straight_flush_a_2_3_4_5 ... ok
test aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3 ... FAILED
test aces_cannot_be_in_the_middle_of_a_straight_q_k_a_2_3 ... ok
test both_hands_have_a_flush_tie_goes_to_high_card_down_to_the_last_one_if_necessary ... ok
test both_hands_have_a_full_house_tie_goes_to_highest_ranked_triplet ... ok
test both_hands_have_four_of_a_kind_tie_goes_to_high_quad ... ok
test both_hands_have_a_straight_flush_tie_goes_to_highest_ranked_card ... ok
test both_hands_have_three_of_a_kind_tie_goes_to_highest_ranked_triplet ... ok
test both_hands_have_the_same_pair_high_card_wins ... ok
test both_hands_have_two_pairs_highest_ranked_pair_wins ... ok
test both_hands_have_two_identically_ranked_pairs_tie_goes_to_remaining_card_kicker ... ok
test both_hands_with_a_straight_tie_goes_to_highest_ranked_card ... ok
test both_hands_have_two_pairs_with_the_same_highest_ranked_pair_tie_goes_to_low_pair ... ok
test even_though_an_ace_is_usually_high_a_5_high_straight_flush_is_the_lowest_scoring_straight_flush ... ok
test both_hands_have_two_pairs_that_add_to_the_same_value_win_goes_to_highest_pair ... ok
test four_of_a_kind_beats_a_full_house ... ok
test even_though_an_ace_is_usually_high_a_5_high_straight_is_the_lowest_scoring_straight ... ok
test full_house_beats_a_flush ... ok
test highest_pair_wins ... ok
test flush_beats_a_straight ... ok
test multiple_hands_with_the_same_high_cards_tie_compares_next_highest_ranked_down_to_last_card ... ok
test highest_card_out_of_all_hands_wins ... FAILED
test one_pair_beats_high_card ... ok
test straight_flush_beats_four_of_a_kind ... FAILED
test single_hand_always_wins ... ok
test two_pairs_beats_one_pair ... ok
test two_pairs_first_ranked_by_largest_pair ... ok
test winning_high_card_hand_also_has_the_lowest_card ... ok
test with_multiple_decks_both_hands_have_a_full_house_with_the_same_triplet_tie_goes_to_the_pair ... ok
test with_multiple_decks_two_players_can_have_same_three_of_a_kind_ties_go_to_highest_remaining_cards ... ok
test with_multiple_decks_both_hands_with_identical_four_of_a_kind_tie_determined_by_kicker ... ok
test three_of_a_kind_beats_two_pair ... ok

failures:

---- a_tie_has_multiple_winners stdout ----

thread 'a_tie_has_multiple_winners' panicked at src/lib.rs:37:22:
Invalid rank: 1
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- aces_can_end_a_straight_flush_10_j_q_k_a stdout ----

thread 'aces_can_end_a_straight_flush_10_j_q_k_a' panicked at src/lib.rs:37:22:
Invalid rank: 1

---- aces_can_end_a_straight_10_j_q_k_a stdout ----

thread 'aces_can_end_a_straight_10_j_q_k_a' panicked at src/lib.rs:37:22:
Invalid rank: 1

---- aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3 stdout ----

thread 'aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3' panicked at src/lib.rs:37:22:
Invalid rank: 1

---- highest_card_out_of_all_hands_wins stdout ----

thread 'highest_card_out_of_all_hands_wins' panicked at src/lib.rs:37:22:
Invalid rank: 1

---- straight_flush_beats_four_of_a_kind stdout ----

thread 'straight_flush_beats_four_of_a_kind' panicked at src/lib.rs:37:22:
Invalid rank: 1


failures:
    a_tie_has_multiple_winners
    aces_can_end_a_straight_10_j_q_k_a
    aces_can_end_a_straight_flush_10_j_q_k_a
    aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3
    highest_card_out_of_all_hands_wins
    straight_flush_beats_four_of_a_kind

test result: FAILED. 31 passed; 6 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

error: test failed, to rerun pass `--test poker`
