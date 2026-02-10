+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' rational-numbers.spec.js
+ npm run test

> test
> jest ./*

FAIL ./rational-numbers.spec.js
  Addition
    ✓ Add two positive rational numbers (19 ms)
    ✓ Add a positive rational number and a negative rational number
    ✓ Add two negative rational numbers
    ✓ Add a rational number to its additive inverse (1 ms)
  Subtraction
    ✓ Subtract two positive rational numbers (1 ms)
    ✓ Subtract a positive rational number and a negative rational number (1 ms)
    ✓ Subtract two negative rational numbers (1 ms)
    ✓ Subtract a rational number from itself (1 ms)
  Multiplication
    ✓ Multiply two positive rational numbers (1 ms)
    ✓ Multiply a negative rational number by a positive rational number (1 ms)
    ✓ Multiply two negative rational numbers (1 ms)
    ✓ Multiply a rational number by its reciprocal
    ✓ Multiply a rational number by 1 (1 ms)
    ✓ Multiply a rational number by 0 (1 ms)
  Division
    ✓ Divide two positive rational numbers
    ✓ Divide a positive rational number by a negative rational number
    ✓ Divide two negative rational numbers (1 ms)
    ✓ Divide a rational number by 1
  Absolute value
    ✓ Absolute value of a positive rational number
    ✓ Absolute value of a negative rational number (98 ms)
    ✓ Absolute value of zero (1 ms)
  Exponentiation of a rational number
    ✓ Raise a positive rational number to a positive integer power (2 ms)
    ✓ Raise a negative rational number to a positive integer power (1 ms)
    ✓ Raise zero to an integer power (2 ms)
    ✓ Raise one to an integer power (1 ms)
    ✓ Raise a positive rational number to the power of zero (2 ms)
    ✓ Raise a negative rational number to the power of zero (3 ms)
  Exponentiation of a real number to a rational number
    ✕ Raise a real number to a positive rational number (18 ms)
    ✕ Raise a real number to a negative rational number (1 ms)
    ✕ Raise a real number to a zero rational number (1 ms)
  Reduction to lowest terms
    ✓ Reduce a positive rational number to lowest terms
    ✓ Reduce a negative rational number to lowest terms (1 ms)
    ✓ Reduce a rational number with a negative denominator to lowest terms (1 ms)
    ✓ Reduce zero to lowest terms
    ✓ Reduce an integer to lowest terms (1 ms)
    ✓ Reduce one to lowest terms (1 ms)

  ● Exponentiation of a real number to a rational number › Raise a real number to a positive rational number

    expect(received).toEqual(expected) // deep equality

    Expected: 16
    Received: 9.988721231519586

      151 |   test('Raise a real number to a positive rational number', () => {
      152 |     const expected = 16.0;
    > 153 |     expect(new Rational(4, 3).expreal(8)).toEqual(expected);
          |                                           ^
      154 |   });
      155 |
      156 |   test('Raise a real number to a negative rational number', () => {

      at Object.toEqual (rational-numbers.spec.js:153:43)

  ● Exponentiation of a real number to a rational number › Raise a real number to a negative rational number

    expect(received).toBeCloseTo(expected, precision)

    Expected: 0.33
    Received: -0.001953125

    Expected precision:    2
    Expected difference: < 0.005
    Received difference:   0.331953125

      155 |
      156 |   test('Raise a real number to a negative rational number', () => {
    > 157 |     expect(new Rational(-1, 2).expreal(9)).toBeCloseTo(0.33, 2);
          |                                            ^
      158 |   });
      159 |
      160 |   test('Raise a real number to a zero rational number', () => {

      at Object.toBeCloseTo (rational-numbers.spec.js:157:44)

  ● Exponentiation of a real number to a rational number › Raise a real number to a zero rational number

    expect(received).toEqual(expected) // deep equality

    Expected: 1
    Received: 0

      160 |   test('Raise a real number to a zero rational number', () => {
      161 |     const expected = 1.0;
    > 162 |     expect(new Rational(0, 1).expreal(2)).toEqual(expected);
          |                                           ^
      163 |   });
      164 | });
      165 |

      at Object.toEqual (rational-numbers.spec.js:162:43)

Test Suites: 1 failed, 1 total
Tests:       3 failed, 33 passed, 36 total
Snapshots:   0 total
Time:        5.088 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/rational-numbers.js|.\/rational-numbers.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
