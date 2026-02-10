+ cargo test -- --include-ignored
   Compiling forth v1.7.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.55s
     Running unittests src/lib.rs (target/debug/deps/forth-23318c838192ec35)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/alloc-attack.rs (target/debug/deps/alloc_attack-f9d387ccdcbb6b82)

running 1 test
test alloc_attack ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/forth.rs (target/debug/deps/forth-635419b7959d9b8a)

running 49 tests
test addition::can_add_two_numbers ... ok
test addition::errors_if_there_is_nothing_on_the_stack ... ok
test addition::errors_if_there_is_only_one_value_on_the_stack ... ok
test case_insensitivity::definitions_are_case_insensitive ... ok
test case_insensitivity::drop_is_case_insensitive ... ok
test case_insensitivity::dup_is_case_insensitive ... ok
test case_insensitivity::over_is_case_insensitive ... ok
test case_insensitivity::swap_is_case_insensitive ... ok
test case_insensitivity::user_defined_words_are_case_insensitive ... ok
test combined_arithmetic::addition_and_subtraction ... ok
test combined_arithmetic::multiplication_and_division ... ok
test division::can_divide_two_numbers ... ok
test division::errors_if_dividing_by_zero ... ok
test division::errors_if_there_is_nothing_on_the_stack ... ok
test division::errors_if_there_is_only_one_value_on_the_stack ... ok
test division::performs_integer_division ... ok
test drop::errors_if_there_is_nothing_on_the_stack ... ok
test drop::removes_the_top_value_on_the_stack_if_it_is_not_the_only_one ... ok
test drop::removes_the_top_value_on_the_stack_if_it_is_the_only_one ... ok
test dup::copies_a_value_on_the_stack ... ok
test dup::copies_the_top_value_on_the_stack ... ok
test dup::errors_if_there_is_nothing_on_the_stack ... ok
test multiplication::can_multiply_two_numbers ... ok
test multiplication::errors_if_there_is_nothing_on_the_stack ... ok
test multiplication::errors_if_there_is_only_one_value_on_the_stack ... ok
test over::copies_the_second_element_if_there_are_more_than_two ... ok
test over::copies_the_second_element_if_there_are_only_two ... ok
test over::errors_if_there_is_nothing_on_the_stack ... ok
test over::errors_if_there_is_only_one_value_on_the_stack ... ok
test parsing_and_numbers::numbers_just_get_pushed_onto_the_stack ... ok
test parsing_and_numbers::pushes_negative_numbers_onto_the_stack ... ok
test subtraction::can_subtract_two_numbers ... ok
test subtraction::errors_if_there_is_nothing_on_the_stack ... ok
test subtraction::errors_if_there_is_only_one_value_on_the_stack ... ok
test swap::errors_if_there_is_nothing_on_the_stack ... ok
test swap::errors_if_there_is_only_one_value_on_the_stack ... ok
test swap::swaps_the_top_two_values_on_the_stack_if_they_are_not_the_only_ones ... ok
test swap::swaps_the_top_two_values_on_the_stack_if_they_are_the_only_ones ... ok
test user_defined_words::can_consist_of_built_in_words ... ok
test user_defined_words::can_define_word_that_uses_word_with_the_same_name ... ok
test user_defined_words::can_override_built_in_operators ... ok
test user_defined_words::can_override_built_in_words ... ok
test user_defined_words::can_override_other_user_defined_words ... ok
test user_defined_words::can_use_different_words_with_the_same_name ... ok
test user_defined_words::cannot_redefine_negative_numbers ... ok
test user_defined_words::cannot_redefine_non_negative_numbers ... ok
test user_defined_words::errors_if_executing_a_non_existent_word ... ok
test user_defined_words::execute_in_the_right_order ... ok
test user_defined_words::only_defines_locally ... ok

test result: ok. 49 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

   Doc-tests forth

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

