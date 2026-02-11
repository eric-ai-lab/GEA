+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/SgfParsing.java:61: error: cannot find symbol
                currentNode.addChild(nextNode);
                           ^
  symbol:   method addChild(SgfNode)
  location: variable currentNode of type SgfNode
/testbed/src/main/java/SgfParsing.java:68: error: cannot find symbol
                currentNode.addChild(variation);
                           ^
  symbol:   method addChild(SgfNode)
  location: variable currentNode of type SgfNode
/testbed/src/main/java/SgfParsing.java:125: error: cannot find symbol
            node.addProperty(key, value);
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

BUILD FAILED in 687ms
1 actionable task: 1 executed
