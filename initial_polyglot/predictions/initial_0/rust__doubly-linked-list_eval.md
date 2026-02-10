+ cargo test -- --include-ignored
   Compiling doubly-linked-list v0.0.0 (/testbed)
warning: unused import: `super::Cursor`
   --> src/lib.rs:312:9
    |
312 |     use super::Cursor;
    |         ^^^^^^^^^^^^^
    |
    = note: `#[warn(unused_imports)]` on by default

error[E0503]: cannot use `self.head` because it was mutably borrowed
  --> src/lib.rs:53:22
   |
50 |       pub fn cursor_front(&mut self) -> Cursor<'_, T> {
   |                           - let's call the lifetime of this reference `'1`
51 | /         Cursor {
52 | |             list: self,
   | |                   ---- `*self` is borrowed here
53 | |             current: self.head,
   | |                      ^^^^^^^^^ use of borrowed `*self`
54 | |             _marker: PhantomData,
55 | |         }
   | |_________- returning this value requires that `*self` is borrowed for `'1`

error[E0503]: cannot use `self.tail` because it was mutably borrowed
  --> src/lib.rs:63:22
   |
60 |       pub fn cursor_back(&mut self) -> Cursor<'_, T> {
   |                          - let's call the lifetime of this reference `'1`
61 | /         Cursor {
62 | |             list: self,
   | |                   ---- `*self` is borrowed here
63 | |             current: self.tail,
   | |                      ^^^^^^^^^ use of borrowed `*self`
64 | |             _marker: PhantomData,
65 | |         }
   | |_________- returning this value requires that `*self` is borrowed for `'1`

For more information about this error, try `rustc --explain E0503`.
warning: `doubly-linked-list` (lib) generated 1 warning
error: could not compile `doubly-linked-list` (lib) due to 2 previous errors; 1 warning emitted
warning: build failed, waiting for other jobs to finish...
warning: `doubly-linked-list` (lib test) generated 1 warning (1 duplicate)
error: could not compile `doubly-linked-list` (lib test) due to 2 previous errors; 1 warning emitted
