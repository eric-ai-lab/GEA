+ ./gradlew test

> Task :compileJava FAILED
/testbed/src/main/java/RestApi.java:18: error: cannot find symbol
                builder.owes(iou.name(), iou.amount());
                                ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:18: error: cannot find symbol
                builder.owes(iou.name(), iou.amount());
                                            ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:21: error: cannot find symbol
                builder.owedBy(iou.name(), iou.amount());
                                  ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:21: error: cannot find symbol
                builder.owedBy(iou.name(), iou.amount());
                                              ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:92: error: cannot find symbol
                if (iou.name().equals(borrower)) {
                       ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:93: error: cannot find symbol
                    currentOwedByBorrower = iou.amount();
                                               ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:101: error: cannot find symbol
                lenderBuilder.owes(iou.name(), iou.amount());
                                      ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:101: error: cannot find symbol
                lenderBuilder.owes(iou.name(), iou.amount());
                                                  ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:104: error: cannot find symbol
                if (!iou.name().equals(borrower)) {
                        ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:105: error: cannot find symbol
                    lenderBuilder.owedBy(iou.name(), iou.amount());
                                            ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:105: error: cannot find symbol
                    lenderBuilder.owedBy(iou.name(), iou.amount());
                                                        ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:117: error: cannot find symbol
                if (iou.name().equals(lender)) {
                       ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:118: error: cannot find symbol
                    currentOwesByBorrower = iou.amount();
                                               ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:126: error: cannot find symbol
                if (!iou.name().equals(lender)) {
                        ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:127: error: cannot find symbol
                    borrowerBuilder.owes(iou.name(), iou.amount());
                                            ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:127: error: cannot find symbol
                    borrowerBuilder.owes(iou.name(), iou.amount());
                                                        ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:131: error: cannot find symbol
                borrowerBuilder.owedBy(iou.name(), iou.amount());
                                          ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:131: error: cannot find symbol
                borrowerBuilder.owedBy(iou.name(), iou.amount());
                                                      ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:156: error: cannot find symbol
            owes.put(iou.name(), iou.amount());
                        ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:156: error: cannot find symbol
            owes.put(iou.name(), iou.amount());
                                    ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:162: error: cannot find symbol
            owedBy.put(iou.name(), iou.amount());
                          ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:162: error: cannot find symbol
            owedBy.put(iou.name(), iou.amount());
                                      ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:167: error: invalid method reference
        double totalOwed = user.owedBy().stream().mapToDouble(Iou::amount).sum();
                                                              ^
  cannot find symbol
    symbol:   method amount(T)
    location: class Iou
  where T is a type-variable:
    T extends Object declared in interface Stream
/testbed/src/main/java/RestApi.java:168: error: invalid method reference
        double totalOwes = user.owes().stream().mapToDouble(Iou::amount).sum();
                                                            ^
  cannot find symbol
    symbol:   method amount(T)
    location: class Iou
  where T is a type-variable:
    T extends Object declared in interface Stream
/testbed/src/main/java/RestApi.java:182: error: cannot find symbol
                owes.put(iou.name(), iou.amount());
                            ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:182: error: cannot find symbol
                owes.put(iou.name(), iou.amount());
                                        ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:188: error: cannot find symbol
                owedBy.put(iou.name(), iou.amount());
                              ^
  symbol:   method name()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:188: error: cannot find symbol
                owedBy.put(iou.name(), iou.amount());
                                          ^
  symbol:   method amount()
  location: variable iou of type Iou
/testbed/src/main/java/RestApi.java:193: error: invalid method reference
            double totalOwed = user.owedBy().stream().mapToDouble(Iou::amount).sum();
                                                                  ^
  cannot find symbol
    symbol:   method amount(T)
    location: class Iou
  where T is a type-variable:
    T extends Object declared in interface Stream
/testbed/src/main/java/RestApi.java:194: error: invalid method reference
            double totalOwes = user.owes().stream().mapToDouble(Iou::amount).sum();
                                                                ^
  cannot find symbol
    symbol:   method amount(T)
    location: class Iou
  where T is a type-variable:
    T extends Object declared in interface Stream
30 errors

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
> Run with --info option to get more log output.
> Run with --scan to get full insights.

BUILD FAILED in 618ms
1 actionable task: 1 executed
