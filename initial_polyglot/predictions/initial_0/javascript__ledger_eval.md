+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' ledger.spec.js
+ npm run test

> test
> jest ./*

FAIL ./ledger.spec.js (5.267 s)
  Ledger
    ✓ empty ledger (25 ms)
    ✓ one entry (133 ms)
    ✓ credit and debit (2 ms)
    ✓ final order tie breaker is change (5 ms)
    ✓ overlong description is truncated (1 ms)
    ✓ euros (1 ms)
    ✕ Dutch locale (58 ms)
    ✓ Dutch locale and euros (1 ms)
    ✕ Dutch negative number with 3 digits before decimal point (5 ms)
    ✓ American negative number with 3 digits before decimal point (1 ms)
    ✓ multiple entries on same date ordered by description (1 ms)

  ● Ledger › Dutch locale

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      Datum      | Omschrijving              | Verandering  
    - 12-03-2015 | Buy present               |   $ 1.234,56 
    + 12-03-2015 | Buy present               | US$ 1.234,56

      87 |       '12-03-2015 | Buy present               |   $ 1.234,56 ',
      88 |     ].join('\n');
    > 89 |     expect(formatEntries(currency, locale, entries)).toEqual(expected);
         |                                                      ^
      90 |   });
      91 |
      92 |   test('Dutch locale and euros', () => {

      at Object.toEqual (ledger.spec.js:89:54)

  ● Ledger › Dutch negative number with 3 digits before decimal point

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      Datum      | Omschrijving              | Verandering  
    - 12-03-2015 | Buy present               |    $ -123,45 
    + 12-03-2015 | Buy present               |  US$ -123,45

      109 |       '12-03-2015 | Buy present               |    $ -123,45 ',
      110 |     ].join('\n');
    > 111 |     expect(formatEntries(currency, locale, entries)).toEqual(expected);
          |                                                      ^
      112 |   });
      113 |
      114 |   test('American negative number with 3 digits before decimal point', () => {

      at Object.toEqual (ledger.spec.js:111:54)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 9 passed, 11 total
Snapshots:   0 total
Time:        5.485 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/ledger.js|.\/ledger.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
