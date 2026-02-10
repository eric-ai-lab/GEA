+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' go-counting.spec.js
+ npm run test

> test
> jest ./*

FAIL ./go-counting.spec.js
  Go Counting
    getTerritory
      ✕ Black corner territory on 5x5 board (55 ms)
      ✕ White center territory on 5x5 board (2 ms)
      ✕ Open corner territory on 5x5 board (18 ms)
      ✓ A stone and not a territory on 5x5 board
      ✕ Invalid because X is too low for 5x5 board (21 ms)
      ✕ Invalid because X is too high for 5x5 board (1 ms)
      ✕ Invalid because Y is too low for 5x5 board
      ✕ Invalid because Y is too high for 5x5 board
    getTerritories
      ✓ One territory is the whole board (1 ms)
      ✕ Two territory rectangular board (1 ms)
      ✕ Two region rectangular board (1 ms)

  ● Go Counting › getTerritory › Black corner territory on 5x5 board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 2

    @@ -1,15 +1,15 @@
      Object {
        "owner": "BLACK",
        "territory": Array [
          Array [
            0,
    -       0,
    +       1,
          ],
          Array [
    +       0,
            0,
    -       1,
          ],
          Array [
            1,
            0,
          ],

      14 |         ],
      15 |       };
    > 16 |       expect(goCounting.getTerritory(0, 1)).toEqual(expectedTerritory);
         |                                             ^
      17 |     });
      18 |
      19 |     test('White center territory on 5x5 board', () => {

      at Object.toEqual (go-counting.spec.js:16:45)

  ● Go Counting › getTerritory › White center territory on 5x5 board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

    @@ -1,7 +1,7 @@
      Object {
    -   "owner": "WHITE",
    +   "owner": "NONE",
        "territory": Array [
          Array [
            2,
            3,
          ],

      21 |       const goCounting = new GoCounting(board);
      22 |       const expectedTerritory = { owner: 'WHITE', territory: [[2, 3]] };
    > 23 |       expect(goCounting.getTerritory(2, 3)).toEqual(expectedTerritory);
         |                                             ^
      24 |     });
      25 |
      26 |     test('Open corner territory on 5x5 board', () => {

      at Object.toEqual (go-counting.spec.js:23:45)

  ● Go Counting › getTerritory › Open corner territory on 5x5 board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 5
    + Received  + 5

      Object {
    -   "owner": "NONE",
    +   "owner": "BLACK",
        "territory": Array [
          Array [
    -       0,
    -       3,
    +       1,
    +       4,
          ],
          Array [
            0,
            4,
          ],
          Array [
    -       1,
    -       4,
    +       0,
    +       3,
          ],
        ],
      }

      35 |         ],
      36 |       };
    > 37 |       expect(goCounting.getTerritory(1, 4)).toEqual(expectedTerritory);
         |                                             ^
      38 |     });
      39 |
      40 |     test('A stone and not a territory on 5x5 board', () => {

      at Object.toEqual (go-counting.spec.js:37:45)

  ● Go Counting › getTerritory › Invalid because X is too low for 5x5 board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 2

      Object {
    -   "error": "Invalid coordinate",
    +   "owner": "NONE",
    +   "territory": Array [],
      }

      49 |       const goCounting = new GoCounting(board);
      50 |       const expectedTerritory = { error: 'Invalid coordinate' };
    > 51 |       expect(goCounting.getTerritory(-1, 1)).toEqual(expectedTerritory);
         |                                              ^
      52 |     });
      53 |
      54 |     test('Invalid because X is too high for 5x5 board', () => {

      at Object.toEqual (go-counting.spec.js:51:46)

  ● Go Counting › getTerritory › Invalid because X is too high for 5x5 board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 2

      Object {
    -   "error": "Invalid coordinate",
    +   "owner": "NONE",
    +   "territory": Array [],
      }

      56 |       const goCounting = new GoCounting(board);
      57 |       const expectedTerritory = { error: 'Invalid coordinate' };
    > 58 |       expect(goCounting.getTerritory(5, 1)).toEqual(expectedTerritory);
         |                                             ^
      59 |     });
      60 |
      61 |     test('Invalid because Y is too low for 5x5 board', () => {

      at Object.toEqual (go-counting.spec.js:58:45)

  ● Go Counting › getTerritory › Invalid because Y is too low for 5x5 board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 2

      Object {
    -   "error": "Invalid coordinate",
    +   "owner": "NONE",
    +   "territory": Array [],
      }

      63 |       const goCounting = new GoCounting(board);
      64 |       const expectedTerritory = { error: 'Invalid coordinate' };
    > 65 |       expect(goCounting.getTerritory(1, -1)).toEqual(expectedTerritory);
         |                                              ^
      66 |     });
      67 |
      68 |     test('Invalid because Y is too high for 5x5 board', () => {

      at Object.toEqual (go-counting.spec.js:65:46)

  ● Go Counting › getTerritory › Invalid because Y is too high for 5x5 board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 2

      Object {
    -   "error": "Invalid coordinate",
    +   "owner": "NONE",
    +   "territory": Array [],
      }

      70 |       const goCounting = new GoCounting(board);
      71 |       const expectedTerritory = { error: 'Invalid coordinate' };
    > 72 |       expect(goCounting.getTerritory(1, 5)).toEqual(expectedTerritory);
         |                                             ^
      73 |     });
      74 |   });
      75 |

      at Object.toEqual (go-counting.spec.js:72:45)

  ● Go Counting › getTerritories › Two territory rectangular board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 3
    + Received  + 3

    @@ -3,21 +3,21 @@
          Array [
            0,
            0,
          ],
          Array [
    +       1,
            0,
    -       1,
          ],
        ],
        "territoryNone": Array [],
        "territoryWhite": Array [
          Array [
    -       3,
            0,
    +       3,
          ],
          Array [
    -       3,
            1,
    +       3,
          ],
        ],
      }

      100 |         territoryNone: [],
      101 |       };
    > 102 |       expect(goCounting.getTerritories()).toEqual(expectedTerritories);
          |                                           ^
      103 |     });
      104 |
      105 |     test('Two region rectangular board', () => {

      at Object.toEqual (go-counting.spec.js:102:43)

  ● Go Counting › getTerritories › Two region rectangular board

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

    @@ -3,12 +3,12 @@
          Array [
            0,
            0,
          ],
          Array [
    -       2,
            0,
    +       2,
          ],
        ],
        "territoryNone": Array [],
        "territoryWhite": Array [],
      }

      114 |         territoryNone: [],
      115 |       };
    > 116 |       expect(goCounting.getTerritories()).toEqual(expectedTerritories);
          |                                           ^
      117 |     });
      118 |   });
      119 | });

      at Object.toEqual (go-counting.spec.js:116:43)

Test Suites: 1 failed, 1 total
Tests:       9 failed, 2 passed, 11 total
Snapshots:   0 total
Time:        3.338 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/go-counting.js|.\/go-counting.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
