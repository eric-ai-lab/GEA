+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' queen-attack.spec.js
+ npm run test

> test
> jest ./*

FAIL ./queen-attack.spec.js
  Queens
    Test creation of Queens with valid and invalid positions
      ✓ queen with a valid position (9 ms)
      ✕ queen must have positive row (58 ms)
      ✕ queen must have row on board (2 ms)
      ✕ queen must have positive column (2 ms)
      ✕ queen must have column on board (3 ms)
      ✓ two queens cannot occupy the same space (2 ms)
    Test the ability of one queen to attack another
      ✓ queens cannot attack (1 ms)
      ✓ queens can attack when they are on the same row
      ✓ queens can attack when they are on the same column
      ✓ queens can attack diagonally
      ✓ queens can attack another diagonally (1 ms)
      ✓ queens can attack yet another diagonally (1 ms)
      ✓ queens can attack diagonally, really
      ✓ queens can attack on a north-east/south-west diagonal
      ✓ queens can attack on another ne/sw diagonal (1 ms)
    Test the board visualisation
      ✕ board (31 ms)
      ✕ board with queens at their starting positions (11 ms)
      ✕ board with the black queen at her starting positions (2 ms)
      ✕ board with queens at the edges (2 ms)

  ● Queens › Test creation of Queens with valid and invalid positions › queen must have positive row

    expect(received).toThrow(expected)

    Expected substring: "Queen must be placed on the board"
    Received message:   "QueenAttack: Invalid queen position"

          32 |     };
          33 |     if (!isValidPosition(this.white) || !isValidPosition(this.black)) {
        > 34 |       throw new Error('QueenAttack: Invalid queen position');
             |             ^
          35 |     }
          36 |
          37 |     // Check for same position

      at new QueenAttack (queen-attack.js:34:13)
      at queen-attack.spec.js:13:20
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (queen-attack.spec.js:13:50)
      at Object.toThrow (queen-attack.spec.js:13:50)

  ● Queens › Test creation of Queens with valid and invalid positions › queen must have row on board

    expect(received).toThrow(expected)

    Expected substring: "Queen must be placed on the board"
    Received message:   "QueenAttack: Invalid queen position"

          32 |     };
          33 |     if (!isValidPosition(this.white) || !isValidPosition(this.black)) {
        > 34 |       throw new Error('QueenAttack: Invalid queen position');
             |             ^
          35 |     }
          36 |
          37 |     // Check for same position

      at new QueenAttack (queen-attack.js:34:13)
      at queen-attack.spec.js:19:20
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (queen-attack.spec.js:19:50)
      at Object.toThrow (queen-attack.spec.js:19:50)

  ● Queens › Test creation of Queens with valid and invalid positions › queen must have positive column

    expect(received).toThrow(expected)

    Expected substring: "Queen must be placed on the board"
    Received message:   "QueenAttack: Invalid queen position"

          32 |     };
          33 |     if (!isValidPosition(this.white) || !isValidPosition(this.black)) {
        > 34 |       throw new Error('QueenAttack: Invalid queen position');
             |             ^
          35 |     }
          36 |
          37 |     // Check for same position

      at new QueenAttack (queen-attack.js:34:13)
      at queen-attack.spec.js:25:20
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (queen-attack.spec.js:25:50)
      at Object.toThrow (queen-attack.spec.js:25:50)

  ● Queens › Test creation of Queens with valid and invalid positions › queen must have column on board

    expect(received).toThrow(expected)

    Expected substring: "Queen must be placed on the board"
    Received message:   "QueenAttack: Invalid queen position"

          32 |     };
          33 |     if (!isValidPosition(this.white) || !isValidPosition(this.black)) {
        > 34 |       throw new Error('QueenAttack: Invalid queen position');
             |             ^
          35 |     }
          36 |
          37 |     // Check for same position

      at new QueenAttack (queen-attack.js:34:13)
      at queen-attack.spec.js:31:20
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (queen-attack.spec.js:31:50)
      at Object.toThrow (queen-attack.spec.js:31:50)

  ● Queens › Test the board visualisation › board

    expect(received).toEqual(expected) // deep equality

    - Expected  -  8
    + Received  + 10

    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ W _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ B _ _
    - _ _ _ _ _ _ _ _
    +   a b c d e f g h
    + 8 _ _ _ _ _ _ _ _ 8
    + 7 _ _ _ _ _ B _ _ 7
    + 6 _ _ _ _ _ _ _ _ 6
    + 5 _ _ _ _ _ _ _ _ 5
    + 4 _ _ W _ _ _ _ _ 4
    + 3 _ _ _ _ _ _ _ _ 3
    + 2 _ _ _ _ _ _ _ _ 2
    + 1 _ _ _ _ _ _ _ _ 1
    +   a b c d e f g h

      100 |         '_ _ _ _ _ _ _ _',
      101 |       ].join('\n');
    > 102 |       expect(queens.toString()).toEqual(board);
          |                                 ^
      103 |     });
      104 |
      105 |     test('board with queens at their starting positions', () => {

      at Object.toEqual (queen-attack.spec.js:102:33)

  ● Queens › Test the board visualisation › board with queens at their starting positions

    expect(received).toEqual(expected) // deep equality

    - Expected  -  8
    + Received  + 10

    - _ _ _ B _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ W _ _ _ _
    +   a b c d e f g h
    + 8 _ _ _ B _ _ _ _ 8
    + 7 _ _ _ _ _ _ _ _ 7
    + 6 _ _ _ _ _ _ _ _ 6
    + 5 _ _ _ _ _ _ _ _ 5
    + 4 _ _ _ _ _ _ _ _ 4
    + 3 _ _ _ _ _ _ _ _ 3
    + 2 _ _ _ _ _ _ _ _ 2
    + 1 _ _ _ W _ _ _ _ 1
    +   a b c d e f g h

      115 |         '_ _ _ W _ _ _ _',
      116 |       ].join('\n');
    > 117 |       expect(queens.toString()).toEqual(board);
          |                                 ^
      118 |     });
      119 |
      120 |     test('board with the black queen at her starting positions', () => {

      at Object.toEqual (queen-attack.spec.js:117:33)

  ● Queens › Test the board visualisation › board with the black queen at her starting positions

    expect(received).toEqual(expected) // deep equality

    - Expected  -  8
    + Received  + 10

    - _ _ _ B _ _ _ _
    - _ _ _ _ _ _ W _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    +   a b c d e f g h
    + 8 _ _ _ B _ _ _ _ 8
    + 7 _ _ _ _ _ _ _ _ 7
    + 6 _ _ _ _ _ _ _ _ 6
    + 5 _ _ _ _ _ _ _ _ 5
    + 4 _ _ _ _ _ _ _ _ 4
    + 3 _ _ _ _ _ _ _ _ 3
    + 2 _ _ _ _ _ _ W _ 2
    + 1 _ _ _ _ _ _ _ _ 1
    +   a b c d e f g h

      130 |         '_ _ _ _ _ _ _ _',
      131 |       ].join('\n');
    > 132 |       expect(queens.toString()).toEqual(board);
          |                                 ^
      133 |     });
      134 |
      135 |     test('board with queens at the edges', () => {

      at Object.toEqual (queen-attack.spec.js:132:33)

  ● Queens › Test the board visualisation › board with queens at the edges

    expect(received).toEqual(expected) // deep equality

    - Expected  -  8
    + Received  + 10

    - W _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ B
    +   a b c d e f g h
    + 8 _ _ _ _ _ _ _ B 8
    + 7 _ _ _ _ _ _ _ _ 7
    + 6 _ _ _ _ _ _ _ _ 6
    + 5 _ _ _ _ _ _ _ _ 5
    + 4 _ _ _ _ _ _ _ _ 4
    + 3 _ _ _ _ _ _ _ _ 3
    + 2 _ _ _ _ _ _ _ _ 2
    + 1 W _ _ _ _ _ _ _ 1
    +   a b c d e f g h

      146 |         '_ _ _ _ _ _ _ B',
      147 |       ].join('\n');
    > 148 |       expect(queens.toString()).toEqual(board);
          |                                 ^
      149 |     });
      150 |   });
      151 | });

      at Object.toEqual (queen-attack.spec.js:148:33)

Test Suites: 1 failed, 1 total
Tests:       8 failed, 11 passed, 19 total
Snapshots:   0 total
Time:        4.339 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/queen-attack.js|.\/queen-attack.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
