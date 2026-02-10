+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' tournament.spec.js
+ npm run test

> test
> jest ./*

FAIL ./tournament.spec.js
  Tournament
    ✓ just the header if no input (5 ms)
    ✕ a win is three points, a loss is zero points (71 ms)
    ✕ a win can also be expressed as a loss (25 ms)
    ✕ a different team can win (1 ms)
    ✕ a draw is one point each (74 ms)
    ✕ there can be more than one match (2 ms)
    ✕ there can be more than one winner (1 ms)
    ✕ there can be more than two teams (2 ms)
    ✕ typical input (1 ms)
    ✕ incomplete competition (not all pairs have played) (16 ms)
    ✕ ties broken alphabetically (2 ms)
    ✕ ensure points sorted numerically (20 ms)

  ● Tournament › a win is three points, a loss is zero points

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 2

      Team                           | MP |  W |  D |  L |  P
    - Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3
    + Allegoric Alaskans              |  1 |  1 |  0 |  0 |  3
    - Blithering Badgers             |  1 |  0 |  0 |  1 |  0
    + Blithering Badgers              |  1 |  0 |  0 |  1 |  0

      13 |       'Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3\n' +
      14 |       'Blithering Badgers             |  1 |  0 |  0 |  1 |  0';
    > 15 |     expect(tally).toEqual(expected);
         |                   ^
      16 |   });
      17 |   test('a win can also be expressed as a loss', () => {
      18 |     const tally = tournamentTally('Blithering Badgers;Allegoric Alaskans;loss');

      at Object.toEqual (tournament.spec.js:15:19)

  ● Tournament › a win can also be expressed as a loss

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 2

      Team                           | MP |  W |  D |  L |  P
    - Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3
    + Allegoric Alaskans              |  1 |  1 |  0 |  0 |  3
    - Blithering Badgers             |  1 |  0 |  0 |  1 |  0
    + Blithering Badgers              |  1 |  0 |  0 |  1 |  0

      21 |       'Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3\n' +
      22 |       'Blithering Badgers             |  1 |  0 |  0 |  1 |  0';
    > 23 |     expect(tally).toEqual(expected);
         |                   ^
      24 |   });
      25 |   test('a different team can win', () => {
      26 |     const tally = tournamentTally('Blithering Badgers;Allegoric Alaskans;win');

      at Object.toEqual (tournament.spec.js:23:19)

  ● Tournament › a different team can win

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 2

      Team                           | MP |  W |  D |  L |  P
    - Blithering Badgers             |  1 |  1 |  0 |  0 |  3
    + Blithering Badgers              |  1 |  1 |  0 |  0 |  3
    - Allegoric Alaskans             |  1 |  0 |  0 |  1 |  0
    + Allegoric Alaskans              |  1 |  0 |  0 |  1 |  0

      29 |       'Blithering Badgers             |  1 |  1 |  0 |  0 |  3\n' +
      30 |       'Allegoric Alaskans             |  1 |  0 |  0 |  1 |  0';
    > 31 |     expect(tally).toEqual(expected);
         |                   ^
      32 |   });
      33 |   test('a draw is one point each', () => {
      34 |     const tally = tournamentTally('Allegoric Alaskans;Blithering Badgers;draw');

      at Object.toEqual (tournament.spec.js:31:19)

  ● Tournament › a draw is one point each

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 2

      Team                           | MP |  W |  D |  L |  P
    - Allegoric Alaskans             |  1 |  0 |  1 |  0 |  1
    + Allegoric Alaskans              |  1 |  0 |  1 |  0 |  1
    - Blithering Badgers             |  1 |  0 |  1 |  0 |  1
    + Blithering Badgers              |  1 |  0 |  1 |  0 |  1

      37 |       'Allegoric Alaskans             |  1 |  0 |  1 |  0 |  1\n' +
      38 |       'Blithering Badgers             |  1 |  0 |  1 |  0 |  1';
    > 39 |     expect(tally).toEqual(expected);
         |                   ^
      40 |   });
      41 |   test('there can be more than one match', () => {
      42 |     const input =

      at Object.toEqual (tournament.spec.js:39:19)

  ● Tournament › there can be more than one match

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 2

      Team                           | MP |  W |  D |  L |  P
    - Allegoric Alaskans             |  2 |  2 |  0 |  0 |  6
    + Allegoric Alaskans              |  2 |  2 |  0 |  0 |  6
    - Blithering Badgers             |  2 |  0 |  0 |  2 |  0
    + Blithering Badgers              |  2 |  0 |  0 |  2 |  0

      48 |       'Allegoric Alaskans             |  2 |  2 |  0 |  0 |  6\n' +
      49 |       'Blithering Badgers             |  2 |  0 |  0 |  2 |  0';
    > 50 |     expect(tally).toEqual(expected);
         |                   ^
      51 |   });
      52 |   test('there can be more than one winner', () => {
      53 |     const input =

      at Object.toEqual (tournament.spec.js:50:19)

  ● Tournament › there can be more than one winner

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 2

      Team                           | MP |  W |  D |  L |  P
    - Allegoric Alaskans             |  2 |  1 |  0 |  1 |  3
    + Allegoric Alaskans              |  2 |  1 |  0 |  1 |  3
    - Blithering Badgers             |  2 |  1 |  0 |  1 |  3
    + Blithering Badgers              |  2 |  1 |  0 |  1 |  3

      59 |       'Allegoric Alaskans             |  2 |  1 |  0 |  1 |  3\n' +
      60 |       'Blithering Badgers             |  2 |  1 |  0 |  1 |  3';
    > 61 |     expect(tally).toEqual(expected);
         |                   ^
      62 |   });
      63 |   test('there can be more than two teams', () => {
      64 |     const input =

      at Object.toEqual (tournament.spec.js:61:19)

  ● Tournament › there can be more than two teams

    expect(received).toEqual(expected) // deep equality

    - Expected  - 3
    + Received  + 3

      Team                           | MP |  W |  D |  L |  P
    - Allegoric Alaskans             |  2 |  2 |  0 |  0 |  6
    + Allegoric Alaskans              |  2 |  2 |  0 |  0 |  6
    - Blithering Badgers             |  2 |  1 |  0 |  1 |  3
    + Blithering Badgers              |  2 |  1 |  0 |  1 |  3
    - Courageous Californians        |  2 |  0 |  0 |  2 |  0
    + Courageous Californians         |  2 |  0 |  0 |  2 |  0

      72 |       'Blithering Badgers             |  2 |  1 |  0 |  1 |  3\n' +
      73 |       'Courageous Californians        |  2 |  0 |  0 |  2 |  0';
    > 74 |     expect(tally).toEqual(expected);
         |                   ^
      75 |   });
      76 |   test('typical input', () => {
      77 |     const input =

      at Object.toEqual (tournament.spec.js:74:19)

  ● Tournament › typical input

    expect(received).toEqual(expected) // deep equality

    - Expected  - 4
    + Received  + 4

      Team                           | MP |  W |  D |  L |  P
    - Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
    + Devastating Donkeys             |  3 |  2 |  1 |  0 |  7
    - Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
    + Allegoric Alaskans              |  3 |  2 |  0 |  1 |  6
    - Blithering Badgers             |  3 |  1 |  0 |  2 |  3
    + Blithering Badgers              |  3 |  1 |  0 |  2 |  3
    - Courageous Californians        |  3 |  0 |  1 |  2 |  1
    + Courageous Californians         |  3 |  0 |  1 |  2 |  1

      89 |       'Blithering Badgers             |  3 |  1 |  0 |  2 |  3\n' +
      90 |       'Courageous Californians        |  3 |  0 |  1 |  2 |  1';
    > 91 |     expect(tally).toEqual(expected);
         |                   ^
      92 |   });
      93 |   test('incomplete competition (not all pairs have played)', () => {
      94 |     const input =

      at Object.toEqual (tournament.spec.js:91:19)

  ● Tournament › incomplete competition (not all pairs have played)

    expect(received).toEqual(expected) // deep equality

    - Expected  - 4
    + Received  + 4

      Team                           | MP |  W |  D |  L |  P
    - Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
    + Allegoric Alaskans              |  3 |  2 |  0 |  1 |  6
    - Blithering Badgers             |  2 |  1 |  1 |  0 |  4
    + Blithering Badgers              |  2 |  1 |  1 |  0 |  4
    - Courageous Californians        |  2 |  0 |  1 |  1 |  1
    + Courageous Californians         |  2 |  0 |  1 |  1 |  1
    - Devastating Donkeys            |  1 |  0 |  0 |  1 |  0
    + Devastating Donkeys             |  1 |  0 |  0 |  1 |  0

      104 |       'Courageous Californians        |  2 |  0 |  1 |  1 |  1\n' +
      105 |       'Devastating Donkeys            |  1 |  0 |  0 |  1 |  0';
    > 106 |     expect(tally).toEqual(expected);
          |                   ^
      107 |   });
      108 |   test('ties broken alphabetically', () => {
      109 |     const input =

      at Object.toEqual (tournament.spec.js:106:19)

  ● Tournament › ties broken alphabetically

    expect(received).toEqual(expected) // deep equality

    - Expected  - 4
    + Received  + 4

      Team                           | MP |  W |  D |  L |  P
    - Allegoric Alaskans             |  3 |  2 |  1 |  0 |  7
    + Allegoric Alaskans              |  3 |  2 |  1 |  0 |  7
    - Courageous Californians        |  3 |  2 |  1 |  0 |  7
    + Courageous Californians         |  3 |  2 |  1 |  0 |  7
    - Blithering Badgers             |  3 |  0 |  1 |  2 |  1
    + Blithering Badgers              |  3 |  0 |  1 |  2 |  1
    - Devastating Donkeys            |  3 |  0 |  1 |  2 |  1
    + Devastating Donkeys             |  3 |  0 |  1 |  2 |  1

      121 |       'Blithering Badgers             |  3 |  0 |  1 |  2 |  1\n' +
      122 |       'Devastating Donkeys            |  3 |  0 |  1 |  2 |  1';
    > 123 |     expect(tally).toEqual(expected);
          |                   ^
      124 |   });
      125 |   test('ensure points sorted numerically', () => {
      126 |     const input =

      at Object.toEqual (tournament.spec.js:123:19)

  ● Tournament › ensure points sorted numerically

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 2

      Team                           | MP |  W |  D |  L |  P
    - Devastating Donkeys            |  5 |  4 |  0 |  1 | 12
    + Devastating Donkeys             |  5 |  4 |  0 |  1 | 12
    - Blithering Badgers             |  5 |  1 |  0 |  4 |  3
    + Blithering Badgers              |  5 |  1 |  0 |  4 |  3

      135 |       'Devastating Donkeys            |  5 |  4 |  0 |  1 | 12\n' +
      136 |       'Blithering Badgers             |  5 |  1 |  0 |  4 |  3';
    > 137 |     expect(tally).toEqual(expected);
          |                   ^
      138 |   });
      139 | });
      140 |

      at Object.toEqual (tournament.spec.js:137:19)

Test Suites: 1 failed, 1 total
Tests:       11 failed, 1 passed, 12 total
Snapshots:   0 total
Time:        5.076 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/tournament.js|.\/tournament.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
