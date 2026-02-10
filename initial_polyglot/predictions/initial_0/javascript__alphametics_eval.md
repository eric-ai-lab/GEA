+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' alphametics.spec.js
+ npm run test

> test
> jest ./*

FAIL ./alphametics.spec.js (24.838 s)
  Solve the alphametics puzzle
    ✓ puzzle with three letters (14 ms)
    ✕ solution must have unique value for each letter (1 ms)
    ✕ leading zero solution is invalid (17 ms)
    ✓ puzzle with four letters (2 ms)
    ✓ puzzle with six letters (203 ms)
    ✓ puzzle with seven letters (498 ms)
    ✓ puzzle with eight letters (1689 ms)
    ✓ puzzle with ten letters (2177 ms)
    ✓ puzzle with ten letters and 199 addends (17458 ms)

  ● Solve the alphametics puzzle › solution must have unique value for each letter

    No solution

      83 |
      84 |   if (solution === null) {
    > 85 |     throw new Error('No solution');
         |           ^
      86 |   }
      87 |   
      88 |   return solution;

      at solve (alphametics.js:85:11)
      at Object.<anonymous> (alphametics.spec.js:16:17)

  ● Solve the alphametics puzzle › leading zero solution is invalid

    No solution

      83 |
      84 |   if (solution === null) {
    > 85 |     throw new Error('No solution');
         |           ^
      86 |   }
      87 |   
      88 |   return solution;

      at solve (alphametics.js:85:11)
      at Object.<anonymous> (alphametics.spec.js:21:17)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 7 passed, 9 total
Snapshots:   0 total
Time:        24.939 s
Ran all test suites matching /.\/LICENSE|.\/alphametics.js|.\/alphametics.spec.js|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
