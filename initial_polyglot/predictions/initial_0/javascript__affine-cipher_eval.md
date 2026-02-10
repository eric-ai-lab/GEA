+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' affine-cipher.spec.js
+ npm run test

> test
> jest ./*

FAIL ./affine-cipher.spec.js (5.034 s)
  Affine cipher
    encode
      ✓ encode yes (27 ms)
      ✓ encode no (6 ms)
      ✓ encode OMG (1 ms)
      ✓ encode O M G
      ✓ encode mindblowingly (1 ms)
      ✓ encode numbers (1 ms)
      ✓ encode deep thought (3 ms)
      ✓ encode all the letters
      ✕ encode with a not coprime to m (199 ms)
    decode
      ✓ decode exercism (1 ms)
      ✓ decode a sentence
      ✓ decode numbers
      ✓ decode all the letters (1 ms)
      ✓ decode with no spaces in input
      ✓ decode with too many spaces
      ✕ decode with a not coprime to m (3 ms)

  ● Affine cipher › encode › encode with a not coprime to m

    expect(received).toThrowError(expected)

    Expected substring: "a and m must be coprime."
    Received message:   "Error: a and 26 are not coprime"

          38 |   const { a, b } = key;
          39 |   if (gcd(a, ALPHABET_SIZE) !== 1) {
        > 40 |     throw new Error('Error: a and 26 are not coprime');
             |           ^
          41 |   }
          42 |
          43 |   const sanitized = sanitize(phrase);

      at encode (affine-cipher.js:40:11)
      at affine-cipher.spec.js:48:15
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrowError] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrowError (affine-cipher.spec.js:49:10)
      at Object.toThrowError (affine-cipher.spec.js:49:10)

  ● Affine cipher › decode › decode with a not coprime to m

    expect(received).toThrowError(expected)

    Expected substring: "a and m must be coprime."
    Received message:   "Error: a and 26 are not coprime"

          63 |   const { a, b } = key;
          64 |   if (gcd(a, ALPHABET_SIZE) !== 1) {
        > 65 |     throw new Error('Error: a and 26 are not coprime');
             |           ^
          66 |   }
          67 |   
          68 |   // Get modular multiplicative inverse of a modulo ALPHABET_SIZE

      at decode (affine-cipher.js:65:11)
      at affine-cipher.spec.js:89:15
      at Object.<anonymous> (../npm-install/node_modules/expect/build/toThrowMatchers.js:74:11)
      at Object.throwingMatcher [as toThrowError] (../npm-install/node_modules/expect/build/index.js:320:21)
      at Object.toThrowError (affine-cipher.spec.js:90:10)
      at Object.toThrowError (affine-cipher.spec.js:90:10)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 14 passed, 16 total
Snapshots:   0 total
Time:        5.241 s
Ran all test suites matching /.\/LICENSE|.\/affine-cipher.js|.\/affine-cipher.spec.js|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
