+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 17 items

scale_generator_test.py FF.FFFFFFFFFFFF..                                [100%]

=================================== FAILURES ===================================
______________ ScaleGeneratorTest.test_chromatic_scale_with_flats ______________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_chromatic_scale_with_flats>

    def test_chromatic_scale_with_flats(self):
        expected = ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]
>       self.assertEqual(Scale("F").chromatic(), expected)
E       AssertionError: Lists differ: ['F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B', 'C', 'D♭', 'D', 'E♭', 'E'] != ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E']
E       
E       First differing element 1:
E       'G♭'
E       'Gb'
E       
E       - ['F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B', 'C', 'D♭', 'D', 'E♭', 'E']
E       ?         ^          ^          ^               ^          ^
E       
E       + ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E']
E       ?         ^          ^          ^               ^          ^

scale_generator_test.py:21: AssertionError
_____________ ScaleGeneratorTest.test_chromatic_scale_with_sharps ______________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_chromatic_scale_with_sharps>

    def test_chromatic_scale_with_sharps(self):
        expected = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
>       self.assertEqual(Scale("C").chromatic(), expected)
E       AssertionError: Lists differ: ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'] != ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
E       
E       First differing element 1:
E       'C♯'
E       'C#'
E       
E       - ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B']
E       ?         ^          ^               ^          ^          ^
E       
E       + ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
E       ?         ^          ^               ^          ^          ^

scale_generator_test.py:17: AssertionError
______________________ ScaleGeneratorTest.test_enigmatic _______________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_enigmatic>

    def test_enigmatic(self):
        expected = ["G", "G#", "B", "C#", "D#", "F", "F#", "G"]
>       self.assertEqual(Scale("G").interval("mAMMMmm"), expected)
E       AssertionError: Lists differ: ['G', 'G♯', 'B', 'C♯', 'D♯', 'F', 'F♯', 'G'] != ['G', 'G#', 'B', 'C#', 'D#', 'F', 'F#', 'G']
E       
E       First differing element 1:
E       'G♯'
E       'G#'
E       
E       - ['G', 'G♯', 'B', 'C♯', 'D♯', 'F', 'F♯', 'G']
E       ?         ^          ^     ^          ^
E       
E       + ['G', 'G#', 'B', 'C#', 'D#', 'F', 'F#', 'G']
E       ?         ^          ^     ^          ^

scale_generator_test.py:82: AssertionError
____________________ ScaleGeneratorTest.test_harmonic_minor ____________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_harmonic_minor>

    def test_harmonic_minor(self):
        expected = ["D", "E", "F", "G", "A", "Bb", "Db", "D"]
>       self.assertEqual(Scale("d").interval("MmMMmAm"), expected)
E       AssertionError: Lists differ: ['D', 'E', 'F', 'G', 'A', 'B♭', 'D♭', 'D'] != ['D', 'E', 'F', 'G', 'A', 'Bb', 'Db', 'D']
E       
E       First differing element 5:
E       'B♭'
E       'Bb'
E       
E       - ['D', 'E', 'F', 'G', 'A', 'B♭', 'D♭', 'D']
E       ?                             ^     ^
E       
E       + ['D', 'E', 'F', 'G', 'A', 'Bb', 'Db', 'D']
E       ?                             ^     ^

scale_generator_test.py:66: AssertionError
______________________ ScaleGeneratorTest.test_hexatonic _______________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_hexatonic>

    def test_hexatonic(self):
        expected = ["Db", "Eb", "F", "G", "A", "B", "Db"]
>       self.assertEqual(Scale("Db").interval("MMMMMM"), expected)
E       AssertionError: Lists differ: ['A', 'B', 'C♯', 'D♯', 'F', 'G', 'A'] != ['Db', 'Eb', 'F', 'G', 'A', 'B', 'Db']
E       
E       First differing element 0:
E       'A'
E       'Db'
E       
E       - ['A', 'B', 'C♯', 'D♯', 'F', 'G', 'A']
E       + ['Db', 'Eb', 'F', 'G', 'A', 'B', 'Db']

scale_generator_test.py:74: AssertionError
_____________________ ScaleGeneratorTest.test_locrian_mode _____________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_locrian_mode>

    def test_locrian_mode(self):
        expected = ["G", "Ab", "Bb", "C", "Db", "Eb", "F", "G"]
>       self.assertEqual(Scale("g").interval("mMMmMMM"), expected)
E       AssertionError: Lists differ: ['G', 'A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G'] != ['G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G']
E       
E       First differing element 1:
E       'A♭'
E       'Ab'
E       
E       - ['G', 'A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G']
E       ?         ^     ^          ^     ^
E       
E       + ['G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G']
E       ?         ^     ^          ^     ^

scale_generator_test.py:62: AssertionError
_____________________ ScaleGeneratorTest.test_lydian_mode ______________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_lydian_mode>

    def test_lydian_mode(self):
        expected = ["A", "B", "C#", "D#", "E", "F#", "G#", "A"]
>       self.assertEqual(Scale("a").interval("MMMmMMm"), expected)
E       AssertionError: Lists differ: ['A', 'B', 'C♯', 'D♯', 'E', 'F♯', 'G♯', 'A'] != ['A', 'B', 'C#', 'D#', 'E', 'F#', 'G#', 'A']
E       
E       First differing element 2:
E       'C♯'
E       'C#'
E       
E       - ['A', 'B', 'C♯', 'D♯', 'E', 'F♯', 'G♯', 'A']
E       ?              ^     ^          ^     ^
E       
E       + ['A', 'B', 'C#', 'D#', 'E', 'F#', 'G#', 'A']
E       ?              ^     ^          ^     ^

scale_generator_test.py:54: AssertionError
________________ ScaleGeneratorTest.test_major_scale_with_flats ________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_major_scale_with_flats>

    def test_major_scale_with_flats(self):
        expected = ["F", "G", "A", "Bb", "C", "D", "E", "F"]
>       self.assertEqual(Scale("F").interval("MMmMMMm"), expected)
E       AssertionError: Lists differ: ['F', 'G', 'A', 'B♭', 'C', 'D', 'E', 'F'] != ['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F']
E       
E       First differing element 3:
E       'B♭'
E       'Bb'
E       
E       - ['F', 'G', 'A', 'B♭', 'C', 'D', 'E', 'F']
E       ?                   ^
E       
E       + ['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F']
E       ?                   ^

scale_generator_test.py:34: AssertionError
_______________ ScaleGeneratorTest.test_major_scale_with_sharps ________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_major_scale_with_sharps>

    def test_major_scale_with_sharps(self):
        expected = ["G", "A", "B", "C", "D", "E", "F#", "G"]
>       self.assertEqual(Scale("G").interval("MMmMMMm"), expected)
E       AssertionError: Lists differ: ['G', 'A', 'B', 'C', 'D', 'E', 'F♯', 'G'] != ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']
E       
E       First differing element 6:
E       'F♯'
E       'F#'
E       
E       - ['G', 'A', 'B', 'C', 'D', 'E', 'F♯', 'G']
E       ?                                  ^
E       
E       + ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']
E       ?                                  ^

scale_generator_test.py:30: AssertionError
________________ ScaleGeneratorTest.test_minor_scale_with_flats ________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_minor_scale_with_flats>

    def test_minor_scale_with_flats(self):
        expected = ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]
>       self.assertEqual(Scale("bb").interval("MmMMmMM"), expected)
E       AssertionError: Lists differ: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'] != ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb']
E       
E       First differing element 0:
E       'A'
E       'Bb'
E       
E       - ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']
E       ?   ^  -----
E       
E       + ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb']
E       ?   ^^          +     +          +     +++++++

scale_generator_test.py:42: AssertionError
_______________ ScaleGeneratorTest.test_minor_scale_with_sharps ________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_minor_scale_with_sharps>

    def test_minor_scale_with_sharps(self):
        expected = ["F#", "G#", "A", "B", "C#", "D", "E", "F#"]
>       self.assertEqual(Scale("f#").interval("MmMMmMM"), expected)
E       AssertionError: Lists differ: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'] != ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#']
E       
E       First differing element 0:
E       'A'
E       'F#'
E       
E       - ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']
E       + ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#']

scale_generator_test.py:38: AssertionError
___________________ ScaleGeneratorTest.test_mixolydian_mode ____________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_mixolydian_mode>

    def test_mixolydian_mode(self):
        expected = ["Eb", "F", "G", "Ab", "Bb", "C", "Db", "Eb"]
>       self.assertEqual(Scale("Eb").interval("MMmMMmM"), expected)
E       AssertionError: Lists differ: ['A', 'B', 'C♯', 'D', 'E', 'F♯', 'G', 'A'] != ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb']
E       
E       First differing element 0:
E       'A'
E       'Eb'
E       
E       - ['A', 'B', 'C♯', 'D', 'E', 'F♯', 'G', 'A']
E       + ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb']

scale_generator_test.py:50: AssertionError
______________________ ScaleGeneratorTest.test_octatonic _______________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_octatonic>

    def test_octatonic(self):
        expected = ["C", "D", "D#", "F", "F#", "G#", "A", "B", "C"]
>       self.assertEqual(Scale("C").interval("MmMmMmMm"), expected)
E       AssertionError: Lists differ: ['C', 'D', 'D♯', 'F', 'F♯', 'G♯', 'A', 'B', 'C'] != ['C', 'D', 'D#', 'F', 'F#', 'G#', 'A', 'B', 'C']
E       
E       First differing element 2:
E       'D♯'
E       'D#'
E       
E       - ['C', 'D', 'D♯', 'F', 'F♯', 'G♯', 'A', 'B', 'C']
E       ?              ^          ^     ^
E       
E       + ['C', 'D', 'D#', 'F', 'F#', 'G#', 'A', 'B', 'C']
E       ?              ^          ^     ^

scale_generator_test.py:70: AssertionError
______________________ ScaleGeneratorTest.test_pentatonic ______________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_pentatonic>

    def test_pentatonic(self):
        expected = ["A", "B", "C#", "E", "F#", "A"]
>       self.assertEqual(Scale("A").interval("MMAMA"), expected)
E       AssertionError: Lists differ: ['A', 'B', 'C♯', 'E', 'F♯', 'A'] != ['A', 'B', 'C#', 'E', 'F#', 'A']
E       
E       First differing element 2:
E       'C♯'
E       'C#'
E       
E       - ['A', 'B', 'C♯', 'E', 'F♯', 'A']
E       ?              ^          ^
E       
E       + ['A', 'B', 'C#', 'E', 'F#', 'A']
E       ?              ^          ^

scale_generator_test.py:78: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED scale_generator_test.py::ScaleGeneratorTest::test_dorian_mode
PASSED scale_generator_test.py::ScaleGeneratorTest::test_phrygian_mode
PASSED scale_generator_test.py::ScaleGeneratorTest::test_simple_major_scale
FAILED scale_generator_test.py::ScaleGeneratorTest::test_chromatic_scale_with_flats
FAILED scale_generator_test.py::ScaleGeneratorTest::test_chromatic_scale_with_sharps
FAILED scale_generator_test.py::ScaleGeneratorTest::test_enigmatic - Assertio...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_harmonic_minor - Ass...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_hexatonic - Assertio...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_locrian_mode - Asser...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_lydian_mode - Assert...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_major_scale_with_flats
FAILED scale_generator_test.py::ScaleGeneratorTest::test_major_scale_with_sharps
FAILED scale_generator_test.py::ScaleGeneratorTest::test_minor_scale_with_flats
FAILED scale_generator_test.py::ScaleGeneratorTest::test_minor_scale_with_sharps
FAILED scale_generator_test.py::ScaleGeneratorTest::test_mixolydian_mode - As...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_octatonic - Assertio...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_pentatonic - Asserti...
========================= 14 failed, 3 passed in 0.15s =========================
