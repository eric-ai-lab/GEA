+ cargo test -- --include-ignored
   Compiling wordy v1.5.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.59s
     Running unittests src/lib.rs (target/debug/deps/wordy-700213af80ce0518)

running 11 tests
test tests::test_addition ... ok
test tests::test_division ... ok
test tests::test_division_by_zero ... ok
test tests::test_exponentiation_without_feature ... ok
test tests::test_invalid_syntax ... ok
test tests::test_invalid_question ... ok
test tests::test_multiple_operations ... ok
test tests::test_numbers ... ok
test tests::test_subtraction ... ok
test tests::test_multiplication ... ok
test tests::test_unsupported_operation ... ok

test result: ok. 11 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/wordy.rs (target/debug/deps/wordy-4bef527a64e7b23d)

running 23 tests
test addition ... ok
test addition_and_subtraction ... ok
test addition_and_multiplication ... ok
test addition_with_negative_numbers ... ok
test division ... ok
test just_a_number ... ok
test large_addition ... ok
test more_addition ... ok
test multiple_division ... ok
test multiple_additions ... ok
test multiple_multiplication ... ok
test multiplication ... ok
test multiple_subtraction ... ok
test non_math_question ... ok
test reject_postfix_notation ... ok
test reject_prefix_notation ... ok
test reject_problem_missing_an_operand ... ok
test reject_problem_with_no_operands_or_operators ... FAILED
test reject_two_operations_in_a_row ... ok
test reject_two_numbers_in_a_row ... ok
test subtraction_then_addition ... ok
test unknown_operation ... ok
test subtraction ... ok

failures:

---- reject_problem_with_no_operands_or_operators stdout ----

thread 'reject_problem_with_no_operands_or_operators' panicked at src/lib.rs:9:27:
begin <= end (8 <= 7) when slicing `What is?`
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    reject_problem_with_no_operands_or_operators

test result: FAILED. 22 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

error: test failed, to rerun pass `--test wordy`
