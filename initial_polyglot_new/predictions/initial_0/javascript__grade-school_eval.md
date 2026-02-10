+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' grade-school.spec.js
+ npm run test

> test
> jest ./*

PASS ./grade-school.spec.js
  School
    ✓ a new school has an empty roster (3 ms)
    ✓ adding a student adds them to the roster for the given grade (1 ms)
    ✓ adding more students to the same grade adds them to the roster (1 ms)
    ✓ adding students to different grades adds them to the roster (6 ms)
    ✓ grade returns the students in that grade in alphabetical order (1 ms)
    ✓ grade returns an empty array if there are no students in that grade (1 ms)
    ✓ the students names in each grade in the roster are sorted (1 ms)
    ✓ roster cannot be modified outside of module (1 ms)
    ✓ roster cannot be modified outside of module using grade() (1 ms)
    ✓ a student can't be in two different grades (1 ms)

Test Suites: 1 passed, 1 total
Tests:       10 passed, 10 total
Snapshots:   0 total
Time:        0.661 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./grade-school.js|./grade-school.spec.js|./node_modules|./package-lock.json|./package.json.
