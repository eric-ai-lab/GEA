+ cargo test -- --include-ignored
   Compiling book_store v1.3.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.42s
     Running unittests src/lib.rs (target/debug/deps/book_store-cbcab676436fae88)

running 10 tests
test tests::test_empty ... ok
test tests::test_four_different_books ... ok
test tests::test_multiple_copies_same_book ... ok
test tests::test_single_book ... ok
test tests::test_five_different_books ... ok
test tests::test_three_different_books ... ok
test tests::test_two_copies_different_books ... ok
test tests::test_two_copies_each_two_books ... ok
test tests::test_two_different_books ... ok
test tests::test_example_from_problem ... ok

test result: ok. 10 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/book-store.rs (target/debug/deps/book_store-f5e484a3525e67ab)

running 18 tests
test empty_basket ... ok
test only_a_single_book ... ok
test three_different_books ... FAILED
test two_different_books ... FAILED
test four_different_books ... FAILED
test two_of_the_same_book ... FAILED
test one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three ... FAILED
test five_different_books ... FAILED
test group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three ... FAILED
test two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three ... FAILED
test two_groups_of_four_is_cheaper_than_groups_of_five_and_three ... FAILED
test two_each_of_first_four_books_and_one_copy_each_of_rest ... FAILED
test check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five has been running for over 60 seconds
test four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three has been running for over 60 seconds
test one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size has been running for over 60 seconds
test three_copies_of_first_book_and_two_each_of_remaining has been running for over 60 seconds
test three_each_of_first_two_books_and_two_each_of_remaining_books has been running for over 60 seconds
test two_copies_of_each_book has been running for over 60 seconds
test two_copies_of_each_book ... FAILED
