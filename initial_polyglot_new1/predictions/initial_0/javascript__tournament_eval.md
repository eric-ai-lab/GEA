+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' tournament.spec.js
+ npm run test

> test
> jest ./*

PASS ./tournament.spec.js
  Tournament
    ✓ just the header if no input (3 ms)
    ✓ a win is three points, a loss is zero points (1 ms)
    ✓ a win can also be expressed as a loss (1 ms)
    ✓ a different team can win
    ✓ a draw is one point each (10 ms)
    ✓ there can be more than one match (1 ms)
    ✓ there can be more than one winner
    ✓ there can be more than two teams
    ✓ typical input
    ✓ incomplete competition (not all pairs have played)
    ✓ ties broken alphabetically
    ✓ ensure points sorted numerically

Test Suites: 1 passed, 1 total
Tests:       12 passed, 12 total
Snapshots:   0 total
Time:        0.738 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./tournament.js|./tournament.spec.js.
