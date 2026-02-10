+ cargo test -- --include-ignored
   Compiling parallel-letter-frequency v0.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.57s
     Running unittests src/lib.rs (target/debug/deps/parallel_letter_frequency-c64734a15700f0e8)

running 12 tests
test tests::test_case_insensitive ... ok
test tests::test_empty_input ... ok
test tests::test_empty_input_multiple_workers ... ok
test tests::test_ignores_non_alphabetic ... ok
test tests::test_mixed_content ... ok
test tests::test_multiple_texts_single_worker ... ok
test tests::test_multiple_texts_multiple_workers ... ok
test tests::test_single_text_single_worker ... ok
test tests::test_single_text_zero_workers ... ok
test tests::test_unicode_letters ... ok
test tests::test_multiple_workers_more_than_texts ... ok
test tests::test_with_many_workers ... ok

test result: ok. 12 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/parallel-letter-frequency.rs (target/debug/deps/parallel_letter_frequency-35506cb6bc18e7e8)

running 10 tests
test all_three_anthems_1_worker ... ok
test case_insensitivity ... ok
test no_texts ... ok
test all_three_anthems_3_workers ... ok
test one_letter ... ok
test many_empty_lines ... ok
test numbers_dont_count ... ok
test many_times_same_text ... ok
test non_integer_multiple_of_threads ... ok
test punctuation_doesnt_count ... ok

test result: ok. 10 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests parallel_letter_frequency

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

