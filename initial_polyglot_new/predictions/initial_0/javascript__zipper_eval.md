+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' zipper.spec.js
+ npm run test

> test
> jest ./*

PASS ./zipper.spec.js
  Zipper
    ✓ data is retained (3 ms)
    ✓ left, right and value (1 ms)
    ✓ dead end (1 ms)
    ✓ tree from deep focus (1 ms)
    ✓ traversing up from top (1 ms)
    ✓ left, right and up (1 ms)
    ✓ setValue (2 ms)
    ✓ setValue after traversing up (1 ms)
    ✓ setLeft with leaf (1 ms)
    ✓ setRight with null
    ✓ setRight with subtree (1 ms)
    ✓ setValue on deep focus (1 ms)
    ✓ left returns a new Zipper (1 ms)
    ✓ right returns a new Zipper
    ✓ setValue returns a new Zipper
    ✓ setRight returns a new Zipper (1 ms)
    ✓ setLeft returns a new Zipper
    ✓ up returns a new Zipper (1 ms)
    ✓ should return same zipper from different paths (1 ms)

Test Suites: 1 passed, 1 total
Tests:       19 passed, 19 total
Snapshots:   0 total
Time:        0.831 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./zipper.js|./zipper.spec.js.
