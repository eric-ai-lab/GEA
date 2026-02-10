+ cargo test -- --include-ignored
    Updating crates.io index
     Locking 15 packages to latest compatible versions
      Adding rand v0.8.5 (available: v0.9.2)
   Compiling libc v0.2.180
   Compiling zerocopy v0.8.33
   Compiling cfg-if v1.0.4
   Compiling lazy_static v1.5.0
   Compiling getrandom v0.2.17
   Compiling rand_core v0.6.4
   Compiling ppv-lite86 v0.2.21
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling robot-name v0.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 3.24s
     Running unittests src/lib.rs (target/debug/deps/robot_name-667ab996fbe3979b)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/robot-name.rs (target/debug/deps/robot_name-9b33eee667234762)

running 5 tests
test different_robots_have_different_names ... ok
test name_should_match_expected_pattern ... ok
test new_name_is_different_from_old_name ... ok
test new_name_should_match_expected_pattern ... ok
test many_different_robots_have_different_names ... ok

test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.03s

   Doc-tests robot_name

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

