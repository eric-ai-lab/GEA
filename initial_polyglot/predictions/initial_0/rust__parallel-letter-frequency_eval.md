+ cargo test -- --include-ignored
   Compiling parallel-letter-frequency v0.0.0 (/testbed)
error[E0521]: borrowed data escapes outside of function
  --> src/lib.rs:30:18
   |
8  | pub fn frequency(input: &[&str], worker_count: usize) -> HashMap<char, usize> {
   |                  -----    - let's call the lifetime of this reference `'1`
   |                  |
   |                  `input` is a reference that is only valid in the function body
...
30 |     for chunk in input.chunks(chunk_size) {
   |                  ^^^^^^^^^^^^^^^^^^^^^^^^
   |                  |
   |                  `input` escapes the function body here
   |                  argument requires that `'1` must outlive `'static`

For more information about this error, try `rustc --explain E0521`.
error: could not compile `parallel-letter-frequency` (lib) due to 1 previous error
warning: build failed, waiting for other jobs to finish...
error: could not compile `parallel-letter-frequency` (lib test) due to 1 previous error
