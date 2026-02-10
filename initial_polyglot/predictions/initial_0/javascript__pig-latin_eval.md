+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' pig-latin.spec.js
+ npm run test

> test
> jest ./*

PASS ./pig-latin.spec.js
  Pig Latin
    ay is added to words that start with vowels
      ✓ word beginning with a (42 ms)
      ✓ word beginning with e
      ✓ word beginning with i (13 ms)
      ✓ word beginning with o (2 ms)
      ✓ word beginning with u (1 ms)
      ✓ word beginning with a vowel and followed by a qu
    first letter and ay are moved to the end of words that start with consonants
      ✓ word beginning with p (2 ms)
      ✓ word beginning with k (2 ms)
      ✓ word beginning with x
      ✓ word beginning with q without a following u (1 ms)
    some letter clusters are treated like a single consonant
      ✓ word beginning with ch
      ✓ word beginning with qu
      ✓ word beginning with qu and a preceding consonant (1 ms)
      ✓ word beginning with th (1 ms)
      ✓ word beginning with thr (1 ms)
      ✓ word beginning with sch
    some letter clusters are treated like a single vowel
      ✓ word beginning with yt
      ✓ word beginning with xr (1 ms)
    position of y in a word determines if it is a consonant or a vowel
      ✓ y is treated like a consonant at the beginning of a word
      ✓ y is treated like a vowel at the end of a consonant cluster
      ✓ y as second letter in two letter word
    phrases are translated
      ✓ a whole phrase

Test Suites: 1 passed, 1 total
Tests:       22 passed, 22 total
Snapshots:   0 total
Time:        3.446 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/pig-latin.js|.\/pig-latin.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
