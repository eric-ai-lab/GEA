+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' affine-cipher.spec.js
+ npm run test

> test
> jest ./*

FAIL ./affine-cipher.spec.js
  Affine cipher
    encode
      ✓ encode yes (3 ms)
      ✓ encode no
      ✓ encode OMG
      ✓ encode O M G (1 ms)
      ✓ encode mindblowingly (1 ms)
      ✓ encode numbers
      ✓ encode deep thought
      ✓ encode all the letters (1 ms)
      ✕ encode with a not coprime to m (1 ms)
    decode
      ✓ decode exercism (1 ms)
      ✓ decode a sentence (1 ms)
      ✓ decode numbers
      ✓ decode all the letters
      ✓ decode with no spaces in input (1 ms)
      ✓ decode with too many spaces
      ✕ decode with a not coprime to m

  ● Affine cipher › encode › encode with a not coprime to m

    TypeError: expect(...).toThrowError is not a function

      47 |       expect(() => {
      48 |         encode('This is a test.', { a: 6, b: 17 });
    > 49 |       }).toThrowError('a and m must be coprime.');
         |          ^
      50 |     });
      51 |   });
      52 |   describe('decode', () => {

      at Object.toThrowError (affine-cipher.spec.js:49:10)

  ● Affine cipher › decode › decode with a not coprime to m

    TypeError: expect(...).toThrowError is not a function

      88 |       expect(() => {
      89 |         decode('Test', { a: 13, b: 5 });
    > 90 |       }).toThrowError('a and m must be coprime.');
         |          ^
      91 |     });
      92 |   });
      93 | });

      at Object.toThrowError (affine-cipher.spec.js:90:10)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 14 passed, 16 total
Snapshots:   0 total
Time:        0.735 s
Ran all test suites matching ./LICENSE|./affine-cipher.js|./affine-cipher.spec.js|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json.
