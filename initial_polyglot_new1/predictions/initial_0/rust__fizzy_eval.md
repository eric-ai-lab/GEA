+ cargo test -- --include-ignored
   Compiling fizzy v0.0.0 (/testbed)
error[E0277]: the trait bound `u8: From<i32>` is not satisfied
  --> tests/fizzy.rs:16:30
   |
16 |     let actual = fizz_buzz::<u8>().apply(1_u8..=16).collect::<Vec<_>>();
   |                              ^^ the trait `From<i32>` is not implemented for `u8`
   |
   = help: the following other types implement trait `From<T>`:
             `u8` implements `From<Char>`
             `u8` implements `From<bool>`
note: required by a bound in `fizzy::fizz_buzz`
  --> /testbed/src/lib.rs:84:20
   |
80 | pub fn fizz_buzz<T>() -> Fizzy<T>
   |        --------- required by a bound in this function
...
84 |     T: PartialEq + From<i32>,
   |                    ^^^^^^^^^ required by this bound in `fizz_buzz`

error[E0277]: the trait bound `u64: From<i32>` is not satisfied
  --> tests/fizzy.rs:27:30
   |
27 |     let actual = fizz_buzz::<u64>().apply(1_u64..=16).collect::<Vec<_>>();
   |                              ^^^ the trait `From<i32>` is not implemented for `u64`
   |
   = help: the following other types implement trait `From<T>`:
             `u64` implements `From<Char>`
             `u64` implements `From<bool>`
             `u64` implements `From<char>`
             `u64` implements `From<u16>`
             `u64` implements `From<u32>`
             `u64` implements `From<u8>`
note: required by a bound in `fizzy::fizz_buzz`
  --> /testbed/src/lib.rs:84:20
   |
80 | pub fn fizz_buzz<T>() -> Fizzy<T>
   |        --------- required by a bound in this function
...
84 |     T: PartialEq + From<i32>,
   |                    ^^^^^^^^^ required by this bound in `fizz_buzz`

error[E0631]: type mismatch in closure arguments
  --> tests/fizzy.rs:56:22
   |
56 |         .add_matcher(Matcher::new(|n: i32| n % 5 == 0, "Buzz"))
   |                      ^^^^^^^^^^^^^--------^^^^^^^^^^^^^^^^^^^^
   |                      |            |
   |                      |            found signature defined here
   |                      expected due to this
   |
   = note: expected closure signature `for<'a> fn(&'a _) -> _`
              found closure signature `fn(i32) -> _`
note: required by a bound in `fizzy::Matcher::<T>::new`
  --> /testbed/src/lib.rs:14:12
   |
12 |     pub fn new<F, S>(matcher: F, subs: S) -> Matcher<T>
   |            --- required by a bound in this associated function
13 |     where
14 |         F: Fn(&T) -> bool + 'static,
   |            ^^^^^^^^^^^^^^ required by this bound in `Matcher::<T>::new`
help: consider adjusting the signature so it borrows its argument
   |
56 |         .add_matcher(Matcher::new(|n: &i32| n % 5 == 0, "Buzz"))
   |                                       +

error[E0631]: type mismatch in closure arguments
  --> tests/fizzy.rs:57:22
   |
57 |         .add_matcher(Matcher::new(|n: i32| n % 3 == 0, "Fizz"))
   |                      ^^^^^^^^^^^^^--------^^^^^^^^^^^^^^^^^^^^
   |                      |            |
   |                      |            found signature defined here
   |                      expected due to this
   |
   = note: expected closure signature `for<'a> fn(&'a _) -> _`
              found closure signature `fn(i32) -> _`
note: required by a bound in `fizzy::Matcher::<T>::new`
  --> /testbed/src/lib.rs:14:12
   |
12 |     pub fn new<F, S>(matcher: F, subs: S) -> Matcher<T>
   |            --- required by a bound in this associated function
13 |     where
14 |         F: Fn(&T) -> bool + 'static,
   |            ^^^^^^^^^^^^^^ required by this bound in `Matcher::<T>::new`
help: consider adjusting the signature so it borrows its argument
   |
57 |         .add_matcher(Matcher::new(|n: &i32| n % 3 == 0, "Fizz"))
   |                                       +

error[E0631]: type mismatch in closure arguments
  --> tests/fizzy.rs:58:22
   |
58 |         .add_matcher(Matcher::new(|n: i32| n % 7 == 0, "Bam"));
   |                      ^^^^^^^^^^^^^--------^^^^^^^^^^^^^^^^^^^
   |                      |            |
   |                      |            found signature defined here
   |                      expected due to this
   |
   = note: expected closure signature `for<'a> fn(&'a _) -> _`
              found closure signature `fn(i32) -> _`
note: required by a bound in `fizzy::Matcher::<T>::new`
  --> /testbed/src/lib.rs:14:12
   |
12 |     pub fn new<F, S>(matcher: F, subs: S) -> Matcher<T>
   |            --- required by a bound in this associated function
13 |     where
14 |         F: Fn(&T) -> bool + 'static,
   |            ^^^^^^^^^^^^^^ required by this bound in `Matcher::<T>::new`
help: consider adjusting the signature so it borrows its argument
   |
58 |         .add_matcher(Matcher::new(|n: &i32| n % 7 == 0, "Bam"));
   |                                       +

error[E0277]: the trait bound `Fizzable: From<i32>` is not satisfied
   --> tests/fizzy.rs:118:30
    |
118 |     let actual = fizz_buzz::<Fizzable>()
    |                              ^^^^^^^^ unsatisfied trait bound
    |
    = help: the trait `From<i32>` is not implemented for `Fizzable`
            but trait `From<u8>` is implemented for it
    = help: for that trait implementation, expected `u8`, found `i32`
note: required by a bound in `fizzy::fizz_buzz`
   --> /testbed/src/lib.rs:84:20
    |
 80 | pub fn fizz_buzz<T>() -> Fizzy<T>
    |        --------- required by a bound in this function
...
 84 |     T: PartialEq + From<i32>,
    |                    ^^^^^^^^^ required by this bound in `fizz_buzz`

Some errors have detailed explanations: E0277, E0631.
For more information about an error, try `rustc --explain E0277`.
error: could not compile `fizzy` (test "fizzy") due to 6 previous errors
warning: build failed, waiting for other jobs to finish...
