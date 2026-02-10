+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' palindrome-products.spec.js
+ npm run test

> test
> jest ./*

FAIL ./palindrome-products.spec.js
  Palindromes
    ✕ smallest palindrome from single digit factors (3 ms)
    ✕ largest palindrome from single digit factors (1 ms)
    ✕ smallest palindrome from double digit factors (1 ms)
    ✕ largest palindrome from double digit factors (1 ms)
    ✕ smallest palindrome from triple digit factors
    ✕ largest palindrome from triple digit factors (1 ms)
    ✕ smallest palindrome from four digit factors (1 ms)
    ✕ empty result for smallest if no palindrome in range (1 ms)
    ✕ empty result for largest if no palindrome in range
    ✕ error for smallest if min is more than max (17 ms)
    ✕ error for largest if min is more than max (2 ms)
    ○ skipped largest palindrome from four digit factors

  ● Palindromes › smallest palindrome from single digit factors

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:5:37)

  ● Palindromes › largest palindrome from single digit factors

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:14:37)

  ● Palindromes › smallest palindrome from double digit factors

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:29:37)

  ● Palindromes › largest palindrome from double digit factors

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:38:37)

  ● Palindromes › smallest palindrome from triple digit factors

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:47:37)

  ● Palindromes › largest palindrome from triple digit factors

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:59:37)

  ● Palindromes › smallest palindrome from four digit factors

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:71:37)

  ● Palindromes › empty result for smallest if no palindrome in range

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:101:37)

  ● Palindromes › empty result for largest if no palindrome in range

    min and max must be provided

      24 |     // Validate inputs
      25 |     if (min === undefined || max === undefined) {
    > 26 |       throw new Error('min and max must be provided');
         |             ^
      27 |     }
      28 |
      29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at Object.generate (palindrome-products.spec.js:112:37)

  ● Palindromes › error for smallest if min is more than max

    expect(received).toThrow(expected)

    Expected message: "min must be <= max"
    Received message: "min and max must be provided"

          24 |     // Validate inputs
          25 |     if (min === undefined || max === undefined) {
        > 26 |       throw new Error('min and max must be provided');
             |             ^
          27 |     }
          28 |
          29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at generate (palindrome-products.spec.js:121:39)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (palindrome-products.spec.js:126:8)
      at Object.toThrow (palindrome-products.spec.js:126:8)

  ● Palindromes › error for largest if min is more than max

    expect(received).toThrow(expected)

    Expected message: "min must be <= max"
    Received message: "min and max must be provided"

          24 |     // Validate inputs
          25 |     if (min === undefined || max === undefined) {
        > 26 |       throw new Error('min and max must be provided');
             |             ^
          27 |     }
          28 |
          29 |     if (min < 1) {

      at Function.generate (palindrome-products.js:26:13)
      at generate (palindrome-products.spec.js:131:39)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (palindrome-products.spec.js:133:8)
      at Object.toThrow (palindrome-products.spec.js:133:8)

Test Suites: 1 failed, 1 total
Tests:       11 failed, 1 skipped, 12 total
Snapshots:   0 total
Time:        0.939 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./palindrome-products.js|./palindrome-products.spec.js.
