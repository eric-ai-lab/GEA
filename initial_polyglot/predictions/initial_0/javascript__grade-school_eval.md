+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' grade-school.spec.js
+ npm run test

> test
> jest ./*

FAIL ./grade-school.spec.js (5.343 s)
  School
    ✕ a new school has an empty roster (51 ms)
    ✕ adding a student adds them to the roster for the given grade (3 ms)
    ✕ adding more students to the same grade adds them to the roster (6 ms)
    ✕ adding students to different grades adds them to the roster (2 ms)
    ✓ grade returns the students in that grade in alphabetical order (1 ms)
    ✓ grade returns an empty array if there are no students in that grade (1 ms)
    ✕ the students names in each grade in the roster are sorted (17 ms)
    ✕ roster cannot be modified outside of module
    ✕ roster cannot be modified outside of module using grade() (1 ms)
    ✕ a student can't be in two different grades (1 ms)

  ● School › a new school has an empty roster

    expect(received).toEqual(expected) // deep equality

    Expected: {}
    Received: []

       9 |
      10 |   test('a new school has an empty roster', () => {
    > 11 |     expect(school.roster()).toEqual({});
         |                             ^
      12 |   });
      13 |
      14 |   test('adding a student adds them to the roster for the given grade', () => {

      at Object.toEqual (grade-school.spec.js:11:29)

  ● School › adding a student adds them to the roster for the given grade

    expect(received).toEqual(expected) // deep equality

    Expected: {"2": ["Aimee"]}
    Received: ["Aimee"]

      16 |
      17 |     const expectedDb = { 2: ['Aimee'] };
    > 18 |     expect(school.roster()).toEqual(expectedDb);
         |                             ^
      19 |   });
      20 |
      21 |   test('adding more students to the same grade adds them to the roster', () => {

      at Object.toEqual (grade-school.spec.js:18:29)

  ● School › adding more students to the same grade adds them to the roster

    expect(received).toEqual(expected) // deep equality

    Expected: {"2": ["Blair", "James", "Paul"]}
    Received: ["Blair", "James", "Paul"]

      25 |
      26 |     const expectedDb = { 2: ['Blair', 'James', 'Paul'] };
    > 27 |     expect(school.roster()).toEqual(expectedDb);
         |                             ^
      28 |   });
      29 |
      30 |   test('adding students to different grades adds them to the roster', () => {

      at Object.toEqual (grade-school.spec.js:27:29)

  ● School › adding students to different grades adds them to the roster

    expect(received).toEqual(expected) // deep equality

    Expected: {"3": ["Chelsea"], "7": ["Logan"]}
    Received: ["Chelsea", "Logan"]

      33 |
      34 |     const expectedDb = { 3: ['Chelsea'], 7: ['Logan'] };
    > 35 |     expect(school.roster()).toEqual(expectedDb);
         |                             ^
      36 |   });
      37 |
      38 |   test('grade returns the students in that grade in alphabetical order', () => {

      at Object.toEqual (grade-school.spec.js:35:29)

  ● School › the students names in each grade in the roster are sorted

    expect(received).toEqual(expected) // deep equality

    Expected: {"3": ["Kyle"], "4": ["Christopher", "Jennifer"], "6": ["Kareem"]}
    Received: ["Kyle", "Christopher", "Jennifer", "Kareem"]

      60 |       6: ['Kareem'],
      61 |     };
    > 62 |     expect(school.roster()).toEqual(expectedSortedStudents);
         |                             ^
      63 |   });
      64 |
      65 |   test('roster cannot be modified outside of module', () => {

      at Object.toEqual (grade-school.spec.js:62:29)

  ● School › roster cannot be modified outside of module

    TypeError: Cannot read properties of undefined (reading 'push')

      66 |     school.add('Aimee', 2);
      67 |     const roster = school.roster();
    > 68 |     roster[2].push('Oops.');
         |               ^
      69 |     const expectedDb = { 2: ['Aimee'] };
      70 |     expect(school.roster()).toEqual(expectedDb);
      71 |   });

      at Object.push (grade-school.spec.js:68:15)

  ● School › roster cannot be modified outside of module using grade()

    expect(received).toEqual(expected) // deep equality

    Expected: {"2": ["Aimee"]}
    Received: ["Aimee"]

      75 |     school.grade(2).push('Oops.');
      76 |     const expectedDb = { 2: ['Aimee'] };
    > 77 |     expect(school.roster()).toEqual(expectedDb);
         |                             ^
      78 |   });
      79 |
      80 |   test("a student can't be in two different grades", () => {

      at Object.toEqual (grade-school.spec.js:77:29)

  ● School › a student can't be in two different grades

    Student already added

      31 |   add(student, grade) {
      32 |     if (this.allStudents.has(student)) {
    > 33 |       throw new Error('Student already added');
         |             ^
      34 |     }
      35 |     this.allStudents.add(student);
      36 |     if (!this.rosterData[grade]) {

      at GradeSchool.add (grade-school.js:33:13)
      at Object.add (grade-school.spec.js:82:12)

Test Suites: 1 failed, 1 total
Tests:       8 failed, 2 passed, 10 total
Snapshots:   0 total
Time:        5.491 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/grade-school.js|.\/grade-school.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
