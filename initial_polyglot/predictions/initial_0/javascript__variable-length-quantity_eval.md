+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' variable-length-quantity.spec.js
+ npm run test

> test
> jest ./*

FAIL ./variable-length-quantity.spec.js
  VariableLengthQuantity
    Encode a series of integers, producing a series of bytes.
      ✓ zero (19 ms)
      ✓ arbitrary single byte (1 ms)
      ✓ largest single byte
      ✓ smallest double byte
      ✓ arbitrary double byte (1 ms)
      ✓ largest double byte (1 ms)
      ✓ smallest triple byte
      ✓ arbitrary triple byte (1 ms)
      ✓ largest triple byte (1 ms)
      ✓ smallest quadruple byte (1 ms)
      ✓ arbitrary quadruple byte (1 ms)
      ✓ largest quadruple byte
      ✓ smallest quintuple byte (1 ms)
      ✓ arbitrary quintuple byte (1 ms)
      ✓ maximum 32-bit integer input
      ✓ two single-byte values (4 ms)
      ✓ two multi-byte values (1 ms)
      ✓ many multi-byte values
    Decode a series of bytes, producing a series of integers.
      ✓ one byte
      ✓ two bytes
      ✓ three bytes (1 ms)
      ✓ four bytes (4 ms)
      ✕ maximum 32-bit integer (36 ms)
      ✓ incomplete sequence causes error (16 ms)
      ✓ incomplete sequence causes error, even if value is zero (1 ms)
      ✓ multiple values (1 ms)

  ● VariableLengthQuantity › Decode a series of bytes, producing a series of integers. › maximum 32-bit integer

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      Array [
    -   4294967295,
    +   -1,
      ]

      101 |
      102 |     test('maximum 32-bit integer', () => {
    > 103 |       expect(decode([0x8f, 0xff, 0xff, 0xff, 0x7f])).toEqual([0xffffffff]);
          |                                                      ^
      104 |     });
      105 |
      106 |     test('incomplete sequence causes error', () => {

      at Object.toEqual (variable-length-quantity.spec.js:103:54)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 25 passed, 26 total
Snapshots:   0 total
Time:        3.051 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/variable-length-quantity.js|.\/variable-length-quantity.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
