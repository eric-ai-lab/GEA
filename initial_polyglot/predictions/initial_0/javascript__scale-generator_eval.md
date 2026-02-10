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
      ✓ Chromatic scale with sharps (10 ms)
      ✓ Chromatic scale with flats (4 ms)
      ✓ Chromatic scale with sharps from D
      ✓ Chromatic scale with flats from D (1 ms)
    Scales with specified intervals
      ✓ Simple major scale (1 ms)
      ✓ Major scale with sharps (1 ms)
      ✓ Major scale with flats (1 ms)
      ✓ Minor scale with sharps
      ✓ Minor scale with flats
      ✓ Dorian mode (1 ms)
      ✓ Phrygian mode (1 ms)
      ✓ Lydian mode (2 ms)
      ✓ Mixolydian mode
      ✓ Locrian mode (4 ms)
      ✓ Harmonic minor (13 ms)
      ✓ Octatonic (1 ms)
      ✓ Hexatonic (1 ms)
      ✓ Pentatonic
      ✓ Enigmatic (1 ms)

Test Suites: 1 passed, 1 total
Tests:       19 passed, 19 total
Snapshots:   0 total
Time:        4.311 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/scale-generator.js|.\/scale-generator.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
