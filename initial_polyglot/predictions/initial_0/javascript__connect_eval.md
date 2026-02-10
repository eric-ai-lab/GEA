+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' connect.spec.js
+ npm run test

> test
> jest ./*

FAIL ./connect.spec.js
  Judging a game of connect
    ✕ an empty board has no winner (4 ms)
    ✕ X can win on a 1x1 board (1 ms)
    ✕ O can win on a 1x1 board
    ✕ only edges does not make a winner
    ✕ illegal diagonal does not make a winner (1 ms)
    ✕ nobody wins crossing adjacent angles (1 ms)
    ✕ X wins crossing from left to right
    ✕ O wins crossing from top to bottom (1 ms)
    ✕ X wins using a convoluted path (1 ms)
    ✕ X wins using a spiral path (1 ms)

  ● Judging a game of connect › an empty board has no winner

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:12:12)

  ● Judging a game of connect › X can win on a 1x1 board

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:17:12)

  ● Judging a game of connect › O can win on a 1x1 board

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:22:12)

  ● Judging a game of connect › only edges does not make a winner

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:27:12)

  ● Judging a game of connect › illegal diagonal does not make a winner

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:38:12)

  ● Judging a game of connect › nobody wins crossing adjacent angles

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:49:12)

  ● Judging a game of connect › X wins crossing from left to right

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:60:12)

  ● Judging a game of connect › O wins crossing from top to bottom

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:71:12)

  ● Judging a game of connect › X wins using a convoluted path

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:82:12)

  ● Judging a game of connect › X wins using a spiral path

    TypeError: board.trim is not a function

      11 |     // The board argument is expected to be a string with newline-delimited rows.
      12 |     // Remove any leading/trailing whitespace and remove spaces in each row.
    > 13 |     this.grid = board.trim().split('\n').map(line => line.replace(/\s+/g, ''));
         |                       ^
      14 |     this.n = this.grid.length;
      15 |     this.m = this.n > 0 ? this.grid[0].length : 0;
      16 |   }

      at new trim (connect.js:13:23)
      at Object.<anonymous> (connect.spec.js:97:12)

Test Suites: 1 failed, 1 total
Tests:       10 failed, 10 total
Snapshots:   0 total
Time:        4.424 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/connect.js|.\/connect.spec.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
