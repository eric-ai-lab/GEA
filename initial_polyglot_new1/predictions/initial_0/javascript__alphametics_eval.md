+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' alphametics.spec.js
+ npm run test

> test
> jest ./*

PASS ./alphametics.spec.js (5.965 s)
  Solve the alphametics puzzle
    ✓ puzzle with three letters (4 ms)
    ✓ solution must have unique value for each letter (1 ms)
    ✓ leading zero solution is invalid (7 ms)
    ✓ puzzle with four letters (6 ms)
    ✓ puzzle with six letters (118 ms)
    ✓ puzzle with seven letters (230 ms)
    ✓ puzzle with eight letters (1860 ms)
    ✓ puzzle with ten letters (1777 ms)
    ✓ puzzle with ten letters and 199 addends (1311 ms)

Test Suites: 1 passed, 1 total
Tests:       9 passed, 9 total
Snapshots:   0 total
Time:        6.079 s
Ran all test suites matching ./LICENSE|./alphametics.js|./alphametics.spec.js|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json.
