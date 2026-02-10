+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' bowling.spec.js
+ npm run test

> test
> jest ./*

FAIL ./bowling.spec.js (5.404 s)
  Bowling
    Check game can be scored correctly.
      ✓ should be able to score a game with all zeros (30 ms)
      ✓ should be able to score a game with no strikes or spares (20 ms)
      ✓ a spare followed by zeros is worth ten points
      ✓ points scored in the roll after a spare are counted twice (1 ms)
      ✓ consecutive spares each get a one roll bonus
      ✓ a spare in the last frame gets a one roll bonus that is counted once (8 ms)
      ✓ a strike earns ten points in a frame with a single roll (1 ms)
      ✓ points scored in the two rolls after a strike are counted twice as a bonus
      ✓ consecutive strikes each get the two roll bonus (1 ms)
      ✓ a strike in the last frame gets a two roll bonuses that is counted once (7 ms)
      ✓ rolling a spare with the two roll bonus does not get a bonus roll (1 ms)
      ✓ strikes with the two roll bonus do not get bonus rolls
      ✓ a strike with the one roll bonus after a spare in the last frame does not get a bonus (1 ms)
      ✓ all strikes is a perfect game (11 ms)
    Check game rules.
      ✕ rolls cannot score negative points (14 ms)
      ✕ a roll cannot score more than 10 points (1 ms)
      ✕ two rolls in a frame cannot score more than 10 points (1 ms)
      ✕ bonus roll after a strike in the last frame cannot score more than 10 points (15 ms)
      ✕ two bonus rolls after a strike in the last frame cannot score more than 10 points (4 ms)
      ✓ two bonus rolls after a strike in the last frame can score more than 10 points if one is a strike (11 ms)
      ✕ the second bonus rolls after a strike in the last frame cannot be a strike if the first one is not a strike
      ✕ second bonus roll after a strike in the last frame cannot score more than 10 points (4 ms)
      ✕ an unstarted game cannot be scored (21 ms)
      ✕ an incomplete game cannot be scored (26 ms)
      ✕ cannot roll if game already has ten frames (4 ms)
      ✕ bonus rolls for a strike in the last frame must be rolled before score can be calculated (19 ms)
      ✕ both bonus rolls for a strike in the last frame must be rolled before score can be calculated (3 ms)
      ✕ bonus roll for a spare in the last frame must be rolled before score can be calculated (1 ms)
      ✕ cannot roll after bonus roll for spare (1 ms)
      ✕ cannot roll after bonus rolls for strike (1 ms)

  ● Bowling › Check game rules. › rolls cannot score negative points

    expect(received).toThrow(expected)

    Expected message: "Negative roll is invalid"

    Received function did not throw

      155 |       expect(() => {
      156 |         bowling.roll(-1);
    > 157 |       }).toThrow(new Error('Negative roll is invalid'));
          |          ^
      158 |     });
      159 |
      160 |     test('a roll cannot score more than 10 points', () => {

      at Object.toThrow (bowling.spec.js:157:10)

  ● Bowling › Check game rules. › a roll cannot score more than 10 points

    expect(received).toThrow(expected)

    Expected message: "Pin count exceeds pins on the lane"

    Received function did not throw

      162 |       expect(() => {
      163 |         bowling.roll(11);
    > 164 |       }).toThrow(new Error('Pin count exceeds pins on the lane'));
          |          ^
      165 |     });
      166 |
      167 |     test('two rolls in a frame cannot score more than 10 points', () => {

      at Object.toThrow (bowling.spec.js:164:10)

  ● Bowling › Check game rules. › two rolls in a frame cannot score more than 10 points

    expect(received).toThrow(expected)

    Expected message: "Pin count exceeds pins on the lane"

    Received function did not throw

      170 |       expect(() => {
      171 |         bowling.roll(6);
    > 172 |       }).toThrow(new Error('Pin count exceeds pins on the lane'));
          |          ^
      173 |     });
      174 |
      175 |     test('bonus roll after a strike in the last frame cannot score more than 10 points', () => {

      at Object.toThrow (bowling.spec.js:172:10)

  ● Bowling › Check game rules. › bonus roll after a strike in the last frame cannot score more than 10 points

    expect(received).toThrow(expected)

    Expected message: "Pin count exceeds pins on the lane"

    Received function did not throw

      181 |       expect(() => {
      182 |         bowling.roll(11);
    > 183 |       }).toThrow(new Error('Pin count exceeds pins on the lane'));
          |          ^
      184 |     });
      185 |
      186 |     test('two bonus rolls after a strike in the last frame cannot score more than 10 points', () => {

      at Object.toThrow (bowling.spec.js:183:10)

  ● Bowling › Check game rules. › two bonus rolls after a strike in the last frame cannot score more than 10 points

    expect(received).toThrow(expected)

    Expected message: "Pin count exceeds pins on the lane"

    Received function did not throw

      194 |       expect(() => {
      195 |         bowling.roll(6);
    > 196 |       }).toThrow(new Error('Pin count exceeds pins on the lane'));
          |          ^
      197 |     });
      198 |
      199 |     test('two bonus rolls after a strike in the last frame can score more than 10 points if one is a strike', () => {

      at Object.toThrow (bowling.spec.js:196:10)

  ● Bowling › Check game rules. › the second bonus rolls after a strike in the last frame cannot be a strike if the first one is not a strike

    expect(received).toThrow(expected)

    Expected message: "Pin count exceeds pins on the lane"

    Received function did not throw

      218 |       expect(() => {
      219 |         bowling.roll(10);
    > 220 |       }).toThrow(new Error('Pin count exceeds pins on the lane'));
          |          ^
      221 |     });
      222 |
      223 |     test('second bonus roll after a strike in the last frame cannot score more than 10 points', () => {

      at Object.toThrow (bowling.spec.js:220:10)

  ● Bowling › Check game rules. › second bonus roll after a strike in the last frame cannot score more than 10 points

    expect(received).toThrow(expected)

    Expected message: "Pin count exceeds pins on the lane"

    Received function did not throw

      231 |       expect(() => {
      232 |         bowling.roll(11);
    > 233 |       }).toThrow(new Error('Pin count exceeds pins on the lane'));
          |          ^
      234 |     });
      235 |
      236 |     test('an unstarted game cannot be scored', () => {

      at Object.toThrow (bowling.spec.js:233:10)

  ● Bowling › Check game rules. › an unstarted game cannot be scored

    expect(received).toThrow(expected)

    Expected message: "Score cannot be taken until the end of the game"

    Received function did not throw

      238 |       expect(() => {
      239 |         bowling.score();
    > 240 |       }).toThrow(new Error('Score cannot be taken until the end of the game'));
          |          ^
      241 |     });
      242 |
      243 |     test('an incomplete game cannot be scored', () => {

      at Object.toThrow (bowling.spec.js:240:10)

  ● Bowling › Check game rules. › an incomplete game cannot be scored

    expect(received).toThrow(expected)

    Expected message: "Score cannot be taken until the end of the game"

    Received function did not throw

      249 |       expect(() => {
      250 |         bowling.score();
    > 251 |       }).toThrow(new Error('Score cannot be taken until the end of the game'));
          |          ^
      252 |     });
      253 |
      254 |     test('cannot roll if game already has ten frames', () => {

      at Object.toThrow (bowling.spec.js:251:10)

  ● Bowling › Check game rules. › cannot roll if game already has ten frames

    expect(received).toThrow(expected)

    Expected message: "Cannot roll after game is over"

    Received function did not throw

      262 |       expect(() => {
      263 |         bowling.roll(0);
    > 264 |       }).toThrow(new Error('Cannot roll after game is over'));
          |          ^
      265 |     });
      266 |
      267 |     test('bonus rolls for a strike in the last frame must be rolled before score can be calculated', () => {

      at Object.toThrow (bowling.spec.js:264:10)

  ● Bowling › Check game rules. › bonus rolls for a strike in the last frame must be rolled before score can be calculated

    expect(received).toThrow(expected)

    Expected message: "Score cannot be taken until the end of the game"

    Received function did not throw

      273 |       expect(() => {
      274 |         bowling.score();
    > 275 |       }).toThrow(new Error('Score cannot be taken until the end of the game'));
          |          ^
      276 |     });
      277 |
      278 |     test('both bonus rolls for a strike in the last frame must be rolled before score can be calculated', () => {

      at Object.toThrow (bowling.spec.js:275:10)

  ● Bowling › Check game rules. › both bonus rolls for a strike in the last frame must be rolled before score can be calculated

    expect(received).toThrow(expected)

    Expected message: "Score cannot be taken until the end of the game"

    Received function did not throw

      286 |       expect(() => {
      287 |         bowling.score();
    > 288 |       }).toThrow(new Error('Score cannot be taken until the end of the game'));
          |          ^
      289 |     });
      290 |
      291 |     test('bonus roll for a spare in the last frame must be rolled before score can be calculated', () => {

      at Object.toThrow (bowling.spec.js:288:10)

  ● Bowling › Check game rules. › bonus roll for a spare in the last frame must be rolled before score can be calculated

    expect(received).toThrow(expected)

    Expected message: "Score cannot be taken until the end of the game"

    Received function did not throw

      299 |       expect(() => {
      300 |         bowling.score();
    > 301 |       }).toThrow(new Error('Score cannot be taken until the end of the game'));
          |          ^
      302 |     });
      303 |
      304 |     test('cannot roll after bonus roll for spare', () => {

      at Object.toThrow (bowling.spec.js:301:10)

  ● Bowling › Check game rules. › cannot roll after bonus roll for spare

    expect(received).toThrow(expected)

    Expected message: "Cannot roll after game is over"

    Received function did not throw

      312 |       expect(() => {
      313 |         bowling.roll(2);
    > 314 |       }).toThrow(new Error('Cannot roll after game is over'));
          |          ^
      315 |     });
      316 |
      317 |     test('cannot roll after bonus rolls for strike', () => {

      at Object.toThrow (bowling.spec.js:314:10)

  ● Bowling › Check game rules. › cannot roll after bonus rolls for strike

    expect(received).toThrow(expected)

    Expected message: "Cannot roll after game is over"

    Received function did not throw

      325 |       expect(() => {
      326 |         bowling.roll(2);
    > 327 |       }).toThrow(new Error('Cannot roll after game is over'));
          |          ^
      328 |     });
      329 |   });
      330 | });

      at Object.toThrow (bowling.spec.js:327:10)

Test Suites: 1 failed, 1 total
Tests:       15 failed, 15 passed, 30 total
Snapshots:   0 total
Time:        5.622 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/bowling.js|.\/bowling.spec.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
