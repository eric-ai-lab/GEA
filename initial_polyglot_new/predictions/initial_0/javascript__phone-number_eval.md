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
      ✓ cleans the number (3 ms)
      ✓ cleans numbers with dots
      ✓ cleans numbers with multiple spaces
      ✕ invalid when 9 digits (20 ms)
      ✕ invalid when 11 digits does not start with a 1 (2 ms)
      ✓ valid when 11 digits and starting with 1
      ✓ valid when 11 digits and starting with 1 even with punctuation
      ✕ invalid when more than 11 digits (2 ms)
      ✕ invalid with letters (2 ms)
      ✕ invalid with punctuations (2 ms)
      ✕ invalid if area code starts with 0 (1 ms)
      ✕ invalid if area code starts with 1 (1 ms)
      ✕ invalid if exchange code starts with 0 (1 ms)
      ✕ invalid if exchange code starts with 1 (1 ms)
      ✕ invalid if area code starts with 0 on valid 11-digit number
      ✕ invalid if area code starts with 1 on valid 11-digit number
      ✕ invalid if exchange code starts with 0 on valid 11-digit number
      ✕ invalid if exchange code starts with 1 on valid 11-digit number

  ● Phone Number › Cleanup user-entered phone numbers › invalid when 9 digits

    expect(received).toThrow(expected)

    Expected message: "Incorrect number of digits"
    Received message: "Invalid phone number"

          16 |   // Validate that we have exactly 10 digits
          17 |   if (cleaned.length !== 10) {
        > 18 |     throw new Error('Invalid phone number');
             |           ^
          19 |   }
          20 |   
          21 |   return cleaned;

      at clean (phone-number.js:18:11)
      at phone-number.spec.js:18:25
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (phone-number.spec.js:18:40)
      at Object.toThrow (phone-number.spec.js:18:40)

  ● Phone Number › Cleanup user-entered phone numbers › invalid when 11 digits does not start with a 1

    expect(received).toThrow(expected)

    Expected message: "11 digits must start with 1"
    Received message: "Invalid phone number"

          16 |   // Validate that we have exactly 10 digits
          17 |   if (cleaned.length !== 10) {
        > 18 |     throw new Error('Invalid phone number');
             |           ^
          19 |   }
          20 |   
          21 |   return cleaned;

      at clean (phone-number.js:18:11)
      at phone-number.spec.js:24:25
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (phone-number.spec.js:24:42)
      at Object.toThrow (phone-number.spec.js:24:42)

  ● Phone Number › Cleanup user-entered phone numbers › invalid when more than 11 digits

    expect(received).toThrow(expected)

    Expected message: "More than 11 digits"
    Received message: "Invalid phone number"

          16 |   // Validate that we have exactly 10 digits
          17 |   if (cleaned.length !== 10) {
        > 18 |     throw new Error('Invalid phone number');
             |           ^
          19 |   }
          20 |   
          21 |   return cleaned;

      at clean (phone-number.js:18:11)
      at phone-number.spec.js:38:25
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (phone-number.spec.js:38:43)
      at Object.toThrow (phone-number.spec.js:38:43)

  ● Phone Number › Cleanup user-entered phone numbers › invalid with letters

    expect(received).toThrow(expected)

    Expected message: "Letters not permitted"
    Received message: "Invalid phone number"

          16 |   // Validate that we have exactly 10 digits
          17 |   if (cleaned.length !== 10) {
        > 18 |     throw new Error('Invalid phone number');
             |           ^
          19 |   }
          20 |   
          21 |   return cleaned;

      at clean (phone-number.js:18:11)
      at phone-number.spec.js:44:25
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (phone-number.spec.js:44:43)
      at Object.toThrow (phone-number.spec.js:44:43)

  ● Phone Number › Cleanup user-entered phone numbers › invalid with punctuations

    expect(received).toThrow(expected)

    Expected message: "Punctuations not permitted"
    Received message: "Invalid phone number"

          16 |   // Validate that we have exactly 10 digits
          17 |   if (cleaned.length !== 10) {
        > 18 |     throw new Error('Invalid phone number');
             |           ^
          19 |   }
          20 |   
          21 |   return cleaned;

      at clean (phone-number.js:18:11)
      at phone-number.spec.js:50:25
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (phone-number.spec.js:50:43)
      at Object.toThrow (phone-number.spec.js:50:43)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if area code starts with 0

    expect(received).toThrow(expected)

    Expected message: "Area code cannot start with zero"

    Received function did not throw

      54 |
      55 |     test('invalid if area code starts with 0', () => {
    > 56 |       expect(() => clean('(023) 456-7890')).toThrow(
         |                                             ^
      57 |         new Error('Area code cannot start with zero'),
      58 |       );
      59 |     });

      at Object.toThrow (phone-number.spec.js:56:45)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if area code starts with 1

    expect(received).toThrow(expected)

    Expected message: "Area code cannot start with one"

    Received function did not throw

      60 |
      61 |     test('invalid if area code starts with 1', () => {
    > 62 |       expect(() => clean('(123) 456-7890')).toThrow(
         |                                             ^
      63 |         new Error('Area code cannot start with one'),
      64 |       );
      65 |     });

      at Object.toThrow (phone-number.spec.js:62:45)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if exchange code starts with 0

    expect(received).toThrow(expected)

    Expected message: "Exchange code cannot start with zero"

    Received function did not throw

      66 |
      67 |     test('invalid if exchange code starts with 0', () => {
    > 68 |       expect(() => clean('(223) 056-7890')).toThrow(
         |                                             ^
      69 |         new Error('Exchange code cannot start with zero'),
      70 |       );
      71 |     });

      at Object.toThrow (phone-number.spec.js:68:45)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if exchange code starts with 1

    expect(received).toThrow(expected)

    Expected message: "Exchange code cannot start with one"

    Received function did not throw

      72 |
      73 |     test('invalid if exchange code starts with 1', () => {
    > 74 |       expect(() => clean('(223) 156-7890')).toThrow(
         |                                             ^
      75 |         new Error('Exchange code cannot start with one'),
      76 |       );
      77 |     });

      at Object.toThrow (phone-number.spec.js:74:45)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if area code starts with 0 on valid 11-digit number

    expect(received).toThrow(expected)

    Expected message: "Area code cannot start with zero"

    Received function did not throw

      78 |
      79 |     test('invalid if area code starts with 0 on valid 11-digit number', () => {
    > 80 |       expect(() => clean('1 (023) 456-7890')).toThrow(
         |                                               ^
      81 |         new Error('Area code cannot start with zero'),
      82 |       );
      83 |     });

      at Object.toThrow (phone-number.spec.js:80:47)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if area code starts with 1 on valid 11-digit number

    expect(received).toThrow(expected)

    Expected message: "Area code cannot start with one"

    Received function did not throw

      84 |
      85 |     test('invalid if area code starts with 1 on valid 11-digit number', () => {
    > 86 |       expect(() => clean('1 (123) 456-7890')).toThrow(
         |                                               ^
      87 |         new Error('Area code cannot start with one'),
      88 |       );
      89 |     });

      at Object.toThrow (phone-number.spec.js:86:47)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if exchange code starts with 0 on valid 11-digit number

    expect(received).toThrow(expected)

    Expected message: "Exchange code cannot start with zero"

    Received function did not throw

      90 |
      91 |     test('invalid if exchange code starts with 0 on valid 11-digit number', () => {
    > 92 |       expect(() => clean('1 (223) 056-7890')).toThrow(
         |                                               ^
      93 |         new Error('Exchange code cannot start with zero'),
      94 |       );
      95 |     });

      at Object.toThrow (phone-number.spec.js:92:47)

  ● Phone Number › Cleanup user-entered phone numbers › invalid if exchange code starts with 1 on valid 11-digit number

    expect(received).toThrow(expected)

    Expected message: "Exchange code cannot start with one"

    Received function did not throw

       96 |
       97 |     test('invalid if exchange code starts with 1 on valid 11-digit number', () => {
    >  98 |       expect(() => clean('1 (223) 156-7890')).toThrow(
          |                                               ^
       99 |         new Error('Exchange code cannot start with one'),
      100 |       );
      101 |     });

      at Object.toThrow (phone-number.spec.js:98:47)

Test Suites: 1 failed, 1 total
Tests:       13 failed, 5 passed, 18 total
Snapshots:   0 total
Time:        0.773 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./phone-number.js|./phone-number.spec.js.
