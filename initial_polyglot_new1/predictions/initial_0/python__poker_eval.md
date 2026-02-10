+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: asyncio-1.3.0, anyio-4.12.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 37 items

poker_test.py .....................................                      [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED poker_test.py::PokerTest::test_a_straight_beats_three_of_a_kind
PASSED poker_test.py::PokerTest::test_a_tie_has_multiple_winners
PASSED poker_test.py::PokerTest::test_aces_can_end_a_straight_10_j_q_k_a
PASSED poker_test.py::PokerTest::test_aces_can_end_a_straight_flush_10_j_q_k_a
PASSED poker_test.py::PokerTest::test_aces_can_start_a_straight_a_2_3_4_5
PASSED poker_test.py::PokerTest::test_aces_can_start_a_straight_flush_a_2_3_4_5
PASSED poker_test.py::PokerTest::test_aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3
PASSED poker_test.py::PokerTest::test_aces_cannot_be_in_the_middle_of_a_straight_q_k_a_2_3
PASSED poker_test.py::PokerTest::test_both_hands_have_a_flush_tie_goes_to_high_card_down_to_the_last_one_if_necessary
PASSED poker_test.py::PokerTest::test_both_hands_have_a_full_house_tie_goes_to_highest_ranked_triplet
PASSED poker_test.py::PokerTest::test_both_hands_have_a_straight_flush_tie_goes_to_highest_ranked_card
PASSED poker_test.py::PokerTest::test_both_hands_have_four_of_a_kind_tie_goes_to_high_quad
PASSED poker_test.py::PokerTest::test_both_hands_have_the_same_pair_high_card_wins
PASSED poker_test.py::PokerTest::test_both_hands_have_three_of_a_kind_tie_goes_to_highest_ranked_triplet
PASSED poker_test.py::PokerTest::test_both_hands_have_two_identically_ranked_pairs_tie_goes_to_remaining_card_kicker
PASSED poker_test.py::PokerTest::test_both_hands_have_two_pairs_highest_ranked_pair_wins
PASSED poker_test.py::PokerTest::test_both_hands_have_two_pairs_that_add_to_the_same_value_win_goes_to_highest_pair
PASSED poker_test.py::PokerTest::test_both_hands_have_two_pairs_with_the_same_highest_ranked_pair_tie_goes_to_low_pair
PASSED poker_test.py::PokerTest::test_both_hands_with_a_straight_tie_goes_to_highest_ranked_card
PASSED poker_test.py::PokerTest::test_even_though_an_ace_is_usually_high_a_5_high_straight_flush_is_the_lowest_scoring_straight_flush
PASSED poker_test.py::PokerTest::test_even_though_an_ace_is_usually_high_a_5_high_straight_is_the_lowest_scoring_straight
PASSED poker_test.py::PokerTest::test_flush_beats_a_straight
PASSED poker_test.py::PokerTest::test_four_of_a_kind_beats_a_full_house
PASSED poker_test.py::PokerTest::test_full_house_beats_a_flush
PASSED poker_test.py::PokerTest::test_highest_card_out_of_all_hands_wins
PASSED poker_test.py::PokerTest::test_highest_pair_wins
PASSED poker_test.py::PokerTest::test_multiple_hands_with_the_same_high_cards_tie_compares_next_highest_ranked_down_to_last_card
PASSED poker_test.py::PokerTest::test_one_pair_beats_high_card
PASSED poker_test.py::PokerTest::test_single_hand_always_wins
PASSED poker_test.py::PokerTest::test_straight_flush_beats_four_of_a_kind
PASSED poker_test.py::PokerTest::test_three_of_a_kind_beats_two_pair
PASSED poker_test.py::PokerTest::test_two_pairs_beats_one_pair
PASSED poker_test.py::PokerTest::test_two_pairs_first_ranked_by_largest_pair
PASSED poker_test.py::PokerTest::test_winning_high_card_hand_also_has_the_lowest_card
PASSED poker_test.py::PokerTest::test_with_multiple_decks_both_hands_have_a_full_house_with_the_same_triplet_tie_goes_to_the_pair
PASSED poker_test.py::PokerTest::test_with_multiple_decks_both_hands_with_identical_four_of_a_kind_tie_determined_by_kicker
PASSED poker_test.py::PokerTest::test_with_multiple_decks_two_players_can_have_same_three_of_a_kind_ties_go_to_highest_remaining_cards
============================== 37 passed in 0.03s ==============================
