+ cargo test -- --include-ignored
   Compiling variable-length-quantity v1.2.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.67s
     Running unittests src/lib.rs (target/debug/deps/variable_length_quantity-23e93d4cf2f55a18)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/variable-length-quantity.rs (target/debug/deps/variable_length_quantity-a4c5a156dc59ef56)

running 26 tests
test arbitrary_double_byte ... ok
test arbitrary_single_byte ... ok
test arbitrary_quadruple_byte ... ok
test arbitrary_quintuple_byte ... ok
test arbitrary_triple_byte ... ok
test four_bytes ... ok
test incomplete_sequence_causes_error ... ok
test incomplete_sequence_causes_error_even_if_value_is_zero ... ok
test largest_double_byte ... ok
test largest_quadruple_byte ... ok
test largest_single_byte ... ok
test largest_triple_byte ... ok
test many_multi_byte_values ... ok
test maximum_32_bit_integer ... ok
test maximum_32_bit_integer_input ... ok
test multiple_values ... ok
test one_byte ... ok
test smallest_double_byte ... ok
test smallest_quadruple_byte ... ok
test smallest_quintuple_byte ... ok
test smallest_triple_byte ... ok
test three_bytes ... ok
test two_bytes ... ok
test two_multi_byte_values ... ok
test two_single_byte_values ... ok
test zero ... ok

test result: ok. 26 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

   Doc-tests variable_length_quantity

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

