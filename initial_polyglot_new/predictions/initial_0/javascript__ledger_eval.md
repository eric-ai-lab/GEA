+ set -e
+ '[' '!' -e node_modules ']'
+ '[' '!' -e package-lock.json ']'
+ sed -i 's/\bxtest(/test(/g' ledger.spec.js
+ npm run test

> test
> jest ./*

PASS ./ledger.spec.js
  Ledger
    ✓ empty ledger (2 ms)
    ✓ one entry (18 ms)
    ✓ credit and debit
    ✓ final order tie breaker is change (1 ms)
    ✓ overlong description is truncated
    ✓ euros
    ✓ Dutch locale
    ✓ Dutch locale and euros
    ✓ Dutch negative number with 3 digits before decimal point (1 ms)
    ✓ American negative number with 3 digits before decimal point
    ✓ multiple entries on same date ordered by description (1 ms)

Test Suites: 1 passed, 1 total
Tests:       11 passed, 11 total
Snapshots:   0 total
Time:        0.611 s, estimated 1 s
Ran all test suites matching /.\/LICENSE|.\/REFACTORING_LOG.md|.\/babel.config.js|.\/eval.sh|.\/ledger.js|.\/ledger.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
