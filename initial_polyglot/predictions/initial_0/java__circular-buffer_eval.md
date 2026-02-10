+ ./gradlew test
Downloading https://services.gradle.org/distributions/gradle-8.7-bin.zip
............10%.............20%.............30%.............40%............50%.............60%.............70%.............80%.............90%............100%

Welcome to Gradle 8.7!

Here are the highlights of this release:
 - Compiling and testing with Java 22
 - Cacheable Groovy script compilation
 - New methods in lazy collection properties

For more details see https://docs.gradle.org/8.7/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)
> Task :compileJava
> Task :processResources NO-SOURCE
> Task :classes

> Task :compileTestJava
/testbed/src/test/java/CircularBufferTest.java:23: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:24: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(1);
                              ^
/testbed/src/test/java/CircularBufferTest.java:32: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:33: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(1);
                              ^
/testbed/src/test/java/CircularBufferTest.java:45: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:46: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(2);
                    ^
/testbed/src/test/java/CircularBufferTest.java:47: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(1);
                              ^
/testbed/src/test/java/CircularBufferTest.java:48: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(2);
                              ^
/testbed/src/test/java/CircularBufferTest.java:56: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:68: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:69: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(1);
                              ^
/testbed/src/test/java/CircularBufferTest.java:70: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(2);
                    ^
/testbed/src/test/java/CircularBufferTest.java:71: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(2);
                              ^
/testbed/src/test/java/CircularBufferTest.java:79: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:80: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(2);
                    ^
/testbed/src/test/java/CircularBufferTest.java:81: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(1);
                              ^
/testbed/src/test/java/CircularBufferTest.java:82: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(3);
                    ^
/testbed/src/test/java/CircularBufferTest.java:83: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(2);
                              ^
/testbed/src/test/java/CircularBufferTest.java:84: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(3);
                              ^
/testbed/src/test/java/CircularBufferTest.java:92: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:105: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:107: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(2);
                    ^
/testbed/src/test/java/CircularBufferTest.java:108: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(2);
                              ^
/testbed/src/test/java/CircularBufferTest.java:117: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:118: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(1);
                              ^
/testbed/src/test/java/CircularBufferTest.java:126: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:128: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(1);
                              ^
/testbed/src/test/java/CircularBufferTest.java:129: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(2);
                              ^
/testbed/src/test/java/CircularBufferTest.java:137: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:138: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(2);
                    ^
/testbed/src/test/java/CircularBufferTest.java:140: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(2);
                              ^
/testbed/src/test/java/CircularBufferTest.java:141: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(3);
                              ^
/testbed/src/test/java/CircularBufferTest.java:149: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:150: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(2);
                    ^
/testbed/src/test/java/CircularBufferTest.java:151: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(3);
                    ^
/testbed/src/test/java/CircularBufferTest.java:152: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(1);
                              ^
/testbed/src/test/java/CircularBufferTest.java:153: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(4);
                    ^
/testbed/src/test/java/CircularBufferTest.java:155: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(3);
                              ^
/testbed/src/test/java/CircularBufferTest.java:156: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(4);
                              ^
/testbed/src/test/java/CircularBufferTest.java:157: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(5);
                              ^
/testbed/src/test/java/CircularBufferTest.java:166: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(1);
                    ^
/testbed/src/test/java/CircularBufferTest.java:167: error: unreported exception BufferIOException; must be caught or declared to be thrown
        buffer.write(2);
                    ^
/testbed/src/test/java/CircularBufferTest.java:170: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(3);
                              ^
/testbed/src/test/java/CircularBufferTest.java:171: error: unreported exception BufferIOException; must be caught or declared to be thrown
        assertThat(buffer.read()).isEqualTo(4);
                              ^
44 errors

> Task :compileTestJava FAILED
2 actionable tasks: 2 executed

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileTestJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 1m 34s
