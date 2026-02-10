+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' rational-numbers.spec.js
+ npm run test

> test
> jest ./*

PASS ./rational-numbers.spec.js
  Addition
    ✓ Add two positive rational numbers (4 ms)
    ✓ Add a positive rational number and a negative rational number (1 ms)
    ✓ Add two negative rational numbers (1 ms)
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
    ✓ Multiply a rational number by 1
    ✓ Multiply a rational number by 0 (1 ms)
  Division
    ✓ Divide two positive rational numbers (1 ms)
    ✓ Divide a positive rational number by a negative rational number
    ✓ Divide two negative rational numbers (1 ms)
    ✓ Divide a rational number by 1
  Absolute value
    ✓ Absolute value of a positive rational number
    ✓ Absolute value of a negative rational number (1 ms)
    ✓ Absolute value of zero
  Exponentiation of a rational number
    ✓ Raise a positive rational number to a positive integer power (1 ms)
    ✓ Raise a negative rational number to a positive integer power
    ✓ Raise zero to an integer power (1 ms)
    ✓ Raise one to an integer power
    ✓ Raise a positive rational number to the power of zero
    ✓ Raise a negative rational number to the power of zero
  Exponentiation of a real number to a rational number
    ✓ Raise a real number to a positive rational number
    ✓ Raise a real number to a negative rational number (1 ms)
    ✓ Raise a real number to a zero rational number
  Reduction to lowest terms
    ✓ Reduce a positive rational number to lowest terms (1 ms)
    ✓ Reduce a negative rational number to lowest terms
    ✓ Reduce a rational number with a negative denominator to lowest terms (1 ms)
    ✓ Reduce zero to lowest terms
    ✓ Reduce an integer to lowest terms
    ✓ Reduce one to lowest terms (1 ms)

Test Suites: 1 passed, 1 total
Tests:       36 passed, 36 total
Snapshots:   0 total
Time:        0.867 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./rational-numbers.js|./rational-numbers.spec.js.
