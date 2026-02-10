+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' sum-of-multiples.spec.js
+ npm run test

> test
> jest ./*

PASS ./sum-of-multiples.spec.js
  Sum Of Multiples
    ✓ no multiples within limit (3 ms)
    ✓ one factor has multiples within limit (1 ms)
    ✓ more than one multiple within limit
    ✓ more than one factor with multiples within limit
    ✓ each multiple is only counted once (1 ms)
    ✓ a much larger limit (1 ms)
    ✓ three factors (1 ms)
    ✓ factors not relatively prime
    ✓ some pairs of factors relatively prime and some not
    ✓ one factor is a multiple of another
    ✓ much larger factors
    ✓ all numbers are multiples of 1
    ✓ no factors means an empty sum (1 ms)
    ✓ the only multiple of 0 is 0 (1 ms)
    ✓ the factor 0 does not affect the sum of multiples of other factors
    ✓ solutions using include-exclude must extend to cardinality greater than 3 (2 ms)

Test Suites: 1 passed, 1 total
Tests:       16 passed, 16 total
Snapshots:   0 total
Time:        0.855 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./sum-of-multiples.js|./sum-of-multiples.spec.js.
