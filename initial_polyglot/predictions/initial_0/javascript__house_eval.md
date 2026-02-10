+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' house.spec.js
+ npm run test

> test
> jest ./*

FAIL ./house.spec.js
  House
    ✕ verse one - the house that jack built (29 ms)
    ✕ verse two - the malt that lay (1 ms)
    ✕ verse three - the rat that ate (1 ms)
    ✕ verse four - the cat that killed
    ✕ verse five - the dog that worried (1 ms)
    ✕ verse six - the cow with the crumpled horn (1 ms)
    ✕ verse seven - the maiden all forlorn (11 ms)
    ✕ verse eight - the man all tattered and torn (1 ms)
    ✕ verse nine - the priest all shaven and shorn (1 ms)
    ✕ verse ten - the rooster that crowed in the morn (1 ms)
    ✕ verse eleven - the farmer sowing his corn (1 ms)
    ✕ verse twelve - the horse and the hound and the horn
    ✕ multiple verses
    ✕ full rhyme (1 ms)

  ● House › verse one - the house that jack built

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the house that Jack built."]
    Received: "This is house that Jack built."

      4 |   test('verse one - the house that jack built', () => {
      5 |     const lyrics = ['This is the house that Jack built.'];
    > 6 |     expect(House.verse(1)).toEqual(lyrics);
        |                            ^
      7 |   });
      8 |
      9 |   test('verse two - the malt that lay', () => {

      at Object.toEqual (house.spec.js:6:28)

  ● House › verse two - the malt that lay

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the malt", "that lay in the house that Jack built."]
    Received: "This is malt
    that lay in house that Jack built."

      12 |       'that lay in the house that Jack built.',
      13 |     ];
    > 14 |     expect(House.verse(2)).toEqual(lyrics);
         |                            ^
      15 |   });
      16 |
      17 |   test('verse three - the rat that ate', () => {

      at Object.toEqual (house.spec.js:14:28)

  ● House › verse three - the rat that ate

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the rat", "that ate the malt", "that lay in the house that Jack built."]
    Received: "This is rat
    that ate malt
    that lay in house that Jack built."

      21 |       'that lay in the house that Jack built.',
      22 |     ];
    > 23 |     expect(House.verse(3)).toEqual(lyrics);
         |                            ^
      24 |   });
      25 |
      26 |   test('verse four - the cat that killed', () => {

      at Object.toEqual (house.spec.js:23:28)

  ● House › verse four - the cat that killed

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built."]
    Received: "This is cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      31 |       'that lay in the house that Jack built.',
      32 |     ];
    > 33 |     expect(House.verse(4)).toEqual(lyrics);
         |                            ^
      34 |   });
      35 |
      36 |   test('verse five - the dog that worried', () => {

      at Object.toEqual (house.spec.js:33:28)

  ● House › verse five - the dog that worried

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the dog", "that worried the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built."]
    Received: "This is dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      42 |       'that lay in the house that Jack built.',
      43 |     ];
    > 44 |     expect(House.verse(5)).toEqual(lyrics);
         |                            ^
      45 |   });
      46 |
      47 |   test('verse six - the cow with the crumpled horn', () => {

      at Object.toEqual (house.spec.js:44:28)

  ● House › verse six - the cow with the crumpled horn

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the cow with the crumpled horn", "that tossed the dog", "that worried the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built."]
    Received: "This is cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      54 |       'that lay in the house that Jack built.',
      55 |     ];
    > 56 |     expect(House.verse(6)).toEqual(lyrics);
         |                            ^
      57 |   });
      58 |
      59 |   test('verse seven - the maiden all forlorn', () => {

      at Object.toEqual (house.spec.js:56:28)

  ● House › verse seven - the maiden all forlorn

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the maiden all forlorn", "that milked the cow with the crumpled horn", "that tossed the dog", "that worried the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built."]
    Received: "This is maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      67 |       'that lay in the house that Jack built.',
      68 |     ];
    > 69 |     expect(House.verse(7)).toEqual(lyrics);
         |                            ^
      70 |   });
      71 |
      72 |   test('verse eight - the man all tattered and torn', () => {

      at Object.toEqual (house.spec.js:69:28)

  ● House › verse eight - the man all tattered and torn

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the man all tattered and torn", "that kissed the maiden all forlorn", "that milked the cow with the crumpled horn", "that tossed the dog", "that worried the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built."]
    Received: "This is man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      81 |       'that lay in the house that Jack built.',
      82 |     ];
    > 83 |     expect(House.verse(8)).toEqual(lyrics);
         |                            ^
      84 |   });
      85 |
      86 |   test('verse nine - the priest all shaven and shorn', () => {

      at Object.toEqual (house.spec.js:83:28)

  ● House › verse nine - the priest all shaven and shorn

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the priest all shaven and shorn", "that married the man all tattered and torn", "that kissed the maiden all forlorn", "that milked the cow with the crumpled horn", "that tossed the dog", "that worried the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built."]
    Received: "This is priest all shaven and shorn
    that married man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

       96 |       'that lay in the house that Jack built.',
       97 |     ];
    >  98 |     expect(House.verse(9)).toEqual(lyrics);
          |                            ^
       99 |   });
      100 |
      101 |   test('verse ten - the rooster that crowed in the morn', () => {

      at Object.toEqual (house.spec.js:98:28)

  ● House › verse ten - the rooster that crowed in the morn

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the rooster that crowed in the morn", "that woke the priest all shaven and shorn", "that married the man all tattered and torn", "that kissed the maiden all forlorn", "that milked the cow with the crumpled horn", "that tossed the dog", "that worried the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built."]
    Received: "This is rooster that crowed in the morn
    that woke priest all shaven and shorn
    that married man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      112 |       'that lay in the house that Jack built.',
      113 |     ];
    > 114 |     expect(House.verse(10)).toEqual(lyrics);
          |                             ^
      115 |   });
      116 |
      117 |   test('verse eleven - the farmer sowing his corn', () => {

      at Object.toEqual (house.spec.js:114:29)

  ● House › verse eleven - the farmer sowing his corn

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the farmer sowing his corn", "that kept the rooster that crowed in the morn", "that woke the priest all shaven and shorn", "that married the man all tattered and torn", "that kissed the maiden all forlorn", "that milked the cow with the crumpled horn", "that tossed the dog", "that worried the cat", "that killed the rat", "that ate the malt", …]
    Received: "This is farmer sowing his corn
    that kept rooster that crowed in the morn
    that woke priest all shaven and shorn
    that married man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      129 |       'that lay in the house that Jack built.',
      130 |     ];
    > 131 |     expect(House.verse(11)).toEqual(lyrics);
          |                             ^
      132 |   });
      133 |
      134 |   test('verse twelve - the horse and the hound and the horn', () => {

      at Object.toEqual (house.spec.js:131:29)

  ● House › verse twelve - the horse and the hound and the horn

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the horse and the hound and the horn", "that belonged to the farmer sowing his corn", "that kept the rooster that crowed in the morn", "that woke the priest all shaven and shorn", "that married the man all tattered and torn", "that kissed the maiden all forlorn", "that milked the cow with the crumpled horn", "that tossed the dog", "that worried the cat", "that killed the rat", …]
    Received: "This is horse and the hound and the horn
    that belonged to farmer sowing his corn
    that kept rooster that crowed in the morn
    that woke priest all shaven and shorn
    that married man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      147 |       'that lay in the house that Jack built.',
      148 |     ];
    > 149 |     expect(House.verse(12)).toEqual(lyrics);
          |                             ^
      150 |   });
      151 |
      152 |   test('multiple verses', () => {

      at Object.toEqual (house.spec.js:149:29)

  ● House › multiple verses

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built.", "", "This is the dog", "that worried the cat", "that killed the rat", "that ate the malt", "that lay in the house that Jack built.", …]
    Received: "This is cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      189 |       'that lay in the house that Jack built.',
      190 |     ];
    > 191 |     expect(House.verses(startVerse, endVerse)).toEqual(lyrics);
          |                                                ^
      192 |   });
      193 |
      194 |   test('full rhyme', () => {

      at Object.toEqual (house.spec.js:191:48)

  ● House › full rhyme

    expect(received).toEqual(expected) // deep equality

    Expected: ["This is the house that Jack built.", "", "This is the malt", "that lay in the house that Jack built.", "", "This is the rat", "that ate the malt", "that lay in the house that Jack built.", "", "This is the cat", …]
    Received: "This is house that Jack built.·
    This is malt
    that lay in house that Jack built.·
    This is rat
    that ate malt
    that lay in house that Jack built.·
    This is cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is priest all shaven and shorn
    that married man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is rooster that crowed in the morn
    that woke priest all shaven and shorn
    that married man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is farmer sowing his corn
    that kept rooster that crowed in the morn
    that woke priest all shaven and shorn
    that married man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built.·
    This is horse and the hound and the horn
    that belonged to farmer sowing his corn
    that kept rooster that crowed in the morn
    that woke priest all shaven and shorn
    that married man all tattered and torn
    that kissed maiden all forlorn
    that milked cow with the crumpled horn
    that tossed dog
    that worried cat
    that killed rat
    that ate malt
    that lay in house that Jack built."

      286 |       'that lay in the house that Jack built.',
      287 |     ];
    > 288 |     expect(House.verses(startVerse, endVerse)).toEqual(lyrics);
          |                                                ^
      289 |   });
      290 | });
      291 |

      at Object.toEqual (house.spec.js:288:48)

Test Suites: 1 failed, 1 total
Tests:       14 failed, 14 total
Snapshots:   0 total
Time:        3.25 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/house.js|.\/house.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
