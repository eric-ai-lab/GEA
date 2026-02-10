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

/testbed/src/main/java/KindergartenGarden.java:28: error: cannot find symbol
                plants.add(Plant.fromChar(row1.charAt(j)));
                                ^
  symbol:   method fromChar(char)
  location: class Plant
/testbed/src/main/java/KindergartenGarden.java:32: error: cannot find symbol
                plants.add(Plant.fromChar(row2.charAt(j)));
                                ^
  symbol:   method fromChar(char)
  location: class Plant
> Task :compileJava
2 errors

> Task :compileJava FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> 1 actionable task: 1 executed
Run with --scan to get full insights.

BUILD FAILED in 1m 21s
