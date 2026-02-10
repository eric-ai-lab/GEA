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
/testbed/src/main/java/Dominoes.java:21: error: left has private access in Domino
            if (chain.get(0).left == chain.get(chain.size()-1).right) {
                            ^
/testbed/src/main/java/Dominoes.java:21: error: right has private access in Domino
            if (chain.get(0).left == chain.get(chain.size()-1).right) {
                                                              ^
/testbed/src/main/java/Dominoes.java:32: error: right has private access in Domino
            current = chain.get(chain.size()-1).right;
                                               ^
/testbed/src/main/java/Dominoes.java:41: error: cannot find symbol
                Domino flipped = domino.flip();
                                       ^
  symbol:   method flip()
  location: variable domino of type Domino
/testbed/src/main/java/Dominoes.java:43: error: left has private access in Domino
                if (!(domino.left == domino.right)) {
                            ^
/testbed/src/main/java/Dominoes.java:43: error: right has private access in Domino
                if (!(domino.left == domino.right)) {
                                           ^
/testbed/src/main/java/Dominoes.java:47: error: left has private access in Domino
                if (domino.left == current)
                          ^
/testbed/src/main/java/Dominoes.java:49: error: right has private access in Domino
                if (domino.right == current) {
                          ^
/testbed/src/main/java/Dominoes.java:50: error: cannot find symbol
                    Domino flipped = domino.flip();
                                           ^
  symbol:   method flip()
  location: variable domino of type Domino
/testbed/src/main/java/Dominoes.java:52: error: left has private access in Domino
                    if (!(domino.left == domino.right)) {
                                ^
/testbed/src/main/java/Dominoes.java:52: error: right has private access in Domino
                    if (!(domino.left == domino.right)) {
                                               ^
/testbed/src/main/java/Dominoes.java:64: error: left has private access in Domino
                    newStart = candidate.left;
                                        ^
12 errors

> Task :compileJava FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 1m 29s
1 actionable task: 1 executed
