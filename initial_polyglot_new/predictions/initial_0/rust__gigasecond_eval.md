+ cargo test -- --include-ignored
    Updating crates.io index
     Locking 12 packages to latest compatible versions
   Compiling powerfmt v0.2.0
   Compiling num-conv v0.1.0
   Compiling time-core v0.1.6
   Compiling deranged v0.5.5
   Compiling time v0.3.44
   Compiling gigasecond v2.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 2.18s
     Running unittests src/lib.rs (target/debug/deps/gigasecond-537e44f2cb8dd964)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/gigasecond.rs (target/debug/deps/gigasecond-8ccb65c1a6f10f83)

running 5 tests
test date_only_specification_of_time ... ok
test full_time_specified ... ok
test full_time_with_day_roll_over ... ok
test second_test_for_date_only_specification_of_time ... ok
test third_test_for_date_only_specification_of_time ... ok

test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests gigasecond

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

