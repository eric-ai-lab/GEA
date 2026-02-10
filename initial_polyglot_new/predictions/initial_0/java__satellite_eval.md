+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/Satellite.java:32: error: incompatible types: Character cannot be converted to Node
        Tree root = new Tree(rootValue);
                             ^
/testbed/src/main/java/Satellite.java:41: error: cannot find symbol
        root.left = buildTree(preorder, preStart + 1, preStart + leftSubtreeSize,
            ^
  symbol:   variable left
  location: variable root of type Tree
/testbed/src/main/java/Satellite.java:45: error: cannot find symbol
        root.right = buildTree(preorder, preStart + leftSubtreeSize + 1, preEnd,
            ^
  symbol:   variable right
  location: variable root of type Tree
Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output
3 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 625ms
1 actionable task: 1 executed
