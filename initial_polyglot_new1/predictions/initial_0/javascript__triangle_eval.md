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
      ✓ all sides are equal (3 ms)
      ✓ any side is unequal (1 ms)
      ✓ no sides are equal (1 ms)
      ✕ all zero sides is not a triangle (1 ms)
      ✓ sides may be floats
    isosceles triangle
      ✓ last two sides are equal (1 ms)
      ✓ first two sides are equal (1 ms)
      ✓ first and last sides are equal (1 ms)
      ✓ equilateral triangles are also isosceles
      ✓ no sides are equal (10 ms)
      ✕ first triangle inequality violation
      ✕ second triangle inequality violation
      ✕ third triangle inequality violation
      ✓ sides may be floats
    scalene triangle
      ✓ no sides are equal
      ✓ all sides are equal (1 ms)
      ✓ two sides are equal
      ✕ may not violate triangle inequality (1 ms)
      ✓ sides may be floats (1 ms)

  ● Triangle › equilateral triangle › all zero sides is not a triangle

    Triangle inequality violated

      15 |     // Check that all sides are greater than 0
      16 |     if (a <= 0 || b <= 0 || c <= 0) {
    > 17 |       throw new Error('Triangle inequality violated');
         |             ^
      18 |     }
      19 |     
      20 |     // Check triangle inequality: sum of any two sides must be >= third side

      at Triangle.validateTriangle (triangle.js:17:13)
      at new validateTriangle (triangle.js:9:10)
      at Object.<anonymous> (triangle.spec.js:21:24)

  ● Triangle › isosceles triangle › first triangle inequality violation

    Triangle inequality violated

      20 |     // Check triangle inequality: sum of any two sides must be >= third side
      21 |     if (a + b < c || b + c < a || a + c < b) {
    > 22 |       throw new Error('Triangle inequality violated');
         |             ^
      23 |     }
      24 |   }
      25 |

      at Triangle.validateTriangle (triangle.js:22:13)
      at new validateTriangle (triangle.js:9:10)
      at Object.<anonymous> (triangle.spec.js:58:24)

  ● Triangle › isosceles triangle › second triangle inequality violation

    Triangle inequality violated

      20 |     // Check triangle inequality: sum of any two sides must be >= third side
      21 |     if (a + b < c || b + c < a || a + c < b) {
    > 22 |       throw new Error('Triangle inequality violated');
         |             ^
      23 |     }
      24 |   }
      25 |

      at Triangle.validateTriangle (triangle.js:22:13)
      at new validateTriangle (triangle.js:9:10)
      at Object.<anonymous> (triangle.spec.js:63:24)

  ● Triangle › isosceles triangle › third triangle inequality violation

    Triangle inequality violated

      20 |     // Check triangle inequality: sum of any two sides must be >= third side
      21 |     if (a + b < c || b + c < a || a + c < b) {
    > 22 |       throw new Error('Triangle inequality violated');
         |             ^
      23 |     }
      24 |   }
      25 |

      at Triangle.validateTriangle (triangle.js:22:13)
      at new validateTriangle (triangle.js:9:10)
      at Object.<anonymous> (triangle.spec.js:68:24)

  ● Triangle › scalene triangle › may not violate triangle inequality

    Triangle inequality violated

      20 |     // Check triangle inequality: sum of any two sides must be >= third side
      21 |     if (a + b < c || b + c < a || a + c < b) {
    > 22 |       throw new Error('Triangle inequality violated');
         |             ^
      23 |     }
      24 |   }
      25 |

      at Triangle.validateTriangle (triangle.js:22:13)
      at new validateTriangle (triangle.js:9:10)
      at Object.<anonymous> (triangle.spec.js:95:24)

Test Suites: 1 failed, 1 total
Tests:       5 failed, 14 passed, 19 total
Snapshots:   0 total
Time:        0.668 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./triangle.js|./triangle.spec.js.
