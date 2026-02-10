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
    ✓ data is retained (25 ms)
    ✓ left, right and value
    ✓ dead end
    ✓ tree from deep focus
    ✓ traversing up from top
    ✓ left, right and up (1 ms)
    ✓ setValue (1 ms)
    ✓ setValue after traversing up (1 ms)
    ✓ setLeft with leaf (1 ms)
    ✓ setRight with null (11 ms)
    ✓ setRight with subtree (1 ms)
    ✓ setValue on deep focus
    ✓ left returns a new Zipper
    ✓ right returns a new Zipper (1 ms)
    ✓ setValue returns a new Zipper
    ✓ setRight returns a new Zipper (1 ms)
    ✓ setLeft returns a new Zipper
    ✓ up returns a new Zipper (1 ms)
    ✓ should return same zipper from different paths

Test Suites: 1 passed, 1 total
Tests:       19 passed, 19 total
Snapshots:   0 total
Time:        2.896 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/zipper.js|.\/zipper.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
