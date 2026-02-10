+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' killer-sudoku-helper.spec.js
+ npm run test

> test
> jest ./*

PASS ./killer-sudoku-helper.spec.js
  Trivial 1-digit cages
    ✓ 1 (3 ms)
    ✓ 2
    ✓ 3
    ✓ 4
    ✓ 5 (1 ms)
    ✓ 6 (1 ms)
    ✓ 7 (1 ms)
    ✓ 8 (1 ms)
    ✓ 9 (1 ms)
  Other cages
    ✓ Cage with sum 45 contains all digits 1:9 (1 ms)
    ✓ Cage with only 1 possible combination (1 ms)
    ✓ Cage with several combinations (1 ms)
    ✓ Cage with several combinations that is restricted

Test Suites: 1 passed, 1 total
Tests:       13 passed, 13 total
Snapshots:   0 total
Time:        0.715 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./killer-sudoku-helper.js|./killer-sudoku-helper.spec.js|./node_modules|./package-lock.json|./package.json.
