+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' bottle-song.spec.js
+ npm run test

> test
> jest ./*

PASS ./bottle-song.spec.js
  Bottle Song
    verse
      single verse
        ✓ first generic verse (3 ms)
        ✓ last generic verse (1 ms)
        ✓ verse with 2 bottles (1 ms)
        ✓ verse with 1 bottle
    lyrics
      multiple verses
        ✓ first two verses (1 ms)
        ✓ last three verses
        ✓ all verses (1 ms)

Test Suites: 1 passed, 1 total
Tests:       7 passed, 7 total
Snapshots:   0 total
Time:        0.661 s
Ran all test suites matching ./LICENSE|./babel.config.js|./bottle-song.js|./bottle-song.spec.js|./eval.sh|./node_modules|./package-lock.json|./package.json.
