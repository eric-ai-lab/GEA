+ ./gradlew test
> Task :compileJava
> Task :processResources NO-SOURCE
> Task :classes
> Task :compileTestJava
> Task :processTestResources NO-SOURCE
> Task :testClasses

> Task :test

BankAccountTest > multipleDeposits() SKIPPED

BankAccountTest > canHandleConcurrentTransactions() SKIPPED

BankAccountTest > cannotCheckBalanceOfClosedAccount() SKIPPED

BankAccountTest > cannotDepositNegativeAmount() SKIPPED

BankAccountTest > cannotDepositIntoUnopenedAccount() SKIPPED

BankAccountTest > withdrawTwice() SKIPPED

BankAccountTest > reopenedAccountDoesNotRetainBalance() SKIPPED

BankAccountTest > cannotWithdrawNegativeAmount() SKIPPED

BankAccountTest > singleDeposit() SKIPPED

BankAccountTest > cannotWithdrawMoreThanWasDeposited() SKIPPED

BankAccountTest > cannotWithdrawFromClosedAccount() SKIPPED

BankAccountTest > cannotCloseAnAccountThatWasNotOpened() SKIPPED

BankAccountTest > newlyOpenedAccountHasEmptyBalance() PASSED

BankAccountTest > canDoMultipleOperationsSequentially() SKIPPED

BankAccountTest > withdrawOnce() SKIPPED

BankAccountTest > cannotOpenAnAlreadyOpenedAccount() SKIPPED

BankAccountTest > cannotDepositIntoClosedAccount() SKIPPED

Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.7/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD SUCCESSFUL in 1s
3 actionable tasks: 3 executed
