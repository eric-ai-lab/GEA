+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' ocr-numbers.spec.js
+ npm run test

> test
> jest ./*

FAIL ./ocr-numbers.spec.js
  ● Test suite failed to run

    Jest encountered an unexpected token

    Jest failed to parse a file. This happens e.g. when your code or its dependencies use non-standard JavaScript syntax, or when Jest is not configured to support such syntax.

    Out of the box Jest supports Babel, which will be used to transform your files into valid JS based on your Babel configuration.

    By default "node_modules" folder is ignored by transformers.

    Here's what you can do:
     • If you are trying to use ECMAScript Modules, see https://jestjs.io/docs/ecmascript-modules for how to enable it.
     • If you are trying to use TypeScript, see https://jestjs.io/docs/getting-started#using-typescript
     • To have some of your "node_modules" files transformed, you can specify a custom "transformIgnorePatterns" in your config.
     • If you need a custom transformation specify a "transform" option in your config.
     • If you simply want to mock your non-JS modules (e.g. binary assets) you can stub them out with the "moduleNameMapper" config option.

    You'll find more details and examples of these config options in the docs:
    https://jestjs.io/docs/configuration
    For information about custom transformations, see:
    https://jestjs.io/docs/code-transformation

    Details:

    SyntaxError: /testbed/ocr-numbers.js: Unexpected token (66:10)

      64 |   // A helper mapping from the digit's 4-line string (concatenated) to the corresponding numeral
      65 |   const DIGITS = {
    > 66 |     ' _ ' + '| |' + '|_|' + '   ': '0',
         |           ^
      67 |     '   ' + '  |' + '  |' + '   ': '1',
      68 |     ' _ ' + ' _|' + '|_ ' + '   ': '2',
      69 |     ' _ ' + ' _|' + ' _|' + '   ': '3',

    > 1 | import { convert } from './ocr-numbers';
        | ^
      2 |
      3 | describe('ocr', () => {
      4 |   test('recognizes zero', () => {

      at constructor (../npm-install/node_modules/@babel/parser/src/parse-error.ts:95:45)
      at Parser.toParseError [as raise] (../npm-install/node_modules/@babel/parser/src/tokenizer/index.ts:1497:19)
      at Parser.raise [as unexpected] (../npm-install/node_modules/@babel/parser/src/tokenizer/index.ts:1537:16)
      at Parser.unexpected [as parseObjPropValue] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:2335:21)
      at Parser.parseObjPropValue [as parsePropertyDefinition] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:2175:17)
      at Parser.parsePropertyDefinition [as parseObjectLike] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:2042:21)
      at Parser.parseObjectLike [as parseExprAtom] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:1155:21)
      at Parser.parseExprAtom [as parseExprSubscripts] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:710:23)
      at Parser.parseExprSubscripts [as parseUpdate] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:689:21)
      at Parser.parseUpdate [as parseMaybeUnary] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:651:23)
      at Parser.parseMaybeUnary [as parseMaybeUnaryOrPrivate] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:385:14)
      at Parser.parseMaybeUnaryOrPrivate [as parseExprOps] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:397:23)
      at Parser.parseExprOps [as parseMaybeConditional] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:352:23)
      at Parser.parseMaybeConditional [as parseMaybeAssign] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:294:21)
      at parseMaybeAssign (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:252:12)
      at Parser.callback [as allowInAnd] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:3111:16)
      at Parser.allowInAnd [as parseMaybeAssignAllowIn] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:251:17)
      at Parser.parseMaybeAssignAllowIn [as parseVar] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1546:18)
      at Parser.parseVar [as parseVarStatement] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1210:10)
      at Parser.parseVarStatement [as parseStatementContent] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:566:21)
      at Parser.parseStatementContent [as parseStatementLike] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:437:17)
      at Parser.parseStatementLike [as parseStatementListItem] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:386:17)
      at Parser.parseStatementListItem [as parseBlockOrModuleBlockBody] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1403:16)
      at Parser.parseBlockOrModuleBlockBody [as parseBlockBody] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1376:10)
      at Parser.parseBlockBody [as parseBlock] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1344:10)
      at Parser.parseBlock [as parseFunctionBody] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:2558:24)
      at Parser.parseFunctionBody [as parseArrowExpression] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:2499:10)
      at Parser.parseArrowExpression [as parseParenAndDistinguishExpression] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:1790:12)
      at Parser.parseParenAndDistinguishExpression [as parseExprAtom] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:1127:21)
      at Parser.parseExprAtom [as parseExprSubscripts] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:710:23)
      at Parser.parseExprSubscripts [as parseUpdate] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:689:21)
      at Parser.parseUpdate [as parseMaybeUnary] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:651:23)
      at Parser.parseMaybeUnary [as parseMaybeUnaryOrPrivate] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:385:14)
      at Parser.parseMaybeUnaryOrPrivate [as parseExprOps] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:397:23)
      at Parser.parseExprOps [as parseMaybeConditional] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:352:23)
      at Parser.parseMaybeConditional [as parseMaybeAssign] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:294:21)
      at parseMaybeAssign (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:252:12)
      at Parser.callback [as allowInAnd] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:3111:16)
      at Parser.allowInAnd [as parseMaybeAssignAllowIn] (../npm-install/node_modules/@babel/parser/src/parser/expression.ts:251:17)
      at Parser.parseMaybeAssignAllowIn [as parseVar] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1546:18)
      at Parser.parseVar [as parseVarStatement] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1210:10)
      at Parser.parseVarStatement [as parseStatementContent] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:566:21)
      at Parser.parseStatementContent [as parseStatementLike] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:437:17)
      at Parser.parseStatementLike [as parseStatementListItem] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:386:17)
      at Parser.parseStatementListItem (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:2583:17)
      at Parser.parseExportDeclaration [as maybeParseExportDeclaration] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:2505:31)
      at Parser.maybeParseExportDeclaration [as parseExport] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:2386:29)
      at Parser.parseExport [as parseStatementContent] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:603:25)
      at Parser.parseStatementContent [as parseStatementLike] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:437:17)
      at Parser.parseStatementLike [as parseModuleItem] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:374:17)
      at Parser.parseModuleItem [as parseBlockOrModuleBlockBody] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1402:16)
      at Parser.parseBlockOrModuleBlockBody [as parseBlockBody] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:1376:10)
      at Parser.parseBlockBody [as parseProgram] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:225:10)
      at Parser.parseProgram [as parseTopLevel] (../npm-install/node_modules/@babel/parser/src/parser/statement.ts:203:25)
      at Parser.parseTopLevel [as parse] (../npm-install/node_modules/@babel/parser/src/parser/index.ts:90:10)
      at parse (../npm-install/node_modules/@babel/parser/src/index.ts:92:38)
      at parser (../npm-install/node_modules/@babel/core/src/parser/index.ts:28:19)
          at parser.next (<anonymous>)
      at normalizeFile (../npm-install/node_modules/@babel/core/src/transformation/normalize-file.ts:50:24)
          at normalizeFile.next (<anonymous>)
      at run (../npm-install/node_modules/@babel/core/src/transformation/index.ts:39:36)
          at run.next (<anonymous>)
      at transform (../npm-install/node_modules/@babel/core/src/transform.ts:29:20)
          at transform.next (<anonymous>)
      at evaluateSync (../npm-install/node_modules/gensync/index.js:251:28)
      at sync (../npm-install/node_modules/gensync/index.js:89:14)
      at fn (../npm-install/node_modules/@babel/core/src/errors/rewrite-stack-trace.ts:99:14)
      at transformSync (../npm-install/node_modules/@babel/core/src/transform.ts:66:52)
      at ScriptTransformer.transformSource (../npm-install/node_modules/@jest/transform/build/ScriptTransformer.js:545:31)
      at ScriptTransformer._transformAndBuildScript (../npm-install/node_modules/@jest/transform/build/ScriptTransformer.js:674:40)
      at ScriptTransformer.transform (../npm-install/node_modules/@jest/transform/build/ScriptTransformer.js:726:19)
      at Object.require (ocr-numbers.spec.js:1:1)

Test Suites: 1 failed, 1 total
Tests:       0 total
Snapshots:   0 total
Time:        1.947 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/node_modules|.\/ocr-numbers.js|.\/ocr-numbers.spec.js|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
