+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' binary.spec.js
+ npm run test

> test
> jest ./*

PASS ./binary.spec.js
  binary
    ✓ 0 is decimal 0 (3 ms)
    ✓ 1 is decimal 1
    ✓ 10 is decimal 2
    ✓ 11 is decimal 3 (1 ms)
    ✓ 100 is decimal 4 (1 ms)
    ✓ 1001 is decimal 9
    ✓ 11010 is decimal 26
    ✓ 10001101000 is decimal 1128 (1 ms)
    ✓ ignores leading zeros (1 ms)
    ✓ invalid inputs are null (2 ms)

Test Suites: 1 passed, 1 total
Tests:       10 passed, 10 total
Snapshots:   0 total
Time:        0.633 s
Ran all test suites matching ./LICENSE|./babel.config.js|./binary.js|./binary.spec.js|./eval.sh|./node_modules|./package-lock.json|./package.json.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.7.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
npm notice To update run: npm install -g npm@11.7.0
npm notice
