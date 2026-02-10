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
      ✕ queen with a valid position (4 ms)
      ✕ queen must have positive row (14 ms)
      ✕ queen must have row on board (2 ms)
      ✕ queen must have positive column (2 ms)
      ✕ queen must have column on board (1 ms)
      ✕ two queens cannot occupy the same space (1 ms)
    Test the ability of one queen to attack another
      ✓ queens cannot attack (1 ms)
      ✓ queens can attack when they are on the same row
      ✓ queens can attack when they are on the same column
      ✓ queens can attack diagonally (1 ms)
      ✓ queens can attack another diagonally (1 ms)
      ✓ queens can attack yet another diagonally (1 ms)
      ✓ queens can attack diagonally, really
      ✓ queens can attack on a north-east/south-west diagonal
      ✓ queens can attack on another ne/sw diagonal (1 ms)
    Test the board visualisation
      ✕ board (3 ms)
      ✕ board with queens at their starting positions
      ✕ board with the black queen at her starting positions (1 ms)
      ✕ board with queens at the edges (1 ms)

  ● Queens › Test creation of Queens with valid and invalid positions › queen with a valid position

    expect(received).toEqual(expected) // deep equality

    Expected: [2, 2]
    Received: undefined

       5 |     test('queen with a valid position', () => {
       6 |       const queens = new QueenAttack({ white: [2, 2] });
    >  7 |       expect(queens.white).toEqual([2, 2]);
         |                            ^
       8 |     });
       9 |
      10 |     test('queen must have positive row', () => {

      at Object.toEqual (queen-attack.spec.js:7:28)

  ● Queens › Test creation of Queens with valid and invalid positions › queen must have positive row

    expect(received).toThrow(expected)

    Expected substring: "Queen must be placed on the board"
    Received message:   "A queen must be placed on a valid position on the board"

          30 |     
          31 |     if (row < 0 || row > 7 || column < 0 || column > 7) {
        > 32 |       throw new Error(`A queen must be placed on a valid position on the board`);
             |             ^
          33 |     }
          34 |   }
          35 |

      at QueenAttack.validatePosition (queen-attack.js:32:13)
      at new validatePosition (queen-attack.js:13:10)
      at queen-attack.spec.js:13:20
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (queen-attack.spec.js:13:50)
      at Object.toThrow (queen-attack.spec.js:13:50)

  ● Queens › Test creation of Queens with valid and invalid positions › queen must have row on board

    expect(received).toThrow(expected)

    Expected substring: "Queen must be placed on the board"
    Received message:   "A queen must be placed on a valid position on the board"

          30 |     
          31 |     if (row < 0 || row > 7 || column < 0 || column > 7) {
        > 32 |       throw new Error(`A queen must be placed on a valid position on the board`);
             |             ^
          33 |     }
          34 |   }
          35 |

      at QueenAttack.validatePosition (queen-attack.js:32:13)
      at new validatePosition (queen-attack.js:13:10)
      at queen-attack.spec.js:19:20
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (queen-attack.spec.js:19:50)
      at Object.toThrow (queen-attack.spec.js:19:50)

  ● Queens › Test creation of Queens with valid and invalid positions › queen must have positive column

    expect(received).toThrow(expected)

    Expected substring: "Queen must be placed on the board"
    Received message:   "A queen must be placed on a valid position on the board"

          30 |     
          31 |     if (row < 0 || row > 7 || column < 0 || column > 7) {
        > 32 |       throw new Error(`A queen must be placed on a valid position on the board`);
             |             ^
          33 |     }
          34 |   }
          35 |

      at QueenAttack.validatePosition (queen-attack.js:32:13)
      at new validatePosition (queen-attack.js:13:10)
      at queen-attack.spec.js:25:20
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (queen-attack.spec.js:25:50)
      at Object.toThrow (queen-attack.spec.js:25:50)

  ● Queens › Test creation of Queens with valid and invalid positions › queen must have column on board

    expect(received).toThrow(expected)

    Expected substring: "Queen must be placed on the board"
    Received message:   "A queen must be placed on a valid position on the board"

          30 |     
          31 |     if (row < 0 || row > 7 || column < 0 || column > 7) {
        > 32 |       throw new Error(`A queen must be placed on a valid position on the board`);
             |             ^
          33 |     }
          34 |   }
          35 |

      at QueenAttack.validatePosition (queen-attack.js:32:13)
      at new validatePosition (queen-attack.js:13:10)
      at queen-attack.spec.js:31:20
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (queen-attack.spec.js:31:50)
      at Object.toThrow (queen-attack.spec.js:31:50)

  ● Queens › Test creation of Queens with valid and invalid positions › two queens cannot occupy the same space

    expect(received).toThrow(expected)

    Expected substring: "Queens cannot share the same space"
    Received message:   "Queens cannot share the same position"

          15 |     // Check that queens are not at the same position
          16 |     if (blackRow === whiteRow && blackColumn === whiteColumn) {
        > 17 |       throw new Error('Queens cannot share the same position');
             |             ^
          18 |     }
          19 |     
          20 |     this.blackRow = blackRow;

      at new QueenAttack (queen-attack.js:17:13)
      at queen-attack.spec.js:37:20
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (queen-attack.spec.js:37:50)
      at Object.toThrow (queen-attack.spec.js:37:50)

  ● Queens › Test the board visualisation › board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 8
    + Received  + 8

    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ B _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ W _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ W _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ B _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _

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

    - Expected  - 8
    + Received  + 8

    - _ _ _ B _ _ _ _
    + _ _ _ B _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ W _ _ _ _
    + _ _ _ W _ _ _ _

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

    - Expected  - 8
    + Received  + 8

    - _ _ _ B _ _ _ _
    + _ _ _ B _ _ _ _ 
    - _ _ _ _ _ _ W _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ W _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _

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

    - Expected  - 8
    + Received  + 8

    - W _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ B 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    + _ _ _ _ _ _ _ _ 
    - _ _ _ _ _ _ _ _
    - _ _ _ _ _ _ _ B
    + _ _ _ _ _ _ _ _ 
    + W _ _ _ _ _ _ _

      146 |         '_ _ _ _ _ _ _ B',
      147 |       ].join('\n');
    > 148 |       expect(queens.toString()).toEqual(board);
          |                                 ^
      149 |     });
      150 |   });
      151 | });

      at Object.toEqual (queen-attack.spec.js:148:33)

Test Suites: 1 failed, 1 total
Tests:       10 failed, 9 passed, 19 total
Snapshots:   0 total
Time:        0.735 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./queen-attack.js|./queen-attack.spec.js.
