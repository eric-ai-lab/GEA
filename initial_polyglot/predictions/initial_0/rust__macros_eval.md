+ cargo test -- --include-ignored
   Compiling macros v0.1.0 (/testbed)
warning: variable does not need to be mutable
  --> src/lib.rs:10:14
   |
10 |          let mut hm = ::std::collections::HashMap::new();
   |              ----^^
   |              |
   |              help: remove this `mut`
...
23 |         let map: ::std::collections::HashMap<i32, i32> = hashmap!();
   |                                                          ---------- in this macro invocation
   |
   = note: `#[warn(unused_mut)]` on by default
   = note: this warning originates in the macro `hashmap` (in Nightly builds, run with -Z macro-backtrace for more info)

warning: `macros` (lib test) generated 1 warning (run `cargo fix --lib -p macros --tests` to apply 1 suggestion)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 1.01s
     Running unittests src/lib.rs (target/debug/deps/macros-3011f7f98e0e27f1)

running 2 tests
test tests::test_hashmap_macro ... ok
test tests::test_hashmap_macro_empty ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/macros.rs (target/debug/deps/macros-a730441bf4cb1436)

running 18 tests
test nested ... ok
test empty ... ok
test no_trailing_comma ... ok
test single ... ok
test test::macro_out_of_scope ... ok
test test::type_not_in_scope ... ok
test trailing_comma ... ok
test type_override ... ok
test compile_fails_two_arrows ... ok
test compile_fails_triple_arguments ... ok
test compile_fails_leading_comma ... ok
test compile_fails_double_commas ... ok
test compile_fails_single_argument ... ok
test compile_fails_comma_sep ... ok
test compile_fails_only_comma ... FAILED
test compile_fails_no_comma ... ok
test compile_fails_missing_argument ... ok
test compile_fails_only_arrow ... ok

failures:

---- compile_fails_only_comma stdout ----

thread 'compile_fails_only_comma' panicked at tests/macros.rs:208:13:
Expected "tests/invalid/only-comma.rs" to fail to compile, but it succeeded.
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    compile_fails_only_comma

test result: FAILED. 17 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 1.03s

error: test failed, to rerun pass `--test macros`
