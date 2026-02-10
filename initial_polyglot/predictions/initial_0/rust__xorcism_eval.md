+ cargo test -- --include-ignored
   Compiling xorcism v0.1.0 (/testbed)
error[E0309]: the associated type `<Data as IntoIterator>::IntoIter` may not live long enough
  --> src/lib.rs:46:9
   |
11 |   impl<'a> Xorcism<'a> {
   |        -- the associated type `<Data as IntoIterator>::IntoIter` must be valid for the lifetime `'a` as defined here...
...
46 | /         MungeIter {
47 | |             iter: data.into_iter().map(|item| *item.borrow()),
48 | |             xorcism: self,
49 | |         }
   | |_________^ ...so that the type `<Data as IntoIterator>::IntoIter` will meet its required lifetime bounds
   |
help: consider adding an explicit lifetime bound
   |
44 |         Data::Item: Borrow<u8>, <Data as IntoIterator>::IntoIter: 'a
   |                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

error: lifetime may not live long enough
  --> src/lib.rs:48:22
   |
11 | impl<'a> Xorcism<'a> {
   |      -- lifetime `'a` defined here
...
41 |     pub fn munge<Data>(&mut self, data: Data) -> impl Iterator<Item = u8> + '_
   |                        - let's call the lifetime of this reference `'1`
...
48 |             xorcism: self,
   |                      ^^^^ this usage requires that `'1` must outlive `'a`

For more information about this error, try `rustc --explain E0309`.
error: could not compile `xorcism` (lib test) due to 2 previous errors
warning: build failed, waiting for other jobs to finish...
error: could not compile `xorcism` (lib) due to 2 previous errors
