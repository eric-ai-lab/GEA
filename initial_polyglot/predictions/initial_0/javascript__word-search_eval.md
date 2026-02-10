+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' word-search.spec.js
+ npm run test

> test
> jest ./*

FAIL ./word-search.spec.js
  single line grids
    ✓ Should accept an initial game grid (8 ms)
    ✕ can accept a target search word (1 ms)
    ✕ should locate a word written left to right (1 ms)
    ✕ can locate a left to right word in a different position
    ✕ can locate a different left to right word
    ✕ can locate that different left to right word in a different position (2 ms)
  multi line grids
    ✕ can locate a left to right word in a two line grid
    ✕ can locate a left to right word in a different position in a two line grid
    ✕ can locate a left to right word in a three line grid
    ✕ can locate a left to right word in a ten line grid (1 ms)
    ✕ can locate a left to right word in a different position in a ten line grid (1 ms)
    ✕ can locate a different left to right word in a ten line grid (1 ms)
  can find multiple words
    ✕ can find two words written left to right (1 ms)
  different directions
    ✕ should locate a single word written right to left (1 ms)
    ✕ should locate multiple words written in different horizontal directions
  vertical directions
    ✕ should locate words written top to bottom
    ✕ should locate words written bottom to top (1 ms)
    ✕ should locate words written top left to bottom right
    ✕ should locate words written bottom right to top left
    ✕ should locate words written bottom left to top right (1 ms)
    ✕ should locate words written top right to bottom left (4 ms)
    word doesn't exist
      ✕ should fail to locate a word that is not in the puzzle

  ● single line grids › can accept a target search word

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:15:23)

  ● single line grids › should locate a word written left to right

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:28:23)

  ● single line grids › can locate a left to right word in a different position

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:41:23)

  ● single line grids › can locate a different left to right word

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:54:23)

  ● single line grids › can locate that different left to right word in a different position

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:66:23)

  ● multi line grids › can locate a left to right word in a two line grid

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:83:23)

  ● multi line grids › can locate a left to right word in a different position in a two line grid

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:95:23)

  ● multi line grids › can locate a left to right word in a three line grid

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:107:23)

  ● multi line grids › can locate a left to right word in a ten line grid

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:132:23)

  ● multi line grids › can locate a left to right word in a different position in a ten line grid

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:157:23)

  ● multi line grids › can locate a different left to right word in a ten line grid

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:180:23)

  ● can find multiple words › can find two words written left to right

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:211:23)

  ● different directions › should locate a single word written right to left

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:226:23)

  ● different directions › should locate multiple words written in different horizontal directions

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:253:23)

  ● vertical directions › should locate words written top to bottom

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:287:23)

  ● vertical directions › should locate words written bottom to top

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:325:18)

  ● vertical directions › should locate words written top left to bottom right

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:366:18)

  ● vertical directions › should locate words written bottom right to top left

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:412:18)

  ● vertical directions › should locate words written bottom left to top right

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:469:18)

  ● vertical directions › should locate words written top right to bottom left

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:531:18)

  ● vertical directions › word doesn't exist › should fail to locate a word that is not in the puzzle

    Word must be a non-empty string

      17 |   find(word) {
      18 |     if (typeof word !== 'string' || word.length === 0) {
    > 19 |       throw new Error('Word must be a non-empty string');
         |             ^
      20 |     }
      21 |
      22 |     const directions = [

      at WordSearch.find (word-search.js:19:13)
      at Object.find (word-search.spec.js:564:25)

Test Suites: 1 failed, 1 total
Tests:       21 failed, 1 passed, 22 total
Snapshots:   0 total
Time:        3.001 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/word-search.js|.\/word-search.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
