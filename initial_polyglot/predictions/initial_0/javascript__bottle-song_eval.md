+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' bottle-song.spec.js
+ npm run test

> test
> jest ./*

FAIL ./bottle-song.spec.js (5.136 s)
  Bottle Song
    verse
      single verse
        ✕ first generic verse (39 ms)
        ✕ last generic verse (1 ms)
        ✕ verse with 2 bottles (1 ms)
        ✕ verse with 1 bottle (4 ms)
    lyrics
      multiple verses
        ✕ first two verses (2 ms)
        ✕ last three verses (1 ms)
        ✕ all verses (9 ms)

  ● Bottle Song › verse › single verse › first generic verse

    expect(received).toEqual(expected) // deep equality

    Expected: ["Ten green bottles hanging on the wall,", "Ten green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be nine green bottles hanging on the wall."]
    Received: "Ten green bottles hanging on the wall,
    Ten green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Nine green bottles hanging on the wall."

      11 |           `There'll be nine green bottles hanging on the wall.`,
      12 |         ];
    > 13 |         expect(recite(10, 1)).toEqual(expected);
         |                               ^
      14 |       });
      15 |
      16 |       test('last generic verse', () => {

      at Object.toEqual (bottle-song.spec.js:13:31)

  ● Bottle Song › verse › single verse › last generic verse

    expect(received).toEqual(expected) // deep equality

    Expected: ["Three green bottles hanging on the wall,", "Three green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be two green bottles hanging on the wall."]
    Received: "Three green bottles hanging on the wall,
    Three green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Two green bottles hanging on the wall."

      21 |           `There'll be two green bottles hanging on the wall.`,
      22 |         ];
    > 23 |         expect(recite(3, 1)).toEqual(expected);
         |                              ^
      24 |       });
      25 |
      26 |       test('verse with 2 bottles', () => {

      at Object.toEqual (bottle-song.spec.js:23:30)

  ● Bottle Song › verse › single verse › verse with 2 bottles

    expect(received).toEqual(expected) // deep equality

    Expected: ["Two green bottles hanging on the wall,", "Two green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be one green bottle hanging on the wall."]
    Received: "Two green bottles hanging on the wall,
    Two green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be one green bottle hanging on the wall."

      31 |           `There'll be one green bottle hanging on the wall.`,
      32 |         ];
    > 33 |         expect(recite(2, 1)).toEqual(expected);
         |                              ^
      34 |       });
      35 |
      36 |       test('verse with 1 bottle', () => {

      at Object.toEqual (bottle-song.spec.js:33:30)

  ● Bottle Song › verse › single verse › verse with 1 bottle

    expect(received).toEqual(expected) // deep equality

    Expected: ["One green bottle hanging on the wall,", "One green bottle hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be no green bottles hanging on the wall."]
    Received: "One green bottle hanging on the wall,
    One green bottle hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be no green bottles hanging on the wall."

      41 |           `There'll be no green bottles hanging on the wall.`,
      42 |         ];
    > 43 |         expect(recite(1, 1)).toEqual(expected);
         |                              ^
      44 |       });
      45 |     });
      46 |   });

      at Object.toEqual (bottle-song.spec.js:43:30)

  ● Bottle Song › lyrics › multiple verses › first two verses

    expect(received).toEqual(expected) // deep equality

    Expected: ["Ten green bottles hanging on the wall,", "Ten green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be nine green bottles hanging on the wall.", "", "Nine green bottles hanging on the wall,", "Nine green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be eight green bottles hanging on the wall."]
    Received: "Ten green bottles hanging on the wall,
    Ten green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Nine green bottles hanging on the wall.·
    Nine green bottles hanging on the wall,
    Nine green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Eight green bottles hanging on the wall."

      60 |           `There'll be eight green bottles hanging on the wall.`,
      61 |         ];
    > 62 |         expect(recite(10, 2)).toEqual(expected);
         |                               ^
      63 |       });
      64 |
      65 |       test('last three verses', () => {

      at Object.toEqual (bottle-song.spec.js:62:31)

  ● Bottle Song › lyrics › multiple verses › last three verses

    expect(received).toEqual(expected) // deep equality

    Expected: ["Three green bottles hanging on the wall,", "Three green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be two green bottles hanging on the wall.", "", "Two green bottles hanging on the wall,", "Two green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be one green bottle hanging on the wall.", "", …]
    Received: "Three green bottles hanging on the wall,
    Three green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Two green bottles hanging on the wall.·
    Two green bottles hanging on the wall,
    Two green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be one green bottle hanging on the wall.·
    One green bottle hanging on the wall,
    One green bottle hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be no green bottles hanging on the wall."

      80 |           `There'll be no green bottles hanging on the wall.`,
      81 |         ];
    > 82 |         expect(recite(3, 3)).toEqual(expected);
         |                              ^
      83 |       });
      84 |
      85 |       test('all verses', () => {

      at Object.toEqual (bottle-song.spec.js:82:30)

  ● Bottle Song › lyrics › multiple verses › all verses

    expect(received).toEqual(expected) // deep equality

    Expected: ["Ten green bottles hanging on the wall,", "Ten green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be nine green bottles hanging on the wall.", "", "Nine green bottles hanging on the wall,", "Nine green bottles hanging on the wall,", "And if one green bottle should accidentally fall,", "There'll be eight green bottles hanging on the wall.", "", …]
    Received: "Ten green bottles hanging on the wall,
    Ten green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Nine green bottles hanging on the wall.·
    Nine green bottles hanging on the wall,
    Nine green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Eight green bottles hanging on the wall.·
    Eight green bottles hanging on the wall,
    Eight green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Seven green bottles hanging on the wall.·
    Seven green bottles hanging on the wall,
    Seven green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Six green bottles hanging on the wall.·
    Six green bottles hanging on the wall,
    Six green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Five green bottles hanging on the wall.·
    Five green bottles hanging on the wall,
    Five green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Four green bottles hanging on the wall.·
    Four green bottles hanging on the wall,
    Four green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Three green bottles hanging on the wall.·
    Three green bottles hanging on the wall,
    Three green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be Two green bottles hanging on the wall.·
    Two green bottles hanging on the wall,
    Two green bottles hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be one green bottle hanging on the wall.·
    One green bottle hanging on the wall,
    One green bottle hanging on the wall,
    And if one green bottle should accidentally fall,
    There'll be no green bottles hanging on the wall."

      135 |           `There'll be no green bottles hanging on the wall.`,
      136 |         ];
    > 137 |         expect(recite(10, 10)).toEqual(expected);
          |                                ^
      138 |       });
      139 |     });
      140 |   });

      at Object.toEqual (bottle-song.spec.js:137:32)

Test Suites: 1 failed, 1 total
Tests:       7 failed, 7 total
Snapshots:   0 total
Time:        5.324 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/bottle-song.js|.\/bottle-song.spec.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
