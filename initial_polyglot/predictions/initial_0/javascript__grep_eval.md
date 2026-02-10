+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' grep.spec.js
+ npm run test

> test
> jest ./*

FAIL ./grep.spec.js (5.209 s)
  grep exercise
    Test grepping a single file
      ✓ One file, one match, no flags (315 ms)
      ○ skipped One file, one match, print line numbers flag
      ○ skipped One file, one match, case-insensitive flag
      ○ skipped One file, one match, print file names flag
      ○ skipped One file, one match, match entire lines flag
      ○ skipped One file, one match, multiple flags
      ○ skipped One file, several matches, no flags
      ○ skipped One file, several matches, print line numbers flag
      ○ skipped One file, several matches, match entire lines flag
      ○ skipped One file, several matches, case-insensitive flag
      ○ skipped One file, several matches, inverted flag
      ○ skipped One file, no matches, various flags
      ○ skipped One file, one match, file flag takes precedence over line flag
      ○ skipped One file, several matches, inverted and match entire lines flags
    Test grepping multiples files at once
      ✕ Multiple files, one match, print file names flag (281 ms)
      ○ skipped Multiple files, one match, no flags
      ○ skipped Multiple files, several matches, no flags
      ○ skipped Multiple files, several matches, print line numbers flag
      ○ skipped Multiple files, several matches, case-insensitive flag
      ○ skipped Multiple files, several matches, inverted flag
      ○ skipped Multiple files, one match, match entire lines flag
      ○ skipped Multiple files, one match, multiple flags
      ○ skipped Multiple files, no matches, various flags
      ○ skipped Multiple files, several matches, file flag takes precedence over line number flag
      ○ skipped Multiple files, several matches, inverted and match entire lines flags

  ● grep exercise › Test grepping multiples files at once › Multiple files, one match, print file names flag

    expect(received).resolves.toBe()

    Received promise rejected instead of resolved
    Rejected to value: "Error reading file: who"

      286 |
      287 |     it('Multiple files, one match, print file names flag', () => {
    > 288 |       return expect(
          |              ^
      289 |         spawnGrep({
      290 |           pattern: 'who',
      291 |           flags: ['-l'],

      at expect (../npm-install/node_modules/expect/build/index.js:113:15)
      at Object.expect (grep.spec.js:288:14)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 23 skipped, 1 passed, 25 total
Snapshots:   0 total
Time:        5.352 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/data|.\/eval.sh|.\/grep.js|.\/grep.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
