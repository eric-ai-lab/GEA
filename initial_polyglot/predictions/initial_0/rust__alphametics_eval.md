+ cargo test -- --include-ignored
   Compiling alphametics v1.3.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 6.47s
     Running unittests src/lib.rs (target/debug/deps/alphametics-164acc9d0b31bd5d)

running 2 tests
test tests::test_send_more_money ... ok
test tests::test_no_solution has been running for over 60 seconds
test tests::test_no_solution ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 60.42s

     Running tests/alphametics.rs (target/debug/deps/alphametics-a12dfd4d0cec00cf)

running 10 tests
error: test failed, to rerun pass `--test alphametics`
test leading_zero_solution_is_invalid ... ok
test puzzle_with_eight_letters ... FAILED
test puzzle_with_seven_letters ... FAILED
test puzzle_with_four_letters ... FAILED
test puzzle_with_six_letters ... FAILED
test puzzle_with_ten_letters ... FAILED
test puzzle_with_three_letters ... FAILED
test puzzle_with_ten_letters_and_199_addends ... FAILED
test solution_must_have_unique_value_for_each_letter ... ok
test puzzle_with_two_digits_final_carry ... FAILED

failures:

---- puzzle_with_eight_letters stdout ----

thread 'puzzle_with_eight_letters' panicked at tests/alphametics.rs:86:5:
assertion `left == right` failed
  left: None
 right: Some({'D': 7, 'R': 8, 'Y': 2, 'O': 0, 'N': 6, 'S': 9, 'E': 5, 'M': 1})
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- puzzle_with_seven_letters stdout ----

thread 'puzzle_with_seven_letters' panicked at tests/alphametics.rs:67:5:
assertion `left == right` failed
  left: None
 right: Some({'T': 7, 'H': 5, 'E': 4, 'L': 1, 'I': 0, 'S': 9, 'G': 2})

---- puzzle_with_four_letters stdout ----

thread 'puzzle_with_four_letters' panicked at tests/alphametics.rs:39:5:
assertion `left == right` failed
  left: None
 right: Some({'S': 2, 'A': 9, 'M': 1, 'O': 0})

---- puzzle_with_six_letters stdout ----

thread 'puzzle_with_six_letters' panicked at tests/alphametics.rs:49:5:
assertion `left == right` failed
  left: None
 right: Some({'T': 9, 'L': 1, 'E': 2, 'N': 7, 'A': 0, 'O': 4})

---- puzzle_with_ten_letters stdout ----

thread 'puzzle_with_ten_letters' panicked at tests/alphametics.rs:107:5:
assertion `left == right` failed
  left: None
 right: Some({'N': 0, 'D': 3, 'F': 7, 'O': 2, 'A': 5, 'R': 1, 'T': 9, 'G': 8, 'E': 4, 'S': 6})

---- puzzle_with_three_letters stdout ----

thread 'puzzle_with_three_letters' panicked at tests/alphametics.rs:7:5:
assertion `left == right` failed
  left: None
 right: Some({'L': 0, 'B': 9, 'I': 1})

---- puzzle_with_ten_letters_and_199_addends stdout ----

thread 'puzzle_with_ten_letters_and_199_addends' panicked at tests/alphametics.rs:128:5:
assertion `left == right` failed
  left: None
 right: Some({'T': 9, 'H': 8, 'S': 4, 'O': 6, 'A': 1, 'F': 5, 'I': 7, 'R': 3, 'E': 0, 'L': 2})

---- puzzle_with_two_digits_final_carry stdout ----

thread 'puzzle_with_two_digits_final_carry' panicked at tests/alphametics.rs:29:5:
assertion `left == right` failed
  left: None
 right: Some({'B': 1, 'C': 0, 'A': 9})


failures:
    puzzle_with_eight_letters
    puzzle_with_four_letters
    puzzle_with_seven_letters
    puzzle_with_six_letters
    puzzle_with_ten_letters
    puzzle_with_ten_letters_and_199_addends
    puzzle_with_three_letters
    puzzle_with_two_digits_final_carry

test result: FAILED. 2 passed; 8 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

