+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' simple-linked-list.spec.js
+ npm run test

> test
> jest ./*

PASS ./simple-linked-list.spec.js
  Element class
    ✓ has constructor (3 ms)
    ✓ value reflects constructor arg (1 ms)
    ✓ has null for next by default (1 ms)
  List class
    ✓ has constructor (1 ms)
    ✓ new lists should have length 0 (1 ms)
    ✓ can add a element (1 ms)
    ✓ adding a element increments length
    ✓ adding two elements increments twice
    ✓ new Lists have a null head element
    ✓ adding an Element to an empty list sets the head Element (1 ms)
    ✓ adding a second Element updates the head Element (1 ms)
    ✓ can get the next Element from the head (1 ms)
    ✓ can be initialized with an array (1 ms)
  Lists with multiple elements
    ✓ with correct length (1 ms)
    ✓ with correct head value (1 ms)
    ✓ can traverse the list
    ✓ can convert to an array (1 ms)
    ✓ head of list is final element from input array (1 ms)
    ✓ can convert longer list to an array
    ✓ can be reversed
    ✓ can be reversed when it has more elements (1 ms)
    ✓ can reverse with many elements (1 ms)
    ✓ can reverse a reversal

Test Suites: 1 passed, 1 total
Tests:       23 passed, 23 total
Snapshots:   0 total
Time:        0.714 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./simple-linked-list.js|./simple-linked-list.spec.js.
