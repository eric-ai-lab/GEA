+ cargo test -- --include-ignored
   Compiling accumulate v0.0.0 (/testbed)
error[E0308]: mismatched types
  --> tests/accumulate.rs:43:20
   |
43 |     assert_eq!(map(input, |x| x * x), expected);
   |                --- ^^^^^ expected `Vec<i32>`, found `Vec<{float}>`
   |                |
   |                arguments to this function are incorrect
   |
   = note: expected struct `Vec<i32>`
              found struct `Vec<{float}>`
note: function defined here
  --> /testbed/src/lib.rs:6:8
   |
6  | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
   |        ^^^

error[E0277]: can't compare `i32` with `{float}`
  --> tests/accumulate.rs:43:5
   |
43 |     assert_eq!(map(input, |x| x * x), expected);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ no implementation for `i32 == {float}`
   |
   = help: the trait `PartialEq<{float}>` is not implemented for `i32`
           but trait `PartialEq<i32>` is implemented for it
   = help: for that trait implementation, expected `i32`, found `{float}`
   = note: required for `Vec<i32>` to implement `PartialEq<Vec<{float}>>`
   = note: this error originates in the macro `assert_eq` (in Nightly builds, run with -Z macro-backtrace for more info)

error[E0599]: no method named `repeat` found for type `i32` in the current scope
  --> tests/accumulate.rs:51:33
   |
51 |     assert_eq!(map(input, |s| s.repeat(2)), expected);
   |                                 ^^^^^^ method not found in `i32`

error[E0308]: mismatched types
  --> tests/accumulate.rs:51:20
   |
51 |     assert_eq!(map(input, |s| s.repeat(2)), expected);
   |                --- ^^^^^ expected `Vec<i32>`, found `Vec<String>`
   |                |
   |                arguments to this function are incorrect
   |
   = note: expected struct `Vec<i32>`
              found struct `Vec<String>`
note: function defined here
  --> /testbed/src/lib.rs:6:8
   |
6  | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
   |        ^^^

error[E0277]: can't compare `i32` with `String`
  --> tests/accumulate.rs:51:5
   |
51 |     assert_eq!(map(input, |s| s.repeat(2)), expected);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ no implementation for `i32 == String`
   |
   = help: the trait `PartialEq<String>` is not implemented for `i32`
           but trait `PartialEq<i32>` is implemented for it
   = help: for that trait implementation, expected `i32`, found `String`
   = note: required for `Vec<i32>` to implement `PartialEq<Vec<String>>`
   = note: this error originates in the macro `assert_eq` (in Nightly builds, run with -Z macro-backtrace for more info)

error[E0631]: type mismatch in function arguments
  --> tests/accumulate.rs:59:27
   |
59 |     assert_eq!(map(input, str::to_uppercase), expected);
   |                ---        ^^^^^^^^^^^^^^^^^
   |                |          |
   |                |          expected due to this
   |                |          found signature defined here
   |                required by a bound introduced by this call
   |
   = note: expected function signature `fn(i32) -> _`
              found function signature `fn(&str) -> _`
note: required by a bound in `accumulate::map`
  --> /testbed/src/lib.rs:8:8
   |
6  | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
   |        --- required by a bound in this function
7  | where
8  |     F: Fn(i32) -> i32,
   |        ^^^^^^^^^^^^^^ required by this bound in `map`
help: consider wrapping the function in a closure
   |
59 |     assert_eq!(map(input, |arg0: i32| str::to_uppercase(/* &str */)), expected);
   |                           +++++++++++                  ++++++++++++

error[E0308]: mismatched types
  --> tests/accumulate.rs:59:20
   |
59 |     assert_eq!(map(input, str::to_uppercase), expected);
   |                --- ^^^^^ expected `Vec<i32>`, found `Vec<&str>`
   |                |
   |                arguments to this function are incorrect
   |
   = note: expected struct `Vec<i32>`
              found struct `Vec<&str>`
note: function defined here
  --> /testbed/src/lib.rs:6:8
   |
6  | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
   |        ^^^

error[E0277]: can't compare `i32` with `&str`
  --> tests/accumulate.rs:59:5
   |
59 |     assert_eq!(map(input, str::to_uppercase), expected);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ no implementation for `i32 == &str`
   |
   = help: the trait `PartialEq<&str>` is not implemented for `i32`
           but trait `PartialEq<i32>` is implemented for it
   = help: for that trait implementation, expected `i32`, found `&str`
   = note: required for `Vec<i32>` to implement `PartialEq<Vec<&str>>`
   = note: this error originates in the macro `assert_eq` (in Nightly builds, run with -Z macro-backtrace for more info)

error[E0631]: type mismatch in closure arguments
  --> tests/accumulate.rs:68:27
   |
67 |     let reverse = |s: &str| s.chars().rev().collect::<String>();
   |                   --------- found signature defined here
68 |     assert_eq!(map(input, reverse), expected);
   |                ---        ^^^^^^^ expected due to this
   |                |
   |                required by a bound introduced by this call
   |
   = note: expected closure signature `fn(i32) -> _`
              found closure signature `fn(&str) -> _`
note: required by a bound in `accumulate::map`
  --> /testbed/src/lib.rs:8:19
   |
6  | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
   |        --- required by a bound in this function
7  | where
8  |     F: Fn(i32) -> i32,
   |                   ^^^ required by this bound in `map`
help: consider wrapping the function in a closure
   |
68 |     assert_eq!(map(input, |arg0: i32| reverse(/* &str */)), expected);
   |                           +++++++++++        ++++++++++++

error[E0308]: mismatched types
  --> tests/accumulate.rs:68:20
   |
68 |     assert_eq!(map(input, reverse), expected);
   |                --- ^^^^^ expected `Vec<i32>`, found `Vec<&str>`
   |                |
   |                arguments to this function are incorrect
   |
   = note: expected struct `Vec<i32>`
              found struct `Vec<&str>`
note: function defined here
  --> /testbed/src/lib.rs:6:8
   |
6  | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
   |        ^^^

error[E0277]: can't compare `i32` with `&str`
  --> tests/accumulate.rs:68:5
   |
68 |     assert_eq!(map(input, reverse), expected);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ no implementation for `i32 == &str`
   |
   = help: the trait `PartialEq<&str>` is not implemented for `i32`
           but trait `PartialEq<i32>` is implemented for it
   = help: for that trait implementation, expected `i32`, found `&str`
   = note: required for `Vec<i32>` to implement `PartialEq<Vec<&str>>`
   = note: this error originates in the macro `assert_eq` (in Nightly builds, run with -Z macro-backtrace for more info)

error[E0308]: mismatched types
  --> tests/accumulate.rs:81:33
   |
81 |         map(input, |x| map(vec!["1", "2", "3"], |y| [x, y].join(""))),
   |                                 ^^^ expected `i32`, found `&str`

error[E0599]: the method `join` exists for array `[i32; 2]`, but its trait bounds were not satisfied
  --> tests/accumulate.rs:81:60
   |
81 |         map(input, |x| map(vec!["1", "2", "3"], |y| [x, y].join(""))),
   |                                                            ^^^^ method cannot be called on `[i32; 2]` due to unsatisfied trait bounds
   |
   = note: the following trait bounds were not satisfied:
           `[i32]: Join<_>`

error[E0308]: mismatched types
  --> tests/accumulate.rs:81:24
   |
81 |         map(input, |x| map(vec!["1", "2", "3"], |y| [x, y].join(""))),
   |                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ expected `i32`, found `Vec<i32>`
   |
   = note: expected type `i32`
            found struct `Vec<i32>`

error[E0308]: mismatched types
  --> tests/accumulate.rs:81:13
   |
81 |         map(input, |x| map(vec!["1", "2", "3"], |y| [x, y].join(""))),
   |         --- ^^^^^ expected `Vec<i32>`, found `Vec<&str>`
   |         |
   |         arguments to this function are incorrect
   |
   = note: expected struct `Vec<i32>`
              found struct `Vec<&str>`
note: function defined here
  --> /testbed/src/lib.rs:6:8
   |
6  | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
   |        ^^^

error[E0277]: can't compare `i32` with `Vec<&str>`
  --> tests/accumulate.rs:80:5
   |
80 | /     assert_eq!(
81 | |         map(input, |x| map(vec!["1", "2", "3"], |y| [x, y].join(""))),
82 | |         expected
83 | |     );
   | |_____^ no implementation for `i32 == Vec<&str>`
   |
   = help: the trait `PartialEq<Vec<&str>>` is not implemented for `i32`
           but trait `PartialEq<i32>` is implemented for it
   = help: for that trait implementation, expected `i32`, found `Vec<&str>`
   = note: required for `Vec<i32>` to implement `PartialEq<Vec<Vec<&str>>>`
   = note: this error originates in the macro `assert_eq` (in Nightly builds, run with -Z macro-backtrace for more info)

error[E0308]: mismatched types
  --> tests/accumulate.rs:91:31
   |
91 |     assert_eq!(map(input, |s| s.to_string()), expected);
   |                               ^^^^^^^^^^^^^ expected `i32`, found `String`
   |
help: try removing the method call
   |
91 -     assert_eq!(map(input, |s| s.to_string()), expected);
91 +     assert_eq!(map(input, |s| s), expected);
   |

error[E0308]: mismatched types
  --> tests/accumulate.rs:91:20
   |
91 |     assert_eq!(map(input, |s| s.to_string()), expected);
   |                --- ^^^^^ expected `Vec<i32>`, found `Vec<&str>`
   |                |
   |                arguments to this function are incorrect
   |
   = note: expected struct `Vec<i32>`
              found struct `Vec<&str>`
note: function defined here
  --> /testbed/src/lib.rs:6:8
   |
6  | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
   |        ^^^

error[E0277]: can't compare `i32` with `String`
  --> tests/accumulate.rs:91:5
   |
91 |     assert_eq!(map(input, |s| s.to_string()), expected);
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ no implementation for `i32 == String`
   |
   = help: the trait `PartialEq<String>` is not implemented for `i32`
           but trait `PartialEq<i32>` is implemented for it
   = help: for that trait implementation, expected `i32`, found `String`
   = note: required for `Vec<i32>` to implement `PartialEq<Vec<String>>`
   = note: this error originates in the macro `assert_eq` (in Nightly builds, run with -Z macro-backtrace for more info)

error[E0631]: type mismatch in closure arguments
   --> tests/accumulate.rs:100:18
    |
100 |       let result = map(input, |x: i64| {
    |                    ^          -------- found signature defined here
    |  __________________|
    | |
101 | |         counter += 1;
102 | |         x.abs()
103 | |     });
    | |______^ expected due to this
    |
    = note: expected closure signature `fn(i32) -> _`
               found closure signature `fn(i64) -> _`
note: required by a bound in `accumulate::map`
   --> /testbed/src/lib.rs:8:8
    |
6   | pub fn map<F>(input: Vec<i32>, function: F) -> Vec<i32>
    |        --- required by a bound in this function
7   | where
8   |     F: Fn(i32) -> i32,
    |        ^^^^^^^^^^^^^^ required by this bound in `map`

error[E0308]: mismatched types
   --> tests/accumulate.rs:114:14
    |
114 |     map(vec![Foo], |_| Bar);
    |              ^^^ expected `i32`, found `Foo`

error[E0308]: mismatched types
   --> tests/accumulate.rs:114:24
    |
114 |     map(vec![Foo], |_| Bar);
    |                        ^^^ expected `i32`, found `Bar`

Some errors have detailed explanations: E0277, E0308, E0599, E0631.
For more information about an error, try `rustc --explain E0277`.
error: could not compile `accumulate` (test "accumulate") due to 22 previous errors
