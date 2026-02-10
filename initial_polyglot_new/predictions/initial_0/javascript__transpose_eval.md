+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' transpose.spec.js
+ npm run test

> test
> jest ./*

PASS ./transpose.spec.js
  Transpose
    ✓ empty string (3 ms)
    ✓ two characters in a row
    ✓ two characters in a column
    ✓ simple
    ✓ single line (1 ms)
    ✓ first line longer than second line
    ✓ second line longer than first line (1 ms)
    ✓ mixed line length (1 ms)
    ✓ square (1 ms)
    ✓ rectangle (1 ms)
    ✓ triangle (1 ms)
    ✓ jagged triangle (1 ms)
    ✓ many lines (1 ms)

Test Suites: 1 passed, 1 total
Tests:       13 passed, 13 total
Snapshots:   0 total
Time:        0.723 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./transpose.js|./transpose.spec.js.
