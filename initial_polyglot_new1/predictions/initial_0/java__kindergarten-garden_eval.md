+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/KindergartenGarden.java:55: error: cannot find symbol
                return Plant.RADISH;
                            ^
  symbol:   variable RADISH
  location: class Plant
/testbed/src/main/java/KindergartenGarden.java:57: error: cannot find symbol
                return Plant.VIOLET;
                            ^
  symbol:   variable VIOLET
  location: class Plant
2 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 614ms
1 actionable task: 1 executed
