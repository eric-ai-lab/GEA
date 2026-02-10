+ cargo test -- --include-ignored
    Updating crates.io index
     Locking 11 packages to latest compatible versions
 Downloading crates ...
  Downloaded num-conv v0.1.0
  Downloaded powerfmt v0.2.0
  Downloaded deranged v0.4.0
  Downloaded serde v1.0.219
  Downloaded time-core v0.1.4
  Downloaded time v0.3.41
   Compiling powerfmt v0.2.0
   Compiling num-conv v0.1.0
   Compiling time-core v0.1.4
   Compiling deranged v0.4.0
   Compiling time v0.3.41
   Compiling gigasecond v2.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 7.50s
     Running unittests src/lib.rs (target/debug/deps/gigasecond-9e76514c59442cac)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/gigasecond.rs (target/debug/deps/gigasecond-529884312c9e0a56)

running 5 tests
   Doc-tests gigasecond
test date_only_specification_of_time ... ok
test third_test_for_date_only_specification_of_time ... ok
test full_time_specified ... ok
test full_time_with_day_roll_over ... ok
test second_test_for_date_only_specification_of_time ... ok

test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s


running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

