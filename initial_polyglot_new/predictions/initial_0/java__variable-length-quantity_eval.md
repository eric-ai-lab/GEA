+ ./gradlew test
Starting a Gradle Daemon, 1 incompatible and 2 stopped Daemons could not be reused, use --status for details
> Task :compileJava
> Task :processResources NO-SOURCE
> Task :classes
> Task :compileTestJava
> Task :processTestResources NO-SOURCE
> Task :testClasses

> Task :test FAILED

VariableLengthQuantityTest > testLargestDoubleByte() SKIPPED

VariableLengthQuantityTest > testLargestTripleByte() SKIPPED

VariableLengthQuantityTest > testLargestSingleByte() SKIPPED

VariableLengthQuantityTest > testArbitraryDoubleByte() SKIPPED

VariableLengthQuantityTest > testSmallestDoubleByte() SKIPPED

VariableLengthQuantityTest > testArbitraryTripleByte() SKIPPED

VariableLengthQuantityTest > testSmallestTripleByte() SKIPPED

VariableLengthQuantityTest > testArbitrarySingleByte() SKIPPED

VariableLengthQuantityTest > testMaximum32BitIntegerInput() SKIPPED

VariableLengthQuantityTest > testDecodeMultipleBytes() SKIPPED

VariableLengthQuantityTest > testTwoSingleByteValues() SKIPPED

VariableLengthQuantityTest > testZero() FAILED
    org.opentest4j.AssertionFailedError: 
    expected: ["0x0"]
     but was: ["00"]
        at java.base@21.0.9/jdk.internal.reflect.DirectConstructorHandleAccessor.newInstance(DirectConstructorHandleAccessor.java:62)
        at java.base@21.0.9/java.lang.reflect.Constructor.newInstanceWithCaller(Constructor.java:502)
        at app//VariableLengthQuantityTest.testZero(VariableLengthQuantityTest.java:20)

VariableLengthQuantityTest > testDecodeFourBytes() SKIPPED

VariableLengthQuantityTest > testCannotDecodeIncompleteSequence() SKIPPED

VariableLengthQuantityTest > testDecodeTwoBytes() SKIPPED

VariableLengthQuantityTest > testManyMultiByteValues() SKIPPED

VariableLengthQuantityTest > testTwoMultiByteValues() SKIPPED

VariableLengthQuantityTest > testDecodeThreeBytes() SKIPPED

VariableLengthQuantityTest > testArbitraryQuadrupleByte() SKIPPED

VariableLengthQuantityTest > testSmallestQuadrupleByte() SKIPPED

VariableLengthQuantityTest > testDecodeOneByte() SKIPPED

VariableLengthQuantityTest > testCannotDecodeIncompleteSequenceEvenIfValueIsZero() SKIPPED

VariableLengthQuantityTest > testLargestQuadrupleByte() SKIPPED

VariableLengthQuantityTest > testDecodeMaximum32BitInteger() SKIPPED

VariableLengthQuantityTest > testArbitraryQuintupleByte() SKIPPED

VariableLengthQuantityTest > testSmallestQuintupleByte() SKIPPED

26 tests completed, 1 failed, 25 skipped

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
