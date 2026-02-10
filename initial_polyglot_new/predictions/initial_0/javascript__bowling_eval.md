+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' bowling.spec.js
+ npm run test

> test
> jest ./*

PASS ./bowling.spec.js
  Bowling
    Check game can be scored correctly.
      ✓ should be able to score a game with all zeros (3 ms)
      ✓ should be able to score a game with no strikes or spares
      ✓ a spare followed by zeros is worth ten points
      ✓ points scored in the roll after a spare are counted twice
      ✓ consecutive spares each get a one roll bonus
      ✓ a spare in the last frame gets a one roll bonus that is counted once
      ✓ a strike earns ten points in a frame with a single roll
      ✓ points scored in the two rolls after a strike are counted twice as a bonus
      ✓ consecutive strikes each get the two roll bonus
      ✓ a strike in the last frame gets a two roll bonuses that is counted once
      ✓ rolling a spare with the two roll bonus does not get a bonus roll (1 ms)
      ✓ strikes with the two roll bonus do not get bonus rolls (10 ms)
      ✓ a strike with the one roll bonus after a spare in the last frame does not get a bonus (1 ms)
      ✓ all strikes is a perfect game (1 ms)
    Check game rules.
      ✓ rolls cannot score negative points (36 ms)
      ✓ a roll cannot score more than 10 points (1 ms)
      ✓ two rolls in a frame cannot score more than 10 points (1 ms)
      ✓ bonus roll after a strike in the last frame cannot score more than 10 points (1 ms)
      ✓ two bonus rolls after a strike in the last frame cannot score more than 10 points (1 ms)
      ✓ two bonus rolls after a strike in the last frame can score more than 10 points if one is a strike
      ✓ the second bonus rolls after a strike in the last frame cannot be a strike if the first one is not a strike
      ✓ second bonus roll after a strike in the last frame cannot score more than 10 points (1 ms)
      ✓ an unstarted game cannot be scored (1 ms)
      ✓ an incomplete game cannot be scored (1 ms)
      ✓ cannot roll if game already has ten frames (1 ms)
      ✓ bonus rolls for a strike in the last frame must be rolled before score can be calculated
      ✓ both bonus rolls for a strike in the last frame must be rolled before score can be calculated
      ✓ bonus roll for a spare in the last frame must be rolled before score can be calculated (1 ms)
      ✓ cannot roll after bonus roll for spare (1 ms)
      ✓ cannot roll after bonus rolls for strike

Test Suites: 1 passed, 1 total
Tests:       30 passed, 30 total
Snapshots:   0 total
Time:        0.883 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./bowling.js|./bowling.spec.js|./eval.sh|./node_modules|./package-lock.json|./package.json.
