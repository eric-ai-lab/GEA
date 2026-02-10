+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' forth.spec.js
+ npm run test

> test
> jest ./*

FAIL ./forth.spec.js
  Forth
    parsing and numbers
      ✓ numbers just get pushed onto the stack (4 ms)
      ✓ pushes negative numbers onto the stack (1 ms)
    addition
      ✓ can add two numbers (1 ms)
      ✕ errors if there is nothing on the stack (30 ms)
      ✕ errors if there is only one value on the stack (8 ms)
    subtraction
      ✓ can subtract two numbers (1 ms)
      ✕ errors if there is nothing on the stack (3 ms)
      ✕ errors if there is only one value on the stack (3 ms)
    multiplication
      ✓ can multiply two numbers (2 ms)
      ✕ errors if there is nothing on the stack (3 ms)
      ✕ errors if there is only one value on the stack (3 ms)
    division
      ✓ can divide two numbers (2 ms)
      ✓ performs integer division (1 ms)
      ✓ errors if dividing by zero (2 ms)
      ✕ errors if there is nothing on the stack (14 ms)
      ✕ errors if there is only one value on the stack (2 ms)
    combined arithmetic
      ✓ addition and subtraction (1 ms)
      ✓ multiplication and division (1 ms)
    dup
      ✓ copies a value on the stack
      ✓ copies the top value on the stack (1 ms)
      ✕ errors if there is nothing on the stack (2 ms)
    drop
      ✓ removes the top value on the stack if it is the only one (1 ms)
      ✓ removes the top value on the stack if it is not the only one
      ✕ errors if there is nothing on the stack (2 ms)
    swap
      ✓ swaps the top two values on the stack if they are the only ones
      ✓ swaps the top two values on the stack if they are not the only ones (1 ms)
      ✕ errors if there is nothing on the stack (1 ms)
      ✕ errors if there is only one value on the stack (1 ms)
    over
      ✓ copies the second element if there are only two
      ✓ copies the second element if there are more than two (1 ms)
      ✕ errors if there is nothing on the stack (1 ms)
      ✕ errors if there is only one value on the stack (1 ms)
    user-defined words
      ✓ can consist of built-in words
      ✓ execute in the right order
      ✓ can override other user-defined words
      ✕ can override built-in words
      ✕ can override built-in operators (2 ms)
      ✕ can use different words with the same name (1 ms)
      ✕ can define word that uses word with the same name (11 ms)
      ✕ cannot redefine numbers (2 ms)
      ✕ cannot redefine negative numbers (1 ms)
      ✕ errors if executing a non-existent word (1 ms)
      ✕ only defines locally (1 ms)
    case-insensitivity
      ✓ DUP is case-insensitive (1 ms)
      ✓ DROP is case-insensitive
      ✓ SWAP is case-insensitive
      ✓ OVER is case-insensitive (1 ms)
      ✓ user-defined words are case-insensitive
      ✕ definitions are case-insensitive

  ● Forth › addition › errors if there is nothing on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for +"

          154 |   _performAddition() {
          155 |     if (this._stack.length < 2) {
        > 156 |       throw new Error('Not enough values on the stack for +');
              |             ^
          157 |     }
          158 |     const b = this._stack.pop();
          159 |     const a = this._stack.pop();

      at Forth._performAddition (forth.js:156:13)
      at Forth._performAddition [as _executeBuiltInWord] (forth.js:126:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:30:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:31:10)
      at Object.toThrow (forth.spec.js:31:10)

  ● Forth › addition › errors if there is only one value on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for +"

          154 |   _performAddition() {
          155 |     if (this._stack.length < 2) {
        > 156 |       throw new Error('Not enough values on the stack for +');
              |             ^
          157 |     }
          158 |     const b = this._stack.pop();
          159 |     const a = this._stack.pop();

      at Forth._performAddition (forth.js:156:13)
      at Forth._performAddition [as _executeBuiltInWord] (forth.js:126:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:36:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:37:10)
      at Object.toThrow (forth.spec.js:37:10)

  ● Forth › subtraction › errors if there is nothing on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for -"

          163 |   _performSubtraction() {
          164 |     if (this._stack.length < 2) {
        > 165 |       throw new Error('Not enough values on the stack for -');
              |             ^
          166 |     }
          167 |     const b = this._stack.pop();
          168 |     const a = this._stack.pop();

      at Forth._performSubtraction (forth.js:165:13)
      at Forth._performSubtraction (forth.js:129:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:49:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:50:10)
      at Object.toThrow (forth.spec.js:50:10)

  ● Forth › subtraction › errors if there is only one value on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for -"

          163 |   _performSubtraction() {
          164 |     if (this._stack.length < 2) {
        > 165 |       throw new Error('Not enough values on the stack for -');
              |             ^
          166 |     }
          167 |     const b = this._stack.pop();
          168 |     const a = this._stack.pop();

      at Forth._performSubtraction (forth.js:165:13)
      at Forth._performSubtraction (forth.js:129:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:55:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:56:10)
      at Object.toThrow (forth.spec.js:56:10)

  ● Forth › multiplication › errors if there is nothing on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for *"

          172 |   _performMultiplication() {
          173 |     if (this._stack.length < 2) {
        > 174 |       throw new Error('Not enough values on the stack for *');
              |             ^
          175 |     }
          176 |     const b = this._stack.pop();
          177 |     const a = this._stack.pop();

      at Forth._performMultiplication (forth.js:174:13)
      at Forth._performMultiplication [as _executeBuiltInWord] (forth.js:132:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:68:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:69:10)
      at Object.toThrow (forth.spec.js:69:10)

  ● Forth › multiplication › errors if there is only one value on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for *"

          172 |   _performMultiplication() {
          173 |     if (this._stack.length < 2) {
        > 174 |       throw new Error('Not enough values on the stack for *');
              |             ^
          175 |     }
          176 |     const b = this._stack.pop();
          177 |     const a = this._stack.pop();

      at Forth._performMultiplication (forth.js:174:13)
      at Forth._performMultiplication [as _executeBuiltInWord] (forth.js:132:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:74:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:75:10)
      at Object.toThrow (forth.spec.js:75:10)

  ● Forth › division › errors if there is nothing on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for /"

          181 |   _performDivision() {
          182 |     if (this._stack.length < 2) {
        > 183 |       throw new Error('Not enough values on the stack for /');
              |             ^
          184 |     }
          185 |     const b = this._stack.pop();
          186 |     const a = this._stack.pop();

      at Forth._performDivision (forth.js:183:13)
      at Forth._performDivision [as _executeBuiltInWord] (forth.js:135:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:98:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:99:10)
      at Object.toThrow (forth.spec.js:99:10)

  ● Forth › division › errors if there is only one value on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for /"

          181 |   _performDivision() {
          182 |     if (this._stack.length < 2) {
        > 183 |       throw new Error('Not enough values on the stack for /');
              |             ^
          184 |     }
          185 |     const b = this._stack.pop();
          186 |     const a = this._stack.pop();

      at Forth._performDivision (forth.js:183:13)
      at Forth._performDivision [as _executeBuiltInWord] (forth.js:135:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:104:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:105:10)
      at Object.toThrow (forth.spec.js:105:10)

  ● Forth › dup › errors if there is nothing on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for DUP"

          194 |   _dup() {
          195 |     if (this._stack.length < 1) {
        > 196 |       throw new Error('Not enough values on the stack for DUP');
              |             ^
          197 |     }
          198 |     const value = this._stack[this._stack.length - 1];
          199 |     this._stack.push(value);

      at Forth._dup (forth.js:196:13)
      at Forth._dup [as _executeBuiltInWord] (forth.js:138:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:134:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:135:10)
      at Object.toThrow (forth.spec.js:135:10)

  ● Forth › drop › errors if there is nothing on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for DROP"

          202 |   _drop() {
          203 |     if (this._stack.length < 1) {
        > 204 |       throw new Error('Not enough values on the stack for DROP');
              |             ^
          205 |     }
          206 |     this._stack.pop();
          207 |   }

      at Forth._drop (forth.js:204:13)
      at Forth._drop [as _executeBuiltInWord] (forth.js:141:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:152:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:153:10)
      at Object.toThrow (forth.spec.js:153:10)

  ● Forth › swap › errors if there is nothing on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for SWAP"

          209 |   _swap() {
          210 |     if (this._stack.length < 2) {
        > 211 |       throw new Error('Not enough values on the stack for SWAP');
              |             ^
          212 |     }
          213 |     const length = this._stack.length;
          214 |     const temp = this._stack[length - 1];

      at Forth._swap (forth.js:211:13)
      at Forth._swap [as _executeBuiltInWord] (forth.js:144:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:170:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:171:10)
      at Object.toThrow (forth.spec.js:171:10)

  ● Forth › swap › errors if there is only one value on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for SWAP"

          209 |   _swap() {
          210 |     if (this._stack.length < 2) {
        > 211 |       throw new Error('Not enough values on the stack for SWAP');
              |             ^
          212 |     }
          213 |     const length = this._stack.length;
          214 |     const temp = this._stack[length - 1];

      at Forth._swap (forth.js:211:13)
      at Forth._swap [as _executeBuiltInWord] (forth.js:144:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:176:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:177:10)
      at Object.toThrow (forth.spec.js:177:10)

  ● Forth › over › errors if there is nothing on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for OVER"

          219 |   _over() {
          220 |     if (this._stack.length < 2) {
        > 221 |       throw new Error('Not enough values on the stack for OVER');
              |             ^
          222 |     }
          223 |     const length = this._stack.length;
          224 |     this._stack.push(this._stack[length - 2]);

      at Forth._over (forth.js:221:13)
      at Forth._over [as _executeBuiltInWord] (forth.js:147:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:194:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:195:10)
      at Object.toThrow (forth.spec.js:195:10)

  ● Forth › over › errors if there is only one value on the stack

    expect(received).toThrow(expected)

    Expected message: "Stack empty"
    Received message: "Not enough values on the stack for OVER"

          219 |   _over() {
          220 |     if (this._stack.length < 2) {
        > 221 |       throw new Error('Not enough values on the stack for OVER');
              |             ^
          222 |     }
          223 |     const length = this._stack.length;
          224 |     this._stack.push(this._stack[length - 2]);

      at Forth._over (forth.js:221:13)
      at Forth._over [as _executeBuiltInWord] (forth.js:147:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:200:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:201:10)
      at Object.toThrow (forth.spec.js:201:10)

  ● Forth › user-defined words › can override built-in words

    Not enough values on the stack for SWAP

      209 |   _swap() {
      210 |     if (this._stack.length < 2) {
    > 211 |       throw new Error('Not enough values on the stack for SWAP');
          |             ^
      212 |     }
      213 |     const length = this._stack.length;
      214 |     const temp = this._stack[length - 1];

      at Forth._swap (forth.js:211:13)
      at Forth._swap [as _executeBuiltInWord] (forth.js:144:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at Object.evaluate (forth.spec.js:227:13)

  ● Forth › user-defined words › can override built-in operators

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      Array [
    -   12,
    +   7,
      ]

      232 |       forth.evaluate(': + * ;');
      233 |       forth.evaluate('3 4 +');
    > 234 |       expect(forth.stack).toEqual([12]);
          |                           ^
      235 |     });
      236 |
      237 |     test('can use different words with the same name', () => {

      at Object.toEqual (forth.spec.js:234:27)

  ● Forth › user-defined words › can use different words with the same name

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      Array [
    -   5,
    +   6,
        6,
      ]

      240 |       forth.evaluate(': foo 6 ;');
      241 |       forth.evaluate('bar foo');
    > 242 |       expect(forth.stack).toEqual([5, 6]);
          |                           ^
      243 |     });
      244 |
      245 |     test('can define word that uses word with the same name', () => {

      at Object.toEqual (forth.spec.js:242:27)

  ● Forth › user-defined words › can define word that uses word with the same name

    RangeError: Maximum call stack size exceeded

      106 |           this._executeBuiltInWord(word);
      107 |           i++;
    > 108 |         } else if (Object.prototype.hasOwnProperty.call(this._dictionary, word)) {
          |                ^
      109 |           // Execute custom word
      110 |           this._processTokens(this._dictionary[word]);
      111 |           i++;

      at Forth._processTokens (forth.js:108:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)
      at Forth._processTokens (forth.js:110:16)

  ● Forth › user-defined words › cannot redefine numbers

    expect(received).toThrow(expected)

    Expected message: "Invalid definition"
    Received message: "Invalid word definition"

          80 |           i++;
          81 |           if (i >= tokens.length || tokens[i].type !== 'word') {
        > 82 |             throw new Error('Invalid word definition');
             |                   ^
          83 |           }
          84 |           
          85 |           const wordName = tokens[i].value.toUpperCase();

      at Forth._processTokens (forth.js:82:19)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:254:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:255:10)
      at Object.toThrow (forth.spec.js:255:10)

  ● Forth › user-defined words › cannot redefine negative numbers

    expect(received).toThrow(expected)

    Expected message: "Invalid definition"
    Received message: "Invalid word definition"

          80 |           i++;
          81 |           if (i >= tokens.length || tokens[i].type !== 'word') {
        > 82 |             throw new Error('Invalid word definition');
             |                   ^
          83 |           }
          84 |           
          85 |           const wordName = tokens[i].value.toUpperCase();

      at Forth._processTokens (forth.js:82:19)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:259:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:260:10)
      at Object.toThrow (forth.spec.js:260:10)

  ● Forth › user-defined words › errors if executing a non-existent word

    expect(received).toThrow(expected)

    Expected message: "Unknown command"
    Received message: "Unknown word: foo"

          111 |           i++;
          112 |         } else {
        > 113 |           throw new Error(`Unknown word: ${token.value}`);
              |                 ^
          114 |         }
          115 |       }
          116 |     }

      at Forth._processTokens (forth.js:113:17)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at evaluate (forth.spec.js:265:15)
      at Object.<anonymous> (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:1824:9)
      at Object.throwingMatcher [as toThrow] (../npm-install/node_modules/@jest/expect/node_modules/expect/build/index.js:2235:93)
      at Object.toThrow (forth.spec.js:266:10)
      at Object.toThrow (forth.spec.js:266:10)

  ● Forth › user-defined words › only defines locally

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      Array [
    -   0,
    +   2,
      ]

      273 |       first.evaluate('1 1 +');
      274 |       second.evaluate('1 1 +');
    > 275 |       expect(first.stack).toEqual([0]);
          |                           ^
      276 |       expect(second.stack).toEqual([2]);
      277 |     });
      278 |   });

      at Object.toEqual (forth.spec.js:275:27)

  ● Forth › case-insensitivity › definitions are case-insensitive

    Not enough values on the stack for SWAP

      209 |   _swap() {
      210 |     if (this._stack.length < 2) {
    > 211 |       throw new Error('Not enough values on the stack for SWAP');
          |             ^
      212 |     }
      213 |     const length = this._stack.length;
      214 |     const temp = this._stack[length - 1];

      at Forth._swap (forth.js:211:13)
      at Forth._swap [as _executeBuiltInWord] (forth.js:144:14)
      at Forth._executeBuiltInWord [as _processTokens] (forth.js:106:16)
      at Forth._processTokens [as evaluate] (forth.js:21:10)
      at Object.evaluate (forth.spec.js:309:13)

Test Suites: 1 failed, 1 total
Tests:       23 failed, 26 passed, 49 total
Snapshots:   0 total
Time:        0.924 s
Ran all test suites matching ./LICENSE|./babel.config.js|./eval.sh|./forth.js|./forth.spec.js|./node_modules|./package-lock.json|./package.json.
