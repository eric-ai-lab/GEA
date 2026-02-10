+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' two-bucket.spec.js
+ npm run test

> test
> jest ./*

FAIL ./two-bucket.spec.js
  TwoBucket
    Measure using bucket one of size 3 and bucket two of size 5
      ✓ start with bucket one (14 ms)
      ✓ start with bucket two (1 ms)
    Measure using bucket one of size 7 and bucket two of size 11
      ✓ start with bucket one (1 ms)
      ✓ start with bucket two (1 ms)
    Measure one step using bucket one of size 1 and bucket two of size 3
      ✓ start with bucket two (1 ms)
    Measure using bucket one of size 2 and bucket two of size 3
      ✕ start with bucket one and end with bucket two (10 ms)
    Reachability
      ✕ Not possible to reach the goal, start with bucket one (2 ms)
      ✕ Not possible to reach the goal, start with bucket two (3 ms)
      ✓ With the same buckets but a different goal, then it is possible (8 ms)
    Goal larger than both buckets
      ✕ Is impossible

  ● TwoBucket › Measure using bucket one of size 2 and bucket two of size 3 › start with bucket one and end with bucket two

    expect(received).toEqual(expected) // deep equality

    Expected: 2
    Received: 1

      68 |       const twoBucket = new TwoBucket(2, 3, 3, 'one');
      69 |       const result = twoBucket.solve();
    > 70 |       expect(result.moves).toEqual(2);
         |                            ^
      71 |       expect(result.goalBucket).toEqual('two');
      72 |       expect(result.otherBucket).toEqual(2);
      73 |     });

      at Object.toEqual (two-bucket.spec.js:70:28)

  ● TwoBucket › Reachability › Not possible to reach the goal, start with bucket one

    expect(received).toThrow()

    Received function did not throw

      79 |
      80 |     test('Not possible to reach the goal, start with bucket one', () => {
    > 81 |       expect(() => new TwoBucket(buckOne, buckTwo, 5, 'one')).toThrow();
         |                                                               ^
      82 |     });
      83 |
      84 |     test('Not possible to reach the goal, start with bucket two', () => {

      at Object.toThrow (two-bucket.spec.js:81:63)

  ● TwoBucket › Reachability › Not possible to reach the goal, start with bucket two

    expect(received).toThrow()

    Received function did not throw

      83 |
      84 |     test('Not possible to reach the goal, start with bucket two', () => {
    > 85 |       expect(() => new TwoBucket(buckOne, buckTwo, 5, 'two')).toThrow();
         |                                                               ^
      86 |     });
      87 |
      88 |     test('With the same buckets but a different goal, then it is possible', () => {

      at Object.toThrow (two-bucket.spec.js:85:63)

  ● TwoBucket › Goal larger than both buckets › Is impossible

    expect(received).toThrow()

    Received function did not throw

       99 |   describe('Goal larger than both buckets', () => {
      100 |     test('Is impossible', () => {
    > 101 |       expect(() => new TwoBucket(5, 7, 8, 'one')).toThrow();
          |                                                   ^
      102 |     });
      103 |   });
      104 | });

      at Object.toThrow (two-bucket.spec.js:101:51)

Test Suites: 1 failed, 1 total
Tests:       4 failed, 6 passed, 10 total
Snapshots:   0 total
Time:        3.601 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/two-bucket.js|.\/two-bucket.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
