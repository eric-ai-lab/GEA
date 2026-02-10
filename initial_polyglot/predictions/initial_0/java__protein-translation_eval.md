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

ProteinTranslatorTest > testTryptophanRnaSequence1() SKIPPED

ProteinTranslatorTest > testTranslationOfRnaToProteinList() SKIPPED

ProteinTranslatorTest > testSequenceOfTwoProteinCodonsTranslatesIntoProteins() SKIPPED

ProteinTranslatorTest > testMethionineRnaSequence() SKIPPED

ProteinTranslatorTest > testSequenceOfTwoNonStopCodonsDoNotTranslateToAStopCodon() SKIPPED

ProteinTranslatorTest > testTranslationStopsIfStopCodonInMiddle1() SKIPPED

ProteinTranslatorTest > testTranslationStopsIfStopCodonInMiddle2() SKIPPED

ProteinTranslatorTest > testEmptyRnaSequenceResultInNoproteins() PASSED

ProteinTranslatorTest > testSequenceOfTwoDifferentProteinCodonsTranslatesIntoProteins() SKIPPED

ProteinTranslatorTest > testTyrosineRnaSequence1() SKIPPED

ProteinTranslatorTest > testTyrosineRnaSequence2() SKIPPED

ProteinTranslatorTest > testNonExistingCodonCantTranslate() SKIPPED

ProteinTranslatorTest > testIncompleteRnaSequenceCanTranslateIfValidUntilAStopCodon() SKIPPED

ProteinTranslatorTest > testTranslationStopsIfStopCodonAtEnd1() SKIPPED

ProteinTranslatorTest > testTranslationStopsIfStopCodonAtEnd2() SKIPPED

ProteinTranslatorTest > testLeucineRnaSequence1() SKIPPED

ProteinTranslatorTest > testLeucineRnaSequence2() SKIPPED

ProteinTranslatorTest > testStopRnaSequence1() SKIPPED

ProteinTranslatorTest > testStopRnaSequence2() SKIPPED

ProteinTranslatorTest > testStopRnaSequence3() SKIPPED

ProteinTranslatorTest > testPhenylalanineRnaSequence1() SKIPPED

ProteinTranslatorTest > testPhenylalanineRnaSequence2() SKIPPED

ProteinTranslatorTest > testUnknownAminoAcidsNotPartOfACodonCantTranslate() SKIPPED

ProteinTranslatorTest > testSerineRnaSequence1() SKIPPED

ProteinTranslatorTest > testSerineRnaSequence2() SKIPPED

ProteinTranslatorTest > testSerineRnaSequence3() SKIPPED

ProteinTranslatorTest > testSerineRnaSequence4() SKIPPED

ProteinTranslatorTest > testTranslationStopsIfStopCodonAtBeginning() SKIPPED

ProteinTranslatorTest > testIncompleteRnaSequenceCantTranslate() SKIPPED

ProteinTranslatorTest > testCysteineRnaSequence1() SKIPPED

ProteinTranslatorTest > testCysteineRnaSequence2() SKIPPED
