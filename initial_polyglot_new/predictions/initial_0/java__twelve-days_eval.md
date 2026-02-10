+ ./gradlew test
> Task :compileJava
> Task :processResources NO-SOURCE
> Task :classes
> Task :compileTestJava
> Task :processTestResources NO-SOURCE
> Task :testClasses

> Task :test FAILED

TwelveDaysTest > testVerseEight() SKIPPED

TwelveDaysTest > testVerseSeven() SKIPPED

TwelveDaysTest > testVerseThree() SKIPPED

TwelveDaysTest > testVerseOne() FAILED
    org.opentest4j.AssertionFailedError: 
    expected: 
      "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
      "
     but was: 
      "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
        at java.base@21.0.9/jdk.internal.reflect.DirectConstructorHandleAccessor.newInstance(DirectConstructorHandleAccessor.java:62)
        at java.base@21.0.9/java.lang.reflect.Constructor.newInstanceWithCaller(Constructor.java:502)
        at app//TwelveDaysTest.testVerseOne(TwelveDaysTest.java:19)

TwelveDaysTest > testVerseSix() SKIPPED

TwelveDaysTest > testVerseTen() SKIPPED

TwelveDaysTest > testVerseTwo() SKIPPED

TwelveDaysTest > testVerseFive() SKIPPED

TwelveDaysTest > testVerseFour() SKIPPED

TwelveDaysTest > testVerseNine() SKIPPED

TwelveDaysTest > testVerseEleven() SKIPPED

TwelveDaysTest > testVerseTwelve() SKIPPED

TwelveDaysTest > testFirstThreeVerses() SKIPPED

TwelveDaysTest > testSingWholeSong() SKIPPED

TwelveDaysTest > testFourthToSixthVerses() SKIPPED

15 tests completed, 1 failed, 14 skipped

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':test'.
> There were failing tests. See the report at: file:///testbed/build/reports/tests/test/index.html

* Try:
> Run with --scan to get full insights.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.7/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 6s
3 actionable tasks: 3 executed
