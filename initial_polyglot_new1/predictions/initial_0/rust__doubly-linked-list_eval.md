+ cargo test -- --include-ignored
   Compiling doubly-linked-list v0.0.0 (/testbed)
warning: trait `AssertSend` is never used
   --> tests/doubly-linked-list.rs:300:11
    |
300 |     trait AssertSend: Send {}
    |           ^^^^^^^^^^
    |
    = note: `#[warn(dead_code)]` (part of `#[warn(unused)]`) on by default

warning: trait `AssertSync` is never used
   --> tests/doubly-linked-list.rs:301:11
    |
301 |     trait AssertSync: Sync {}
    |           ^^^^^^^^^^

warning: `doubly-linked-list` (test "doubly-linked-list") generated 2 warnings
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.40s
     Running unittests src/lib.rs (target/debug/deps/doubly_linked_list-60c7a6fbc34e5c9d)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/doubly-linked-list.rs (target/debug/deps/doubly_linked_list-0d13a38d60d936a0)

running 19 tests
test advanced_is_covariant ... ok
test advanced_linked_list_is_send_sync ... ok
test basics_empty_list ... ok
test basics_push_back_pop_front ... ok
test basics_push_front_pop_back ... ok
test basics_push_pop_at_back ... ok
test basics_push_pop_at_front ... ok
test basics_single_element_back ... ok
test basics_single_element_front ... ok
test cursor_insert_after_in_middle ... ok
test cursor_insert_before_in_middle ... ok
test cursor_insert_before_on_empty_list ... ok
test cursor_next_and_peek ... ok
test cursor_prev_and_peek ... ok
test cursor_take ... ok
test drop_no_double_frees ... ok
test is_generic ... ok
test iter ... ok
test drop_large_list ... ok

test result: ok. 19 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.37s

     Running tests/step_4_leak_test_1.rs (target/debug/deps/step_4_leak_test_1-f095d7d93da06d5a)

running 1 test
test drop_no_leak_when_removing_single_element ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/step_4_leak_test_2.rs (target/debug/deps/step_4_leak_test_2-c30e901a348ecdf8)

running 1 test
test drop_no_leaks ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests doubly_linked_list

running 2 tests
test src/pre_implemented.rs - pre_implemented::IllegalSync (line 72) - compile fail ... ok
test src/pre_implemented.rs - pre_implemented::IllegalSend (line 63) - compile fail ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.06s

