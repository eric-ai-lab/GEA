+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' zebra-puzzle.spec.js
+ npm run test

> test
> jest ./*

FAIL ./zebra-puzzle.spec.js
  Zebra puzzle
    ✕ resident who drinks water (350 ms)
    ✕ resident who owns zebra (129 ms)

  ● Zebra puzzle › resident who drinks water

    expect(received).toEqual(expected) // deep equality

    Expected: "Norwegian"
    Received: "Japanese"

      4 |   test('resident who drinks water', () => {
      5 |     const puzzle = new ZebraPuzzle();
    > 6 |     expect(puzzle.waterDrinker()).toEqual('Norwegian');
        |                                   ^
      7 |   });
      8 |   test('resident who owns zebra', () => {
      9 |     const puzzle = new ZebraPuzzle();

      at Object.toEqual (zebra-puzzle.spec.js:6:35)

  ● Zebra puzzle › resident who owns zebra

    expect(received).toEqual(expected) // deep equality

    Expected: "Japanese"
    Received: "Ukrainian"

       8 |   test('resident who owns zebra', () => {
       9 |     const puzzle = new ZebraPuzzle();
    > 10 |     expect(puzzle.zebraOwner()).toEqual('Japanese');
         |                                 ^
      11 |   });
      12 | });
      13 |

      at Object.toEqual (zebra-puzzle.spec.js:10:33)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 2 total
Snapshots:   0 total
Time:        2.848 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/zebra-puzzle.js|.\/zebra-puzzle.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
