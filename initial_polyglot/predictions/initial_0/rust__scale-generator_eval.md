+ cargo test -- --include-ignored
   Compiling scale_generator v2.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.68s
     Running unittests src/lib.rs (target/debug/deps/scale_generator-895304eac80ffb99)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/scale-generator.rs (target/debug/deps/scale_generator-39545888c07c42b7)

running 17 tests
test chromatic_scale_with_sharps ... FAILED
test chromatic_scale_with_flats ... FAILED
test dorian_mode ... FAILED
test harmonic_minor ... FAILED
test enigmatic ... ok
test hexatonic ... ok
test locrian_mode ... FAILED
test lydian_mode ... FAILED
test major_scale_with_flats ... ok
test major_scale_with_sharps ... ok
test minor_scale_with_flats ... FAILED
test minor_scale_with_sharps ... FAILED
test mixolydian_mode ... ok
test pentatonic ... ok
test octatonic ... ok
test phrygian_mode ... FAILED
test simple_major_scale ... ok

failures:

---- chromatic_scale_with_sharps stdout ----

thread 'chromatic_scale_with_sharps' panicked at tests/scale-generator.rs:16:5:
assertion `left == right` failed
  left: ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
 right: ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- chromatic_scale_with_flats stdout ----

thread 'chromatic_scale_with_flats' panicked at tests/scale-generator.rs:16:5:
assertion `left == right` failed
  left: ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]
 right: ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F"]

---- dorian_mode stdout ----

thread 'dorian_mode' panicked at tests/scale-generator.rs:25:5:
assertion `left == right` failed
  left: ["d", "e", "f", "g", "a", "b", "c", "d"]
 right: ["D", "E", "F", "G", "A", "B", "C", "D"]

---- harmonic_minor stdout ----

thread 'harmonic_minor' panicked at tests/scale-generator.rs:25:5:
assertion `left == right` failed
  left: ["d", "e", "f", "g", "a", "bb", "db", "d"]
 right: ["D", "E", "F", "G", "A", "Bb", "Db", "D"]

---- locrian_mode stdout ----

thread 'locrian_mode' panicked at tests/scale-generator.rs:25:5:
assertion `left == right` failed
  left: ["g", "ab", "bb", "c", "db", "eb", "f", "g"]
 right: ["G", "Ab", "Bb", "C", "Db", "Eb", "F", "G"]

---- lydian_mode stdout ----

thread 'lydian_mode' panicked at tests/scale-generator.rs:25:5:
assertion `left == right` failed
  left: ["a", "b", "c#", "d#", "e", "f#", "g#", "a"]
 right: ["A", "B", "C#", "D#", "E", "F#", "G#", "A"]

---- minor_scale_with_flats stdout ----

thread 'minor_scale_with_flats' panicked at tests/scale-generator.rs:25:5:
assertion `left == right` failed
  left: ["bb", "c", "db", "eb", "f", "gb", "ab", "bb"]
 right: ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]

---- minor_scale_with_sharps stdout ----

thread 'minor_scale_with_sharps' panicked at tests/scale-generator.rs:25:5:
assertion `left == right` failed
  left: ["f#", "g#", "a", "b", "c#", "d", "e", "f#"]
 right: ["F#", "G#", "A", "B", "C#", "D", "E", "F#"]

---- phrygian_mode stdout ----

thread 'phrygian_mode' panicked at tests/scale-generator.rs:25:5:
assertion `left == right` failed
  left: ["e", "f", "g", "a", "b", "c", "d", "e"]
 right: ["E", "F", "G", "A", "B", "C", "D", "E"]


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
