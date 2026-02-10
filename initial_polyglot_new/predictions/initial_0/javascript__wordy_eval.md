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
    ✓ just a number (4 ms)
    ✓ addition (1 ms)
    ✓ more addition (1 ms)
    ✓ addition with negative numbers (1 ms)
    ✓ large addition
    ✓ subtraction
    ✓ multiplication (1 ms)
    ✓ division (1 ms)
    ✓ multiple additions (1 ms)
    ✓ addition and subtraction (1 ms)
    ✓ multiple subtraction (1 ms)
    ✓ subtraction then addition (1 ms)
    ✓ multiple multiplication (1 ms)
    ✓ addition and multiplication (1 ms)
    ✓ multiple division (1 ms)
    ✓ unknown operation (11 ms)
    ✓ Non math question (1 ms)
    ✓ reject problem missing an operand (1 ms)
    ✕ reject problem with no operands or operators (13 ms)
    ✓ reject two operations in a row
    ✕ reject two numbers in a row (2 ms)
    ✕ reject postfix notation (2 ms)
    ✓ reject prefix notation (1 ms)

  ● Wordy › reject problem with no operands or operators

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Unknown operation"

           7 |   // Check if the question is asking "What is"
           8 |   if (!question.startsWith('What is ')) {
        >  9 |     throw new Error('Unknown operation');
             |           ^
          10 |   }
          11 |
          12 |   // Extract the math expression

      at answer (wordy.js:9:11)
      at wordy.spec.js:81:24
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (wordy.spec.js:81:38)
      at Object.toThrow (wordy.spec.js:81:38)

  ● Wordy › reject two numbers in a row

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Unknown operation"

          42 |       const operator = tokens[i];
          43 |       if (!isValidOperator(operator)) {
        > 44 |         throw new Error('Unknown operation');
             |               ^
          45 |       }
          46 |       throw new Error('Syntax error');
          47 |     }

      at parseMathExpression (wordy.js:44:15)
      at parseMathExpression (wordy.js:23:10)
      at wordy.spec.js:91:24
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (wordy.spec.js:91:49)
      at Object.toThrow (wordy.spec.js:91:49)

  ● Wordy › reject postfix notation

    expect(received).toThrow(expected)

    Expected message: "Syntax error"
    Received message: "Unknown operation"

          80 |     } else {
          81 |       // Unknown operator
        > 82 |       throw new Error('Unknown operation');
             |             ^
          83 |     }
          84 |     
          85 |     i = nextIndex + 1;

      at parseMathExpression (wordy.js:82:13)
      at parseMathExpression (wordy.js:23:10)
      at wordy.spec.js:97:24
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (wordy.spec.js:97:47)
      at Object.toThrow (wordy.spec.js:97:47)

Test Suites: 1 failed, 1 total
Tests:       3 failed, 20 passed, 23 total
Snapshots:   0 total
Time:        0.74 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./wordy.js|./wordy.spec.js.
