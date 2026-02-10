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
      ✓ word beginning with a (4 ms)
      ✓ word beginning with e (1 ms)
      ✓ word beginning with i (1 ms)
      ✓ word beginning with o
      ✓ word beginning with u
      ✓ word beginning with a vowel and followed by a qu
    first letter and ay are moved to the end of words that start with consonants
      ✓ word beginning with p
      ✓ word beginning with k
      ✓ word beginning with x (1 ms)
      ✓ word beginning with q without a following u (1 ms)
    some letter clusters are treated like a single consonant
      ✓ word beginning with ch (1 ms)
      ✓ word beginning with qu (1 ms)
      ✓ word beginning with qu and a preceding consonant (1 ms)
      ✓ word beginning with th
      ✓ word beginning with thr (1 ms)
      ✓ word beginning with sch
    some letter clusters are treated like a single vowel
      ✓ word beginning with yt
      ✓ word beginning with xr
    position of y in a word determines if it is a consonant or a vowel
      ✓ y is treated like a consonant at the beginning of a word (1 ms)
      ✓ y is treated like a vowel at the end of a consonant cluster
      ✓ y as second letter in two letter word (1 ms)
    phrases are translated
      ✓ a whole phrase

Test Suites: 1 passed, 1 total
Tests:       22 passed, 22 total
Snapshots:   0 total
Time:        1.027 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./pig-latin.js|./pig-latin.spec.js.
