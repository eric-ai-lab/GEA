+ cargo test -- --include-ignored
   Compiling react v2.0.0 (/testbed)
error[E0502]: cannot borrow `*self` as immutable because it is also borrowed as mutable
   --> src/lib.rs:151:26
    |
148 |             for cell in &mut self.compute_cells {
    |                         -----------------------
    |                         |
    |                         mutable borrow occurs here
    |                         mutable borrow later used here
...
151 |                     .map(|dep| self.get_cell_value(*dep))
    |                          ^^^^^ ---- second borrow occurs due to use of `*self` in closure
    |                          |
    |                          immutable borrow occurs here

For more information about this error, try `rustc --explain E0502`.
error: could not compile `react` (lib test) due to 1 previous error
warning: build failed, waiting for other jobs to finish...
error: could not compile `react` (lib) due to 1 previous error
