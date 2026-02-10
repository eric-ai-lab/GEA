+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/Connect.java:42: error: cannot find symbol
            return Winner.O;
                         ^
  symbol:   variable O
  location: class Winner
/testbed/src/main/java/Connect.java:47: error: cannot find symbol
            return Winner.X;
                         ^
  symbol:   variable X
  location: class Winner
2 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 734ms
1 actionable task: 1 executed
