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
    ✕ smallest palindrome from single digit factors (4 ms)
    ✕ largest palindrome from single digit factors
    ✕ smallest palindrome from double digit factors
    ✕ largest palindrome from double digit factors
    ✕ smallest palindrome from triple digit factors
    ✕ largest palindrome from triple digit factors (1 ms)
    ✕ smallest palindrome from four digit factors
    ✕ empty result for smallest if no palindrome in range
    ✕ empty result for largest if no palindrome in range
    ✕ error for smallest if min is more than max (52 ms)
    ✕ error for largest if min is more than max (10 ms)
    ○ skipped largest palindrome from four digit factors

  ● Palindromes › smallest palindrome from single digit factors

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:5:37)

  ● Palindromes › largest palindrome from single digit factors

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:14:37)

  ● Palindromes › smallest palindrome from double digit factors

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:29:37)

  ● Palindromes › largest palindrome from double digit factors

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:38:37)

  ● Palindromes › smallest palindrome from triple digit factors

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:47:37)

  ● Palindromes › largest palindrome from triple digit factors

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:59:37)

  ● Palindromes › smallest palindrome from four digit factors

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:71:37)

  ● Palindromes › empty result for smallest if no palindrome in range

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:101:37)

  ● Palindromes › empty result for largest if no palindrome in range

    No palindromes found in the range undefined to undefined

      26 |
      27 |     if (palindromes.size === 0) {
    > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
         |             ^
      29 |     }
      30 |
      31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at Object.generate (palindrome-products.spec.js:112:37)

  ● Palindromes › error for smallest if min is more than max

    expect(received).toThrow(expected)

    Expected message: "min must be <= max"
    Received message: "No palindromes found in the range undefined to undefined"

          26 |
          27 |     if (palindromes.size === 0) {
        > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
             |             ^
          29 |     }
          30 |
          31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at generate (palindrome-products.spec.js:121:39)
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (palindrome-products.spec.js:126:8)
      at Object.toThrow (palindrome-products.spec.js:126:8)

  ● Palindromes › error for largest if min is more than max

    expect(received).toThrow(expected)

    Expected message: "min must be <= max"
    Received message: "No palindromes found in the range undefined to undefined"

          26 |
          27 |     if (palindromes.size === 0) {
        > 28 |       throw new Error(`No palindromes found in the range ${min} to ${max}`);
             |             ^
          29 |     }
          30 |
          31 |     const products = Array.from(palindromes.keys()).sort((a, b) => a - b);

      at Function.generate (palindrome-products.js:28:13)
      at generate (palindrome-products.spec.js:131:39)
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (palindrome-products.spec.js:133:8)
      at Object.toThrow (palindrome-products.spec.js:133:8)

Test Suites: 1 failed, 1 total
Tests:       11 failed, 1 skipped, 12 total
Snapshots:   0 total
Time:        3.822 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/palindrome-products.js|.\/palindrome-products.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
