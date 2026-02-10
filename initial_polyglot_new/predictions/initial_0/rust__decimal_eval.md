+ cargo test -- --include-ignored
    Updating crates.io index
     Locking 4 packages to latest compatible versions
   Compiling autocfg v1.5.0
   Compiling num-traits v0.2.19
   Compiling num-integer v0.1.46
   Compiling num-bigint v0.4.6
   Compiling decimal v0.1.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 2.54s
     Running unittests src/lib.rs (target/debug/deps/decimal-416c3169d6bfd22e)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/decimal.rs (target/debug/deps/decimal-c5556e3b37f0881c)

running 44 tests
test add ... ok
test add_away_decimal ... ok
test add_borrow ... ok
test add_borrow_integral ... ok
test add_borrow_integral_zeroes ... ok
test add_carry_over_negative ... ok
test add_carry_over_negative_with_fractional ... ok
test add_id ... ok
test add_into_fewer_digits ... ok
test add_uneven_position ... ok
test add_vary_precision ... ok
test borrow_from_negative ... ok
test carry_from_rightmost_into_integer ... ok
test carry_from_rightmost_more ... ok
test carry_from_rightmost_one ... ok
test carry_into_fractional_with_digits_to_right ... ok
test carry_into_integer ... ok
test cleanup_precision ... ok
test eq ... ok
test eq_vary_sig_digits ... ok
test explicit_positive ... ok
test gt ... ok
test gt_negative_and_zero ... ok
test gt_positive_and_negative ... ok
test gt_positive_and_zero ... ok
test gt_varying_negative_precisions ... ok
test gt_varying_positive_precisions ... ok
test lt ... ok
test mul_id ... ok
test mul ... ok
test multiply_by_negative ... ok
test ne ... ok
test negatives ... ok
test simple_partial_cmp ... ok
test sub ... ok
test sub_away_decimal ... ok
test sub_borrow ... ok
test sub_borrow_integral ... ok
test sub_borrow_integral_zeroes ... ok
test sub_carry_over_negative ... ok
test sub_carry_over_negative_with_fractional ... ok
test sub_id ... ok
test sub_into_fewer_digits ... ok
test unequal_number_of_decimal_places ... ok

test result: ok. 44 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

   Doc-tests decimal

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

