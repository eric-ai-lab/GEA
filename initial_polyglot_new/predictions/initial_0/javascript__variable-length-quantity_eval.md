+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' variable-length-quantity.spec.js
+ npm run test

> test
> jest ./*

PASS ./variable-length-quantity.spec.js
  VariableLengthQuantity
    Encode a series of integers, producing a series of bytes.
      ✓ zero (3 ms)
      ✓ arbitrary single byte (1 ms)
      ✓ largest single byte (1 ms)
      ✓ smallest double byte (1 ms)
      ✓ arbitrary double byte
      ✓ largest double byte
      ✓ smallest triple byte
      ✓ arbitrary triple byte (1 ms)
      ✓ largest triple byte (1 ms)
      ✓ smallest quadruple byte (1 ms)
      ✓ arbitrary quadruple byte (1 ms)
      ✓ largest quadruple byte (1 ms)
      ✓ smallest quintuple byte
      ✓ arbitrary quintuple byte
      ✓ maximum 32-bit integer input (1 ms)
      ✓ two single-byte values (1 ms)
      ✓ two multi-byte values
      ✓ many multi-byte values (1 ms)
    Decode a series of bytes, producing a series of integers.
      ✓ one byte (1 ms)
      ✓ two bytes
      ✓ three bytes (1 ms)
      ✓ four bytes
      ✓ maximum 32-bit integer (1 ms)
      ✓ incomplete sequence causes error (70 ms)
      ✓ incomplete sequence causes error, even if value is zero
      ✓ multiple values

Test Suites: 1 passed, 1 total
Tests:       26 passed, 26 total
Snapshots:   0 total
Time:        0.786 s, estimated 1 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./node_modules|./package-lock.json|./package.json|./variable-length-quantity.js|./variable-length-quantity.spec.js.
