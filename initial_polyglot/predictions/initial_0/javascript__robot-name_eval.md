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
    ✓ has a name (3 ms)
    ✓ name is the same each time (1 ms)
    ✓ different robots have different names (1 ms)
    ✕ is able to reset the name (1 ms)
    ✕ should set a unique name after reset
    ✓ internal name cannot be modified (2 ms)
    ✓ new names should not be sequential (1 ms)
    ✕ names from reset should not be sequential (1 ms)
    ○ skipped all the names can be generated

  ● Robot › is able to reset the name

    TypeError: robot.reset is not a function

      50 |     const originalName = robot.name;
      51 |
    > 52 |     robot.reset();
         |           ^
      53 |     const newName = robot.name;
      54 |
      55 |     expect(newName).toMatch(/^[A-Z]{2}\d{3}$/);

      at Object.reset (robot-name.spec.js:52:11)

  ● Robot › should set a unique name after reset

    TypeError: robot.reset is not a function

      63 |     usedNames.add(robot.name);
      64 |     for (let i = 0; i < NUMBER_OF_ROBOTS; i += 1) {
    > 65 |       robot.reset();
         |             ^
      66 |       usedNames.add(robot.name);
      67 |     }
      68 |

      at Object.reset (robot-name.spec.js:65:13)

  ● Robot › names from reset should not be sequential

    TypeError: robot.reset is not a function

      88 |   test('names from reset should not be sequential', () => {
      89 |     const name1 = robot.name;
    > 90 |     robot.reset();
         |           ^
      91 |     const name2 = robot.name;
      92 |     robot.reset();
      93 |     const name3 = robot.name;

      at Object.reset (robot-name.spec.js:90:11)

Test Suites: 1 failed, 1 total
Tests:       3 failed, 1 skipped, 5 passed, 9 total
Snapshots:   0 total
Time:        0.667 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./robot-name.js|./robot-name.spec.js.
