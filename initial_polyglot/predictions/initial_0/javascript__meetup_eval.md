+ set -e
+ '[' '!' -e node_modules ']'
+ ln -s /npm-install/node_modules .
+ '[' '!' -e package-lock.json ']'
+ ln -s /npm-install/package-lock.json .
+ sed -i 's/\bxtest(/test(/g' meetup.spec.js
+ npm run test

> test
> jest ./*

FAIL ./meetup.spec.js
  Meetup
    ✕ monteenth of May 2013 (5 ms)
    ✕ monteenth of August 2013 (1 ms)
    ✕ monteenth of September 2013 (1 ms)
    ✕ tuesteenth of March 2013
    ✕ tuesteenth of April 2013 (1 ms)
    ✕ tuesteenth of August 2013 (2 ms)
    ✕ wednesteenth of January 2013 (1 ms)
    ✕ wednesteenth of February 2013 (1 ms)
    ✕ wednesteenth of June 2013 (1 ms)
    ✕ thursteenth of May 2013 (1 ms)
    ✕ thursteenth of June 2013 (1 ms)
    ✕ thursteenth of September 2013 (1 ms)
    ✕ friteenth of April 2013 (1 ms)
    ✕ friteenth of August 2013 (1 ms)
    ✕ friteenth of September 2013
    ✕ saturteenth of February 2013 (16 ms)
    ✕ saturteenth of April 2013
    ✕ saturteenth of October 2013
    ✕ sunteenth of May 2013
    ✕ sunteenth of June 2013 (1 ms)
    ✕ sunteenth of October 2013
    ✕ first Monday of March 2013
    ✕ first Monday of April 2013
    ✕ first Tuesday of May 2013
    ✕ first Tuesday of June 2013
    ✕ first Wednesday of July 2013
    ✕ first Wednesday of August 2013 (3 ms)
    ✕ first Thursday of September 2013 (5 ms)
    ✕ first Thursday of October 2013
    ✕ first Friday of November 2013 (7 ms)
    ✕ first Friday of December 2013 (1 ms)
    ✕ first Saturday of January 2013 (1 ms)
    ✕ first Saturday of February 2013
    ✕ first Sunday of March 2013
    ✕ first Sunday of April 2013
    ✕ second Monday of March 2013
    ✕ second Monday of April 2013
    ✕ second Tuesday of May 2013 (1 ms)
    ✕ second Tuesday of June 2013
    ✕ second Wednesday of July 2013 (1 ms)
    ✕ second Wednesday of August 2013
    ✕ second Thursday of September 2013
    ✕ second Thursday of October 2013
    ✕ second Friday of November 2013
    ✕ second Friday of December 2013 (1 ms)
    ✕ second Saturday of January 2013
    ✕ second Saturday of February 2013
    ✕ second Sunday of March 2013 (1 ms)
    ✕ second Sunday of April 2013
    ✕ third Monday of March 2013
    ✕ third Monday of April 2013 (1 ms)
    ✕ third Tuesday of May 2013 (1 ms)
    ✕ third Tuesday of June 2013
    ✕ third Wednesday of July 2013 (1 ms)
    ✕ third Wednesday of August 2013
    ✕ third Thursday of September 2013
    ✕ third Thursday of October 2013
    ✕ third Friday of November 2013
    ✕ third Friday of December 2013
    ✕ third Saturday of January 2013
    ✕ third Saturday of February 2013
    ✕ third Sunday of March 2013
    ✕ third Sunday of April 2013
    ✕ fourth Monday of March 2013
    ✕ fourth Monday of April 2013
    ✕ fourth Tuesday of May 2013
    ✕ fourth Tuesday of June 2013 (1 ms)
    ✕ fourth Wednesday of July 2013
    ✕ fourth Wednesday of August 2013
    ✕ fourth Thursday of September 2013
    ✕ fourth Thursday of October 2013 (20 ms)
    ✕ fourth Friday of November 2013
    ✕ fourth Friday of December 2013 (8 ms)
    ✕ fourth Saturday of January 2013
    ✕ fourth Saturday of February 2013
    ✕ fourth Sunday of March 2013 (41 ms)
    ✕ fourth Sunday of April 2013
    ✕ last Monday of March 2013 (1 ms)
    ✕ last Monday of April 2013
    ✕ last Tuesday of May 2013
    ✕ last Tuesday of June 2013
    ✕ last Wednesday of July 2013 (1 ms)
    ✕ last Wednesday of August 2013 (4 ms)
    ✕ last Thursday of September 2013
    ✕ last Thursday of October 2013
    ✕ last Friday of November 2013
    ✕ last Friday of December 2013
    ✕ last Saturday of January 2013
    ✕ last Saturday of February 2013 (1 ms)
    ✕ last Sunday of March 2013
    ✕ last Sunday of April 2013 (1 ms)
    ✕ last Wednesday of February 2012
    ✕ last Wednesday of December 2014
    ✕ last Sunday of February 2015
    ✕ first Friday of December 2012

  ● Meetup › monteenth of May 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:5:18)

  ● Meetup › monteenth of August 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:9:18)

  ● Meetup › monteenth of September 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:13:18)

  ● Meetup › tuesteenth of March 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:17:18)

  ● Meetup › tuesteenth of April 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:21:18)

  ● Meetup › tuesteenth of August 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:25:18)

  ● Meetup › wednesteenth of January 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:29:18)

  ● Meetup › wednesteenth of February 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:35:18)

  ● Meetup › wednesteenth of June 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:41:18)

  ● Meetup › thursteenth of May 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:47:18)

  ● Meetup › thursteenth of June 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:53:18)

  ● Meetup › thursteenth of September 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:59:18)

  ● Meetup › friteenth of April 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:65:18)

  ● Meetup › friteenth of August 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:69:18)

  ● Meetup › friteenth of September 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:73:18)

  ● Meetup › saturteenth of February 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:77:18)

  ● Meetup › saturteenth of April 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:83:18)

  ● Meetup › saturteenth of October 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:89:18)

  ● Meetup › sunteenth of May 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:95:18)

  ● Meetup › sunteenth of June 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:99:18)

  ● Meetup › sunteenth of October 2013

    Invalid weekday: teenth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:103:18)

  ● Meetup › first Monday of March 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:107:18)

  ● Meetup › first Monday of April 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:111:18)

  ● Meetup › first Tuesday of May 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:115:18)

  ● Meetup › first Tuesday of June 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:119:18)

  ● Meetup › first Wednesday of July 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:123:18)

  ● Meetup › first Wednesday of August 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:127:18)

  ● Meetup › first Thursday of September 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:131:18)

  ● Meetup › first Thursday of October 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:135:18)

  ● Meetup › first Friday of November 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:139:18)

  ● Meetup › first Friday of December 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:143:18)

  ● Meetup › first Saturday of January 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:147:18)

  ● Meetup › first Saturday of February 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:151:18)

  ● Meetup › first Sunday of March 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:155:18)

  ● Meetup › first Sunday of April 2013

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:159:18)

  ● Meetup › second Monday of March 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:163:18)

  ● Meetup › second Monday of April 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:167:18)

  ● Meetup › second Tuesday of May 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:171:18)

  ● Meetup › second Tuesday of June 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:175:18)

  ● Meetup › second Wednesday of July 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:179:18)

  ● Meetup › second Wednesday of August 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:185:18)

  ● Meetup › second Thursday of September 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:191:18)

  ● Meetup › second Thursday of October 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:197:18)

  ● Meetup › second Friday of November 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:203:18)

  ● Meetup › second Friday of December 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:207:18)

  ● Meetup › second Saturday of January 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:213:18)

  ● Meetup › second Saturday of February 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:219:18)

  ● Meetup › second Sunday of March 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:223:18)

  ● Meetup › second Sunday of April 2013

    Invalid weekday: second

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:227:18)

  ● Meetup › third Monday of March 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:231:18)

  ● Meetup › third Monday of April 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:235:18)

  ● Meetup › third Tuesday of May 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:239:18)

  ● Meetup › third Tuesday of June 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:243:18)

  ● Meetup › third Wednesday of July 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:247:18)

  ● Meetup › third Wednesday of August 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:253:18)

  ● Meetup › third Thursday of September 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:259:18)

  ● Meetup › third Thursday of October 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:263:18)

  ● Meetup › third Friday of November 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:269:18)

  ● Meetup › third Friday of December 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:273:18)

  ● Meetup › third Saturday of January 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:277:18)

  ● Meetup › third Saturday of February 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:281:18)

  ● Meetup › third Sunday of March 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:285:18)

  ● Meetup › third Sunday of April 2013

    Invalid weekday: third

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:289:18)

  ● Meetup › fourth Monday of March 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:293:18)

  ● Meetup › fourth Monday of April 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:297:18)

  ● Meetup › fourth Tuesday of May 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:301:18)

  ● Meetup › fourth Tuesday of June 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:305:18)

  ● Meetup › fourth Wednesday of July 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:309:18)

  ● Meetup › fourth Wednesday of August 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:315:18)

  ● Meetup › fourth Thursday of September 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:321:18)

  ● Meetup › fourth Thursday of October 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:327:18)

  ● Meetup › fourth Friday of November 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:333:18)

  ● Meetup › fourth Friday of December 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:339:18)

  ● Meetup › fourth Saturday of January 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:345:18)

  ● Meetup › fourth Saturday of February 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:351:18)

  ● Meetup › fourth Sunday of March 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:357:18)

  ● Meetup › fourth Sunday of April 2013

    Invalid weekday: fourth

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:361:18)

  ● Meetup › last Monday of March 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:365:18)

  ● Meetup › last Monday of April 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:369:18)

  ● Meetup › last Tuesday of May 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:373:18)

  ● Meetup › last Tuesday of June 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:377:18)

  ● Meetup › last Wednesday of July 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:381:18)

  ● Meetup › last Wednesday of August 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:385:18)

  ● Meetup › last Thursday of September 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:389:18)

  ● Meetup › last Thursday of October 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:393:18)

  ● Meetup › last Friday of November 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:397:18)

  ● Meetup › last Friday of December 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:401:18)

  ● Meetup › last Saturday of January 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:405:18)

  ● Meetup › last Saturday of February 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:409:18)

  ● Meetup › last Sunday of March 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:413:18)

  ● Meetup › last Sunday of April 2013

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:417:18)

  ● Meetup › last Wednesday of February 2012

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:421:18)

  ● Meetup › last Wednesday of December 2014

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:425:18)

  ● Meetup › last Sunday of February 2015

    Invalid weekday: last

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:431:18)

  ● Meetup › first Friday of December 2012

    Invalid weekday: first

      19 |   const targetDay = weekdayMap[weekday];
      20 |   if (targetDay === undefined) {
    > 21 |     throw new Error(`Invalid weekday: ${weekday}`);
         |           ^
      22 |   }
      23 |
      24 |   // Adjust month index for Date constructor (0-indexed)

      at meetup (meetup.js:21:11)
      at Object.<anonymous> (meetup.spec.js:435:18)

Test Suites: 1 failed, 1 total
Tests:       95 failed, 95 total
Snapshots:   0 total
Time:        3.733 s
Ran all test suites matching /.\/LICENSE|.\/babel.config.js|.\/eval.sh|.\/meetup.js|.\/meetup.spec.js|.\/node_modules|.\/package-lock.json|.\/package.json/i.
npm notice
npm notice New major version of npm available! 10.8.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
