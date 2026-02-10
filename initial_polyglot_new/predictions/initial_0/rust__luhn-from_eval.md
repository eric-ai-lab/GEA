+ cargo test -- --include-ignored
   Compiling luhn-from v0.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.35s
     Running unittests src/lib.rs (target/debug/deps/luhn_from-85e0337faf8738bf)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/luhn-from.rs (target/debug/deps/luhn_from-793b56dbf66b04fe)

running 14 tests
test input_digit_9_is_still_correctly_converted_to_output_digit_9 ... ok
test invalid_canadian_sin_is_invalid ... ok
test invalid_credit_card_is_invalid ... ok
test single_digit_string_is_invalid ... ok
test single_zero_string_is_invalid ... ok
test strings_that_contain_non_digits_are_invalid ... ok
test valid_canadian_sin_is_valid ... ok
test you_can_validate_from_a_str ... ok
test you_can_validate_from_a_string ... ok
test you_can_validate_from_a_u16 ... ok
test you_can_validate_from_a_u32 ... ok
test you_can_validate_from_a_u64 ... ok
test you_can_validate_from_a_u8 ... ok
test you_can_validate_from_a_usize ... ok

test result: ok. 14 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests luhn_from

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

