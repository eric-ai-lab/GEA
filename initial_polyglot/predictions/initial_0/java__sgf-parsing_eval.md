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
/testbed/src/main/java/SgfParsing.java:65: error: cannot find symbol
                    currentNode.addChild(node);
                               ^
  symbol:   method addChild(SgfNode)
  location: variable currentNode of type SgfNode
/testbed/src/main/java/SgfParsing.java:77: error: cannot find symbol
                currentNode.addChild(variation);
                           ^
  symbol:   method addChild(SgfNode)
  location: variable currentNode of type SgfNode
/testbed/src/main/java/SgfParsing.java:107: error: cannot find symbol
                    node.addProperty(key, value);
                        ^
  symbol:   method addProperty(String,String)
  location: variable node of type SgfNode
3 errors

> Task :compileJava FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 1m 24s
1 actionable task: 1 executed
