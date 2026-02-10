+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' scale-generator.spec.js
+ npm run test

> test
> jest ./*

PASS ./scale-generator.spec.js
  ScaleGenerator
    Chromatic scales
      ✓ Chromatic scale with sharps (3 ms)
      ✓ Chromatic scale with flats (1 ms)
      ✓ Chromatic scale with sharps from D (1 ms)
      ✓ Chromatic scale with flats from D (1 ms)
    Scales with specified intervals
      ✓ Simple major scale (1 ms)
      ✓ Major scale with sharps (1 ms)
      ✓ Major scale with flats (1 ms)
      ✓ Minor scale with sharps (1 ms)
      ✓ Minor scale with flats (1 ms)
      ✓ Dorian mode (1 ms)
      ✓ Phrygian mode (1 ms)
      ✓ Lydian mode (1 ms)
      ✓ Mixolydian mode (1 ms)
      ✓ Locrian mode (1 ms)
      ✓ Harmonic minor (1 ms)
      ✓ Octatonic (1 ms)
      ✓ Hexatonic (1 ms)
      ✓ Pentatonic (1 ms)
      ✓ Enigmatic

Test Suites: 1 passed, 1 total
Tests:       19 passed, 19 total
Snapshots:   0 total
Time:        0.746 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./scale-generator.js|./scale-generator.spec.js.
