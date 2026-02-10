+ ./gradlew test
Downloading https://services.gradle.org/distributions/gradle-8.7-bin.zip
............10%.............20%.............30%.............40%............50%.............60%.............70%.............80%.............90%............100%

Welcome to Gradle 8.7!

Here are the highlights of this release:
 - Compiling and testing with Java 22
 - Cacheable Groovy script compilation
 - New methods in lazy collection properties

For more details see https://docs.gradle.org/8.7/release-notes.html

Starting a Gradle Daemon (subsequent builds will be faster)
> Task :compileJava
> Task :processResources NO-SOURCE
> Task :classes
> Task :compileTestJava
> Task :processTestResources NO-SOURCE
> Task :testClasses

> Task :test

WordSearcherTest > testShouldLocateThatDifferentLeftToRightWordInADifferentPosition() SKIPPED

WordSearcherTest > testLocatesWordsWrittenTopRightToBottomLeft() SKIPPED

WordSearcherTest > testAcceptsInitialGridAndTargetWord() PASSED

WordSearcherTest > testNotWrapAroundVerticallyToFindAWord() SKIPPED

WordSearcherTest > testShouldLocateMultipleWords() SKIPPED

WordSearcherTest > testLocatesWordsWrittenBottomRightToTopLeft() SKIPPED

WordSearcherTest > testLocatesSameWordWrittenLeftToRightInDifferentTenLineGrid() SKIPPED

WordSearcherTest > testShouldLocateMultipleWordsWrittenInDifferentHorizontalDirections() SKIPPED

WordSearcherTest > testFailsToLocateAWordsThatIsNotInThePuzzle() SKIPPED

WordSearcherTest > testShouldLocateASingleWordRightToLeft() SKIPPED

WordSearcherTest > testLocatesWordsWrittenTopToBottom() SKIPPED

WordSearcherTest > testLocatesWordWrittenLeftToRightInTenLineGrid() SKIPPED

WordSearcherTest > testFailToLocateWordsThatAreNotOnHorizontalVerticalOrDiagonalLines() SKIPPED

WordSearcherTest > testLocatesWordsWrittenTopLeftToBottomRight() SKIPPED

WordSearcherTest > testLocatesWordsWrittenBottomToTop() SKIPPED

WordSearcherTest > testShouldLocateLeftToRightWordInThreeLineGrid() SKIPPED

WordSearcherTest > testNotConcatenateDifferentLinesToFindAHorizontalWord() SKIPPED

WordSearcherTest > testNotWrapAroundHorizontallyToFindAWord() SKIPPED

WordSearcherTest > testLocatesOneWordWrittenLeftToRight() SKIPPED

WordSearcherTest > testLocatesDifferentWordWrittenLeftToRightInTenLineGrid() SKIPPED

WordSearcherTest > testShouldLocateTheSameWordLeftToRightInDifferentPosition() SKIPPED

WordSearcherTest > testShouldLocateADifferentLeftToRightWord() SKIPPED

WordSearcherTest > testShouldLocateLeftToRightWordInTwoLineGrid() SKIPPED

WordSearcherTest > testLocatesWordsWrittenBottomLeftToTopRight() SKIPPED

Deprecated Gradle features were used in this build, making it incompatible with Gradle 9.0.

You can use '--warning-mode all' to show the individual deprecation warnings and determine if they come from your own scripts or plugins.

For more on this, please refer to https://docs.gradle.org/8.7/userguide/command_line_interface.html#sec:command_line_warnings in the Gradle documentation.

BUILD SUCCESSFUL in 15s
3 actionable tasks: 3 executed
