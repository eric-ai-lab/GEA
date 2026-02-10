+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' binary.spec.js
+ npm run test

> test
> jest ./*

FAIL ./binary.spec.js
  binary
    ✓ 0 is decimal 0 (18 ms)
    ✓ 1 is decimal 1 (1 ms)
    ✓ 10 is decimal 2 (1 ms)
    ✓ 11 is decimal 3
    ✓ 100 is decimal 4 (1 ms)
    ✓ 1001 is decimal 9 (21 ms)
    ✓ 11010 is decimal 26 (2 ms)
    ✓ 10001101000 is decimal 1128 (1 ms)
    ✓ ignores leading zeros (2 ms)
    ✕ invalid inputs are null (11 ms)

  ● binary › invalid inputs are null

    expect(received).toEqual(expected) // deep equality

    Expected: null
    Received: 0

      29 |   test('invalid inputs are null', () => {
      30 |     // "2 is not a valid binary digit
    > 31 |     expect(new Binary('2').toDecimal()).toEqual(null);
         |                                         ^
      32 |
      33 |     // a number containing a non-binary digit is invalid
      34 |     expect(new Binary('01201').toDecimal()).toEqual(null);

      at Object.toEqual (binary.spec.js:31:41)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 9 passed, 10 total
Snapshots:   0 total
Time:        3.996 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/binary.js|.\/binary.spec.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
