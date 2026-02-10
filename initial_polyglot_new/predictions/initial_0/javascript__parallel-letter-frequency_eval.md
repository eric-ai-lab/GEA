+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' parallel-letter-frequency.spec.js
+ npm run test

> test
> jest ./*

FAIL ./parallel-letter-frequency.spec.js
  ParallelLetterFrequency
    ✓ no texts (3 ms)
    ✕ one text with one letter (80 ms)
    ✕ one text with multiple letters (39 ms)
    ✕ two texts with one letter (40 ms)
    ✕ two texts with multiple letters (31 ms)
    ✕ ignore letter casing (42 ms)
    ✕ ignore whitespace (31 ms)
    ✕ ignore punctuation (36 ms)
    ✕ ignore numbers (39 ms)
    ✕ Unicode letters (45 ms)
    ✕ combination of lower- and uppercase letters, punctuation and white space (38 ms)
    ✕ large texts (31 ms)
    ✕ many small texts (63 ms)

  ● ParallelLetterFrequency › one text with one letter

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      14 |     };
      15 |     const actual = parallelLetterFrequency(texts);
    > 16 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      17 |   });
      18 |
      19 |   test('one text with multiple letters', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:16:11)

  ● ParallelLetterFrequency › one text with multiple letters

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      25 |     };
      26 |     const actual = parallelLetterFrequency(texts);
    > 27 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      28 |   });
      29 |
      30 |   test('two texts with one letter', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:27:11)

  ● ParallelLetterFrequency › two texts with one letter

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      35 |     };
      36 |     const actual = parallelLetterFrequency(texts);
    > 37 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      38 |   });
      39 |
      40 |   test('two texts with multiple letters', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:37:11)

  ● ParallelLetterFrequency › two texts with multiple letters

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      46 |     };
      47 |     const actual = parallelLetterFrequency(texts);
    > 48 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      49 |   });
      50 |
      51 |   test('ignore letter casing', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:48:11)

  ● ParallelLetterFrequency › ignore letter casing

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      55 |     };
      56 |     const actual = parallelLetterFrequency(texts);
    > 57 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      58 |   });
      59 |
      60 |   test('ignore whitespace', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:57:11)

  ● ParallelLetterFrequency › ignore whitespace

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      62 |     const expected = {};
      63 |     const actual = parallelLetterFrequency(texts);
    > 64 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      65 |   });
      66 |
      67 |   test('ignore punctuation', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:64:11)

  ● ParallelLetterFrequency › ignore punctuation

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      69 |     const expected = {};
      70 |     const actual = parallelLetterFrequency(texts);
    > 71 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      72 |   });
      73 |
      74 |   test('ignore numbers', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:71:11)

  ● ParallelLetterFrequency › ignore numbers

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      76 |     const expected = {};
      77 |     const actual = parallelLetterFrequency(texts);
    > 78 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      79 |   });
      80 |
      81 |   test('Unicode letters', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:78:11)

  ● ParallelLetterFrequency › Unicode letters

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      88 |     };
      89 |     const actual = parallelLetterFrequency(texts);
    > 90 |     await expect(actual).resolves.toEqual(expected);
         |           ^
      91 |   });
      92 |
      93 |   test('combination of lower- and uppercase letters, punctuation and white space', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:90:11)

  ● ParallelLetterFrequency › combination of lower- and uppercase letters, punctuation and white space

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      120 |     };
      121 |     const actual = parallelLetterFrequency(texts);
    > 122 |     await expect(actual).resolves.toEqual(expected);
          |           ^
      123 |   });
      124 |
      125 |   test('large texts', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:122:11)

  ● ParallelLetterFrequency › large texts

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      158 |     };
      159 |     const actual = parallelLetterFrequency(texts);
    > 160 |     await expect(actual).resolves.toEqual(expected);
          |           ^
      161 |   });
      162 |
      163 |   test('many small texts', async () => {

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:160:11)

  ● ParallelLetterFrequency › many small texts

    expect(received).resolves.toEqual()

    Received promise rejected instead of resolved
    Rejected to value: [Error: Cannot find module '/testbed/worker.js']

      169 |     };
      170 |     const actual = parallelLetterFrequency(texts);
    > 171 |     await expect(actual).resolves.toEqual(expected);
          |           ^
      172 |   });
      173 | });
      174 |

      at expect (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2116:15)
      at Object.expect (parallel-letter-frequency.spec.js:171:11)

Test Suites: 1 failed, 1 total
Tests:       12 failed, 1 passed, 13 total
Snapshots:   0 total
Time:        1.323 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./parallel-letter-frequency.js|./parallel-letter-frequency.spec.js.
