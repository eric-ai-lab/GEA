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
    ✓ age on Earth (3 ms)
    ✓ age on Mercury (1 ms)
    ✓ age on Venus (1 ms)
    ✓ age on Mars (1 ms)
    ✓ age on Jupiter
    ✓ age on Saturn
    ✓ age on Uranus (1 ms)
    ✓ age on Neptune (1 ms)

Test Suites: 1 passed, 1 total
Tests:       8 passed, 8 total
Snapshots:   0 total
Time:        0.638 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./space-age.js|./space-age.spec.js.
