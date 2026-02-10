+ cargo test -- --include-ignored
   Compiling accumulate v0.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.39s
     Running unittests src/lib.rs (target/debug/deps/accumulate-9ed237c45ec2c342)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/accumulate.rs (target/debug/deps/accumulate-259825a28bc5ef81)

running 12 tests
test accumulate_empty ... ok
test accumulate_recursively ... ok
test accumulate_reversed_strings ... ok
test accumulate_squares ... ok
test accumulate_upcases ... ok
test change_in_type ... ok
test closure ... ok
test closure_floats ... ok
test func_single ... ok
test minimal_bounds_on_input_and_output ... ok
test mutating_closure ... ok
test strings ... ok

test result: ok. 12 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests accumulate

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

