+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' poker.spec.js
+ npm run test

> test
> jest ./*

PASS ./poker.spec.js
  Poker
    ✓ single hand always wins (4 ms)
    ✓ highest card out of all hands wins (1 ms)
    ✓ a tie has multiple winners (1 ms)
    ✓ multiple hands with the same high cards, tie compares next highest ranked, down to last card (1 ms)
    ✓ one pair beats high card (1 ms)
    ✓ highest pair wins (1 ms)
    ✓ two pairs beats one pair (1 ms)
    ✓ both hands have two pairs, highest ranked pair wins (1 ms)
    ✓ both hands have two pairs, with the same highest ranked pair, tie goes to low pair (1 ms)
    ✓ both hands have two identically ranked pairs, tie goes to remaining card (kicker) (1 ms)
    ✓ three of a kind beats two pair (1 ms)
    ✓ both hands have three of a kind, tie goes to highest ranked triplet (8 ms)
    ✓ with multiple decks, two players can have same three of a kind, ties go to highest remaining cards
    ✓ a straight beats three of a kind
    ✓ aces can end a straight (10 J Q K A)
    ✓ aces can start a straight (A 2 3 4 5) (1 ms)
    ✓ both hands with a straight, tie goes to highest ranked card
    ✓ even though an ace is usually high, a 5-high straight is the lowest-scoring straight
    ✓ flush beats a straight (1 ms)
    ✓ both hands have a flush, tie goes to high card, down to the last one if necessary
    ✓ full house beats a flush (1 ms)
    ✓ both hands have a full house, tie goes to highest-ranked triplet
    ✓ with multiple decks, both hands have a full house with the same triplet, tie goes to the pair (1 ms)
    ✓ four of a kind beats a full house
    ✓ both hands have four of a kind, tie goes to high quad (1 ms)
    ✓ with multiple decks, both hands with identical four of a kind, tie determined by kicker
    ✓ straight flush beats four of a kind
    ✓ both hands have straight flush, tie goes to highest-ranked card

Test Suites: 1 passed, 1 total
Tests:       28 passed, 28 total
Snapshots:   0 total
Time:        0.805 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./poker.js|./poker.spec.js.
