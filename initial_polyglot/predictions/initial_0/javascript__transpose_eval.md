+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' transpose.spec.js
+ npm run test

> test
> jest ./*

FAIL ./transpose.spec.js (5.014 s)
  Transpose
    ✕ empty string (3 ms)
    ✕ two characters in a row (1 ms)
    ✕ two characters in a column (3 ms)
    ✕ simple (1 ms)
    ✕ single line
    ✕ first line longer than second line (1 ms)
    ✕ second line longer than first line (1 ms)
    ✕ mixed line length
    ✕ square
    ✕ rectangle
    ✕ triangle
    ✕ jagged triangle (1 ms)
    ✕ many lines (1 ms)

  ● Transpose › empty string

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:5:21)

  ● Transpose › two characters in a row

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:11:21)

  ● Transpose › two characters in a column

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:17:21)

  ● Transpose › simple

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:23:21)

  ● Transpose › single line

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:42:21)

  ● Transpose › first line longer than second line

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:65:21)

  ● Transpose › second line longer than first line

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:88:21)

  ● Transpose › mixed line length

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:117:21)

  ● Transpose › square

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:123:21)

  ● Transpose › rectangle

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:138:21)

  ● Transpose › triangle

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:151:21)

  ● Transpose › jagged triangle

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:164:21)

  ● Transpose › many lines

    TypeError: input.split is not a function

      19 | export const transpose = (input) => {
      20 |   // Split the input into rows
    > 21 |   const rows = input.split("\n");
         |                      ^
      22 |   
      23 |   // Find maximum row length
      24 |   const maxLen = rows.reduce((max, row) => Math.max(max, row.length), 0);

      at split (transpose.js:21:22)
      at Object.<anonymous> (transpose.spec.js:239:21)

Test Suites: 1 failed, 1 total
Tests:       13 failed, 13 total
Snapshots:   0 total
Time:        5.371 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/transpose.js|.\/transpose.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
