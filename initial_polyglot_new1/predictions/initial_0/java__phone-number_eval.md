+ ./gradlew test
> Task :compileJava
> Task :processResources NO-SOURCE
> Task :classes
> Task :compileTestJava
> Task :processTestResources NO-SOURCE
> Task :testClasses

> Task :test

PhoneNumberTest > invalidWhen9Digits() SKIPPED

PhoneNumberTest > invalidIfAreaCodeStartsWith0OnValid11DigitNumber() SKIPPED

PhoneNumberTest > invalidIfAreaCodeStartsWith1OnValid11DigitNumber() SKIPPED

PhoneNumberTest > invalidWhenMoreThan11Digits() SKIPPED

PhoneNumberTest > invalidIfExchangeCodeStartsWith0OnValid11DigitNumber() SKIPPED

PhoneNumberTest > invalidIfExchangeCodeStartsWith1OnValid11DigitNumber() SKIPPED

PhoneNumberTest > invalidWhen11DigitsDoesNotStartWith1() SKIPPED

PhoneNumberTest > invalidWithLetters() SKIPPED

PhoneNumberTest > cleansNumbersWithMultipleSpaces() SKIPPED

PhoneNumberTest > cleansTheNumber() PASSED

PhoneNumberTest > validWhen11DigitsAndStartingWith1() SKIPPED

PhoneNumberTest > invalidWithPunctuations() SKIPPED

PhoneNumberTest > cleansNumbersWithDots() SKIPPED

PhoneNumberTest > validWhen11DigitsAndStartingWith1EvenWithPunctuation() SKIPPED

PhoneNumberTest > invalidIfAreaCodeStartsWith0() SKIPPED

PhoneNumberTest > invalidIfAreaCodeStartsWith1() SKIPPED

PhoneNumberTest > invalidIfExchangeCodeStartsWith0() SKIPPED

PhoneNumberTest > invalidIfExchangeCodeStartsWith1() SKIPPED

Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.7/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD SUCCESSFUL in 1s
3 actionable tasks: 3 executed
