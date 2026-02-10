+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' list-ops.spec.js
+ npm run test

> test
> jest ./*

FAIL ./list-ops.spec.js
  append entries to a list and return the new list
    ✓ empty lists (40 ms)
    ✓ empty list to list
    ✕ non-empty lists (9 ms)
  concat lists and lists of lists into new list
    ✕ empty list
    ✕ list of lists
  filter list returning only values that satisfy the filter function
    ✕ empty list (1 ms)
    ✕ non empty list (1 ms)
  returns the length of a list
    ✓ empty list
    ✓ non-empty list (1 ms)
  returns a list of elements whose values equal the list value transformed by the mapping function
    ✕ empty list (1 ms)
    ✕ non-empty list
  folds (reduces) the given list from the left with a function
    ✓ empty list
    ✓ direction independent function applied to non-empty list (1 ms)
    ✓ direction dependent function applied to non-empty list
  folds (reduces) the given list from the right with a function
    ✓ empty list
    ✓ direction independent function applied to non-empty list
    ✕ direction dependent function applied to non-empty list
  reverse the elements of a list
    ✕ empty list (1 ms)
    ✕ non-empty list (1 ms)
    ✕ list of lists is not flattened (1 ms)

  ● append entries to a list and return the new list › non-empty lists

    expect(received).toEqual(expected) // deep equality

    Expected: [1, 2, 2, 3, 4, 5]
    Received: undefined

      17 |     const list1 = new List([1, 2]);
      18 |     const list2 = new List([2, 3, 4, 5]);
    > 19 |     expect(list1.append(list2).values).toEqual([1, 2, 2, 3, 4, 5]);
         |                                        ^
      20 |   });
      21 | });
      22 |

      at Object.toEqual (list-ops.spec.js:19:40)

  ● concat lists and lists of lists into new list › empty list

    expect(received).toEqual(expected) // deep equality

    Expected: []
    Received: undefined

      25 |     const list1 = new List();
      26 |     const list2 = new List();
    > 27 |     expect(list1.concat(list2).values).toEqual([]);
         |                                        ^
      28 |   });
      29 |
      30 |   test('list of lists', () => {

      at Object.toEqual (list-ops.spec.js:27:40)

  ● concat lists and lists of lists into new list › list of lists

    expect(received).toEqual(expected) // deep equality

    Expected: [1, 2, 3, 4, 5, 6]
    Received: undefined

      34 |     const list4 = new List([4, 5, 6]);
      35 |     const listOfLists = new List([list2, list3, list4]);
    > 36 |     expect(list1.concat(listOfLists).values).toEqual([1, 2, 3, 4, 5, 6]);
         |                                              ^
      37 |   });
      38 | });
      39 |

      at Object.toEqual (list-ops.spec.js:36:46)

  ● filter list returning only values that satisfy the filter function › empty list

    expect(received).toEqual(expected) // deep equality

    Expected: []
    Received: undefined

      41 |   test('empty list', () => {
      42 |     const list1 = new List([]);
    > 43 |     expect(list1.filter((el) => el % 2 === 1).values).toEqual([]);
         |                                                       ^
      44 |   });
      45 |
      46 |   test('non empty list', () => {

      at Object.toEqual (list-ops.spec.js:43:55)

  ● filter list returning only values that satisfy the filter function › non empty list

    expect(received).toEqual(expected) // deep equality

    Expected: [1, 3, 5]
    Received: undefined

      46 |   test('non empty list', () => {
      47 |     const list1 = new List([1, 2, 3, 5]);
    > 48 |     expect(list1.filter((el) => el % 2 === 1).values).toEqual([1, 3, 5]);
         |                                                       ^
      49 |   });
      50 | });
      51 |

      at Object.toEqual (list-ops.spec.js:48:55)

  ● returns a list of elements whose values equal the list value transformed by the mapping function › empty list

    expect(received).toEqual(expected) // deep equality

    Expected: []
    Received: undefined

      65 |   test('empty list', () => {
      66 |     const list1 = new List();
    > 67 |     expect(list1.map((el) => ++el).values).toEqual([]);
         |                                            ^
      68 |   });
      69 |
      70 |   test('non-empty list', () => {

      at Object.toEqual (list-ops.spec.js:67:44)

  ● returns a list of elements whose values equal the list value transformed by the mapping function › non-empty list

    expect(received).toEqual(expected) // deep equality

    Expected: [2, 4, 6, 8]
    Received: undefined

      70 |   test('non-empty list', () => {
      71 |     const list1 = new List([1, 3, 5, 7]);
    > 72 |     expect(list1.map((el) => ++el).values).toEqual([2, 4, 6, 8]);
         |                                            ^
      73 |   });
      74 | });
      75 |

      at Object.toEqual (list-ops.spec.js:72:44)

  ● folds (reduces) the given list from the right with a function › direction dependent function applied to non-empty list

    expect(received).toEqual(expected) // deep equality

    Expected: 9
    Received: 1

      104 |   test('direction dependent function applied to non-empty list', () => {
      105 |     const list1 = new List([1, 2, 3, 4]);
    > 106 |     expect(list1.foldr((acc, el) => el / acc, 24)).toEqual(9);
          |                                                    ^
      107 |   });
      108 | });
      109 |

      at Object.toEqual (list-ops.spec.js:106:52)

  ● reverse the elements of a list › empty list

    expect(received).toEqual(expected) // deep equality

    Expected: []
    Received: undefined

      111 |   test('empty list', () => {
      112 |     const list1 = new List();
    > 113 |     expect(list1.reverse().values).toEqual([]);
          |                                    ^
      114 |   });
      115 |
      116 |   test('non-empty list', () => {

      at Object.toEqual (list-ops.spec.js:113:36)

  ● reverse the elements of a list › non-empty list

    expect(received).toEqual(expected) // deep equality

    Expected: [7, 5, 3, 1]
    Received: undefined

      116 |   test('non-empty list', () => {
      117 |     const list1 = new List([1, 3, 5, 7]);
    > 118 |     expect(list1.reverse().values).toEqual([7, 5, 3, 1]);
          |                                    ^
      119 |   });
      120 |
      121 |   test('list of lists is not flattened', () => {

      at Object.toEqual (list-ops.spec.js:118:36)

  ● reverse the elements of a list › list of lists is not flattened

    expect(received).toEqual(expected) // deep equality

    Expected: [[4, 5, 6], [], [3], [1, 2]]
    Received: undefined

      121 |   test('list of lists is not flattened', () => {
      122 |     const list1 = new List([[1, 2], [3], [], [4, 5, 6]]);
    > 123 |     expect(list1.reverse().values).toEqual([[4, 5, 6], [], [3], [1, 2]]);
          |                                    ^
      124 |   });
      125 | });
      126 |

      at Object.toEqual (list-ops.spec.js:123:36)

Test Suites: 1 failed, 1 total
Tests:       11 failed, 9 passed, 20 total
Snapshots:   0 total
Time:        3.216 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/list-ops.js|.\/list-ops.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
