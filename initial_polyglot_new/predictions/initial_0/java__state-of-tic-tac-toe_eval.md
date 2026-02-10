+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/StateOfTicTacToe.java:2: error: cannot find symbol
    public GameState determineState(String[] board) throws InvalidBoardException {
                                                           ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
/testbed/src/main/java/StateOfTicTacToe.java:55: error: cannot find symbol
    private char[][] parseBoard(String[] board) throws InvalidBoardException {
                                                       ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
/testbed/src/main/java/StateOfTicTacToe.java:18: error: cannot find symbol
            throw new InvalidBoardException("Invalid turn order");
                      ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
/testbed/src/main/java/StateOfTicTacToe.java:27: error: cannot find symbol
            throw new InvalidBoardException("Both players cannot win");
                      ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
/testbed/src/main/java/StateOfTicTacToe.java:34: error: cannot find symbol
            throw new InvalidBoardException("Game continued after X won");
                      ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
/testbed/src/main/java/StateOfTicTacToe.java:38: error: cannot find symbol
            throw new InvalidBoardException("Game continued after O won");
                      ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
/testbed/src/main/java/StateOfTicTacToe.java:57: error: cannot find symbol
            throw new InvalidBoardException("Invalid board");
                      ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
/testbed/src/main/java/StateOfTicTacToe.java:64: error: cannot find symbol
                throw new InvalidBoardException("Invalid board");
                          ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
/testbed/src/main/java/StateOfTicTacToe.java:69: error: cannot find symbol
                    throw new InvalidBoardException("Invalid board");
                              ^
  symbol:   class InvalidBoardException
  location: class StateOfTicTacToe
9 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 830ms
1 actionable task: 1 executed
