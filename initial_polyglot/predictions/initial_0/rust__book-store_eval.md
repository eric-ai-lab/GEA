+ cargo test -- --include-ignored
   Compiling book_store v1.3.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 4.16s
     Running unittests src/lib.rs (target/debug/deps/book_store-ebd47dda931eb721)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/book-store.rs (target/debug/deps/book_store-67eb611317633f59)

running 18 tests
test check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five ... FAILED
test empty_basket ... FAILED
test four_different_books ... FAILED
test group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three ... FAILED
test one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size ... FAILED
test only_a_single_book ... FAILED
test three_different_books ... FAILED
test three_copies_of_first_book_and_two_each_of_remaining ... FAILED
test three_each_of_first_two_books_and_two_each_of_remaining_books ... FAILED
test two_copies_of_each_book ... FAILED
test four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three ... FAILED
test two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three ... FAILED
test two_groups_of_four_is_cheaper_than_groups_of_five_and_three ... FAILED
test two_different_books ... FAILED
test two_of_the_same_book ... FAILED
test two_each_of_first_four_books_and_one_copy_each_of_rest ... FAILED
test one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three ... FAILED
test five_different_books ... FAILED

failures:

---- check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five stdout ----

thread 'check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- empty_basket stdout ----

thread 'empty_basket' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- four_different_books stdout ----

thread 'four_different_books' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three stdout ----

thread 'group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size stdout ----

thread 'one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- only_a_single_book stdout ----

thread 'only_a_single_book' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- three_different_books stdout ----

thread 'three_different_books' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- three_copies_of_first_book_and_two_each_of_remaining stdout ----

thread 'three_copies_of_first_book_and_two_each_of_remaining' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- three_each_of_first_two_books_and_two_each_of_remaining_books stdout ----

thread 'three_each_of_first_two_books_and_two_each_of_remaining_books' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- two_copies_of_each_book stdout ----

thread 'two_copies_of_each_book' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three stdout ----

thread 'four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three stdout ----

thread 'two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- two_groups_of_four_is_cheaper_than_groups_of_five_and_three stdout ----

thread 'two_groups_of_four_is_cheaper_than_groups_of_five_and_three' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- two_different_books stdout ----

thread 'two_different_books' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- two_of_the_same_book stdout ----

thread 'two_of_the_same_book' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- two_each_of_first_four_books_and_one_copy_each_of_rest stdout ----

thread 'two_each_of_first_four_books_and_one_copy_each_of_rest' panicked at src/lib.rs:55:5:
There should be exactly 5 book types.

---- one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three stdout ----

thread 'one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three' panicked at tests/book-store.rs:155:5:
assertion `left == right` failed
  left: 7440
 right: 3360

---- five_different_books stdout ----

thread 'five_different_books' panicked at tests/book-store.rs:62:5:
assertion `left == right` failed
  left: 10000
 right: 3000


failures:
    check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five
    empty_basket
    five_different_books
    four_different_books
    four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three
    group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three
    one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three
    one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size
    only_a_single_book
    three_copies_of_first_book_and_two_each_of_remaining
    three_different_books
    three_each_of_first_two_books_and_two_each_of_remaining_books
    two_copies_of_each_book
    two_different_books
    two_each_of_first_four_books_and_one_copy_each_of_rest
    two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three
    two_groups_of_four_is_cheaper_than_groups_of_five_and_three
    two_of_the_same_book

test result: FAILED. 0 passed; 18 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.03s

error: test failed, to rerun pass `--test book-store`
