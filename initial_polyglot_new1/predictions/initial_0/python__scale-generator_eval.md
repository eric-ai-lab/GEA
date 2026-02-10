+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: asyncio-1.3.0, anyio-4.12.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 17 items

scale_generator_test.py .F.F...F.F.F.FF..                                [100%]

=================================== FAILURES ===================================
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
_______________ ScaleGeneratorTest.test_minor_scale_with_sharps ________________

self = <scale_generator_test.ScaleGeneratorTest testMethod=test_minor_scale_with_sharps>

    def test_minor_scale_with_sharps(self):
        expected = ["F#", "G#", "A", "B", "C#", "D", "E", "F#"]
>       self.assertEqual(Scale("f#").interval("MmMMmMM"), expected)
E       AssertionError: Lists differ: ['F♯', 'G♯', 'A', 'B', 'C♯', 'D', 'E', 'F♯'] != ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#']
E       
E       First differing element 0:
E       'F♯'
E       'F#'
E       
E       - ['F♯', 'G♯', 'A', 'B', 'C♯', 'D', 'E', 'F♯']
E       ?    ^     ^               ^               ^
E       
E       + ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#']
E       ?    ^     ^               ^               ^

scale_generator_test.py:38: AssertionError
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
PASSED scale_generator_test.py::ScaleGeneratorTest::test_chromatic_scale_with_flats
PASSED scale_generator_test.py::ScaleGeneratorTest::test_dorian_mode
PASSED scale_generator_test.py::ScaleGeneratorTest::test_harmonic_minor
PASSED scale_generator_test.py::ScaleGeneratorTest::test_hexatonic
PASSED scale_generator_test.py::ScaleGeneratorTest::test_locrian_mode
PASSED scale_generator_test.py::ScaleGeneratorTest::test_major_scale_with_flats
PASSED scale_generator_test.py::ScaleGeneratorTest::test_minor_scale_with_flats
PASSED scale_generator_test.py::ScaleGeneratorTest::test_mixolydian_mode
PASSED scale_generator_test.py::ScaleGeneratorTest::test_phrygian_mode
PASSED scale_generator_test.py::ScaleGeneratorTest::test_simple_major_scale
FAILED scale_generator_test.py::ScaleGeneratorTest::test_chromatic_scale_with_sharps
FAILED scale_generator_test.py::ScaleGeneratorTest::test_enigmatic - Assertio...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_lydian_mode - Assert...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_major_scale_with_sharps
FAILED scale_generator_test.py::ScaleGeneratorTest::test_minor_scale_with_sharps
FAILED scale_generator_test.py::ScaleGeneratorTest::test_octatonic - Assertio...
FAILED scale_generator_test.py::ScaleGeneratorTest::test_pentatonic - Asserti...
========================= 7 failed, 10 passed in 0.05s =========================
