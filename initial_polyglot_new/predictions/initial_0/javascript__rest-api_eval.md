+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' rest-api.spec.js
+ npm run test

> test
> jest ./*

PASS ./rest-api.spec.js
  Rest API
    user management
      ✓ no users (3 ms)
      ✓ add user (1 ms)
      ✓ get single user (1 ms)
    iou
      ✓ both users have 0 balance (1 ms)
      ✓ borrower has negative balance (1 ms)
      ✓ lender has negative balance (1 ms)
      ✓ lender owes borrower (1 ms)
      ✓ lender owes borrower less than new loan (1 ms)
      ✓ lender owes borrower same as new loan

Test Suites: 1 passed, 1 total
Tests:       9 passed, 9 total
Snapshots:   0 total
Time:        0.779 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./rest-api.js|./rest-api.spec.js.
