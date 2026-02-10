+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' zebra-puzzle.spec.js
+ npm run test

> test
> jest ./*

PASS ./zebra-puzzle.spec.js
  Zebra puzzle
    ✓ resident who drinks water (5 ms)
    ✓ resident who owns zebra (2 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   0 total
Time:        1.725 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./zebra-puzzle.js|./zebra-puzzle.spec.js.
