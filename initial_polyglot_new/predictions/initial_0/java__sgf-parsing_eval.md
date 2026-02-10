+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/SgfParsing.java:62: error: cannot find symbol
                node.addChild(child);
                    ^
  symbol:   method addChild(SgfNode)
  location: variable node of type SgfNode
/testbed/src/main/java/SgfParsing.java:73: error: cannot find symbol
            node.addChild(child);
                ^
  symbol:   method addChild(SgfNode)
  location: variable node of type SgfNode
/testbed/src/main/java/SgfParsing.java:104: error: cannot find symbol
                node.addProperty(propertyName, value);
                    ^
  symbol:   method addProperty(String,String)
  location: variable node of type SgfNode
3 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 594ms
1 actionable task: 1 executed
