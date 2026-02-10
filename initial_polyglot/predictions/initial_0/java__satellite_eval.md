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
/testbed/src/test/java/SatelliteTest.java:16: error: incompatible types: Satellite.Tree cannot be converted to Tree
        Tree tree = satellite.treeFromTraversals(preorder, inorder);
                                                ^
/testbed/src/test/java/SatelliteTest.java:29: error: incompatible types: Satellite.Tree cannot be converted to Tree
        Tree tree = satellite.treeFromTraversals(preorder, inorder);
                                                ^
/testbed/src/test/java/SatelliteTest.java:42: error: incompatible types: Satellite.Tree cannot be converted to Tree
        Tree tree = satellite.treeFromTraversals(preorder, inorder);
                                                ^
3 errors

> Task :compileTestJava FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileTestJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.
2 actionable tasks: 2 executed

BUILD FAILED in 1m 41s
