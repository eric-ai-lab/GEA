+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' triangle.spec.js
+ npm run test

> test
> jest ./*

FAIL ./triangle.spec.js
  Triangle
    equilateral triangle
      ✓ all sides are equal (34 ms)
      ✓ any side is unequal
      ✓ no sides are equal (1 ms)
      ✕ all zero sides is not a triangle (1 ms)
      ✓ sides may be floats (1 ms)
    isosceles triangle
      ✓ last two sides are equal (3 ms)
      ✓ first two sides are equal (2 ms)
      ✓ first and last sides are equal
      ✓ equilateral triangles are also isosceles
      ✓ no sides are equal (3 ms)
      ✕ first triangle inequality violation
      ✕ second triangle inequality violation (4 ms)
      ✕ third triangle inequality violation (2 ms)
      ✓ sides may be floats (1 ms)
    scalene triangle
      ✓ no sides are equal (17 ms)
      ✓ all sides are equal
      ✓ two sides are equal (2 ms)
      ✕ may not violate triangle inequality
      ✓ sides may be floats (1 ms)

  ● Triangle › equilateral triangle › all zero sides is not a triangle

    Invalid triangle

      16 |     // All sides must be greater than zero
      17 |     if (a <= 0 || b <= 0 || c <= 0) {
    > 18 |       throw new Error('Invalid triangle');
         |             ^
      19 |     }
      20 |
      21 |     // Triangle inequality: the sum of the lengths of any two sides must be at least the third side

      at new Triangle (triangle.js:18:13)
      at Object.<anonymous> (triangle.spec.js:21:24)

  ● Triangle › isosceles triangle › first triangle inequality violation

    Invalid triangle

      21 |     // Triangle inequality: the sum of the lengths of any two sides must be at least the third side
      22 |     if (a + b < c || a + c < b || b + c < a) {
    > 23 |       throw new Error('Invalid triangle');
         |             ^
      24 |     }
      25 |
      26 |     this.sides = sides;

      at new Triangle (triangle.js:23:13)
      at Object.<anonymous> (triangle.spec.js:58:24)

  ● Triangle › isosceles triangle › second triangle inequality violation

    Invalid triangle

      21 |     // Triangle inequality: the sum of the lengths of any two sides must be at least the third side
      22 |     if (a + b < c || a + c < b || b + c < a) {
    > 23 |       throw new Error('Invalid triangle');
         |             ^
      24 |     }
      25 |
      26 |     this.sides = sides;

      at new Triangle (triangle.js:23:13)
      at Object.<anonymous> (triangle.spec.js:63:24)

  ● Triangle › isosceles triangle › third triangle inequality violation

    Invalid triangle

      21 |     // Triangle inequality: the sum of the lengths of any two sides must be at least the third side
      22 |     if (a + b < c || a + c < b || b + c < a) {
    > 23 |       throw new Error('Invalid triangle');
         |             ^
      24 |     }
      25 |
      26 |     this.sides = sides;

      at new Triangle (triangle.js:23:13)
      at Object.<anonymous> (triangle.spec.js:68:24)

  ● Triangle › scalene triangle › may not violate triangle inequality

    Invalid triangle

      21 |     // Triangle inequality: the sum of the lengths of any two sides must be at least the third side
      22 |     if (a + b < c || a + c < b || b + c < a) {
    > 23 |       throw new Error('Invalid triangle');
         |             ^
      24 |     }
      25 |
      26 |     this.sides = sides;

      at new Triangle (triangle.js:23:13)
      at Object.<anonymous> (triangle.spec.js:95:24)

Test Suites: 1 failed, 1 total
Tests:       5 failed, 14 passed, 19 total
Snapshots:   0 total
Time:        2.873 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/triangle.js|.\/triangle.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
