+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' complex-numbers.spec.js
+ npm run test

> test
> jest ./*

FAIL ./complex-numbers.spec.js (6.148 s)
  Complex numbers
    ✓ Real part of a purely real number (23 ms)
    ✓ Real part of a purely imaginary number
    ✓ Real part of a number with real and imaginary part
    ✓ Imaginary part of a purely real number (4 ms)
    ✓ Imaginary part of a purely imaginary number (1 ms)
    ✓ Imaginary part of a number with real and imaginary part (4 ms)
    ✓ Add purely real numbers (3 ms)
    ✓ Add purely imaginary numbers (1 ms)
    ✓ Add numbers with real and imaginary part (1 ms)
    ✓ Subtract purely real numbers (2 ms)
    ✓ Subtract purely imaginary numbers (1 ms)
    ✓ Subtract numbers with real and imaginary part (1 ms)
    ✓ Multiply purely real numbers (1 ms)
    ✓ Multiply imaginary unit (1 ms)
    ✓ Multiply purely imaginary numbers (1 ms)
    ✓ Multiply numbers with real and imaginary part (1 ms)
    ✓ Divide purely real numbers
    ✓ Divide purely imaginary numbers (4 ms)
    ✓ Divide numbers with real and imaginary part
    ✓ Absolute value of a positive purely real number
    ✓ Absolute value of a negative purely real number (1 ms)
    ✓ Absolute value of a purely imaginary number with positive imaginary part
    ✓ Absolute value of a purely imaginary number with negative imaginary part (1 ms)
    ✓ Absolute value of a number with real and imaginary part (3 ms)
    ✕ Conjugate a purely real number (115 ms)
    ✓ Conjugate a purely imaginary number (17 ms)
    ✓ Conjugate a number with real and imaginary part
    ✓ Euler's identity/formula (1 ms)
    ✓ Exponential of 0
    ✓ Exponential of a purely real number (12 ms)
    ✓ Exponential of a number with real and imaginary part (8 ms)

  ● Complex numbers › Conjugate a purely real number

    RangeError: Maximum call stack size exceeded

      174 |     const actual = new ComplexNumber(5, 0).conj;
      175 |
    > 176 |     expect(actual).toEqual(expected);
          |                    ^
      177 |   });
      178 |
      179 |   test('Conjugate a purely imaginary number', () => {

      at Object.toEqual (complex-numbers.spec.js:176:20)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 30 passed, 31 total
Snapshots:   0 total
Time:        6.514 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/complex-numbers.js|.\/complex-numbers.spec.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
