+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' state-of-tic-tac-toe.spec.js
+ npm run test

> test
> jest ./*

PASS ./state-of-tic-tac-toe.spec.js
  Won games
    ✓ Finished game where X won via left column victory (3 ms)
    ✓ Finished game where X won via middle column victory (1 ms)
    ✓ Finished game where X won via right column victory (1 ms)
    ✓ Finished game where O won via left column victory (1 ms)
    ✓ Finished game where O won via middle column victory (1 ms)
    ✓ Finished game where O won via right column victory
    ✓ Finished game where X won via top row victory
    ✓ Finished game where X won via middle row victory (1 ms)
    ✓ Finished game where X won via bottom row victory (1 ms)
    ✓ Finished game where O won via top row victory (1 ms)
    ✓ Finished game where O won via middle row victory (1 ms)
    ✓ Finished game where O won via bottom row victory
    ✓ Finished game where X won via falling diagonal victory (1 ms)
    ✓ Finished game where X won via rising diagonal victory (1 ms)
    ✓ Finished game where O won via falling diagonal victory
    ✓ Finished game where O won via rising diagonal victory (1 ms)
    ✓ Finished game where X won via a row and a column victory
    ✓ Finished game where X won via two diagonal victories
  Draw games
    ✓ Draw (1 ms)
    ✓ Another draw
  Ongoing games
    ✓ Ongoing game: one move in (1 ms)
    ✓ Ongoing game: two moves in
    ✓ Ongoing game: five moves in (1 ms)
  Invalid boards
    ✓ Invalid board: X went twice (11 ms)
    ✓ Invalid board: O started (1 ms)
    ✓ Invalid board: X won and O kept playing (1 ms)
    ✓ Invalid board: players kept playing after a win (1 ms)

Test Suites: 1 passed, 1 total
Tests:       27 passed, 27 total
Snapshots:   0 total
Time:        0.728 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./state-of-tic-tac-toe.js|./state-of-tic-tac-toe.spec.js.
