+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/Poker.java:16: error: cannot find symbol
        ArrayList<Hand> scoredHands = new ArrayList<>();
                  ^
  symbol:   class Hand
  location: class Poker
/testbed/src/main/java/Poker.java:19: error: cannot find symbol
            scoredHands.add(new Hand(s));
                                ^
  symbol:   class Hand
  location: class Poker
/testbed/src/main/java/Poker.java:23: error: cannot find symbol
                .map(Hand::getScore)
                     ^
  symbol:   variable Hand
  location: class Poker
/testbed/src/main/java/Poker.java:29: error: cannot find symbol
                        .map(Hand::getInput)
                             ^
  symbol:   variable Hand
  location: class Poker
/testbed/src/main/java/Poker.java:31: error: incompatible types: Object cannot be converted to List<String>
                .orElseGet(Collections::emptyList);
                          ^
5 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 613ms
1 actionable task: 1 executed
