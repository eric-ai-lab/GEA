+ cargo test -- --include-ignored
   Compiling bowling v1.2.0 (/testbed)
error[E0433]: failed to resolve: use of undeclared type `Error`
  --> tests/bowling.rs:14:35
   |
14 |     assert_eq!(game.roll(11), Err(Error::NotEnoughPinsLeft));
   |                                   ^^^^^ use of undeclared type `Error`
   |
help: consider importing one of these items
   |
1  + use std::error::Error;
   |
1  + use std::fmt::Error;
   |
1  + use std::io::Error;
   |
1  + use core::error::Error;
   |
     and 1 other candidate

error[E0433]: failed to resolve: use of undeclared type `Error`
  --> tests/bowling.rs:61:34
   |
61 |     assert_eq!(game.roll(0), Err(Error::GameComplete));
   |                                  ^^^^^ use of undeclared type `Error`
   |
help: consider importing one of these items
   |
1  + use std::error::Error;
   |
1  + use std::fmt::Error;
   |
1  + use std::io::Error;
   |
1  + use core::error::Error;
   |
     and 1 other candidate

error[E0433]: failed to resolve: use of undeclared type `Error`
   --> tests/bowling.rs:284:34
    |
284 |     assert_eq!(game.roll(6), Err(Error::NotEnoughPinsLeft));
    |                                  ^^^^^ use of undeclared type `Error`
    |
help: consider importing one of these items
    |
1   + use std::error::Error;
    |
1   + use std::fmt::Error;
    |
1   + use std::io::Error;
    |
1   + use core::error::Error;
    |
      and 1 other candidate

error[E0433]: failed to resolve: use of undeclared type `Error`
   --> tests/bowling.rs:298:35
    |
298 |     assert_eq!(game.roll(11), Err(Error::NotEnoughPinsLeft));
    |                                   ^^^^^ use of undeclared type `Error`
    |
help: consider importing one of these items
    |
1   + use std::error::Error;
    |
1   + use std::fmt::Error;
    |
1   + use std::io::Error;
    |
1   + use core::error::Error;
    |
      and 1 other candidate

error[E0433]: failed to resolve: use of undeclared type `Error`
   --> tests/bowling.rs:313:34
    |
313 |     assert_eq!(game.roll(6), Err(Error::NotEnoughPinsLeft));
    |                                  ^^^^^ use of undeclared type `Error`
    |
help: consider importing one of these items
    |
1   + use std::error::Error;
    |
1   + use std::fmt::Error;
    |
1   + use std::io::Error;
    |
1   + use core::error::Error;
    |
      and 1 other candidate

error[E0433]: failed to resolve: use of undeclared type `Error`
   --> tests/bowling.rs:343:35
    |
343 |     assert_eq!(game.roll(10), Err(Error::NotEnoughPinsLeft));
    |                                   ^^^^^ use of undeclared type `Error`
    |
help: consider importing one of these items
    |
1   + use std::error::Error;
    |
1   + use std::fmt::Error;
    |
1   + use std::io::Error;
    |
1   + use core::error::Error;
    |
      and 1 other candidate

error[E0433]: failed to resolve: use of undeclared type `Error`
   --> tests/bowling.rs:359:35
    |
359 |     assert_eq!(game.roll(11), Err(Error::NotEnoughPinsLeft));
    |                                   ^^^^^ use of undeclared type `Error`
    |
help: consider importing one of these items
    |
1   + use std::error::Error;
    |
1   + use std::fmt::Error;
    |
1   + use std::io::Error;
    |
1   + use core::error::Error;
    |
      and 1 other candidate

error[E0433]: failed to resolve: use of undeclared type `Error`
   --> tests/bowling.rs:416:34
    |
416 |     assert_eq!(game.roll(2), Err(Error::GameComplete));
    |                                  ^^^^^ use of undeclared type `Error`
    |
help: consider importing one of these items
    |
1   + use std::error::Error;
    |
1   + use std::fmt::Error;
    |
1   + use std::io::Error;
    |
1   + use core::error::Error;
    |
      and 1 other candidate

error[E0433]: failed to resolve: use of undeclared type `Error`
   --> tests/bowling.rs:432:34
    |
432 |     assert_eq!(game.roll(2), Err(Error::GameComplete));
    |                                  ^^^^^ use of undeclared type `Error`
    |
help: consider importing one of these items
    |
1   + use std::error::Error;
    |
1   + use std::fmt::Error;
    |
1   + use std::io::Error;
    |
1   + use core::error::Error;
    |
      and 1 other candidate

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
 --> tests/bowling.rs:6:26
  |
6 |     assert!(game.roll(0).is_ok());
  |                          ^^^^^ method not found in `()`
  |
note: method `roll` modifies its receiver in-place
 --> tests/bowling.rs:6:18
  |
6 |     assert!(game.roll(0).is_ok());
  |                  ^^^^ this call modifies `game` in-place

error[E0599]: no method named `is_some` found for type `u32` in the current scope
  --> tests/bowling.rs:27:26
   |
27 |     assert!(game.score().is_some());
   |                          ^^^^^^^ method not found in `u32`

error[E0308]: mismatched types
  --> tests/bowling.rs:35:30
   |
35 |     assert_eq!(game.score(), None);
   |                              ^^^^ expected `u32`, found `Option<_>`
   |
   = note: expected type `u32`
              found enum `Option<_>`

error[E0308]: mismatched types
  --> tests/bowling.rs:48:30
   |
48 |     assert_eq!(game.score(), None);
   |                              ^^^^ expected `u32`, found `Option<_>`
   |
   = note: expected type `u32`
              found enum `Option<_>`

error[E0308]: mismatched types
  --> tests/bowling.rs:73:30
   |
73 |     assert_eq!(game.score(), Some(0));
   |                              ^^^^^^^ expected `u32`, found `Option<{integer}>`
   |
   = note: expected type `u32`
              found enum `Option<{integer}>`

error[E0308]: mismatched types
  --> tests/bowling.rs:86:30
   |
86 |     assert_eq!(game.score(), Some(90));
   |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
   |
   = note: expected type `u32`
              found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:101:30
    |
101 |     assert_eq!(game.score(), Some(10));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:117:30
    |
117 |     assert_eq!(game.score(), Some(16));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:135:30
    |
135 |     assert_eq!(game.score(), Some(31));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:151:30
    |
151 |     assert_eq!(game.score(), Some(17));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:165:30
    |
165 |     assert_eq!(game.score(), Some(10));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:181:30
    |
181 |     assert_eq!(game.score(), Some(26));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:199:30
    |
199 |     assert_eq!(game.score(), Some(81));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:215:30
    |
215 |     assert_eq!(game.score(), Some(18));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:231:30
    |
231 |     assert_eq!(game.score(), Some(20));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:247:30
    |
247 |     assert_eq!(game.score(), Some(30));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:263:30
    |
263 |     assert_eq!(game.score(), Some(20));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0308]: mismatched types
   --> tests/bowling.rs:275:30
    |
275 |     assert_eq!(game.score(), Some(300));
    |                              ^^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
   --> tests/bowling.rs:283:26
    |
283 |     assert!(game.roll(5).is_ok());
    |                          ^^^^^ method not found in `()`
    |
note: method `roll` modifies its receiver in-place
   --> tests/bowling.rs:283:18
    |
283 |     assert!(game.roll(5).is_ok());
    |                  ^^^^ this call modifies `game` in-place

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
   --> tests/bowling.rs:312:26
    |
312 |     assert!(game.roll(5).is_ok());
    |                          ^^^^^ method not found in `()`
    |
note: method `roll` modifies its receiver in-place
   --> tests/bowling.rs:312:18
    |
312 |     assert!(game.roll(5).is_ok());
    |                  ^^^^ this call modifies `game` in-place

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
   --> tests/bowling.rs:327:27
    |
327 |     assert!(game.roll(10).is_ok());
    |                           ^^^^^ method not found in `()`
    |
note: method `roll` modifies its receiver in-place
   --> tests/bowling.rs:327:18
    |
327 |     assert!(game.roll(10).is_ok());
    |                  ^^^^ this call modifies `game` in-place

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
   --> tests/bowling.rs:328:26
    |
328 |     assert!(game.roll(6).is_ok());
    |                          ^^^^^ method not found in `()`
    |
note: method `roll` modifies its receiver in-place
   --> tests/bowling.rs:328:18
    |
328 |     assert!(game.roll(6).is_ok());
    |                  ^^^^ this call modifies `game` in-place

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
   --> tests/bowling.rs:342:26
    |
342 |     assert!(game.roll(6).is_ok());
    |                          ^^^^^ method not found in `()`
    |
note: method `roll` modifies its receiver in-place
   --> tests/bowling.rs:342:18
    |
342 |     assert!(game.roll(6).is_ok());
    |                  ^^^^ this call modifies `game` in-place

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
   --> tests/bowling.rs:358:27
    |
358 |     assert!(game.roll(10).is_ok());
    |                           ^^^^^ method not found in `()`
    |
note: method `roll` modifies its receiver in-place
   --> tests/bowling.rs:358:18
    |
358 |     assert!(game.roll(10).is_ok());
    |                  ^^^^ this call modifies `game` in-place

error[E0308]: mismatched types
   --> tests/bowling.rs:373:30
    |
373 |     assert_eq!(game.score(), None);
    |                              ^^^^ expected `u32`, found `Option<_>`
    |
    = note: expected type `u32`
               found enum `Option<_>`

error[E0308]: mismatched types
   --> tests/bowling.rs:377:30
    |
377 |     assert_eq!(game.score(), None);
    |                              ^^^^ expected `u32`, found `Option<_>`
    |
    = note: expected type `u32`
               found enum `Option<_>`

error[E0599]: no method named `is_some` found for type `u32` in the current scope
   --> tests/bowling.rs:381:26
    |
381 |     assert!(game.score().is_some());
    |                          ^^^^^^^ method not found in `u32`

error[E0308]: mismatched types
   --> tests/bowling.rs:396:30
    |
396 |     assert_eq!(game.score(), None);
    |                              ^^^^ expected `u32`, found `Option<_>`
    |
    = note: expected type `u32`
               found enum `Option<_>`

error[E0599]: no method named `is_some` found for type `u32` in the current scope
   --> tests/bowling.rs:400:26
    |
400 |     assert!(game.score().is_some());
    |                          ^^^^^^^ method not found in `u32`

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
   --> tests/bowling.rs:414:26
    |
414 |     assert!(game.roll(2).is_ok());
    |                          ^^^^^ method not found in `()`
    |
note: method `roll` modifies its receiver in-place
   --> tests/bowling.rs:414:18
    |
414 |     assert!(game.roll(2).is_ok());
    |                  ^^^^ this call modifies `game` in-place

error[E0599]: no method named `is_ok` found for unit type `()` in the current scope
   --> tests/bowling.rs:430:26
    |
430 |     assert!(game.roll(2).is_ok());
    |                          ^^^^^ method not found in `()`
    |
note: method `roll` modifies its receiver in-place
   --> tests/bowling.rs:430:18
    |
430 |     assert!(game.roll(2).is_ok());
    |                  ^^^^ this call modifies `game` in-place

error[E0308]: mismatched types
   --> tests/bowling.rs:447:30
    |
447 |     assert_eq!(game.score(), Some(31));
    |                              ^^^^^^^^ expected `u32`, found `Option<{integer}>`
    |
    = note: expected type `u32`
               found enum `Option<{integer}>`

Some errors have detailed explanations: E0308, E0433, E0599.
For more information about an error, try `rustc --explain E0308`.
error: could not compile `bowling` (test "bowling") due to 41 previous errors
