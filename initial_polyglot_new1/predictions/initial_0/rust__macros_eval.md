+ cargo test -- --include-ignored
   Compiling macros v0.1.0 (/testbed)
error[E0308]: mismatched types
   --> tests/macros.rs:112:55
    |
112 |     let _empty: ::std::collections::HashMap<(), ()> = hashmap!();
    |                 -----------------------------------   ^^^^^^^^^^ expected `HashMap<(), ()>`, found `HashMap`
    |                 |
    |                 expected due to this
    |
    = note: `type_override::std::collections::HashMap` and `std::collections::HashMap<(), ()>` have similar names, but are actually distinct types
note: `type_override::std::collections::HashMap` is defined in the current crate
   --> tests/macros.rs:96:13
    |
 96 |             pub struct HashMap;
    |             ^^^^^^^^^^^^^^^^^^
note: `std::collections::HashMap<(), ()>` is defined in crate `std`
   --> /rustc/ded5c06cf21d2b93bffd5d884aa6e96934ee4234/library/std/src/collections/hash/map.rs:246:1
    = note: this error originates in the macro `hashmap` (in Nightly builds, run with -Z macro-backtrace for more info)

For more information about this error, try `rustc --explain E0308`.
error: could not compile `macros` (test "macros") due to 1 previous error
warning: build failed, waiting for other jobs to finish...
