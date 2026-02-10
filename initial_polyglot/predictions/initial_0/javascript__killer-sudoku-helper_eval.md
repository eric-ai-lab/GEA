+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' killer-sudoku-helper.spec.js
+ npm run test

> test
> jest ./*

FAIL ./killer-sudoku-helper.spec.js
  Trivial 1-digit cages
    ✕ 1 (22 ms)
    ✕ 2 (2 ms)
    ✕ 3 (1 ms)
    ✕ 4 (9 ms)
    ✕ 5 (1 ms)
    ✕ 6 (9 ms)
    ✕ 7 (5 ms)
    ✕ 8 (2 ms)
    ✕ 9 (10 ms)
  Other cages
    ✕ Cage with sum 45 contains all digits 1:9 (2 ms)
    ✕ Cage with only 1 possible combination (9 ms)
    ✕ Cage with several combinations (9 ms)
    ✕ Cage with several combinations that is restricted (1 ms)

  ● Trivial 1-digit cages › 1

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     1,
    -   ],
    - ]
    + Array []

      10 |     const expected = [[1]];
      11 |     const actual = combinations(inputCage);
    > 12 |     expect(actual).toEqual(expected);
         |                    ^
      13 |   });
      14 |
      15 |   test('2', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:12:20)

  ● Trivial 1-digit cages › 2

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     2,
    -   ],
    - ]
    + Array []

      21 |     const expected = [[2]];
      22 |     const actual = combinations(inputCage);
    > 23 |     expect(actual).toEqual(expected);
         |                    ^
      24 |   });
      25 |
      26 |   test('3', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:23:20)

  ● Trivial 1-digit cages › 3

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     3,
    -   ],
    - ]
    + Array []

      32 |     const expected = [[3]];
      33 |     const actual = combinations(inputCage);
    > 34 |     expect(actual).toEqual(expected);
         |                    ^
      35 |   });
      36 |
      37 |   test('4', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:34:20)

  ● Trivial 1-digit cages › 4

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     4,
    -   ],
    - ]
    + Array []

      43 |     const expected = [[4]];
      44 |     const actual = combinations(inputCage);
    > 45 |     expect(actual).toEqual(expected);
         |                    ^
      46 |   });
      47 |
      48 |   test('5', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:45:20)

  ● Trivial 1-digit cages › 5

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     5,
    -   ],
    - ]
    + Array []

      54 |     const expected = [[5]];
      55 |     const actual = combinations(inputCage);
    > 56 |     expect(actual).toEqual(expected);
         |                    ^
      57 |   });
      58 |
      59 |   test('6', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:56:20)

  ● Trivial 1-digit cages › 6

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     6,
    -   ],
    - ]
    + Array []

      65 |     const expected = [[6]];
      66 |     const actual = combinations(inputCage);
    > 67 |     expect(actual).toEqual(expected);
         |                    ^
      68 |   });
      69 |
      70 |   test('7', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:67:20)

  ● Trivial 1-digit cages › 7

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     7,
    -   ],
    - ]
    + Array []

      76 |     const expected = [[7]];
      77 |     const actual = combinations(inputCage);
    > 78 |     expect(actual).toEqual(expected);
         |                    ^
      79 |   });
      80 |
      81 |   test('8', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:78:20)

  ● Trivial 1-digit cages › 8

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     8,
    -   ],
    - ]
    + Array []

      87 |     const expected = [[8]];
      88 |     const actual = combinations(inputCage);
    > 89 |     expect(actual).toEqual(expected);
         |                    ^
      90 |   });
      91 |
      92 |   test('9', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:89:20)

  ● Trivial 1-digit cages › 9

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 1

    - Array [
    -   Array [
    -     9,
    -   ],
    - ]
    + Array []

       98 |     const expected = [[9]];
       99 |     const actual = combinations(inputCage);
    > 100 |     expect(actual).toEqual(expected);
          |                    ^
      101 |   });
      102 | });
      103 |

      at Object.toEqual (killer-sudoku-helper.spec.js:100:20)

  ● Other cages › Cage with sum 45 contains all digits 1:9

    expect(received).toEqual(expected) // deep equality

    - Expected  - 13
    + Received  +  1

    - Array [
    -   Array [
    -     1,
    -     2,
    -     3,
    -     4,
    -     5,
    -     6,
    -     7,
    -     8,
    -     9,
    -   ],
    - ]
    + Array []

      111 |     const expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9]];
      112 |     const actual = combinations(inputCage);
    > 113 |     expect(actual).toEqual(expected);
          |                    ^
      114 |   });
      115 |
      116 |   test('Cage with only 1 possible combination', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:113:20)

  ● Other cages › Cage with only 1 possible combination

    expect(received).toEqual(expected) // deep equality

    - Expected  - 7
    + Received  + 1

    - Array [
    -   Array [
    -     1,
    -     2,
    -     4,
    -   ],
    - ]
    + Array []

      122 |     const expected = [[1, 2, 4]];
      123 |     const actual = combinations(inputCage);
    > 124 |     expect(actual).toEqual(expected);
          |                    ^
      125 |   });
      126 |
      127 |   test('Cage with several combinations', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:124:20)

  ● Other cages › Cage with several combinations

    expect(received).toEqual(expected) // deep equality

    - Expected  - 18
    + Received  +  1

    - Array [
    -   Array [
    -     1,
    -     9,
    -   ],
    -   Array [
    -     2,
    -     8,
    -   ],
    -   Array [
    -     3,
    -     7,
    -   ],
    -   Array [
    -     4,
    -     6,
    -   ],
    - ]
    + Array []

      138 |     ];
      139 |     const actual = combinations(inputCage);
    > 140 |     expect(actual).toEqual(expected);
          |                    ^
      141 |   });
      142 |
      143 |   test('Cage with several combinations that is restricted', () => {

      at Object.toEqual (killer-sudoku-helper.spec.js:140:20)

  ● Other cages › Cage with several combinations that is restricted

    expect(received).toEqual(expected) // deep equality

    - Expected  - 10
    + Received  +  1

    - Array [
    -   Array [
    -     2,
    -     8,
    -   ],
    -   Array [
    -     3,
    -     7,
    -   ],
    - ]
    + Array []

      152 |     ];
      153 |     const actual = combinations(inputCage);
    > 154 |     expect(actual).toEqual(expected);
          |                    ^
      155 |   });
      156 | });
      157 |

      at Object.toEqual (killer-sudoku-helper.spec.js:154:20)

Test Suites: 1 failed, 1 total
Tests:       13 failed, 13 total
Snapshots:   0 total
Time:        3.335 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/killer-sudoku-helper.js|.\/killer-sudoku-helper.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
