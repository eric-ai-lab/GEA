+ cargo test -- --include-ignored
   Compiling fizzy v0.0.0 (/testbed)
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
  --> /testbed/src/lib.rs:17:12
   |
15 |     pub fn new<F, S>(matcher: F, subs: S) -> Matcher<T>
   |            --- required by a bound in this associated function
16 |     where
17 |         F: Fn(&T) -> bool + 'static,
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
  --> /testbed/src/lib.rs:17:12
   |
15 |     pub fn new<F, S>(matcher: F, subs: S) -> Matcher<T>
   |            --- required by a bound in this associated function
16 |     where
17 |         F: Fn(&T) -> bool + 'static,
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
  --> /testbed/src/lib.rs:17:12
   |
15 |     pub fn new<F, S>(matcher: F, subs: S) -> Matcher<T>
   |            --- required by a bound in this associated function
16 |     where
17 |         F: Fn(&T) -> bool + 'static,
   |            ^^^^^^^^^^^^^^ required by this bound in `Matcher::<T>::new`
help: consider adjusting the signature so it borrows its argument
   |
58 |         .add_matcher(Matcher::new(|n: &i32| n % 7 == 0, "Bam"));
   |                                       +

For more information about this error, try `rustc --explain E0631`.
error: could not compile `fizzy` (test "fizzy") due to 3 previous errors
