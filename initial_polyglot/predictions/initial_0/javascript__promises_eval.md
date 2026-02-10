+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' promises.spec.js
+ npm run test

> test
> jest ./*

FAIL ./promises.spec.js (13.103 s)
  promises
    promisify
      ✓ returns a function (7 ms)
      ✓ promisified function call returns a Promise (1 ms)
      ✓ promisified function resolves to a callback's success value (67 ms)
      ✓ promisified function rejects a callback's error (13 ms)
    all
      ✓ returns a Promise (2 ms)
      ✓ resolves when given no promises (6 ms)
      ✕ resolves when given no arguments (8 ms)
      ✓ resolved values appear in the order they are passed in (21 ms)
      ✓ rejects if any promises fail (11 ms)
    allSettled
      ✓ returns a Promise (1 ms)
      ✓ resolves when given no promises (3 ms)
      ✕ resolves when given no arguments (1 ms)
      ✕ resolved values appear in the order they are passed in (81 ms)
      ✕ resolves even if some promises fail (21 ms)
    race
      ✓ returns a Promise
      ✕ resolves when given no promises (5011 ms)
      ✕ resolves when given no arguments (6 ms)
      ✓ resolves with value of the fastest successful promise (38 ms)
      ✓ resolves with value of the fastest promise even if other slower promises fail (3 ms)
      ✓ rejects if the fastest promise fails even if other slower promises succeed (31 ms)
    any
      ✓ returns a Promise (1 ms)
      ✕ resolves when given no promises (5001 ms)
      ✕ resolves when given no arguments
      ✓ resolves with value of fastest successful promise (3 ms)
      ✓ resolves with value of the fastest successful promise even if slower promises fail (2 ms)
      ✓ resolves with value of fastest successful promise even if faster promises fail (25 ms)
      ✕ rejects with array of errors if all promises fail (34 ms)

  ● promises › all › resolves when given no arguments

    expect(received).resolves.toBeUndefined()

    Received promise rejected instead of resolved
    Rejected to value: [TypeError: Cannot read properties of undefined (reading 'length')]

      53 |
      54 |     test('resolves when given no arguments', () => {
    > 55 |       return expect(all()).resolves.toBeUndefined();
         |              ^
      56 |     });
      57 |
      58 |     test('resolved values appear in the order they are passed in', () => {

      at expect (../npm-install/node_modules/expect/build/index.js:113:15)
      at Object.expect (promises.spec.js:55:14)

  ● promises › allSettled › resolves when given no arguments

    expect(received).resolves.toBeUndefined()

    Received promise rejected instead of resolved
    Rejected to value: [TypeError: Cannot read properties of undefined (reading 'length')]

      91 |
      92 |     test('resolves when given no arguments', () => {
    > 93 |       return expect(allSettled()).resolves.toBeUndefined();
         |              ^
      94 |     });
      95 |
      96 |     test('resolved values appear in the order they are passed in', () => {

      at expect (../npm-install/node_modules/expect/build/index.js:113:15)
      at Object.expect (promises.spec.js:93:14)

  ● promises › allSettled › resolved values appear in the order they are passed in

    expect(received).resolves.toEqual(expected) // deep equality

    - Expected  -  3
    + Received  + 12

      Array [
    -   "FIRST",
    -   "SECOND",
    -   "THIRD",
    +   Object {
    +     "status": "fulfilled",
    +     "value": "FIRST",
    +   },
    +   Object {
    +     "status": "fulfilled",
    +     "value": "SECOND",
    +   },
    +   Object {
    +     "status": "fulfilled",
    +     "value": "THIRD",
    +   },
      ]

      103 |         fastPromise(THIRD),
      104 |       ]);
    > 105 |       return expect(result).resolves.toEqual([FIRST, SECOND, THIRD]);
          |                                      ^
      106 |     });
      107 |
      108 |     test('resolves even if some promises fail', () => {

      at Object.toEqual (../npm-install/node_modules/expect/build/index.js:174:22)
      at Object.toEqual (promises.spec.js:105:38)

  ● promises › allSettled › resolves even if some promises fail

    expect(received).resolves.toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 8

      Array [
    -   "FIRST",
    -   [Error: Failed callback],
    +   Object {
    +     "status": "fulfilled",
    +     "value": "FIRST",
    +   },
    +   Object {
    +     "reason": [Error: Failed callback],
    +     "status": "rejected",
    +   },
      ]

      109 |       const FIRST = 'FIRST';
      110 |       const result = allSettled([fastPromise(FIRST), failedPromise(null)]);
    > 111 |       return expect(result).resolves.toEqual([FIRST, failedCallback]);
          |                                      ^
      112 |     });
      113 |   });
      114 |

      at Object.toEqual (../npm-install/node_modules/expect/build/index.js:174:22)
      at Object.toEqual (promises.spec.js:111:38)

  ● promises › race › resolves when given no promises

    thrown: "Exceeded timeout of 5000 ms for a test.
    Add a timeout value to this test to increase the timeout, if this is a long-running test. See https://jestjs.io/docs/api#testname-fn-timeout."

      125 |     });
      126 |
    > 127 |     test('resolves when given no promises', () => {
          |     ^
      128 |       return expect(race([])).resolves.toEqual([]);
      129 |     });
      130 |

      at test (promises.spec.js:127:5)
      at describe (promises.spec.js:115:3)
      at Object.describe (promises.spec.js:3:1)

  ● promises › race › resolves when given no arguments

    expect(received).resolves.toBeUndefined()

    Received promise rejected instead of resolved
    Rejected to value: [TypeError: Cannot read properties of undefined (reading 'length')]

      130 |
      131 |     test('resolves when given no arguments', () => {
    > 132 |       return expect(race()).resolves.toBeUndefined();
          |              ^
      133 |     });
      134 |
      135 |     test('resolves with value of the fastest successful promise', () => {

      at expect (../npm-install/node_modules/expect/build/index.js:113:15)
      at Object.expect (promises.spec.js:132:14)

  ● promises › any › resolves when given no promises

    thrown: "Exceeded timeout of 5000 ms for a test.
    Add a timeout value to this test to increase the timeout, if this is a long-running test. See https://jestjs.io/docs/api#testname-fn-timeout."

      170 |     });
      171 |
    > 172 |     test('resolves when given no promises', () => {
          |     ^
      173 |       return expect(race([])).resolves.toEqual([]);
      174 |     });
      175 |

      at test (promises.spec.js:172:5)
      at describe (promises.spec.js:160:3)
      at Object.describe (promises.spec.js:3:1)

  ● promises › any › resolves when given no arguments

    expect(received).resolves.toBeUndefined()

    Received promise rejected instead of resolved
    Rejected to value: [TypeError: Cannot read properties of undefined (reading 'length')]

      175 |
      176 |     test('resolves when given no arguments', () => {
    > 177 |       return expect(race()).resolves.toBeUndefined();
          |              ^
      178 |     });
      179 |
      180 |     test('resolves with value of fastest successful promise', () => {

      at expect (../npm-install/node_modules/expect/build/index.js:113:15)
      at Object.expect (promises.spec.js:177:14)

  ● promises › any › rejects with array of errors if all promises fail

    expect(received).rejects.toEqual(expected) // deep equality

    Expected: [[Error: Failed callback], [Error: Failed callback]]
    Received: [AggregateError: All promises were rejected]

      206 |       return expect(
      207 |         any([failedPromise(null), failedPromise(null)]),
    > 208 |       ).rejects.toEqual([failedCallback, failedCallback]);
          |                 ^
      209 |     });
      210 |   });
      211 | });

      at Object.toEqual (../npm-install/node_modules/expect/build/index.js:218:22)
      at Object.toEqual (promises.spec.js:208:17)

Test Suites: 1 failed, 1 total
Tests:       9 failed, 18 passed, 27 total
Snapshots:   0 total
Time:        13.263 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/promises.js|.\/promises.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
