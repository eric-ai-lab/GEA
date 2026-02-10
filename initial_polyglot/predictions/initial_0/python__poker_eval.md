+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 37 items

poker_test.py .FFF..F.................F....F.......                      [100%]

=================================== FAILURES ===================================
__________________ PokerTest.test_a_tie_has_multiple_winners ___________________

self = <poker_test.PokerTest testMethod=test_a_tie_has_multiple_winners>

    def test_a_tie_has_multiple_winners(self):
        self.assertEqual(
>           best_hands(
                [
                    "4D 5S 6S 8D 3C",
                    "2S 4C 7S 9H 10H",
                    "3S 4S 5D 6H JH",
                    "3H 4H 5C 6C JD",
                ]
            ),
            ["3S 4S 5D 6H JH", "3H 4H 5C 6C JD"],
        )

poker_test.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hands = ['4D 5S 6S 8D 3C', '2S 4C 7S 9H 10H', '3S 4S 5D 6H JH', '3H 4H 5C 6C JD']

    def best_hands(hands):
        """
        Given a list of hand strings, returns the hand or list of hands that wins.
        If there is a tie, return all tied hands in the order they were given.
        """
        # Prepare list of tuples: (original_hand_str, name, cards, rank)
        evaluated = []
        for hand_str in hands:
>           name, cards = parse_hand(hand_str)

poker.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hand_str = '2S 4C 7S 9H 10H'

    def parse_hand(hand_str):
        """
        Parses a hand string.
        The hand string is expected to be in the format "Name: CARD CARD CARD CARD CARD"
        If no colon is present, treat the entire string as cards (without a name).
        Returns a tuple (name, cards) where name may be None if not provided.
        Each card is a tuple (value, suit) with value as int.
        """
        if ':' in hand_str:
            name, cards_part = hand_str.split(':', 1)
            name = name.strip()
            card_tokens = cards_part.strip().split()
        else:
            name = None
            card_tokens = hand_str.split()
    
        cards = []
        for token in card_tokens:
            # card format e.g. "2H", "TD", etc.
            value_char = token[0]
            suit = token[1]
>           value = CARD_VALUES[value_char]
E           KeyError: '1'

poker.py:42: KeyError
______________ PokerTest.test_aces_can_end_a_straight_10_j_q_k_a _______________

self = <poker_test.PokerTest testMethod=test_aces_can_end_a_straight_10_j_q_k_a>

    def test_aces_can_end_a_straight_10_j_q_k_a(self):
        self.assertEqual(
>           best_hands(["4S 5H 4C 8D 4H", "10D JH QS KD AC"]), ["10D JH QS KD AC"]
        )

poker_test.py:122: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hands = ['4S 5H 4C 8D 4H', '10D JH QS KD AC']

    def best_hands(hands):
        """
        Given a list of hand strings, returns the hand or list of hands that wins.
        If there is a tie, return all tied hands in the order they were given.
        """
        # Prepare list of tuples: (original_hand_str, name, cards, rank)
        evaluated = []
        for hand_str in hands:
>           name, cards = parse_hand(hand_str)

poker.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hand_str = '10D JH QS KD AC'

    def parse_hand(hand_str):
        """
        Parses a hand string.
        The hand string is expected to be in the format "Name: CARD CARD CARD CARD CARD"
        If no colon is present, treat the entire string as cards (without a name).
        Returns a tuple (name, cards) where name may be None if not provided.
        Each card is a tuple (value, suit) with value as int.
        """
        if ':' in hand_str:
            name, cards_part = hand_str.split(':', 1)
            name = name.strip()
            card_tokens = cards_part.strip().split()
        else:
            name = None
            card_tokens = hand_str.split()
    
        cards = []
        for token in card_tokens:
            # card format e.g. "2H", "TD", etc.
            value_char = token[0]
            suit = token[1]
>           value = CARD_VALUES[value_char]
E           KeyError: '1'

poker.py:42: KeyError
___________ PokerTest.test_aces_can_end_a_straight_flush_10_j_q_k_a ____________

self = <poker_test.PokerTest testMethod=test_aces_can_end_a_straight_flush_10_j_q_k_a>

    def test_aces_can_end_a_straight_flush_10_j_q_k_a(self):
        self.assertEqual(
>           best_hands(["KC AH AS AD AC", "10C JC QC KC AC"]), ["10C JC QC KC AC"]
        )

poker_test.py:200: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hands = ['KC AH AS AD AC', '10C JC QC KC AC']

    def best_hands(hands):
        """
        Given a list of hand strings, returns the hand or list of hands that wins.
        If there is a tie, return all tied hands in the order they were given.
        """
        # Prepare list of tuples: (original_hand_str, name, cards, rank)
        evaluated = []
        for hand_str in hands:
>           name, cards = parse_hand(hand_str)

poker.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hand_str = '10C JC QC KC AC'

    def parse_hand(hand_str):
        """
        Parses a hand string.
        The hand string is expected to be in the format "Name: CARD CARD CARD CARD CARD"
        If no colon is present, treat the entire string as cards (without a name).
        Returns a tuple (name, cards) where name may be None if not provided.
        Each card is a tuple (value, suit) with value as int.
        """
        if ':' in hand_str:
            name, cards_part = hand_str.split(':', 1)
            name = name.strip()
            card_tokens = cards_part.strip().split()
        else:
            name = None
            card_tokens = hand_str.split()
    
        cards = []
        for token in card_tokens:
            # card format e.g. "2H", "TD", etc.
            value_char = token[0]
            suit = token[1]
>           value = CARD_VALUES[value_char]
E           KeyError: '1'

poker.py:42: KeyError
__ PokerTest.test_aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3 ___

self = <poker_test.PokerTest testMethod=test_aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3>

    def test_aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3(self):
        self.assertEqual(
>           best_hands(["2C AC QC 10C KC", "QH KH AH 2H 3H"]), ["2C AC QC 10C KC"]
        )

poker_test.py:210: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hands = ['2C AC QC 10C KC', 'QH KH AH 2H 3H']

    def best_hands(hands):
        """
        Given a list of hand strings, returns the hand or list of hands that wins.
        If there is a tie, return all tied hands in the order they were given.
        """
        # Prepare list of tuples: (original_hand_str, name, cards, rank)
        evaluated = []
        for hand_str in hands:
>           name, cards = parse_hand(hand_str)

poker.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hand_str = '2C AC QC 10C KC'

    def parse_hand(hand_str):
        """
        Parses a hand string.
        The hand string is expected to be in the format "Name: CARD CARD CARD CARD CARD"
        If no colon is present, treat the entire string as cards (without a name).
        Returns a tuple (name, cards) where name may be None if not provided.
        Each card is a tuple (value, suit) with value as int.
        """
        if ':' in hand_str:
            name, cards_part = hand_str.split(':', 1)
            name = name.strip()
            card_tokens = cards_part.strip().split()
        else:
            name = None
            card_tokens = hand_str.split()
    
        cards = []
        for token in card_tokens:
            # card format e.g. "2H", "TD", etc.
            value_char = token[0]
            suit = token[1]
>           value = CARD_VALUES[value_char]
E           KeyError: '1'

poker.py:42: KeyError
______________ PokerTest.test_highest_card_out_of_all_hands_wins _______________

self = <poker_test.PokerTest testMethod=test_highest_card_out_of_all_hands_wins>

    def test_highest_card_out_of_all_hands_wins(self):
        self.assertEqual(
>           best_hands(["4D 5S 6S 8D 3C", "2S 4C 7S 9H 10H", "3S 4S 5D 6H JH"]),
            ["3S 4S 5D 6H JH"],
        )

poker_test.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hands = ['4D 5S 6S 8D 3C', '2S 4C 7S 9H 10H', '3S 4S 5D 6H JH']

    def best_hands(hands):
        """
        Given a list of hand strings, returns the hand or list of hands that wins.
        If there is a tie, return all tied hands in the order they were given.
        """
        # Prepare list of tuples: (original_hand_str, name, cards, rank)
        evaluated = []
        for hand_str in hands:
>           name, cards = parse_hand(hand_str)

poker.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hand_str = '2S 4C 7S 9H 10H'

    def parse_hand(hand_str):
        """
        Parses a hand string.
        The hand string is expected to be in the format "Name: CARD CARD CARD CARD CARD"
        If no colon is present, treat the entire string as cards (without a name).
        Returns a tuple (name, cards) where name may be None if not provided.
        Each card is a tuple (value, suit) with value as int.
        """
        if ':' in hand_str:
            name, cards_part = hand_str.split(':', 1)
            name = name.strip()
            card_tokens = cards_part.strip().split()
        else:
            name = None
            card_tokens = hand_str.split()
    
        cards = []
        for token in card_tokens:
            # card format e.g. "2H", "TD", etc.
            value_char = token[0]
            suit = token[1]
>           value = CARD_VALUES[value_char]
E           KeyError: '1'

poker.py:42: KeyError
______________ PokerTest.test_straight_flush_beats_four_of_a_kind ______________

self = <poker_test.PokerTest testMethod=test_straight_flush_beats_four_of_a_kind>

    def test_straight_flush_beats_four_of_a_kind(self):
        self.assertEqual(
>           best_hands(["4S 5H 5S 5D 5C", "7S 8S 9S 6S 10S"]), ["7S 8S 9S 6S 10S"]
        )

poker_test.py:195: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hands = ['4S 5H 5S 5D 5C', '7S 8S 9S 6S 10S']

    def best_hands(hands):
        """
        Given a list of hand strings, returns the hand or list of hands that wins.
        If there is a tie, return all tied hands in the order they were given.
        """
        # Prepare list of tuples: (original_hand_str, name, cards, rank)
        evaluated = []
        for hand_str in hands:
>           name, cards = parse_hand(hand_str)

poker.py:139: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hand_str = '7S 8S 9S 6S 10S'

    def parse_hand(hand_str):
        """
        Parses a hand string.
        The hand string is expected to be in the format "Name: CARD CARD CARD CARD CARD"
        If no colon is present, treat the entire string as cards (without a name).
        Returns a tuple (name, cards) where name may be None if not provided.
        Each card is a tuple (value, suit) with value as int.
        """
        if ':' in hand_str:
            name, cards_part = hand_str.split(':', 1)
            name = name.strip()
            card_tokens = cards_part.strip().split()
        else:
            name = None
            card_tokens = hand_str.split()
    
        cards = []
        for token in card_tokens:
            # card format e.g. "2H", "TD", etc.
            value_char = token[0]
            suit = token[1]
>           value = CARD_VALUES[value_char]
E           KeyError: '1'

poker.py:42: KeyError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED poker_test.py::PokerTest::test_a_straight_beats_three_of_a_kind
PASSED poker_test.py::PokerTest::test_aces_can_start_a_straight_a_2_3_4_5
PASSED poker_test.py::PokerTest::test_aces_can_start_a_straight_flush_a_2_3_4_5
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
PASSED poker_test.py::PokerTest::test_highest_pair_wins
PASSED poker_test.py::PokerTest::test_multiple_hands_with_the_same_high_cards_tie_compares_next_highest_ranked_down_to_last_card
PASSED poker_test.py::PokerTest::test_one_pair_beats_high_card
PASSED poker_test.py::PokerTest::test_single_hand_always_wins
PASSED poker_test.py::PokerTest::test_three_of_a_kind_beats_two_pair
PASSED poker_test.py::PokerTest::test_two_pairs_beats_one_pair
PASSED poker_test.py::PokerTest::test_two_pairs_first_ranked_by_largest_pair
PASSED poker_test.py::PokerTest::test_winning_high_card_hand_also_has_the_lowest_card
PASSED poker_test.py::PokerTest::test_with_multiple_decks_both_hands_have_a_full_house_with_the_same_triplet_tie_goes_to_the_pair
PASSED poker_test.py::PokerTest::test_with_multiple_decks_both_hands_with_identical_four_of_a_kind_tie_determined_by_kicker
PASSED poker_test.py::PokerTest::test_with_multiple_decks_two_players_can_have_same_three_of_a_kind_ties_go_to_highest_remaining_cards
FAILED poker_test.py::PokerTest::test_a_tie_has_multiple_winners - KeyError: '1'
FAILED poker_test.py::PokerTest::test_aces_can_end_a_straight_10_j_q_k_a - Ke...
FAILED poker_test.py::PokerTest::test_aces_can_end_a_straight_flush_10_j_q_k_a
FAILED poker_test.py::PokerTest::test_aces_cannot_be_in_the_middle_of_a_straight_flush_q_k_a_2_3
FAILED poker_test.py::PokerTest::test_highest_card_out_of_all_hands_wins - Ke...
FAILED poker_test.py::PokerTest::test_straight_flush_beats_four_of_a_kind - K...
========================= 6 failed, 31 passed in 0.32s =========================
