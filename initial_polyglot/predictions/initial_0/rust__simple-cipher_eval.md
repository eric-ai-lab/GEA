+ cargo test -- --include-ignored
    Updating crates.io index
     Locking 14 packages to latest compatible versions
      Adding rand v0.8.5 (available: v0.9.1)
 Downloading crates ...
  Downloaded cfg-if v1.0.0
  Downloaded ppv-lite86 v0.2.21
  Downloaded rand_core v0.6.4
  Downloaded rand_chacha v0.3.1
  Downloaded getrandom v0.2.16
  Downloaded rand v0.8.5
  Downloaded zerocopy v0.8.25
  Downloaded libc v0.2.172
   Compiling libc v0.2.172
   Compiling zerocopy v0.8.25
   Compiling cfg-if v1.0.0
   Compiling getrandom v0.2.16
   Compiling rand_core v0.6.4
   Compiling ppv-lite86 v0.2.21
   Compiling rand_chacha v0.3.1
   Compiling rand v0.8.5
   Compiling simple-cipher v0.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 4.14s
     Running unittests src/lib.rs (target/debug/deps/simple_cipher-2cf9dd390bad6ca3)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/simple-cipher.rs (target/debug/deps/simple_cipher-1989f9d91882a562)

running 23 tests
test cipher_can_decode_a_message_that_is_shorter_than_the_key ... ok
test cipher_can_double_shift_encode ... ok
test cipher_can_encode_a_message_that_is_shorter_than_the_key ... ok
test cipher_can_decode_with_given_key ... ok
test cipher_can_encode_with_given_key ... ok
test cipher_is_reversible_given_key ... ok
test cipher_can_wrap_encode ... ok
test decode_returns_none_with_an_all_caps_key ... ok
test decode_returns_none_with_an_any_caps_key ... ok
test decode_returns_none_with_any_numeric_key ... ok
test decode_returns_none_with_empty_key ... ok
test decode_returns_none_with_numeric_key ... ok
test encode_random_can_decode ... ok
test encode_random_can_encode ... ok
test encode_random_is_reversible ... ok
test encode_random_uses_key_of_100_characters_or_more ... ok
test encode_random_uses_key_made_of_letters ... ok
test encode_returns_none_with_an_all_caps_key ... ok
test encode_returns_none_with_an_any_caps_key ... ok
test encode_returns_none_with_any_numeric_key ... ok
test encode_returns_none_with_empty_key ... ok
test encode_returns_none_with_numeric_key ... ok
test encode_random_uses_randomly_generated_key ... ok

test result: ok. 23 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

   Doc-tests simple_cipher

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

