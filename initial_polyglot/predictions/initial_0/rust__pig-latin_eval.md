+ cargo test -- --include-ignored
   Compiling pig-latin v1.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.72s
     Running unittests src/lib.rs (target/debug/deps/pig_latin-b84091c2ddcca8f8)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/pig-latin.rs (target/debug/deps/pig_latin-8c55d860a0828935)

running 22 tests
test a_whole_phrase ... ok
test word_beginning_with_a ... ok
test word_beginning_with_a_vowel_and_followed_by_a_qu ... ok
test word_beginning_with_ch ... ok
test word_beginning_with_e ... ok
test word_beginning_with_i ... ok
test word_beginning_with_k ... ok
test word_beginning_with_o ... ok
test word_beginning_with_p ... ok
test word_beginning_with_qu ... ok
test word_beginning_with_q_without_a_following_u ... ok
test word_beginning_with_qu_and_a_preceding_consonant ... ok
test word_beginning_with_sch ... ok
test word_beginning_with_th ... ok
test word_beginning_with_thr ... ok
test word_beginning_with_u ... ok
test word_beginning_with_xr ... ok
test word_beginning_with_x ... ok
test word_beginning_with_yt ... ok
test y_as_second_letter_in_two_letter_word ... ok
test y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster ... ok
test y_is_treated_like_a_consonant_at_the_beginning_of_a_word ... ok

test result: ok. 22 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests pig_latin

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

