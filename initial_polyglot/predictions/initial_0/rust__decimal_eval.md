+ cargo test -- --include-ignored
   Compiling decimal v0.1.0 (/testbed)
error[E0432]: unresolved import `num_bigint`
 --> src/lib.rs:1:5
  |
1 | use num_bigint::BigInt;
  |     ^^^^^^^^^^ use of undeclared crate or module `num_bigint`

error[E0432]: unresolved import `num_traits`
 --> src/lib.rs:2:5
  |
2 | use num_traits::{Zero, One};
  |     ^^^^^^^^^^ use of undeclared crate or module `num_traits`

warning: unused import: `std::str::FromStr`
 --> src/lib.rs:4:5
  |
4 | use std::str::FromStr;
  |     ^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default

For more information about this error, try `rustc --explain E0432`.
warning: `decimal` (lib test) generated 1 warning
error: could not compile `decimal` (lib test) due to 2 previous errors; 1 warning emitted
warning: build failed, waiting for other jobs to finish...
warning: `decimal` (lib) generated 1 warning (1 duplicate)
error: could not compile `decimal` (lib) due to 2 previous errors; 1 warning emitted
