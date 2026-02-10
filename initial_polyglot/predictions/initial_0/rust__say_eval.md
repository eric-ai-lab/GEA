+ cargo test -- --include-ignored
   Compiling say v1.2.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.68s
     Running unittests src/lib.rs (target/debug/deps/say-d0aa4686987cadf8)

running 3 tests
test tests::test_basic ... ok
test tests::test_u64_max ... ok
test tests::test_thousands ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/say.rs (target/debug/deps/say-a2049abf41438ea5)

running 19 tests
test fourteen ... ok
test a_big_number ... ok
test max_i64 ... ok
test max_u64 ... ok
test nine_hundred_ninety_nine ... ok
test ninety_nine ... ok
test one ... ok
test one_billion ... ok
test one_hundred ... ok
test one_hundred_twenty_three ... ok
test one_million ... ok
test one_million_two_thousand_three_hundred_forty_five ... ok
test one_thousand ... ok
test one_thousand_two_hundred_thirty_four ... ok
test thirty ... ok
test twenty ... ok
test twenty_two ... ok
test two_hundred ... ok
test zero ... ok

test result: ok. 19 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests say

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

