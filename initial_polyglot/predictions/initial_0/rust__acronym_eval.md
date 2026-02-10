+ cargo test -- --include-ignored
   Compiling acronym v1.7.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 3.41s
     Running unittests src/lib.rs (target/debug/deps/acronym-01ff2b672c2f9633)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/acronym.rs (target/debug/deps/acronym-4899727a2932a8b4)

running 10 tests
test all_caps_word ... ok
test apostrophes ... FAILED
test basic ... ok
test camelcase ... FAILED
test consecutive_delimiters ... ok
test lowercase_words ... ok
test punctuation ... ok
test underscore_emphasis ... ok
test very_long_abbreviation ... ok
test punctuation_without_whitespace ... ok

failures:

---- apostrophes stdout ----

thread 'apostrophes' panicked at tests/acronym.rs:71:5:
assertion `left == right` failed
  left: "HSC"
 right: "HC"
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- camelcase stdout ----

thread 'camelcase' panicked at tests/acronym.rs:89:5:
assertion `left == right` failed
  left: "HML"
 right: "HTML"


failures:
    apostrophes
    camelcase

test result: FAILED. 8 passed; 2 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test acronym`
