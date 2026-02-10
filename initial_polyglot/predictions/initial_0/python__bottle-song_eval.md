+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 7 items

bottle_song_test.py FFFFFFF                                              [100%]

=================================== FAILURES ===================================
________________________ BottleSongTest.test_all_verses ________________________

self = <bottle_song_test.BottleSongTest testMethod=test_all_verses>

    def test_all_verses(self):
        expected = [
            "Ten green bottles hanging on the wall,",
            "Ten green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be nine green bottles hanging on the wall.",
            "",
            "Nine green bottles hanging on the wall,",
            "Nine green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be eight green bottles hanging on the wall.",
            "",
            "Eight green bottles hanging on the wall,",
            "Eight green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be seven green bottles hanging on the wall.",
            "",
            "Seven green bottles hanging on the wall,",
            "Seven green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be six green bottles hanging on the wall.",
            "",
            "Six green bottles hanging on the wall,",
            "Six green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be five green bottles hanging on the wall.",
            "",
            "Five green bottles hanging on the wall,",
            "Five green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be four green bottles hanging on the wall.",
            "",
            "Four green bottles hanging on the wall,",
            "Four green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be three green bottles hanging on the wall.",
            "",
            "Three green bottles hanging on the wall,",
            "Three green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be two green bottles hanging on the wall.",
            "",
            "Two green bottles hanging on the wall,",
            "Two green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be one green bottle hanging on the wall.",
            "",
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall.",
        ]
>       self.assertEqual(recite(start=10, take=10), expected)
E       AssertionError: "Ten green bottles hanging on the wall,\n[1825 chars]all." != ['Ten green bottles hanging on the wall,'[1923 chars]ll."]

bottle_song_test.py:134: AssertionError
___________________ BottleSongTest.test_first_generic_verse ____________________

self = <bottle_song_test.BottleSongTest testMethod=test_first_generic_verse>

    def test_first_generic_verse(self):
        expected = [
            "Ten green bottles hanging on the wall,",
            "Ten green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be nine green bottles hanging on the wall.",
        ]
>       self.assertEqual(recite(start=10), expected)
E       AssertionError: "Ten green bottles hanging on the wall,\n[138 chars]all." != ['Ten green bottles hanging on the wall,'[146 chars]ll."]

bottle_song_test.py:20: AssertionError
_____________________ BottleSongTest.test_first_two_verses _____________________

self = <bottle_song_test.BottleSongTest testMethod=test_first_two_verses>

    def test_first_two_verses(self):
        expected = [
            "Ten green bottles hanging on the wall,",
            "Ten green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be nine green bottles hanging on the wall.",
            "",
            "Nine green bottles hanging on the wall,",
            "Nine green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be eight green bottles hanging on the wall.",
        ]
>       self.assertEqual(recite(start=10, take=2), expected)
E       AssertionError: "Ten green bottles hanging on the wall,\n[327 chars]all." != ['Ten green bottles hanging on the wall,'[345 chars]ll."]

bottle_song_test.py:61: AssertionError
____________________ BottleSongTest.test_last_generic_verse ____________________

self = <bottle_song_test.BottleSongTest testMethod=test_last_generic_verse>

    def test_last_generic_verse(self):
        expected = [
            "Three green bottles hanging on the wall,",
            "Three green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be two green bottles hanging on the wall.",
        ]
>       self.assertEqual(recite(start=3), expected)
E       AssertionError: "Three green bottles hanging on the wall,[141 chars]all." != ['Three green bottles hanging on the wall[149 chars]ll."]

bottle_song_test.py:29: AssertionError
____________________ BottleSongTest.test_last_three_verses _____________________

self = <bottle_song_test.BottleSongTest testMethod=test_last_three_verses>

    def test_last_three_verses(self):
        expected = [
            "Three green bottles hanging on the wall,",
            "Three green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be two green bottles hanging on the wall.",
            "",
            "Two green bottles hanging on the wall,",
            "Two green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be one green bottle hanging on the wall.",
            "",
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall.",
        ]
>       self.assertEqual(recite(start=3, take=3), expected)
E       AssertionError: "Three green bottles hanging on the wall,[507 chars]all." != ['Three green bottles hanging on the wall[535 chars]ll."]

bottle_song_test.py:80: AssertionError
___________________ BottleSongTest.test_verse_with_1_bottle ____________________

self = <bottle_song_test.BottleSongTest testMethod=test_verse_with_1_bottle>

    def test_verse_with_1_bottle(self):
        expected = [
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall.",
        ]
>       self.assertEqual(recite(start=1), expected)
E       AssertionError: "One green bottle hanging on the wall,\nO[134 chars]all." != ['One green bottle hanging on the wall,',[142 chars]ll."]

bottle_song_test.py:47: AssertionError
___________________ BottleSongTest.test_verse_with_2_bottles ___________________

self = <bottle_song_test.BottleSongTest testMethod=test_verse_with_2_bottles>

    def test_verse_with_2_bottles(self):
        expected = [
            "Two green bottles hanging on the wall,",
            "Two green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be one green bottle hanging on the wall.",
        ]
>       self.assertEqual(recite(start=2), expected)
E       AssertionError: "Two green bottles hanging on the wall,\n[136 chars]all." != ['Two green bottles hanging on the wall,'[144 chars]ll."]

bottle_song_test.py:38: AssertionError
=========================== short test summary info ============================
FAILED bottle_song_test.py::BottleSongTest::test_all_verses - AssertionError:...
FAILED bottle_song_test.py::BottleSongTest::test_first_generic_verse - Assert...
FAILED bottle_song_test.py::BottleSongTest::test_first_two_verses - Assertion...
FAILED bottle_song_test.py::BottleSongTest::test_last_generic_verse - Asserti...
FAILED bottle_song_test.py::BottleSongTest::test_last_three_verses - Assertio...
FAILED bottle_song_test.py::BottleSongTest::test_verse_with_1_bottle - Assert...
FAILED bottle_song_test.py::BottleSongTest::test_verse_with_2_bottles - Asser...
============================== 7 failed in 0.12s ===============================
