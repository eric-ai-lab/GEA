+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' go-counting.spec.js
+ npm run test

> test
> jest ./*

PASS ./go-counting.spec.js
  Go Counting
    getTerritory
      ✓ Black corner territory on 5x5 board (3 ms)
      ✓ White center territory on 5x5 board (1 ms)
      ✓ Open corner territory on 5x5 board (1 ms)
      ✓ A stone and not a territory on 5x5 board
      ✓ Invalid because X is too low for 5x5 board
      ✓ Invalid because X is too high for 5x5 board
      ✓ Invalid because Y is too low for 5x5 board
      ✓ Invalid because Y is too high for 5x5 board
    getTerritories
      ✓ One territory is the whole board (1 ms)
      ✓ Two territory rectangular board (1 ms)
      ✓ Two region rectangular board (1 ms)

Test Suites: 1 passed, 1 total
Tests:       11 passed, 11 total
Snapshots:   0 total
Time:        0.385 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./go-counting.js|./go-counting.spec.js|./node_modules|./package-lock.json|./package.json.
