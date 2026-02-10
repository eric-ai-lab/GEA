+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' rest-api.spec.js
+ npm run test

> test
> jest ./*

FAIL ./rest-api.spec.js
  Rest API
    user management
      ✕ no users (24 ms)
      ✓ add user (1 ms)
      ✕ get single user (3 ms)
    iou
      ✕ both users have 0 balance
      ✕ borrower has negative balance (2 ms)
      ✕ lender has negative balance (1 ms)
      ✕ lender owes borrower (1 ms)
      ✕ lender owes borrower less than new loan (1 ms)
      ✕ lender owes borrower same as new loan (1 ms)

  ● Rest API › user management › no users

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 3

      Object {
    -   "users": Array [],
    +   "users": Array [
    +     Array [],
    +   ],
      }

       5 |     test('no users', () => {
       6 |       const restAPI = new RestAPI({ users: [] });
    >  7 |       expect(restAPI.get('/users')).toEqual({ users: [] });
         |                                     ^
       8 |     });
       9 |
      10 |     test('add user', () => {

      at Object.toEqual (rest-api.spec.js:7:37)

  ● Rest API › user management › get single user

    expect(received).toEqual(expected) // deep equality

    - Expected  - 8
    + Received  + 1

      Object {
    -   "users": Array [
    -     Object {
    -       "balance": 0,
    -       "name": "Bob",
    -       "owed_by": Object {},
    -       "owes": Object {},
    -     },
    -   ],
    +   "users": Array [],
      }

      27 |         { name: 'Bob', owes: {}, owed_by: {}, balance: 0 },
      28 |       ];
    > 29 |       expect(restAPI.get('/users?users=Bob')).toEqual({ users: expectedUsers });
         |                                               ^
      30 |     });
      31 |   });
      32 |

      at Object.toEqual (rest-api.spec.js:29:47)

  ● Rest API › iou › both users have 0 balance

    TypeError: Cannot read properties of undefined (reading 'owes')

      101 |       // First, check if there is any reverse debt that can be canceled out.
      102 |       // That is, if lender owes borrower, then that debt can be reduced.
    > 103 |       if (lender.owes.hasOwnProperty(borrowerName)) {
          |                  ^
      104 |         const debt = lender.owes[borrowerName];
      105 |         if (debt >= amount) {
      106 |           lender.owes[borrowerName] = parseFloat((debt - amount).toFixed(2));

      at RestAPI.owes (rest-api.js:103:18)
      at Object.post (rest-api.spec.js:45:22)

  ● Rest API › iou › borrower has negative balance

    TypeError: Cannot read properties of undefined (reading 'owes')

      101 |       // First, check if there is any reverse debt that can be canceled out.
      102 |       // That is, if lender owes borrower, then that debt can be reduced.
    > 103 |       if (lender.owes.hasOwnProperty(borrowerName)) {
          |                  ^
      104 |         const debt = lender.owes[borrowerName];
      105 |         if (debt >= amount) {
      106 |           lender.owes[borrowerName] = parseFloat((debt - amount).toFixed(2));

      at RestAPI.owes (rest-api.js:103:18)
      at Object.post (rest-api.spec.js:60:22)

  ● Rest API › iou › lender has negative balance

    TypeError: Cannot read properties of undefined (reading 'owes')

      101 |       // First, check if there is any reverse debt that can be canceled out.
      102 |       // That is, if lender owes borrower, then that debt can be reduced.
    > 103 |       if (lender.owes.hasOwnProperty(borrowerName)) {
          |                  ^
      104 |         const debt = lender.owes[borrowerName];
      105 |         if (debt >= amount) {
      106 |           lender.owes[borrowerName] = parseFloat((debt - amount).toFixed(2));

      at RestAPI.owes (rest-api.js:103:18)
      at Object.post (rest-api.spec.js:75:22)

  ● Rest API › iou › lender owes borrower

    TypeError: Cannot read properties of undefined (reading 'owes')

      101 |       // First, check if there is any reverse debt that can be canceled out.
      102 |       // That is, if lender owes borrower, then that debt can be reduced.
    > 103 |       if (lender.owes.hasOwnProperty(borrowerName)) {
          |                  ^
      104 |         const debt = lender.owes[borrowerName];
      105 |         if (debt >= amount) {
      106 |           lender.owes[borrowerName] = parseFloat((debt - amount).toFixed(2));

      at RestAPI.owes (rest-api.js:103:18)
      at Object.post (rest-api.spec.js:89:22)

  ● Rest API › iou › lender owes borrower less than new loan

    TypeError: Cannot read properties of undefined (reading 'owes')

      101 |       // First, check if there is any reverse debt that can be canceled out.
      102 |       // That is, if lender owes borrower, then that debt can be reduced.
    > 103 |       if (lender.owes.hasOwnProperty(borrowerName)) {
          |                  ^
      104 |         const debt = lender.owes[borrowerName];
      105 |         if (debt >= amount) {
      106 |           lender.owes[borrowerName] = parseFloat((debt - amount).toFixed(2));

      at RestAPI.owes (rest-api.js:103:18)
      at Object.post (rest-api.spec.js:103:22)

  ● Rest API › iou › lender owes borrower same as new loan

    TypeError: Cannot read properties of undefined (reading 'owes')

      101 |       // First, check if there is any reverse debt that can be canceled out.
      102 |       // That is, if lender owes borrower, then that debt can be reduced.
    > 103 |       if (lender.owes.hasOwnProperty(borrowerName)) {
          |                  ^
      104 |         const debt = lender.owes[borrowerName];
      105 |         if (debt >= amount) {
      106 |           lender.owes[borrowerName] = parseFloat((debt - amount).toFixed(2));

      at RestAPI.owes (rest-api.js:103:18)
      at Object.post (rest-api.spec.js:117:22)

Test Suites: 1 failed, 1 total
Tests:       8 failed, 1 passed, 9 total
Snapshots:   0 total
Time:        4.431 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/rest-api.js|.\/rest-api.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
