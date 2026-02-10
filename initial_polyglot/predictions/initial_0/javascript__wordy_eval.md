+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' wordy.spec.js
+ npm run test

> test
> jest ./*

FAIL ./wordy.spec.js
  Wordy
    ✓ just a number (6 ms)
    ✓ addition (1 ms)
    ✓ more addition
    ✓ addition with negative numbers
    ✓ large addition (1 ms)
    ✓ subtraction
    ✓ multiplication (1 ms)
    ✓ division (1 ms)
    ✓ multiple additions (1 ms)
    ✓ addition and subtraction
    ✓ multiple subtraction
    ✓ subtraction then addition (1 ms)
    ✓ multiple multiplication (1 ms)
    ✓ addition and multiplication (1 ms)
    ✓ multiple division (1 ms)
    ✕ unknown operation (78 ms)
    ✕ Non math question (4 ms)
    ✕ reject problem missing an operand (10 ms)
    ✕ reject problem with no operands or operators (7 ms)
    ✕ reject two operations in a row (2 ms)
    ✕ reject two numbers in a row (3 ms)
    ✕ reject postfix notation (3 ms)
    ✕ reject prefix notation (3 ms)

  ● Wordy › unknown operation

    expect(received).toThrow(expected)

    Expected message: "Unknown operation"
    Received message: "Unsupported operation"

          47 |       i += 2;
          48 |     } else {
        > 49 |       throw new Error('Unsupported operation');
             |             ^
          50 |     }
          51 |
          52 |     if (i >= tokens.length) {

      at answer (wordy.js:49:13)
      at wordy.spec.js:65:24
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (wordy.spec.js:65:47)
      at Object.toThrow (wordy.spec.js:65:47)

  ● Wordy › Non math question

    expect(received).toThrow(expected)

    Expected message: "Unknown operation"
    Received message: "Invalid question"

           5 | export const answer = (question) => {
           6 |   if (typeof question !== 'string' || !question.startsWith('What is') || !question.endsWith('?')) {
        >  7 |     throw new Error('Invalid question');
             |           ^
           8 |   }
           9 |
          10 |   // Remove the "What is" prefix and the trailing question mark

      at answer (wordy.js:7:11)
      at wordy.spec.js:71:24
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (wordy.spec.js:71:72)
      at Object.toThrow (wordy.spec.js:71:72)

  ● Wordy › reject problem missing an operand

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Syntax error in question"

          51 |
          52 |     if (i >= tokens.length) {
        > 53 |       throw new Error('Syntax error in question');
             |             ^
          54 |     }
          55 |     const number = parseInt(tokens[i], 10);
          56 |     if (isNaN(number)) {

      at answer (wordy.js:53:13)
      at wordy.spec.js:77:24
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (wordy.spec.js:77:45)
      at Object.toThrow (wordy.spec.js:77:45)

  ● Wordy › reject problem with no operands or operators

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Syntax error in question"

          11 |   const content = question.slice(8, -1).trim();
          12 |   if (content.length === 0) {
        > 13 |     throw new Error('Syntax error in question');
             |           ^
          14 |   }
          15 |
          16 |   // Split by space. Note: some operations have two words ("multiplied by", "divided by")

      at answer (wordy.js:13:11)
      at wordy.spec.js:81:24
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (wordy.spec.js:81:38)
      at Object.toThrow (wordy.spec.js:81:38)

  ● Wordy › reject two operations in a row

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Syntax error in question"

          55 |     const number = parseInt(tokens[i], 10);
          56 |     if (isNaN(number)) {
        > 57 |       throw new Error('Syntax error in question');
             |             ^
          58 |     }
          59 |     result = op(result, number);
          60 |     i++;

      at answer (wordy.js:57:13)
      at wordy.spec.js:85:24
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (wordy.spec.js:85:52)
      at Object.toThrow (wordy.spec.js:85:52)

  ● Wordy › reject two numbers in a row

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Unsupported operation"

          47 |       i += 2;
          48 |     } else {
        > 49 |       throw new Error('Unsupported operation');
             |             ^
          50 |     }
          51 |
          52 |     if (i >= tokens.length) {

      at answer (wordy.js:49:13)
      at wordy.spec.js:91:24
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (wordy.spec.js:91:49)
      at Object.toThrow (wordy.spec.js:91:49)

  ● Wordy › reject postfix notation

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Unsupported operation"

          47 |       i += 2;
          48 |     } else {
        > 49 |       throw new Error('Unsupported operation');
             |             ^
          50 |     }
          51 |
          52 |     if (i >= tokens.length) {

      at answer (wordy.js:49:13)
      at wordy.spec.js:97:24
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (wordy.spec.js:97:47)
      at Object.toThrow (wordy.spec.js:97:47)

  ● Wordy › reject prefix notation

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Syntax error in question"

          20 |   let result = parseInt(tokens[0], 10);
          21 |   if (isNaN(result)) {
        > 22 |     throw new Error('Syntax error in question');
             |           ^
          23 |   }
          24 |
          25 |   let i = 1;

      at answer (wordy.js:22:11)
      at wordy.spec.js:103:24
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (wordy.spec.js:103:47)
      at Object.toThrow (wordy.spec.js:103:47)

Test Suites: 1 failed, 1 total
Tests:       8 failed, 15 passed, 23 total
Snapshots:   0 total
Time:        3.017 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/wordy.js|.\/wordy.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
