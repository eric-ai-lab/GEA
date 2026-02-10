+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' promises.spec.js
+ npm run test

> test
> jest ./*

PASS ./promises.spec.js
  promises
    promisify
      ✓ returns a function (3 ms)
      ✓ promisified function call returns a Promise
      ✓ promisified function resolves to a callback's success value (63 ms)
      ✓ promisified function rejects a callback's error (11 ms)
    all
      ✓ returns a Promise (1 ms)
      ✓ resolves when given no promises (1 ms)
      ✓ resolves when given no arguments
      ✓ resolved values appear in the order they are passed in (21 ms)
      ✓ rejects if any promises fail (11 ms)
    allSettled
      ✓ returns a Promise (1 ms)
      ✓ resolves when given no promises (1 ms)
      ✓ resolves when given no arguments
      ✓ resolved values appear in the order they are passed in (20 ms)
      ✓ resolves even if some promises fail (11 ms)
    race
      ✓ returns a Promise (1 ms)
      ✓ resolves when given no promises (1 ms)
      ✓ resolves when given no arguments (1 ms)
      ✓ resolves with value of the fastest successful promise (2 ms)
      ✓ resolves with value of the fastest promise even if other slower promises fail (2 ms)
      ✓ rejects if the fastest promise fails even if other slower promises succeed (10 ms)
    any
      ✓ returns a Promise (1 ms)
      ✓ resolves when given no promises (1 ms)
      ✓ resolves when given no arguments (1 ms)
      ✓ resolves with value of fastest successful promise (2 ms)
      ✓ resolves with value of the fastest successful promise even if slower promises fail (2 ms)
      ✓ resolves with value of fastest successful promise even if faster promises fail (20 ms)
      ✓ rejects with array of errors if all promises fail (11 ms)

Test Suites: 1 passed, 1 total
Tests:       27 passed, 27 total
Snapshots:   0 total
Time:        0.968 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./promises.js|./promises.spec.js.
