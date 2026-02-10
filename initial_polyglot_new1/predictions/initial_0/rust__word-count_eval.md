+ cargo test -- --include-ignored
   Compiling word-count v1.2.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.45s
     Running unittests src/lib.rs (target/debug/deps/word_count-81be8b6b302d61a2)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/word-count.rs (target/debug/deps/word_count-aaee11d8340a9b5e)

running 14 tests
test alternating_word_separators_not_detected_as_a_word ... ok
test count_one_of_each_word ... ok
test count_one_word ... ok
test handles_cramped_lists ... ok
test handles_expanded_lists ... ok
test ignore_punctuation ... ok
test include_numbers ... ok
test multiple_occurrences_of_a_word ... ok
test multiple_spaces_not_detected_as_a_word ... ok
test normalize_case ... ok
test quotation_for_word_with_apostrophe ... ok
test substrings_from_the_beginning ... ok
test with_apostrophes ... ok
test with_quotations ... ok

test result: ok. 14 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests word_count

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

