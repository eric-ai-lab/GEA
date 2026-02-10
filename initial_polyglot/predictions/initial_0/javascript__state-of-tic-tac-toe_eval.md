+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' state-of-tic-tac-toe.spec.js
+ npm run test

> test
> jest ./*

FAIL ./state-of-tic-tac-toe.spec.js (6.194 s)
  Won games
    ✕ Finished game where X won via left column victory (50 ms)
    ✕ Finished game where X won via middle column victory
    ✕ Finished game where X won via right column victory (1 ms)
    ✕ Finished game where O won via left column victory (3 ms)
    ✕ Finished game where O won via middle column victory (8 ms)
    ✕ Finished game where O won via right column victory
    ✕ Finished game where X won via top row victory (1 ms)
    ✕ Finished game where X won via middle row victory
    ✕ Finished game where X won via bottom row victory
    ✕ Finished game where O won via top row victory (6 ms)
    ✕ Finished game where O won via middle row victory
    ✕ Finished game where O won via bottom row victory (1 ms)
    ✕ Finished game where X won via falling diagonal victory (1 ms)
    ✕ Finished game where X won via rising diagonal victory (1 ms)
    ✕ Finished game where O won via falling diagonal victory (1 ms)
    ✕ Finished game where O won via rising diagonal victory
    ✕ Finished game where X won via a row and a column victory
    ✕ Finished game where X won via two diagonal victories (7 ms)
  Draw games
    ✕ Draw
    ✕ Another draw
  Ongoing games
    ✕ Ongoing game: one move in (3 ms)
    ✕ Ongoing game: two moves in
    ✕ Ongoing game: five moves in
  Invalid boards
    ✕ Invalid board: X went twice (89 ms)
    ✕ Invalid board: O started (15 ms)
    ✕ Invalid board: X won and O kept playing (3 ms)
    ✕ Invalid board: players kept playing after a win (12 ms)

  ● Won games › Finished game where X won via left column victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:7:29)

  ● Won games › Finished game where X won via middle column victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:14:29)

  ● Won games › Finished game where X won via right column victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:21:29)

  ● Won games › Finished game where O won via left column victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:28:29)

  ● Won games › Finished game where O won via middle column victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:35:29)

  ● Won games › Finished game where O won via right column victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:42:29)

  ● Won games › Finished game where X won via top row victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:49:29)

  ● Won games › Finished game where X won via middle row victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:56:29)

  ● Won games › Finished game where X won via bottom row victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:63:29)

  ● Won games › Finished game where O won via top row victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:70:29)

  ● Won games › Finished game where O won via middle row victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:77:29)

  ● Won games › Finished game where O won via bottom row victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:84:29)

  ● Won games › Finished game where X won via falling diagonal victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:91:29)

  ● Won games › Finished game where X won via rising diagonal victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:98:29)

  ● Won games › Finished game where O won via falling diagonal victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:105:29)

  ● Won games › Finished game where O won via rising diagonal victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:112:29)

  ● Won games › Finished game where X won via a row and a column victory

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:119:29)

  ● Won games › Finished game where X won via two diagonal victories

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:126:29)

  ● Draw games › Draw

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:135:29)

  ● Draw games › Another draw

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:142:29)

  ● Ongoing games › Ongoing game: one move in

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:151:29)

  ● Ongoing games › Ongoing game: two moves in

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:158:29)

  ● Ongoing games › Ongoing game: five moves in

    Invalid board: Each row must have 3 cells

      76 |   for (let i = 0; i < 3; i++) {
      77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
    > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
         |             ^
      79 |     }
      80 |   }
      81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at Object.<anonymous> (state-of-tic-tac-toe.spec.js:165:29)

  ● Invalid boards › Invalid board: X went twice

    expect(received).toThrow(expected)

    Expected message: "Wrong turn order: X went twice"
    Received message: "Invalid board: Each row must have 3 cells"

          76 |   for (let i = 0; i < 3; i++) {
          77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
        > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
             |             ^
          79 |     }
          80 |   }
          81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at actual (state-of-tic-tac-toe.spec.js:174:35)
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (state-of-tic-tac-toe.spec.js:175:20)
      at Object.toThrow (state-of-tic-tac-toe.spec.js:175:20)

  ● Invalid boards › Invalid board: O started

    expect(received).toThrow(expected)

    Expected message: "Wrong turn order: O started"
    Received message: "Invalid board: Each row must have 3 cells"

          76 |   for (let i = 0; i < 3; i++) {
          77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
        > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
             |             ^
          79 |     }
          80 |   }
          81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at actual (state-of-tic-tac-toe.spec.js:181:35)
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (state-of-tic-tac-toe.spec.js:182:20)
      at Object.toThrow (state-of-tic-tac-toe.spec.js:182:20)

  ● Invalid boards › Invalid board: X won and O kept playing

    expect(received).toThrow(expected)

    Expected message: "Impossible board: game should have ended after the game was won"
    Received message: "Invalid board: Each row must have 3 cells"

          76 |   for (let i = 0; i < 3; i++) {
          77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
        > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
             |             ^
          79 |     }
          80 |   }
          81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at actual (state-of-tic-tac-toe.spec.js:190:35)
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (state-of-tic-tac-toe.spec.js:191:20)
      at Object.toThrow (state-of-tic-tac-toe.spec.js:191:20)

  ● Invalid boards › Invalid board: players kept playing after a win

    expect(received).toThrow(expected)

    Expected message: "Impossible board: game should have ended after the game was won"
    Received message: "Invalid board: Each row must have 3 cells"

          76 |   for (let i = 0; i < 3; i++) {
          77 |     if (!Array.isArray(board[i]) || board[i].length !== 3) {
        > 78 |       throw new Error('Invalid board: Each row must have 3 cells');
             |             ^
          79 |     }
          80 |   }
          81 |

      at gamestate (state-of-tic-tac-toe.js:78:13)
      at actual (state-of-tic-tac-toe.spec.js:199:35)
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrow (state-of-tic-tac-toe.spec.js:200:20)
      at Object.toThrow (state-of-tic-tac-toe.spec.js:200:20)

Test Suites: 1 failed, 1 total
Tests:       27 failed, 27 total
Snapshots:   0 total
Time:        6.274 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/state-of-tic-tac-toe.js|.\/state-of-tic-tac-toe.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
