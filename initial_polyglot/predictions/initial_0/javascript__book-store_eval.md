+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' book-store.spec.js
+ npm run test

> test
> jest ./*

PASS ./book-store.spec.js
  Book Store
    Creating a basket
      ✓ only a single book (30 ms)
      ✓ two of the same book
      ✓ empty basket
      ✓ two different books (8 ms)
      ✓ three different books (1 ms)
      ✓ four different books (1 ms)
      ✓ five different books (5 ms)
      ✓ two groups of four is cheaper than group of five plus group of three (12 ms)
      ✓ two groups of four is cheaper than groups of five and three (3 ms)
      ✓ group of four plus group of two is cheaper than two groups of three (1 ms)
      ✓ two each of first 4 books and 1 copy each of rest (2 ms)
      ✓ two copies of each book (12 ms)
      ✓ three copies of first book and 2 each of remaining (2 ms)
      ✓ three each of first 2 books and 2 each of remaining books (36 ms)
      ✓ four groups of four are cheaper than two groups each of five and three (216 ms)
      ✓ two groups of four and a group of five (16 ms)
      ✓ shuffled book order (11 ms)

Test Suites: 1 passed, 1 total
Tests:       17 passed, 17 total
Snapshots:   0 total
Time:        4.612 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/book-store.js|.\/book-store.spec.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
