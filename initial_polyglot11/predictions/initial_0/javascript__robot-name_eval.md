+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' robot-name.spec.js
+ npm run test

> test
> jest ./*

FAIL ./robot-name.spec.js
  Robot
    ✓ has a name (10 ms)
    ✓ name is the same each time (2 ms)
    ✓ different robots have different names (1 ms)
    ✓ is able to reset the name (1 ms)
    ✕ should set a unique name after reset (75 ms)
    ✓ internal name cannot be modified (3 ms)
    ✓ new names should not be sequential (1 ms)
    ✓ names from reset should not be sequential (1 ms)
    ○ skipped all the names can be generated

  ● Robot › should set a unique name after reset

    expect(received).toEqual(expected) // deep equality

    Expected: 10001
    Received: 9921

      67 |     }
      68 |
    > 69 |     expect(usedNames.size).toEqual(NUMBER_OF_ROBOTS + 1);
         |                            ^
      70 |   });
      71 |
      72 |   test('internal name cannot be modified', () => {

      at Object.toEqual (robot-name.spec.js:69:28)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 skipped, 7 passed, 9 total
Snapshots:   0 total
Time:        2.4 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/robot-name.js|.\/robot-name.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
