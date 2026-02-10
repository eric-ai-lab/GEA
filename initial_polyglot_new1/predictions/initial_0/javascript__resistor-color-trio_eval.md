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
    ✓ Orange and orange and black (4 ms)
    ✓ Blue and grey and brown
    ✓ Red and black and red
    ✓ Green and brown and orange (1 ms)
    ✓ Yellow and violet and yellow (1 ms)
    ✕ Invalid color (1 ms)

  ● Resistor Color Trio › Invalid color

    TypeError: expect(...).toThrowError is not a function

      40 |     expect(
      41 |       () => new ResistorColorTrio(['yellow', 'purple', 'black']).label,
    > 42 |     ).toThrowError(/invalid color/);
         |       ^
      43 |   });
      44 | });
      45 |

      at Object.toThrowError (resistor-color-trio.spec.js:42:7)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 5 passed, 6 total
Snapshots:   0 total
Time:        0.656 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./resistor-color-trio.js|./resistor-color-trio.spec.js.
