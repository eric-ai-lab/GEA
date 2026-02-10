+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' resistor-color-trio.spec.js
+ npm run test

> test
> jest ./*

FAIL ./resistor-color-trio.spec.js
  Resistor Color Trio
    ✕ Orange and orange and black (61 ms)
    ✕ Blue and grey and brown (1 ms)
    ✕ Red and black and red (28 ms)
    ✕ Green and brown and orange (1 ms)
    ✕ Yellow and violet and yellow (29 ms)
    ✕ Invalid color (2 ms)

  ● Resistor Color Trio › Orange and orange and black

    expect(received).toEqual(expected) // deep equality

    Expected: "Resistor value: 33 ohms"
    Received: [Function label]

       7 | describe('Resistor Color Trio', () => {
       8 |   test('Orange and orange and black', () => {
    >  9 |     expect(new ResistorColorTrio(['orange', 'orange', 'black']).label).toEqual(
         |                                                                        ^
      10 |       makeLabel({ value: 33, unit: 'ohms' }),
      11 |     );
      12 |   });

      at Object.toEqual (resistor-color-trio.spec.js:9:72)

  ● Resistor Color Trio › Blue and grey and brown

    expect(received).toEqual(expected) // deep equality

    Expected: "Resistor value: 680 ohms"
    Received: [Function label]

      13 |
      14 |   test('Blue and grey and brown', () => {
    > 15 |     expect(new ResistorColorTrio(['blue', 'grey', 'brown']).label).toEqual(
         |                                                                    ^
      16 |       makeLabel({ value: 680, unit: 'ohms' }),
      17 |     );
      18 |   });

      at Object.toEqual (resistor-color-trio.spec.js:15:68)

  ● Resistor Color Trio › Red and black and red

    expect(received).toEqual(expected) // deep equality

    Expected: "Resistor value: 2 kiloohms"
    Received: [Function label]

      19 |
      20 |   test('Red and black and red', () => {
    > 21 |     expect(new ResistorColorTrio(['red', 'black', 'red']).label).toEqual(
         |                                                                  ^
      22 |       makeLabel({ value: 2, unit: 'kiloohms' }),
      23 |     );
      24 |   });

      at Object.toEqual (resistor-color-trio.spec.js:21:66)

  ● Resistor Color Trio › Green and brown and orange

    expect(received).toEqual(expected) // deep equality

    Expected: "Resistor value: 51 kiloohms"
    Received: [Function label]

      25 |
      26 |   test('Green and brown and orange', () => {
    > 27 |     expect(new ResistorColorTrio(['green', 'brown', 'orange']).label).toEqual(
         |                                                                       ^
      28 |       makeLabel({ value: 51, unit: 'kiloohms' }),
      29 |     );
      30 |   });

      at Object.toEqual (resistor-color-trio.spec.js:27:71)

  ● Resistor Color Trio › Yellow and violet and yellow

    expect(received).toEqual(expected) // deep equality

    Expected: "Resistor value: 470 kiloohms"
    Received: [Function label]

      31 |
      32 |   test('Yellow and violet and yellow', () => {
    > 33 |     expect(new ResistorColorTrio(['yellow', 'violet', 'yellow']).label).toEqual(
         |                                                                         ^
      34 |       makeLabel({ value: 470, unit: 'kiloohms' }),
      35 |     );
      36 |   });

      at Object.toEqual (resistor-color-trio.spec.js:33:73)

  ● Resistor Color Trio › Invalid color

    expect(received).toThrowError(expected)

    Expected pattern: /invalid color/

    Received function did not throw

      40 |     expect(
      41 |       () => new ResistorColorTrio(['yellow', 'purple', 'black']).label,
    > 42 |     ).toThrowError(/invalid color/);
         |       ^
      43 |   });
      44 | });
      45 |

      at Object.toThrowError (resistor-color-trio.spec.js:42:7)

Test Suites: 1 failed, 1 total
Tests:       6 failed, 6 total
Snapshots:   0 total
Time:        4.322 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/resistor-color-trio.js|.\/resistor-color-trio.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
