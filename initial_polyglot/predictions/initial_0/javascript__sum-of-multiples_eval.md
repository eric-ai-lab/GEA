+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' sum-of-multiples.spec.js
+ npm run test

> test
> jest ./*

FAIL ./sum-of-multiples.spec.js
  Sum Of Multiples
    ✕ no multiples within limit (3 ms)
    ✕ one factor has multiples within limit (8 ms)
    ✕ more than one multiple within limit
    ✕ more than one factor with multiples within limit
    ✕ each multiple is only counted once (1 ms)
    ✕ a much larger limit
    ✕ three factors
    ✕ factors not relatively prime
    ✕ some pairs of factors relatively prime and some not
    ✕ one factor is a multiple of another
    ✕ much larger factors
    ✕ all numbers are multiples of 1 (1 ms)
    ✕ no factors means an empty sum
    ✕ the only multiple of 0 is 0
    ✕ the factor 0 does not affect the sum of multiples of other factors
    ✕ solutions using include-exclude must extend to cardinality greater than 3 (1 ms)

  ● Sum Of Multiples › no multiples within limit

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:5:15)

  ● Sum Of Multiples › one factor has multiples within limit

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:9:15)

  ● Sum Of Multiples › more than one multiple within limit

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:13:15)

  ● Sum Of Multiples › more than one factor with multiples within limit

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:17:15)

  ● Sum Of Multiples › each multiple is only counted once

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:21:15)

  ● Sum Of Multiples › a much larger limit

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:25:15)

  ● Sum Of Multiples › three factors

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:29:15)

  ● Sum Of Multiples › factors not relatively prime

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:33:15)

  ● Sum Of Multiples › some pairs of factors relatively prime and some not

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:37:15)

  ● Sum Of Multiples › one factor is a multiple of another

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:41:15)

  ● Sum Of Multiples › much larger factors

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:45:15)

  ● Sum Of Multiples › all numbers are multiples of 1

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:49:15)

  ● Sum Of Multiples › no factors means an empty sum

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:53:15)

  ● Sum Of Multiples › the only multiple of 0 is 0

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:57:15)

  ● Sum Of Multiples › the factor 0 does not affect the sum of multiples of other factors

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:61:15)

  ● Sum Of Multiples › solutions using include-exclude must extend to cardinality greater than 3

    Invalid arguments: level must be a number and bases must be an array

      20 | export const sum = (level, bases) => {
      21 |   if (typeof level !== 'number' || !Array.isArray(bases)) {
    > 22 |     throw new Error('Invalid arguments: level must be a number and bases must be an array');
         |           ^
      23 |   }
      24 |
      25 |   const multiplesSet = new Set();

      at sum (sum-of-multiples.js:22:11)
      at Object.<anonymous> (sum-of-multiples.spec.js:65:15)

Test Suites: 1 failed, 1 total
Tests:       16 failed, 16 total
Snapshots:   0 total
Time:        3.52 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/sum-of-multiples.js|.\/sum-of-multiples.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
