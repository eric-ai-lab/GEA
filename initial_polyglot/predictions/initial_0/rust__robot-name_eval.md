+ cargo test -- --include-ignored
   Compiling robot-name v0.0.0 (/testbed)
error[E0463]: can't find crate for `lazy_static`
  --> src/lib.rs:10:1
   |
10 | extern crate lazy_static;
   | ^^^^^^^^^^^^^^^^^^^^^^^^^ can't find crate

error[E0432]: unresolved import `rand`
 --> src/lib.rs:1:5
  |
1 | use rand::Rng;
  |     ^^^^ use of undeclared crate or module `rand`

error: cannot find macro `lazy_static` in this scope
  --> src/lib.rs:12:1
   |
12 | lazy_static! {
   | ^^^^^^^^^^^
   |
note: `lazy_static` is imported here, but it is an unresolved item, not a macro
  --> src/lib.rs:10:1
   |
10 | extern crate lazy_static;
   | ^^^^^^^^^^^^^^^^^^^^^^^^^

error[E0425]: cannot find value `USED_NAMES` in this scope
  --> src/lib.rs:38:24
   |
38 |         let mut used = USED_NAMES.lock().unwrap();
   |                        ^^^^^^^^^^ not found in this scope

error[E0425]: cannot find value `USED_NAMES` in this scope
  --> src/lib.rs:76:28
   |
76 |             let mut used = USED_NAMES.lock().unwrap();
   |                            ^^^^^^^^^^ not found in this scope

warning: unused import: `std::collections::HashSet`
 --> src/lib.rs:3:5
  |
3 | use std::collections::HashSet;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default

warning: unused import: `std::sync::Mutex`
 --> src/lib.rs:4:5
  |
4 | use std::sync::Mutex;
  |     ^^^^^^^^^^^^^^^^

error[E0433]: failed to resolve: use of undeclared crate or module `rand`
  --> src/lib.rs:18:19
   |
18 |     let mut rng = rand::thread_rng();
   |                   ^^^^ use of undeclared crate or module `rand`

Some errors have detailed explanations: E0425, E0432, E0433, E0463.
For more information about an error, try `rustc --explain E0425`.
warning: `robot-name` (lib) generated 2 warnings (2 duplicates)
error: could not compile `robot-name` (lib) due to 6 previous errors; 2 warnings emitted
warning: build failed, waiting for other jobs to finish...
warning: `robot-name` (lib test) generated 2 warnings
error: could not compile `robot-name` (lib test) due to 6 previous errors; 2 warnings emitted
