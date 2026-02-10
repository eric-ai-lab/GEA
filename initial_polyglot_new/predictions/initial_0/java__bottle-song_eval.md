+ ./gradlew test
> Task :compileJava
> Task :processResources NO-SOURCE
> Task :classes
> Task :compileTestJava
> Task :processTestResources NO-SOURCE
> Task :testClasses

> Task :test FAILED

BottleSongTest > lastThreeVerses() SKIPPED

BottleSongTest > lastGenericVerse() SKIPPED

BottleSongTest > allVerses() SKIPPED

BottleSongTest > verseWithOneBottle() SKIPPED

BottleSongTest > verseWithTwoBottles() SKIPPED

BottleSongTest > firstGenericVerse() FAILED
    org.opentest4j.AssertionFailedError: 
    expected: 
      "Ten green bottles hanging on the wall,
      Ten green bottles hanging on the wall,
      And if one green bottle should accidentally fall,
      There'll be nine green bottles hanging on the wall.
      "
     but was: 
      "ten green bottles hanging on the wall,
      ten green bottles hanging on the wall,
      And if one green bottle should accidentally fall,
      There'll be nine green bottles hanging on the wall."
        at java.base@21.0.9/jdk.internal.reflect.DirectConstructorHandleAccessor.newInstance(DirectConstructorHandleAccessor.java:62)
        at java.base@21.0.9/java.lang.reflect.Constructor.newInstanceWithCaller(Constructor.java:502)
        at app//BottleSongTest.firstGenericVerse(BottleSongTest.java:18)

BottleSongTest > firstTwoVerses() SKIPPED

7 tests completed, 1 failed, 6 skipped

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':test'.
> There were failing tests. See the report at: file:///testbed/build/reports/tests/test/index.html

* Try:
> Run with --scan to get full insights.

Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.7/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD FAILED in 7s
3 actionable tasks: 3 executed
