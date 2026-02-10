+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' beer-song.spec.js
+ npm run test

> test
> jest ./*

PASS ./beer-song.spec.js
  Beer Song
    verse
      single verse
        ✓ first generic verse (3 ms)
        ✓ last generic verse (1 ms)
        ✓ verse with 2 bottles (1 ms)
        ✓ verse with 1 bottle (1 ms)
        ✓ verse with 0 bottles (2 ms)
    lyrics
      multiple verses
        ✓ first two verses (1 ms)
        ✓ last three verses (1 ms)
        ✓ all verses (10 ms)

Test Suites: 1 passed, 1 total
Tests:       8 passed, 8 total
Snapshots:   0 total
Time:        0.695 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./beer-song.js|./beer-song.spec.js|./eval.sh|./node_modules|./package-lock.json|./package.json.
