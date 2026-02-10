+ cargo test -- --include-ignored
   Compiling word-count v1.2.0 (/testbed)
error[E0433]: failed to resolve: use of undeclared crate or module `regex`
  --> src/lib.rs:28:14
   |
28 |     let re = regex::Regex::new(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)*").unwrap();
   |              ^^^^^ use of undeclared crate or module `regex`

For more information about this error, try `rustc --explain E0433`.
error: could not compile `word-count` (lib) due to 1 previous error
warning: build failed, waiting for other jobs to finish...
error: could not compile `word-count` (lib test) due to 1 previous error
