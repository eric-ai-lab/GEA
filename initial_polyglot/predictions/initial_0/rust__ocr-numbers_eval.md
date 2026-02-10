+ cargo test -- --include-ignored
   Compiling ocr-numbers v0.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.68s
     Running unittests src/lib.rs (target/debug/deps/ocr_numbers-7d145ebe7dc27bd5)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/ocr-numbers.rs (target/debug/deps/ocr_numbers-7aa0c5d898cf4603)

running 17 tests
test input_with_columns_not_multiple_of_three_is_error ... ok
test input_with_lines_not_multiple_of_four_is_error ... ok
test numbers_across_multiple_lines_are_joined_by_commas ... ok
test recognizes_0 ... ok
test recognizes_1 ... ok
test recognizes_110101100 ... ok
test recognizes_2 ... ok
test recognizes_3 ... ok
test recognizes_5 ... ok
test recognizes_4 ... ok
test recognizes_6 ... ok
test recognizes_7 ... ok
test recognizes_8 ... ok
test recognizes_9 ... ok
test recognizes_string_of_decimal_numbers ... ok
test replaces_only_garbled_numbers_with_question_mark ... ok
test unrecognized_characters_return_question_mark ... ok

test result: ok. 17 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests ocr_numbers

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

