+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' food-chain.spec.js
+ npm run test

> test
> jest ./*

FAIL ./food-chain.spec.js
  Food Chain
    ✕ fly (38 ms)
    ✕ spider (1 ms)
    ✕ bird (2 ms)
    ✕ cat (28 ms)
    ✕ dog (3 ms)
    ✕ goat (2 ms)
    ✕ cow (1 ms)
    ✕ horse (1 ms)
    ✕ multiple verses (1 ms)
    ✕ the whole song (7 ms)

  ● Food Chain › fly

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 0

      I know an old lady who swallowed a fly.
      I don't know why she swallowed the fly. Perhaps she'll die.
    -

      13 | `;
      14 |
    > 15 |     expect(song.verse(1)).toEqual(expected);
         |                           ^
      16 |   });
      17 |
      18 |   test('spider', () => {

      at Object.toEqual (food-chain.spec.js:15:27)

  ● Food Chain › spider

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 0

      I know an old lady who swallowed a spider.
      It wriggled and jiggled and tickled inside her.
      She swallowed the spider to catch the fly.
      I don't know why she swallowed the fly. Perhaps she'll die.
    -

      23 | `;
      24 |
    > 25 |     expect(song.verse(2)).toEqual(expected);
         |                           ^
      26 |   });
      27 |
      28 |   test('bird', () => {

      at Object.toEqual (food-chain.spec.js:25:27)

  ● Food Chain › bird

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 0

      I know an old lady who swallowed a bird.
      How absurd to swallow a bird!
      She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
      She swallowed the spider to catch the fly.
      I don't know why she swallowed the fly. Perhaps she'll die.
    -

      34 | `;
      35 |
    > 36 |     expect(song.verse(3)).toEqual(expected);
         |                           ^
      37 |   });
      38 |
      39 |   test('cat', () => {

      at Object.toEqual (food-chain.spec.js:36:27)

  ● Food Chain › cat

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 0

    @@ -2,6 +2,5 @@
      Imagine that, to swallow a cat!
      She swallowed the cat to catch the bird.
      She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
      She swallowed the spider to catch the fly.
      I don't know why she swallowed the fly. Perhaps she'll die.
    -

      46 | `;
      47 |
    > 48 |     expect(song.verse(4)).toEqual(expected);
         |                           ^
      49 |   });
      50 |
      51 |   test('dog', () => {

      at Object.toEqual (food-chain.spec.js:48:27)

  ● Food Chain › dog

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 0

    @@ -3,6 +3,5 @@
      She swallowed the dog to catch the cat.
      She swallowed the cat to catch the bird.
      She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
      She swallowed the spider to catch the fly.
      I don't know why she swallowed the fly. Perhaps she'll die.
    -

      59 | `;
      60 |
    > 61 |     expect(song.verse(5)).toEqual(expected);
         |                           ^
      62 |   });
      63 |
      64 |   test('goat', () => {

      at Object.toEqual (food-chain.spec.js:61:27)

  ● Food Chain › goat

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 0

    @@ -4,6 +4,5 @@
      She swallowed the dog to catch the cat.
      She swallowed the cat to catch the bird.
      She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
      She swallowed the spider to catch the fly.
      I don't know why she swallowed the fly. Perhaps she'll die.
    -

      73 | `;
      74 |
    > 75 |     expect(song.verse(6)).toEqual(expected);
         |                           ^
      76 |   });
      77 |
      78 |   test('cow', () => {

      at Object.toEqual (food-chain.spec.js:75:27)

  ● Food Chain › cow

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 0

    @@ -5,6 +5,5 @@
      She swallowed the dog to catch the cat.
      She swallowed the cat to catch the bird.
      She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
      She swallowed the spider to catch the fly.
      I don't know why she swallowed the fly. Perhaps she'll die.
    -

      88 | `;
      89 |
    > 90 |     expect(song.verse(7)).toEqual(expected);
         |                           ^
      91 |   });
      92 |
      93 |   test('horse', () => {

      at Object.toEqual (food-chain.spec.js:90:27)

  ● Food Chain › horse

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 0

      I know an old lady who swallowed a horse.
      She's dead, of course!
    -

       96 | `;
       97 |
    >  98 |     expect(song.verse(8)).toEqual(expected);
          |                           ^
       99 |   });
      100 |
      101 |   test('multiple verses', () => {

      at Object.toEqual (food-chain.spec.js:98:27)

  ● Food Chain › multiple verses

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 0

    @@ -3,7 +3,5 @@

      I know an old lady who swallowed a spider.
      It wriggled and jiggled and tickled inside her.
      She swallowed the spider to catch the fly.
      I don't know why she swallowed the fly. Perhaps she'll die.
    -
    -

      110 | `;
      111 |
    > 112 |     expect(song.verses(1, 2)).toEqual(expected);
          |                               ^
      113 |   });
      114 |
      115 |   test('the whole song', () => {

      at Object.toEqual (food-chain.spec.js:112:31)

  ● Food Chain › the whole song

    expect(received).toEqual(expected) // deep equality

    - Expected  - 2
    + Received  + 0

    @@ -46,7 +46,5 @@
      She swallowed the spider to catch the fly.
      I don't know why she swallowed the fly. Perhaps she'll die.

      I know an old lady who swallowed a horse.
      She's dead, of course!
    -
    -

      167 | `;
      168 |
    > 169 |     expect(song.verses(1, 8)).toEqual(expected);
          |                               ^
      170 |   });
      171 | });
      172 |

      at Object.toEqual (food-chain.spec.js:169:31)

Test Suites: 1 failed, 1 total
Tests:       10 failed, 10 total
Snapshots:   0 total
Time:        4.721 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/food-chain.js|.\/food-chain.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
