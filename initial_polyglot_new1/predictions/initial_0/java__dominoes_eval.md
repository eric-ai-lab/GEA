+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/Dominoes.java:78: error: cannot find symbol
            first = first.flip();
                         ^
  symbol:   method flip()
  location: variable first of type Domino
/testbed/src/main/java/Dominoes.java:113: error: cannot find symbol
                Domino flipped = d.flip();
                                  ^
  symbol:   method flip()
  location: variable d of type Domino
2 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 641ms
1 actionable task: 1 executed
