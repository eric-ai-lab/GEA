+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' simple-linked-list.spec.js
+ npm run test

> test
> jest ./*

FAIL ./simple-linked-list.spec.js
  Element class
    ✓ has constructor (26 ms)
    ✓ value reflects constructor arg (1 ms)
    ✓ has null for next by default (39 ms)
  List class
    ✓ has constructor (1 ms)
    ✓ new lists should have length 0 (1 ms)
    ✓ can add a element (1 ms)
    ✓ adding a element increments length (8 ms)
    ✓ adding two elements increments twice (1 ms)
    ✓ new Lists have a null head element
    ✕ adding an Element to an empty list sets the head Element (81 ms)
    ✕ adding a second Element updates the head Element (4 ms)
    ✕ can get the next Element from the head (1 ms)
    ✕ can be initialized with an array
  Lists with multiple elements
    ✕ with correct length (11 ms)
    ✕ with correct head value (2 ms)
    ✕ can traverse the list
    ✕ can convert to an array (15 ms)
    ✕ head of list is final element from input array (1 ms)
    ✕ can convert longer list to an array (2 ms)
    ✕ can be reversed (1 ms)
    ✕ can be reversed when it has more elements
    ✕ can reverse with many elements (9 ms)
    ✕ can reverse a reversal (1 ms)

  ● List class › adding an Element to an empty list sets the head Element

    expect(received).toEqual(expected) // deep equality

    Expected: 1
    Received: {"_next": null, "_value": 1}

      60 |     const element = new Element(1);
      61 |     list.add(element);
    > 62 |     expect(list.head.value).toEqual(1);
         |                             ^
      63 |   });
      64 |
      65 |   test('adding a second Element updates the head Element', () => {

      at Object.toEqual (simple-linked-list.spec.js:62:29)

  ● List class › adding a second Element updates the head Element

    expect(received).toEqual(expected) // deep equality

    Expected: 3
    Received: {"_next": null, "_value": 1}

      69 |     list.add(element1);
      70 |     list.add(element2);
    > 71 |     expect(list.head.value).toEqual(3);
         |                             ^
      72 |   });
      73 |
      74 |   test('can get the next Element from the head', () => {

      at Object.toEqual (simple-linked-list.spec.js:71:29)

  ● List class › can get the next Element from the head

    expect(received).toEqual(expected) // deep equality

    Expected: 1
    Received: {"_next": null, "_value": 3}

      78 |     list.add(element1);
      79 |     list.add(element2);
    > 80 |     expect(list.head.next.value).toEqual(1);
         |                                  ^
      81 |   });
      82 |
      83 |   test('can be initialized with an array', () => {

      at Object.toEqual (simple-linked-list.spec.js:80:34)

  ● List class › can be initialized with an array

    expect(received).toEqual(expected) // deep equality

    Expected: 3
    Received: 0

      83 |   test('can be initialized with an array', () => {
      84 |     const list = new List([1, 2, 3]);
    > 85 |     expect(list.length).toEqual(3);
         |                         ^
      86 |     expect(list.head.value).toEqual(3);
      87 |   });
      88 | });

      at Object.toEqual (simple-linked-list.spec.js:85:25)

  ● Lists with multiple elements › with correct length

    expect(received).toEqual(expected) // deep equality

    Expected: 10
    Received: 0

      94 |   });
      95 |   test('with correct length', () => {
    > 96 |     expect(list.length).toEqual(10);
         |                         ^
      97 |   });
      98 |   test('with correct head value', () => {
      99 |     expect(list.head.value).toEqual(10);

      at Object.toEqual (simple-linked-list.spec.js:96:25)

  ● Lists with multiple elements › with correct head value

    TypeError: Cannot read properties of null (reading 'value')

       97 |   });
       98 |   test('with correct head value', () => {
    >  99 |     expect(list.head.value).toEqual(10);
          |                      ^
      100 |   });
      101 |   test('can traverse the list', () => {
      102 |     expect(list.head.next.next.next.value).toEqual(7);

      at Object.value (simple-linked-list.spec.js:99:22)

  ● Lists with multiple elements › can traverse the list

    TypeError: Cannot read properties of null (reading 'next')

      100 |   });
      101 |   test('can traverse the list', () => {
    > 102 |     expect(list.head.next.next.next.value).toEqual(7);
          |                      ^
      103 |   });
      104 |   test('can convert to an array', () => {
      105 |     const oneList = new List([1]);

      at Object.next (simple-linked-list.spec.js:102:22)

  ● Lists with multiple elements › can convert to an array

    expect(received).toEqual(expected) // deep equality

    - Expected  - 3
    + Received  + 1

    - Array [
    -   1,
    - ]
    + Array []

      104 |   test('can convert to an array', () => {
      105 |     const oneList = new List([1]);
    > 106 |     expect(oneList.toArray()).toEqual([1]);
          |                               ^
      107 |   });
      108 |   test('head of list is final element from input array', () => {
      109 |     const twoList = new List([1, 2]);

      at Object.toEqual (simple-linked-list.spec.js:106:31)

  ● Lists with multiple elements › head of list is final element from input array

    TypeError: Cannot read properties of null (reading 'value')

      108 |   test('head of list is final element from input array', () => {
      109 |     const twoList = new List([1, 2]);
    > 110 |     expect(twoList.head.value).toEqual(2);
          |                         ^
      111 |   });
      112 |   test('can convert longer list to an array', () => {
      113 |     expect(list.toArray()).toEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]);

      at Object.value (simple-linked-list.spec.js:110:25)

  ● Lists with multiple elements › can convert longer list to an array

    expect(received).toEqual(expected) // deep equality

    - Expected  - 12
    + Received  +  1

    - Array [
    -   10,
    -   9,
    -   8,
    -   7,
    -   6,
    -   5,
    -   4,
    -   3,
    -   2,
    -   1,
    - ]
    + Array []

      111 |   });
      112 |   test('can convert longer list to an array', () => {
    > 113 |     expect(list.toArray()).toEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]);
          |                            ^
      114 |   });
      115 |   test('can be reversed', () => {
      116 |     const twoList = new List([1, 2]);

      at Object.toEqual (simple-linked-list.spec.js:113:28)

  ● Lists with multiple elements › can be reversed

    TypeError: Cannot read properties of undefined (reading 'toArray')

      115 |   test('can be reversed', () => {
      116 |     const twoList = new List([1, 2]);
    > 117 |     expect(twoList.reverse().toArray()).toEqual([1, 2]);
          |                             ^
      118 |   });
      119 |   test('can be reversed when it has more elements', () => {
      120 |     const threeList = new List([1, 2, 3]);

      at Object.<anonymous> (simple-linked-list.spec.js:117:29)

  ● Lists with multiple elements › can be reversed when it has more elements

    TypeError: Cannot read properties of undefined (reading 'toArray')

      119 |   test('can be reversed when it has more elements', () => {
      120 |     const threeList = new List([1, 2, 3]);
    > 121 |     expect(threeList.reverse().toArray()).toEqual([1, 2, 3]);
          |                               ^
      122 |   });
      123 |   test('can reverse with many elements', () => {
      124 |     expect(list.reverse().toArray()).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

      at Object.<anonymous> (simple-linked-list.spec.js:121:31)

  ● Lists with multiple elements › can reverse with many elements

    TypeError: Cannot read properties of undefined (reading 'toArray')

      122 |   });
      123 |   test('can reverse with many elements', () => {
    > 124 |     expect(list.reverse().toArray()).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
          |                          ^
      125 |   });
      126 |   test('can reverse a reversal', () => {
      127 |     expect(list.reverse().reverse().toArray()).toEqual([

      at Object.<anonymous> (simple-linked-list.spec.js:124:26)

  ● Lists with multiple elements › can reverse a reversal

    TypeError: Cannot read properties of undefined (reading 'reverse')

      125 |   });
      126 |   test('can reverse a reversal', () => {
    > 127 |     expect(list.reverse().reverse().toArray()).toEqual([
          |                          ^
      128 |       10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
      129 |     ]);
      130 |   });

      at Object.<anonymous> (simple-linked-list.spec.js:127:26)

Test Suites: 1 failed, 1 total
Tests:       14 failed, 9 passed, 23 total
Snapshots:   0 total
Time:        5.094 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/simple-linked-list.js|.\/simple-linked-list.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
