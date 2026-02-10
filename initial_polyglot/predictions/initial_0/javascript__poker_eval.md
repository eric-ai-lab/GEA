+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' poker.spec.js
+ npm run test

> test
> jest ./*

FAIL ./poker.spec.js
  Poker
    ✓ single hand always wins (25 ms)
    ✓ highest card out of all hands wins (1 ms)
    ✓ a tie has multiple winners (1 ms)
    ✓ multiple hands with the same high cards, tie compares next highest ranked, down to last card (2 ms)
    ✓ one pair beats high card (1 ms)
    ✓ highest pair wins (1 ms)
    ✓ two pairs beats one pair
    ✓ both hands have two pairs, highest ranked pair wins
    ✓ both hands have two pairs, with the same highest ranked pair, tie goes to low pair (1 ms)
    ✓ both hands have two identically ranked pairs, tie goes to remaining card (kicker) (1 ms)
    ✓ three of a kind beats two pair (1 ms)
    ✓ both hands have three of a kind, tie goes to highest ranked triplet
    ✓ with multiple decks, two players can have same three of a kind, ties go to highest remaining cards
    ✓ a straight beats three of a kind (1 ms)
    ✕ aces can end a straight (10 J Q K A) (15 ms)
    ✓ aces can start a straight (A 2 3 4 5)
    ✓ both hands with a straight, tie goes to highest ranked card
    ✓ even though an ace is usually high, a 5-high straight is the lowest-scoring straight (1 ms)
    ✓ flush beats a straight
    ✓ both hands have a flush, tie goes to high card, down to the last one if necessary (1 ms)
    ✓ full house beats a flush
    ✓ both hands have a full house, tie goes to highest-ranked triplet
    ✓ with multiple decks, both hands have a full house with the same triplet, tie goes to the pair
    ✓ four of a kind beats a full house (28 ms)
    ✓ both hands have four of a kind, tie goes to high quad (2 ms)
    ✓ with multiple decks, both hands with identical four of a kind, tie determined by kicker
    ✕ straight flush beats four of a kind (2 ms)
    ✓ both hands have straight flush, tie goes to highest-ranked card (1 ms)

  ● Poker › aces can end a straight (10 J Q K A)

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      Array [
    -   "10D JH QS KD AC",
    +   "4S 5H 4C 8D 4H",
      ]

      94 |     const hands = ['4S 5H 4C 8D 4H', '10D JH QS KD AC'];
      95 |     const expected = ['10D JH QS KD AC'];
    > 96 |     expect(bestHands(hands)).toEqual(expected);
         |                              ^
      97 |   });
      98 |
      99 |   test('aces can start a straight (A 2 3 4 5)', () => {

      at Object.toEqual (poker.spec.js:96:30)

  ● Poker › straight flush beats four of a kind

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      Array [
    -   "7S 8S 9S 6S 10S",
    +   "4S 5H 5S 5D 5C",
      ]

      166 |     const hands = ['4S 5H 5S 5D 5C', '7S 8S 9S 6S 10S'];
      167 |     const expected = ['7S 8S 9S 6S 10S'];
    > 168 |     expect(bestHands(hands)).toEqual(expected);
          |                              ^
      169 |   });
      170 |
      171 |   test('both hands have straight flush, tie goes to highest-ranked card', () => {

      at Object.toEqual (poker.spec.js:168:30)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 26 passed, 28 total
Snapshots:   0 total
Time:        3.737 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/poker.js|.\/poker.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
