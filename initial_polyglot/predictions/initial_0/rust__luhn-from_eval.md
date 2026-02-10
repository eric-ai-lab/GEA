+ cargo test -- --include-ignored
   Compiling luhn-from v0.0.0 (/testbed)
error[E0277]: the trait bound `luhn_from::Luhn: From<u8>` is not satisfied
  --> tests/luhn-from.rs:23:17
   |
23 |     let valid = Luhn::from(240u8);
   |                 ^^^^ the trait `From<u8>` is not implemented for `luhn_from::Luhn`
   |
   = help: the following other types implement trait `From<T>`:
             `luhn_from::Luhn` implements `From<&str>`
             `luhn_from::Luhn` implements `From<String>`
             `luhn_from::Luhn` implements `From<u32>`
             `luhn_from::Luhn` implements `From<u64>`

error[E0277]: the trait bound `luhn_from::Luhn: From<u8>` is not satisfied
  --> tests/luhn-from.rs:24:19
   |
24 |     let invalid = Luhn::from(241u8);
   |                   ^^^^ the trait `From<u8>` is not implemented for `luhn_from::Luhn`
   |
   = help: the following other types implement trait `From<T>`:
             `luhn_from::Luhn` implements `From<&str>`
             `luhn_from::Luhn` implements `From<String>`
             `luhn_from::Luhn` implements `From<u32>`
             `luhn_from::Luhn` implements `From<u64>`

error[E0277]: the trait bound `luhn_from::Luhn: From<u16>` is not satisfied
  --> tests/luhn-from.rs:32:17
   |
32 |     let valid = Luhn::from(64_436u16);
   |                 ^^^^ the trait `From<u16>` is not implemented for `luhn_from::Luhn`
   |
   = help: the following other types implement trait `From<T>`:
             `luhn_from::Luhn` implements `From<&str>`
             `luhn_from::Luhn` implements `From<String>`
             `luhn_from::Luhn` implements `From<u32>`
             `luhn_from::Luhn` implements `From<u64>`

error[E0277]: the trait bound `luhn_from::Luhn: From<u16>` is not satisfied
  --> tests/luhn-from.rs:33:19
   |
33 |     let invalid = Luhn::from(64_437u16);
   |                   ^^^^ the trait `From<u16>` is not implemented for `luhn_from::Luhn`
   |
   = help: the following other types implement trait `From<T>`:
             `luhn_from::Luhn` implements `From<&str>`
             `luhn_from::Luhn` implements `From<String>`
             `luhn_from::Luhn` implements `From<u32>`
             `luhn_from::Luhn` implements `From<u64>`

error[E0277]: the trait bound `luhn_from::Luhn: From<usize>` is not satisfied
  --> tests/luhn-from.rs:59:17
   |
59 |     let valid = Luhn::from(8273_1232_7352_0562usize);
   |                 ^^^^ the trait `From<usize>` is not implemented for `luhn_from::Luhn`
   |
   = help: the following other types implement trait `From<T>`:
             `luhn_from::Luhn` implements `From<&str>`
             `luhn_from::Luhn` implements `From<String>`
             `luhn_from::Luhn` implements `From<u32>`
             `luhn_from::Luhn` implements `From<u64>`

error[E0277]: the trait bound `luhn_from::Luhn: From<usize>` is not satisfied
  --> tests/luhn-from.rs:60:19
   |
60 |     let invalid = Luhn::from(8273_1232_7352_0569usize);
   |                   ^^^^ the trait `From<usize>` is not implemented for `luhn_from::Luhn`
   |
   = help: the following other types implement trait `From<T>`:
             `luhn_from::Luhn` implements `From<&str>`
             `luhn_from::Luhn` implements `From<String>`
             `luhn_from::Luhn` implements `From<u32>`
             `luhn_from::Luhn` implements `From<u64>`

For more information about this error, try `rustc --explain E0277`.
error: could not compile `luhn-from` (test "luhn-from") due to 6 previous errors
warning: build failed, waiting for other jobs to finish...
