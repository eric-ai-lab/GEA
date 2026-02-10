+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' react.spec.js
+ npm run test

> test
> jest ./*

FAIL ./react.spec.js
  React module
    ✓ accepts input (9 ms)
    ✓ allows input cell value to be set (4 ms)
    ✕ allows setting compute cells (1 ms)
    ✕ compute cell takes inputs in correct order
    ✕ compute cells update value when inputs are changed
    ✕ compute cells can depend on other compute cells (1 ms)
    ✕ compute cells fire callbacks
    ✕ callbacks fire only when output values change (1 ms)
    ✕ static callbacks fire even if their own value has not changed (1 ms)
    ✕ callbacks can be added and removed
    ✕ removing a callback multiple times doesn't interfere with other callbacks (1 ms)
    ✕ callbacks should only be called once, even if multiple dependencies change
    ✕ callbacks should not be called if dependencies change but output value doesn't change (1 ms)

  ● React module › allows setting compute cells

    TypeError: Cannot read properties of undefined (reading 'value')

      15 |   test('allows setting compute cells', () => {
      16 |     const inputCell = new InputCell(1);
    > 17 |     const fn = (inputCells) => inputCells[0].value + 1;
         |                                              ^
      18 |     const computeCell = new ComputeCell([inputCell], fn);
      19 |     expect(computeCell.value).toEqual(2);
      20 |   });

      at ComputeCell.value [as fn] (react.spec.js:17:46)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:18:25)

  ● React module › compute cell takes inputs in correct order

    TypeError: Cannot read properties of undefined (reading 'value')

      25 |     const computeCell = new ComputeCell(
      26 |       inputCells,
    > 27 |       (inputs) => inputs[0].value + inputs[1].value * 10,
         |                             ^
      28 |     );
      29 |
      30 |     expect(computeCell.value).toEqual(21);

      at ComputeCell.value [as fn] (react.spec.js:27:29)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:25:25)

  ● React module › compute cells update value when inputs are changed

    TypeError: Cannot read properties of undefined (reading 'value')

      35 |     const computeCell = new ComputeCell(
      36 |       [inputCell],
    > 37 |       (inputs) => inputs[0].value + 1,
         |                             ^
      38 |     );
      39 |     inputCell.setValue(3);
      40 |     expect(computeCell.value).toEqual(4);

      at ComputeCell.value [as fn] (react.spec.js:37:29)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:35:25)

  ● React module › compute cells can depend on other compute cells

    TypeError: Cannot read properties of undefined (reading 'value')

      45 |     const timesTwo = new ComputeCell(
      46 |       [inputCell],
    > 47 |       (inputs) => inputs[0].value * 2,
         |                             ^
      48 |     );
      49 |
      50 |     const timesThirty = new ComputeCell(

      at ComputeCell.value [as fn] (react.spec.js:47:29)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:45:22)

  ● React module › compute cells fire callbacks

    TypeError: Cannot read properties of undefined (reading 'value')

      68 |     const output = new ComputeCell(
      69 |       [inputCell],
    > 70 |       (inputs) => inputs[0].value + 1,
         |                             ^
      71 |     );
      72 |
      73 |     const callback = new CallbackCell((cell) => cell.value);

      at ComputeCell.value [as fn] (react.spec.js:70:29)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:68:20)

  ● React module › callbacks fire only when output values change

    TypeError: Cannot read properties of undefined (reading 'value')

      81 |     const inputCell = new InputCell(1);
      82 |     const output = new ComputeCell([inputCell], (inputs) =>
    > 83 |       inputs[0].value < 3 ? 111 : 222,
         |                 ^
      84 |     );
      85 |
      86 |     const callback = new CallbackCell((cell) => cell.value);

      at ComputeCell.value [as fn] (react.spec.js:83:17)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:82:20)

  ● React module › static callbacks fire even if their own value has not changed

    TypeError: Cannot read properties of undefined (reading 'value')

       97 |     const inputCell = new InputCell(1);
       98 |     const output = new ComputeCell([inputCell], (inputs) =>
    >  99 |       inputs[0].value < 3 ? 111 : 222,
          |                 ^
      100 |     );
      101 |
      102 |     const callback = new CallbackCell(() => 'cell changed');

      at ComputeCell.value [as fn] (react.spec.js:99:17)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:98:20)

  ● React module › callbacks can be added and removed

    TypeError: Cannot read properties of undefined (reading 'value')

      120 |     const output = new ComputeCell(
      121 |       [inputCell],
    > 122 |       (inputs) => inputs[0].value + 1,
          |                             ^
      123 |     );
      124 |
      125 |     const callback1 = new CallbackCell((cell) => cell.value);

      at ComputeCell.value [as fn] (react.spec.js:122:29)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:120:20)

  ● React module › removing a callback multiple times doesn't interfere with other callbacks

    TypeError: Cannot read properties of undefined (reading 'value')

      147 |     const output = new ComputeCell(
      148 |       [inputCell],
    > 149 |       (inputs) => inputs[0].value + 1,
          |                             ^
      150 |     );
      151 |
      152 |     const callback1 = new CallbackCell((cell) => cell.value);

      at ComputeCell.value [as fn] (react.spec.js:149:29)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:147:20)

  ● React module › callbacks should only be called once, even if multiple dependencies change

    TypeError: Cannot read properties of undefined (reading 'value')

      170 |     const plusOne = new ComputeCell(
      171 |       [inputCell],
    > 172 |       (inputs) => inputs[0].value + 1,
          |                             ^
      173 |     );
      174 |
      175 |     const minusOne1 = new ComputeCell(

      at ComputeCell.value [as fn] (react.spec.js:172:29)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:170:21)

  ● React module › callbacks should not be called if dependencies change but output value doesn't change

    TypeError: Cannot read properties of undefined (reading 'value')

      200 |     const plusOne = new ComputeCell(
      201 |       [inputCell],
    > 202 |       (inputs) => inputs[0].value + 1,
          |                             ^
      203 |     );
      204 |
      205 |     const minusOne = new ComputeCell(

      at ComputeCell.value [as fn] (react.spec.js:202:29)
      at ComputeCell.fn [as compute] (react.js:76:17)
      at new compute (react.js:61:23)
      at Object.<anonymous> (react.spec.js:200:21)

Test Suites: 1 failed, 1 total
Tests:       11 failed, 2 passed, 13 total
Snapshots:   0 total
Time:        3.128 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/package-lock.json|.\/package.json|.\/react.js|.\/react.spec.js/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
