+ cargo test -- --include-ignored
warning: no edition set: defaulting to the 2015 edition while the latest is 2024
   Compiling nucleotide_codons v0.1.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.74s
     Running unittests src/lib.rs (target/debug/deps/nucleotide_codons-c675e541dafc3416)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/nucleotide-codons.rs (target/debug/deps/nucleotide_codons-b692d65ce2069c98)

running 11 tests
test arginine_name ... ok
test cysteine_tgt ... ok
test cysteine_tgy ... ok
test empty_is_invalid ... ok
test isoleucine ... ok
test methionine ... ok
test stop ... ok
test too_long_is_invalid ... ok
test too_short_is_invalid ... ok
test valine ... ok
test x_is_not_shorthand_so_is_invalid ... ok

test result: ok. 11 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests nucleotide_codons

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

