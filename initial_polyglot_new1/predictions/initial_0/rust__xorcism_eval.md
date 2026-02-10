+ cargo test -- --include-ignored
   Compiling xorcism v0.1.0 (/testbed)
error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
  --> tests/xorcism.rs:52:18
   |
52 |         xs.munge(data.as_bytes()).collect::<Vec<_>>(),
   |            ----- ^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
   |            |
   |            required by a bound introduced by this call
   |
note: the method call chain might not have had the expected associated types
  --> tests/xorcism.rs:52:23
   |
49 |     let data = "This is super-secret, cutting edge encryption, folks.";
   |                ------------------------------------------------------- this expression has type `&str`
...
52 |         xs.munge(data.as_bytes()).collect::<Vec<_>>(),
   |                       ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
  --> /testbed/src/lib.rs:61:41
   |
61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
   |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
  --> tests/xorcism.rs:52:12
   |
52 |         xs.munge(data.as_bytes()).collect::<Vec<_>>(),
   |            ^^^^^ expected `u8`, found `&u8`
   |
note: required by a bound in `XorIterator`
  --> /testbed/src/lib.rs:12:40
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
  --> tests/xorcism.rs:52:35
   |
52 |         xs.munge(data.as_bytes()).collect::<Vec<_>>(),
   |                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
   |
  ::: /testbed/src/lib.rs:12:1
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   | -------------------------------------------------- doesn't satisfy `_: Iterator`
   |
   = note: the following trait bounds were not satisfied:
           `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
           which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
           `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
           which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0271]: type mismatch resolving `<&[{integer}; 2] as IntoIterator>::Item == u8`
  --> tests/xorcism.rs:67:33
   |
67 |     let out1: Vec<_> = xs.munge(input).collect();
   |                           ----- ^^^^^ expected `u8`, found `&{integer}`
   |                           |
   |                           required by a bound introduced by this call
   |
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
  --> /testbed/src/lib.rs:61:41
   |
61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
   |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, {integer}>` to be an iterator that yields `u8`, but it yields `&{integer}`
  --> tests/xorcism.rs:67:27
   |
67 |     let out1: Vec<_> = xs.munge(input).collect();
   |                           ^^^^^ expected `u8`, found `&{integer}`
   |
note: required by a bound in `XorIterator`
  --> /testbed/src/lib.rs:12:40
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, {integer}>>`, but its trait bounds were not satisfied
  --> tests/xorcism.rs:67:40
   |
67 |     let out1: Vec<_> = xs.munge(input).collect();
   |                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, {integer}>>` due to unsatisfied trait bounds
   |
  ::: /testbed/src/lib.rs:12:1
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   | -------------------------------------------------- doesn't satisfy `_: Iterator`
   |
   = note: the following trait bounds were not satisfied:
           `<std::slice::Iter<'_, {integer}> as Iterator>::Item = u8`
           which is required by `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           which is required by `&mut XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`

error[E0271]: type mismatch resolving `<&[{integer}; 2] as IntoIterator>::Item == u8`
  --> tests/xorcism.rs:68:33
   |
68 |     let out2: Vec<_> = xs.munge(input).collect();
   |                           ----- ^^^^^ expected `u8`, found `&{integer}`
   |                           |
   |                           required by a bound introduced by this call
   |
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
  --> /testbed/src/lib.rs:61:41
   |
61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
   |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, {integer}>` to be an iterator that yields `u8`, but it yields `&{integer}`
  --> tests/xorcism.rs:68:27
   |
68 |     let out2: Vec<_> = xs.munge(input).collect();
   |                           ^^^^^ expected `u8`, found `&{integer}`
   |
note: required by a bound in `XorIterator`
  --> /testbed/src/lib.rs:12:40
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, {integer}>>`, but its trait bounds were not satisfied
  --> tests/xorcism.rs:68:40
   |
68 |     let out2: Vec<_> = xs.munge(input).collect();
   |                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, {integer}>>` due to unsatisfied trait bounds
   |
  ::: /testbed/src/lib.rs:12:1
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   | -------------------------------------------------- doesn't satisfy `_: Iterator`
   |
   = note: the following trait bounds were not satisfied:
           `<std::slice::Iter<'_, {integer}> as Iterator>::Item = u8`
           which is required by `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           which is required by `&mut XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`

error[E0271]: type mismatch resolving `<&[{integer}; 2] as IntoIterator>::Item == u8`
  --> tests/xorcism.rs:69:33
   |
69 |     let out3: Vec<_> = xs.munge(input).collect();
   |                           ----- ^^^^^ expected `u8`, found `&{integer}`
   |                           |
   |                           required by a bound introduced by this call
   |
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
  --> /testbed/src/lib.rs:61:41
   |
61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
   |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, {integer}>` to be an iterator that yields `u8`, but it yields `&{integer}`
  --> tests/xorcism.rs:69:27
   |
69 |     let out3: Vec<_> = xs.munge(input).collect();
   |                           ^^^^^ expected `u8`, found `&{integer}`
   |
note: required by a bound in `XorIterator`
  --> /testbed/src/lib.rs:12:40
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, {integer}>>`, but its trait bounds were not satisfied
  --> tests/xorcism.rs:69:40
   |
69 |     let out3: Vec<_> = xs.munge(input).collect();
   |                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, {integer}>>` due to unsatisfied trait bounds
   |
  ::: /testbed/src/lib.rs:12:1
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   | -------------------------------------------------- doesn't satisfy `_: Iterator`
   |
   = note: the following trait bounds were not satisfied:
           `<std::slice::Iter<'_, {integer}> as Iterator>::Item = u8`
           which is required by `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           which is required by `&mut XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`

error[E0271]: type mismatch resolving `<&[{integer}; 2] as IntoIterator>::Item == u8`
  --> tests/xorcism.rs:70:33
   |
70 |     let out4: Vec<_> = xs.munge(input).collect();
   |                           ----- ^^^^^ expected `u8`, found `&{integer}`
   |                           |
   |                           required by a bound introduced by this call
   |
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
  --> /testbed/src/lib.rs:61:41
   |
61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
   |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, {integer}>` to be an iterator that yields `u8`, but it yields `&{integer}`
  --> tests/xorcism.rs:70:27
   |
70 |     let out4: Vec<_> = xs.munge(input).collect();
   |                           ^^^^^ expected `u8`, found `&{integer}`
   |
note: required by a bound in `XorIterator`
  --> /testbed/src/lib.rs:12:40
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, {integer}>>`, but its trait bounds were not satisfied
  --> tests/xorcism.rs:70:40
   |
70 |     let out4: Vec<_> = xs.munge(input).collect();
   |                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, {integer}>>` due to unsatisfied trait bounds
   |
  ::: /testbed/src/lib.rs:12:1
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   | -------------------------------------------------- doesn't satisfy `_: Iterator`
   |
   = note: the following trait bounds were not satisfied:
           `<std::slice::Iter<'_, {integer}> as Iterator>::Item = u8`
           which is required by `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           which is required by `&mut XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`

error[E0271]: type mismatch resolving `<&[{integer}; 2] as IntoIterator>::Item == u8`
  --> tests/xorcism.rs:71:33
   |
71 |     let out5: Vec<_> = xs.munge(input).collect();
   |                           ----- ^^^^^ expected `u8`, found `&{integer}`
   |                           |
   |                           required by a bound introduced by this call
   |
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
  --> /testbed/src/lib.rs:61:41
   |
61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
   |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, {integer}>` to be an iterator that yields `u8`, but it yields `&{integer}`
  --> tests/xorcism.rs:71:27
   |
71 |     let out5: Vec<_> = xs.munge(input).collect();
   |                           ^^^^^ expected `u8`, found `&{integer}`
   |
note: required by a bound in `XorIterator`
  --> /testbed/src/lib.rs:12:40
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, {integer}>>`, but its trait bounds were not satisfied
  --> tests/xorcism.rs:71:40
   |
71 |     let out5: Vec<_> = xs.munge(input).collect();
   |                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, {integer}>>` due to unsatisfied trait bounds
   |
  ::: /testbed/src/lib.rs:12:1
   |
12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
   | -------------------------------------------------- doesn't satisfy `_: Iterator`
   |
   = note: the following trait bounds were not satisfied:
           `<std::slice::Iter<'_, {integer}> as Iterator>::Item = u8`
           which is required by `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           `XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`
           which is required by `&mut XorIterator<'_, std::slice::Iter<'_, {integer}>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:102:45
    |
102 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:116:44
    |
116 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:117:49
    |
117 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:117:55
    |
117 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                 ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                                 |
    |                                                 this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:117:43
    |
117 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:117:67
    |
117 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:126:45
    |
126 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:128:45
    |
128 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:128:51
    |
128 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                             ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                             |
    |                                             this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:128:39
    |
128 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:129:50
    |
129 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:129:62
    |
129 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:150:45
    |
150 |             let mut xorcism1 = Xorcism::new(key);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:167:44
    |
167 |             let mut xorcism = Xorcism::new(key);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:168:49
    |
168 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                           ----- ^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:165:31
    |
165 |             let input = INPUT.as_bytes();
    |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                         |
    |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:168:43
    |
168 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:168:56
    |
168 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:180:45
    |
180 |             let mut xorcism1 = Xorcism::new(key);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:182:45
    |
182 |             let munge_iter = xorcism1.munge(input);
    |                                       ----- ^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:178:31
    |
178 |             let input = INPUT.as_bytes();
    |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                         |
    |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:182:39
    |
182 |             let munge_iter = xorcism1.munge(input);
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:183:50
    |
183 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:183:62
    |
183 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:200:45
    |
200 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:216:44
    |
216 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:228:45
    |
228 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:313:45
    |
313 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:327:44
    |
327 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:328:49
    |
328 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:328:55
    |
328 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                 ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                                 |
    |                                                 this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:328:43
    |
328 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:328:67
    |
328 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:337:45
    |
337 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:339:45
    |
339 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:339:51
    |
339 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                             ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                             |
    |                                             this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:339:39
    |
339 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:340:50
    |
340 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:340:62
    |
340 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:361:45
    |
361 |             let mut xorcism1 = Xorcism::new(key);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:378:44
    |
378 |             let mut xorcism = Xorcism::new(key);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:379:49
    |
379 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                           ----- ^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:376:31
    |
376 |             let input = INPUT.as_bytes();
    |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                         |
    |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:379:43
    |
379 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:379:56
    |
379 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:391:45
    |
391 |             let mut xorcism1 = Xorcism::new(key);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:393:45
    |
393 |             let munge_iter = xorcism1.munge(input);
    |                                       ----- ^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:389:31
    |
389 |             let input = INPUT.as_bytes();
    |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                         |
    |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:393:39
    |
393 |             let munge_iter = xorcism1.munge(input);
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:394:50
    |
394 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:394:62
    |
394 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:411:45
    |
411 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:427:44
    |
427 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:439:45
    |
439 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:524:45
    |
524 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:538:44
    |
538 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:539:49
    |
539 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:539:55
    |
539 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                 ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                                 |
    |                                                 this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:539:43
    |
539 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:539:67
    |
539 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:548:45
    |
548 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:550:45
    |
550 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:550:51
    |
550 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                             ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                             |
    |                                             this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:550:39
    |
550 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:551:50
    |
551 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:551:62
    |
551 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:572:45
    |
572 |             let mut xorcism1 = Xorcism::new(key);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:589:44
    |
589 |             let mut xorcism = Xorcism::new(key);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:590:49
    |
590 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                           ----- ^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:587:31
    |
587 |             let input = INPUT.as_bytes();
    |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                         |
    |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:590:43
    |
590 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:590:56
    |
590 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:602:45
    |
602 |             let mut xorcism1 = Xorcism::new(key);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:604:45
    |
604 |             let munge_iter = xorcism1.munge(input);
    |                                       ----- ^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:600:31
    |
600 |             let input = INPUT.as_bytes();
    |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                         |
    |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:604:39
    |
604 |             let munge_iter = xorcism1.munge(input);
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:605:50
    |
605 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:605:62
    |
605 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:622:45
    |
622 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:638:44
    |
638 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:650:45
    |
650 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:738:45
    |
738 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:752:44
    |
752 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:753:49
    |
753 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:753:55
    |
753 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                 ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                                 |
    |                                                 this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:753:43
    |
753 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:753:67
    |
753 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:762:45
    |
762 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:764:45
    |
764 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:764:51
    |
764 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                             ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                             |
    |                                             this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:764:39
    |
764 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:765:50
    |
765 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:765:62
    |
765 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:786:45
    |
786 |             let mut xorcism1 = Xorcism::new(key);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:803:44
    |
803 |             let mut xorcism = Xorcism::new(key);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:804:49
    |
804 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                           ----- ^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:801:31
    |
801 |             let input = INPUT.as_bytes();
    |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                         |
    |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:804:43
    |
804 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:804:56
    |
804 |             let result: Vec<u8> = xorcism.munge(input).collect();
    |                                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
   --> tests/xorcism.rs:816:45
    |
816 |             let mut xorcism1 = Xorcism::new(key);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:818:45
    |
818 |             let munge_iter = xorcism1.munge(input);
    |                                       ----- ^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:814:31
    |
814 |             let input = INPUT.as_bytes();
    |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                         |
    |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:818:39
    |
818 |             let munge_iter = xorcism1.munge(input);
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:819:50
    |
819 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:819:62
    |
819 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:836:45
    |
836 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:852:44
    |
852 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:864:45
    |
864 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:952:45
    |
952 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:966:44
    |
966 |             let mut xorcism = Xorcism::new(KEY);
    |                               ------------ ^^^ doesn't have a size known at compile-time
    |                               |
    |                               required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:967:49
    |
967 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                           |
    |                                           required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:967:55
    |
967 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                 ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                                 |
    |                                                 this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:967:43
    |
967 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                           ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:967:67
    |
967 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
    |                                                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
   --> tests/xorcism.rs:976:45
    |
976 |             let mut xorcism1 = Xorcism::new(KEY);
    |                                ------------ ^^^ doesn't have a size known at compile-time
    |                                |
    |                                required by a bound introduced by this call
    |
    = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
   --> /testbed/src/lib.rs:35:16
    |
 35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
    |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
   --> tests/xorcism.rs:978:45
    |
978 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
    |                                       |
    |                                       required by a bound introduced by this call
    |
note: the method call chain might not have had the expected associated types
   --> tests/xorcism.rs:978:51
    |
978 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                             ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
    |                                             |
    |                                             this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:978:39
    |
978 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
    |                                       ^^^^^ expected `u8`, found `&u8`
    |
note: required by a bound in `XorIterator`
   --> /testbed/src/lib.rs:12:40
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
   --> tests/xorcism.rs:979:50
    |
979 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
    |                                            |
    |                                            required by a bound introduced by this call
    |
    = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
   --> /testbed/src/lib.rs:61:41
    |
 61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
    |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
   --> tests/xorcism.rs:979:62
    |
979 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
    |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
    |
   ::: /testbed/src/lib.rs:12:1
    |
 12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
    | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
    |
    = note: the following trait bounds were not satisfied:
            `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
            which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
            which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1000:45
     |
1000 |             let mut xorcism1 = Xorcism::new(key);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1017:44
     |
1017 |             let mut xorcism = Xorcism::new(key);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1018:49
     |
1018 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                           ----- ^^^^^ expected `u8`, found `&u8`
     |                                           |
     |                                           required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1015:31
     |
1015 |             let input = INPUT.as_bytes();
     |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                         |
     |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1018:43
     |
1018 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                           ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1018:56
     |
1018 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1030:45
     |
1030 |             let mut xorcism1 = Xorcism::new(key);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1032:45
     |
1032 |             let munge_iter = xorcism1.munge(input);
     |                                       ----- ^^^^^ expected `u8`, found `&u8`
     |                                       |
     |                                       required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1028:31
     |
1028 |             let input = INPUT.as_bytes();
     |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                         |
     |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1032:39
     |
1032 |             let munge_iter = xorcism1.munge(input);
     |                                       ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1033:50
     |
1033 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
     |                                            |
     |                                            required by a bound introduced by this call
     |
     = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1033:62
     |
1033 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1050:45
     |
1050 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1066:44
     |
1066 |             let mut xorcism = Xorcism::new(KEY);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1078:45
     |
1078 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1163:45
     |
1163 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1177:44
     |
1177 |             let mut xorcism = Xorcism::new(KEY);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1178:49
     |
1178 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                           ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
     |                                           |
     |                                           required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1178:55
     |
1178 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                                 ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                                                 |
     |                                                 this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1178:43
     |
1178 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                           ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1178:67
     |
1178 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1187:45
     |
1187 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1189:45
     |
1189 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                       ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
     |                                       |
     |                                       required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1189:51
     |
1189 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                             ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                                             |
     |                                             this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1189:39
     |
1189 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                       ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1190:50
     |
1190 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
     |                                            |
     |                                            required by a bound introduced by this call
     |
     = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1190:62
     |
1190 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1211:45
     |
1211 |             let mut xorcism1 = Xorcism::new(key);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1228:44
     |
1228 |             let mut xorcism = Xorcism::new(key);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1229:49
     |
1229 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                           ----- ^^^^^ expected `u8`, found `&u8`
     |                                           |
     |                                           required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1226:31
     |
1226 |             let input = INPUT.as_bytes();
     |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                         |
     |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1229:43
     |
1229 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                           ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1229:56
     |
1229 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1241:45
     |
1241 |             let mut xorcism1 = Xorcism::new(key);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1243:45
     |
1243 |             let munge_iter = xorcism1.munge(input);
     |                                       ----- ^^^^^ expected `u8`, found `&u8`
     |                                       |
     |                                       required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1239:31
     |
1239 |             let input = INPUT.as_bytes();
     |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                         |
     |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1243:39
     |
1243 |             let munge_iter = xorcism1.munge(input);
     |                                       ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1244:50
     |
1244 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
     |                                            |
     |                                            required by a bound introduced by this call
     |
     = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1244:62
     |
1244 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1261:45
     |
1261 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1277:44
     |
1277 |             let mut xorcism = Xorcism::new(KEY);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1289:45
     |
1289 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1375:45
     |
1375 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1389:44
     |
1389 |             let mut xorcism = Xorcism::new(KEY);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1390:49
     |
1390 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                           ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
     |                                           |
     |                                           required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1390:55
     |
1390 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                                 ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                                                 |
     |                                                 this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1390:43
     |
1390 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                           ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1390:67
     |
1390 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1399:45
     |
1399 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1401:45
     |
1401 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                       ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
     |                                       |
     |                                       required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1401:51
     |
1401 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                             ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                                             |
     |                                             this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1401:39
     |
1401 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                       ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1402:50
     |
1402 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
     |                                            |
     |                                            required by a bound introduced by this call
     |
     = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1402:62
     |
1402 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1423:45
     |
1423 |             let mut xorcism1 = Xorcism::new(key);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1440:44
     |
1440 |             let mut xorcism = Xorcism::new(key);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1441:49
     |
1441 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                           ----- ^^^^^ expected `u8`, found `&u8`
     |                                           |
     |                                           required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1438:31
     |
1438 |             let input = INPUT.as_bytes();
     |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                         |
     |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1441:43
     |
1441 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                           ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1441:56
     |
1441 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1453:45
     |
1453 |             let mut xorcism1 = Xorcism::new(key);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1455:45
     |
1455 |             let munge_iter = xorcism1.munge(input);
     |                                       ----- ^^^^^ expected `u8`, found `&u8`
     |                                       |
     |                                       required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1451:31
     |
1451 |             let input = INPUT.as_bytes();
     |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                         |
     |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1455:39
     |
1455 |             let munge_iter = xorcism1.munge(input);
     |                                       ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1456:50
     |
1456 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
     |                                            |
     |                                            required by a bound introduced by this call
     |
     = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1456:62
     |
1456 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1473:45
     |
1473 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1489:44
     |
1489 |             let mut xorcism = Xorcism::new(KEY);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1501:45
     |
1501 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1586:45
     |
1586 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1600:44
     |
1600 |             let mut xorcism = Xorcism::new(KEY);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1601:49
     |
1601 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                           ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
     |                                           |
     |                                           required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1601:55
     |
1601 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                                 ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                                                 |
     |                                                 this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1601:43
     |
1601 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                           ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1601:67
     |
1601 |             let result: Vec<u8> = xorcism.munge(INPUT.as_bytes()).collect();
     |                                                                   ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1610:45
     |
1610 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1612:45
     |
1612 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                       ----- ^^^^^^^^^^^^^^^^ expected `u8`, found `&u8`
     |                                       |
     |                                       required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1612:51
     |
1612 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                             ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                                             |
     |                                             this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1612:39
     |
1612 |             let munge_iter = xorcism1.munge(INPUT.as_bytes());
     |                                       ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1613:50
     |
1613 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
     |                                            |
     |                                            required by a bound introduced by this call
     |
     = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1613:62
     |
1613 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1634:45
     |
1634 |             let mut xorcism1 = Xorcism::new(key);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1651:44
     |
1651 |             let mut xorcism = Xorcism::new(key);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1652:49
     |
1652 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                           ----- ^^^^^ expected `u8`, found `&u8`
     |                                           |
     |                                           required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1649:31
     |
1649 |             let input = INPUT.as_bytes();
     |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                         |
     |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1652:43
     |
1652 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                           ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, std::slice::Iter<'_, u8>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1652:56
     |
1652 |             let result: Vec<u8> = xorcism.munge(input).collect();
     |                                                        ^^^^^^^ method cannot be called on `XorIterator<'_, std::slice::Iter<'_, u8>>` due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<std::slice::Iter<'_, u8> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `&mut XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`

error[E0277]: the size for values of type `[u8]` cannot be known at compilation time
    --> tests/xorcism.rs:1664:45
     |
1664 |             let mut xorcism1 = Xorcism::new(key);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `[u8]`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0271]: type mismatch resolving `<&[u8] as IntoIterator>::Item == u8`
    --> tests/xorcism.rs:1666:45
     |
1666 |             let munge_iter = xorcism1.munge(input);
     |                                       ----- ^^^^^ expected `u8`, found `&u8`
     |                                       |
     |                                       required by a bound introduced by this call
     |
note: the method call chain might not have had the expected associated types
    --> tests/xorcism.rs:1662:31
     |
1662 |             let input = INPUT.as_bytes();
     |                         ----- ^^^^^^^^^^ `IntoIterator::Item` is `&u8` here
     |                         |
     |                         this expression has type `&str`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1666:39
     |
1666 |             let munge_iter = xorcism1.munge(input);
     |                                       ^^^^^ expected `u8`, found `&u8`
     |
note: required by a bound in `XorIterator`
    --> /testbed/src/lib.rs:12:40
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     |                                        ^^^^^^^^^ required by this bound in `XorIterator`

error[E0271]: expected `Iter<'_, u8>` to be an iterator that yields `u8`, but it yields `&u8`
    --> tests/xorcism.rs:1667:50
     |
1667 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                            ----- ^^^^^^^^^^ expected `u8`, found `&u8`
     |                                            |
     |                                            required by a bound introduced by this call
     |
     = note: required for `XorIterator<'_, std::slice::Iter<'_, u8>>` to implement `Iterator`
note: required by a bound in `xorcism::Xorcism::<'a>::munge`
    --> /testbed/src/lib.rs:61:41
     |
  61 |     pub fn munge<'x, Data: IntoIterator<Item = u8>>(&'x self, data: Data) -> XorIterator<'x, Data::IntoIter> {
     |                                         ^^^^^^^^^ required by this bound in `Xorcism::<'a>::munge`

error[E0599]: the method `collect` exists for struct `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>`, but its trait bounds were not satisfied
    --> tests/xorcism.rs:1667:62
     |
1667 |             let result: Vec<u8> = xorcism2.munge(munge_iter).collect();
     |                                                              ^^^^^^^ method cannot be called due to unsatisfied trait bounds
     |
    ::: /testbed/src/lib.rs:12:1
     |
  12 | pub struct XorIterator<'x, I: Iterator<Item = u8>> {
     | -------------------------------------------------- doesn't satisfy `<_ as Iterator>::Item = u8` or `_: Iterator`
     |
     = note: the following trait bounds were not satisfied:
             `<XorIterator<'_, std::slice::Iter<'_, u8>> as Iterator>::Item = u8`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, std::slice::Iter<'_, u8>>: Iterator`
             which is required by `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             `XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`
             which is required by `&mut XorIterator<'_, XorIterator<'_, std::slice::Iter<'_, u8>>>: Iterator`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1684:45
     |
1684 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1700:44
     |
1700 |             let mut xorcism = Xorcism::new(KEY);
     |                               ------------ ^^^ doesn't have a size known at compile-time
     |                               |
     |                               required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

error[E0277]: the size for values of type `str` cannot be known at compilation time
    --> tests/xorcism.rs:1712:45
     |
1712 |             let mut xorcism1 = Xorcism::new(KEY);
     |                                ------------ ^^^ doesn't have a size known at compile-time
     |                                |
     |                                required by a bound introduced by this call
     |
     = help: the trait `Sized` is not implemented for `str`
note: required by an implicit `Sized` bound in `xorcism::Xorcism::<'a>::new`
    --> /testbed/src/lib.rs:35:16
     |
  35 |     pub fn new<Key: AsRef<[u8]>>(key: &'a Key) -> Xorcism<'a> {
     |                ^^^ required by the implicit `Sized` requirement on this type parameter in `Xorcism::<'a>::new`

Some errors have detailed explanations: E0271, E0277, E0599.
For more information about an error, try `rustc --explain E0271`.
error: could not compile `xorcism` (test "xorcism") due to 202 previous errors
