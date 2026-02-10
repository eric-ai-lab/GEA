+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' space-age.spec.js
+ npm run test

> test
> jest ./*

PASS ./space-age.spec.js
  Space Age
    ✓ age on Earth (9 ms)
    ✓ age on Mercury (1 ms)
    ✓ age on Venus (1 ms)
    ✓ age on Mars
    ✓ age on Jupiter (1 ms)
    ✓ age on Saturn
    ✓ age on Uranus (1 ms)
    ✓ age on Neptune (2 ms)

Test Suites: 1 passed, 1 total
Tests:       8 passed, 8 total
Snapshots:   0 total
Time:        3.554 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/space-age.js|.\/space-age.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
