+ cargo test -- --include-ignored
   Compiling two-bucket v1.4.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.70s
     Running unittests src/lib.rs (target/debug/deps/two_bucket-4f5f52090078ec77)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/two-bucket.rs (target/debug/deps/two_bucket-20366ad1af3d7319)

running 9 tests
test goal_larger_than_both_buckets_is_impossible ... ok
test measure_one_step_using_bucket_one_of_size_1_and_bucket_two_of_size_3_start_with_bucket_two ... ok
test measure_using_bucket_one_of_size_2_and_bucket_two_of_size_3_start_with_bucket_one_and_end_with_bucket_two ... ok
test measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_two ... ok
test measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_one ... ok
test measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_one ... ok
test measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_two ... ok
test with_the_same_buckets_but_a_different_goal_then_it_is_possible ... ok
test not_possible_to_reach_the_goal ... ok

test result: ok. 9 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests two_bucket

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

