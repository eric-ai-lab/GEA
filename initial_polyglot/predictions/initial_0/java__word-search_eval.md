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
/testbed/src/main/java/WordSearcher.java:60: error: constructor WordLocation in class WordLocation cannot be applied to given types;
                            return Optional.of(new WordLocation(row + 1, col + 1, endRow + 1, endCol + 1));
                                               ^
  required: Pair,Pair
  found:    int,int,int,int
  reason: actual and formal argument lists differ in length
/testbed/src/main/java/WordSearcher.java:87: error: constructor WordLocation in class WordLocation cannot be applied to given types;
                            return Optional.of(new WordLocation(endRow + 1, endCol + 1, row + 1, col + 1));
                                               ^
  required: Pair,Pair
  found:    int,int,int,int
  reason: actual and formal argument lists differ in length
2 errors

> Task :compileJava FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.
1 actionable task: 1 executed

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 1m 25s
