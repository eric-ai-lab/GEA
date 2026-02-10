+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' rectangles.spec.js
+ npm run test

> test
> jest ./*

FAIL ./rectangles.spec.js
  Rectangles
    ✕ no rows (4 ms)
    ✕ no columns
    ✕ no rectangles
    ✕ one rectangle
    ✕ two rectangles without shared parts (1 ms)
    ✕ five rectangles with shared parts
    ✕ rectangle of height 1 is counted (1 ms)
    ✕ rectangle of width 1 is counted (1 ms)
    ✕ 1x1 square is counted
    ✕ only complete rectangles are counted (6 ms)
    ✕ rectangles can be of different sizes
    ✕ corner is required for a rectangle to be complete
    ✕ large input with many rectangles
    ✕ rectangles must have four sides (1 ms)

  ● Rectangles › no rows

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:6:25)

  ● Rectangles › no columns

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:13:25)

  ● Rectangles › no rectangles

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:20:25)

  ● Rectangles › one rectangle

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:27:25)

  ● Rectangles › two rectangles without shared parts

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:34:25)

  ● Rectangles › five rectangles with shared parts

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:41:25)

  ● Rectangles › rectangle of height 1 is counted

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:48:25)

  ● Rectangles › rectangle of width 1 is counted

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:55:25)

  ● Rectangles › 1x1 square is counted

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:62:25)

  ● Rectangles › only complete rectangles are counted

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:69:25)

  ● Rectangles › rectangles can be of different sizes

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:76:25)

  ● Rectangles › corner is required for a rectangle to be complete

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:89:25)

  ● Rectangles › large input with many rectangles

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:102:25)

  ● Rectangles › rectangles must have four sides

    TypeError: diagram.split is not a function

       9 | export function count(diagram) {
      10 |   // Split the diagram into rows
    > 11 |   const rows = diagram.split('\n');
         |                        ^
      12 |   const height = rows.length;
      13 |   if (height === 0) return 0;
      14 |   const width = rows[0].length;

      at split (rectangles.js:11:24)
      at Object.<anonymous> (rectangles.spec.js:118:25)

Test Suites: 1 failed, 1 total
Tests:       14 failed, 14 total
Snapshots:   0 total
Time:        2.257 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/rectangles.js|.\/rectangles.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
