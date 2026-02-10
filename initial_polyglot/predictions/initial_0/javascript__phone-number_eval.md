+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' phone-number.spec.js
+ npm run test

> test
> jest ./*

FAIL ./phone-number.spec.js
  Phone Number
    Cleanup user-entered phone numbers
      ✓ cleans the number (5 ms)
      ✓ cleans numbers with dots
      ✓ cleans numbers with multiple spaces (44 ms)
      ✕ invalid when 9 digits (75 ms)
      ✕ invalid when 11 digits does not start with a 1 (3 ms)
      ✓ valid when 11 digits and starting with 1 (1 ms)
      ✓ valid when 11 digits and starting with 1 even with punctuation (1 ms)
      ✕ invalid when more than 11 digits (2 ms)
      ✕ invalid with letters (2 ms)
      ✕ invalid with punctuations (2 ms)
      ✕ invalid if area code starts with 0 (2 ms)
      ✕ invalid if area code starts with 1 (2 ms)
      ✕ invalid if exchange code starts with 0 (3 ms)
      ✕ invalid if exchange code starts with 1 (2 ms)
      ✕ invalid if area code starts with 0 on valid 11-digit number (1 ms)
      ✕ invalid if area code starts with 1 on valid 11-digit number (2 ms)
      ✕ invalid if exchange code starts with 0 on valid 11-digit number (5 ms)
      ✕ invalid if exchange code starts with 1 on valid 11-digit number (1 ms)

  ● Phone Number › Cleanup user-entered phone numbers › invalid when 9 digits

    expect(received).toThrow(expected)

    Expected message: "Incorrect number of digits"
    Received message: "incorrect number"

          38 |   // Check for exactly 10 digits
          39 |   if (digits.length !== 10) {
        > 40 |     throw new Error('incorrect number');
             |           ^
          41 |   }
          42 |
          43 |   // The first digit of the area code (digits[0]) must be 2-9

      at clean (phone-number.js:40:11)
      at phone-number.spec.js:18:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:18:40)
      at Object.toThrow (phone-number.spec.js:18:40)

  ● Phone Number › Cleanup user-entered phone numbers › invalid when 11 digits does not start with a 1

    expect(received).toThrow(expected)

    Expected message: "11 digits must start with 1"
    Received message: "incorrect number"

          32 |       digits = digits.slice(1);
          33 |     } else {
        > 34 |       throw new Error('incorrect number');
             |             ^
          35 |     }
          36 |   }
          37 |

      at clean (phone-number.js:34:13)
      at phone-number.spec.js:24:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:24:42)
      at Object.toThrow (phone-number.spec.js:24:42)

  ● Phone Number › Cleanup user-entered phone numbers › invalid when more than 11 digits

    expect(received).toThrow(expected)

    Expected message: "More than 11 digits"
    Received message: "incorrect number"

          38 |   // Check for exactly 10 digits
          39 |   if (digits.length !== 10) {
        > 40 |     throw new Error('incorrect number');
             |           ^
          41 |   }
          42 |
          43 |   // The first digit of the area code (digits[0]) must be 2-9

      at clean (phone-number.js:40:11)
      at phone-number.spec.js:38:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:38:43)
      at Object.toThrow (phone-number.spec.js:38:43)

  ● Phone Number › Cleanup user-entered phone numbers › invalid with letters

    expect(received).toThrow(expected)

    Expected message: "Letters not permitted"
    Received message: "incorrect number"

          38 |   // Check for exactly 10 digits
          39 |   if (digits.length !== 10) {
        > 40 |     throw new Error('incorrect number');
             |           ^
          41 |   }
          42 |
          43 |   // The first digit of the area code (digits[0]) must be 2-9

      at clean (phone-number.js:40:11)
      at phone-number.spec.js:44:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:44:43)
      at Object.toThrow (phone-number.spec.js:44:43)

  ● Phone Number › Cleanup user-entered phone numbers › invalid with punctuations

    expect(received).toThrow(expected)

    Expected message: "Punctuations not permitted"
    Received message: "incorrect number"

          38 |   // Check for exactly 10 digits
          39 |   if (digits.length !== 10) {
        > 40 |     throw new Error('incorrect number');
             |           ^
          41 |   }
          42 |
          43 |   // The first digit of the area code (digits[0]) must be 2-9

      at clean (phone-number.js:40:11)
      at phone-number.spec.js:50:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:50:43)
      at Object.toThrow (phone-number.spec.js:50:43)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if area code starts with 0

    expect(received).toThrow(expected)

    Expected message: "Area code cannot start with zero"
    Received message: "incorrect number"

          43 |   // The first digit of the area code (digits[0]) must be 2-9
          44 |   if (!/^[2-9]/.test(digits)) {
        > 45 |     throw new Error('incorrect number');
             |           ^
          46 |   }
          47 |
          48 |   // The first digit of the exchange code (digits[3]) must be 2-9

      at clean (phone-number.js:45:11)
      at phone-number.spec.js:56:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:56:45)
      at Object.toThrow (phone-number.spec.js:56:45)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if area code starts with 1

    expect(received).toThrow(expected)

    Expected message: "Area code cannot start with one"
    Received message: "incorrect number"

          43 |   // The first digit of the area code (digits[0]) must be 2-9
          44 |   if (!/^[2-9]/.test(digits)) {
        > 45 |     throw new Error('incorrect number');
             |           ^
          46 |   }
          47 |
          48 |   // The first digit of the exchange code (digits[3]) must be 2-9

      at clean (phone-number.js:45:11)
      at phone-number.spec.js:62:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:62:45)
      at Object.toThrow (phone-number.spec.js:62:45)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if exchange code starts with 0

    expect(received).toThrow(expected)

    Expected message: "Exchange code cannot start with zero"
    Received message: "incorrect number"

          48 |   // The first digit of the exchange code (digits[3]) must be 2-9
          49 |   if (!/^[2-9]/.test(digits.slice(3, 4))) {
        > 50 |     throw new Error('incorrect number');
             |           ^
          51 |   }
          52 |
          53 |   return digits;

      at clean (phone-number.js:50:11)
      at phone-number.spec.js:68:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:68:45)
      at Object.toThrow (phone-number.spec.js:68:45)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if exchange code starts with 1

    expect(received).toThrow(expected)

    Expected message: "Exchange code cannot start with one"
    Received message: "incorrect number"

          48 |   // The first digit of the exchange code (digits[3]) must be 2-9
          49 |   if (!/^[2-9]/.test(digits.slice(3, 4))) {
        > 50 |     throw new Error('incorrect number');
             |           ^
          51 |   }
          52 |
          53 |   return digits;

      at clean (phone-number.js:50:11)
      at phone-number.spec.js:74:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:74:45)
      at Object.toThrow (phone-number.spec.js:74:45)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if area code starts with 0 on valid 11-digit number

    expect(received).toThrow(expected)

    Expected message: "Area code cannot start with zero"
    Received message: "incorrect number"

          43 |   // The first digit of the area code (digits[0]) must be 2-9
          44 |   if (!/^[2-9]/.test(digits)) {
        > 45 |     throw new Error('incorrect number');
             |           ^
          46 |   }
          47 |
          48 |   // The first digit of the exchange code (digits[3]) must be 2-9

      at clean (phone-number.js:45:11)
      at phone-number.spec.js:80:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:80:47)
      at Object.toThrow (phone-number.spec.js:80:47)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if area code starts with 1 on valid 11-digit number

    expect(received).toThrow(expected)

    Expected message: "Area code cannot start with one"
    Received message: "incorrect number"

          43 |   // The first digit of the area code (digits[0]) must be 2-9
          44 |   if (!/^[2-9]/.test(digits)) {
        > 45 |     throw new Error('incorrect number');
             |           ^
          46 |   }
          47 |
          48 |   // The first digit of the exchange code (digits[3]) must be 2-9

      at clean (phone-number.js:45:11)
      at phone-number.spec.js:86:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:86:47)
      at Object.toThrow (phone-number.spec.js:86:47)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if exchange code starts with 0 on valid 11-digit number

    expect(received).toThrow(expected)

    Expected message: "Exchange code cannot start with zero"
    Received message: "incorrect number"

          48 |   // The first digit of the exchange code (digits[3]) must be 2-9
          49 |   if (!/^[2-9]/.test(digits.slice(3, 4))) {
        > 50 |     throw new Error('incorrect number');
             |           ^
          51 |   }
          52 |
          53 |   return digits;

      at clean (phone-number.js:50:11)
      at phone-number.spec.js:92:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:92:47)
      at Object.toThrow (phone-number.spec.js:92:47)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if exchange code starts with 1 on valid 11-digit number

    expect(received).toThrow(expected)

    Expected message: "Exchange code cannot start with one"
    Received message: "incorrect number"

          48 |   // The first digit of the exchange code (digits[3]) must be 2-9
          49 |   if (!/^[2-9]/.test(digits.slice(3, 4))) {
        > 50 |     throw new Error('incorrect number');
             |           ^
          51 |   }
          52 |
          53 |   return digits;

      at clean (phone-number.js:50:11)
      at phone-number.spec.js:98:25
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (phone-number.spec.js:98:47)
      at Object.toThrow (phone-number.spec.js:98:47)

Test Suites: 1 failed, 1 total
Tests:       13 failed, 5 passed, 18 total
Snapshots:   0 total
Time:        2.796 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/phone-number.js|.\/phone-number.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
