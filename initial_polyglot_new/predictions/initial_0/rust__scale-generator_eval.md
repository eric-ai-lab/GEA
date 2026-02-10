+ cargo test -- --include-ignored
   Compiling scale_generator v2.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.38s
     Running unittests src/lib.rs (target/debug/deps/scale_generator-ca8562481bb6a916)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/scale-generator.rs (target/debug/deps/scale_generator-9d702363af89d907)

running 17 tests
test chromatic_scale_with_flats ... FAILED
test chromatic_scale_with_sharps ... FAILED
test dorian_mode ... FAILED
test enigmatic ... ok
test harmonic_minor ... FAILED
test hexatonic ... ok
test locrian_mode ... FAILED
test lydian_mode ... FAILED
test major_scale_with_flats ... ok
test major_scale_with_sharps ... ok
test minor_scale_with_flats ... FAILED
test minor_scale_with_sharps ... FAILED
test mixolydian_mode ... ok
test octatonic ... ok
test pentatonic ... ok
test phrygian_mode ... FAILED
test simple_major_scale ... ok

failures:

---- chromatic_scale_with_flats stdout ----

thread 'chromatic_scale_with_flats' (4624) panicked at tests/scale-generator.rs:16:5:
assertion `left == right` failed
  left: ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]
 right: ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F"]
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- chromatic_scale_with_sharps stdout ----

thread 'chromatic_scale_with_sharps' (4625) panicked at tests/scale-generator.rs:16:5:
assertion `left == right` failed
  left: ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
 right: ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]

---- dorian_mode stdout ----

thread 'dorian_mode' (4626) panicked at tests/scale-generator.rs:24:42:
called `Result::unwrap()` on an `Err` value: Error

---- harmonic_minor stdout ----

thread 'harmonic_minor' (4628) panicked at tests/scale-generator.rs:24:42:
called `Result::unwrap()` on an `Err` value: Error

---- locrian_mode stdout ----

thread 'locrian_mode' (4630) panicked at tests/scale-generator.rs:24:42:
called `Result::unwrap()` on an `Err` value: Error

---- lydian_mode stdout ----

thread 'lydian_mode' (4631) panicked at tests/scale-generator.rs:24:42:
called `Result::unwrap()` on an `Err` value: Error

---- minor_scale_with_flats stdout ----

thread 'minor_scale_with_flats' (4634) panicked at tests/scale-generator.rs:24:42:
called `Result::unwrap()` on an `Err` value: Error

---- minor_scale_with_sharps stdout ----

thread 'minor_scale_with_sharps' (4635) panicked at tests/scale-generator.rs:24:42:
called `Result::unwrap()` on an `Err` value: Error

---- phrygian_mode stdout ----

thread 'phrygian_mode' (4639) panicked at tests/scale-generator.rs:24:42:
called `Result::unwrap()` on an `Err` value: Error


failures:
    chromatic_scale_with_flats
    chromatic_scale_with_sharps
    dorian_mode
    harmonic_minor
    locrian_mode
    lydian_mode
    minor_scale_with_flats
    minor_scale_with_sharps
    phrygian_mode

test result: FAILED. 8 passed; 9 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

error: test failed, to rerun pass `--test scale-generator`
