+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 8 items

beer_song_test.py FFFFFFFF                                               [100%]

=================================== FAILURES ===================================
_________________________ BeerSongTest.test_all_verses _________________________

self = <beer_song_test.BeerSongTest testMethod=test_all_verses>

    def test_all_verses(self):
        expected = [
            "99 bottles of beer on the wall, 99 bottles of beer.",
            "Take one down and pass it around, 98 bottles of beer on the wall.",
            "",
            "98 bottles of beer on the wall, 98 bottles of beer.",
            "Take one down and pass it around, 97 bottles of beer on the wall.",
            "",
            "97 bottles of beer on the wall, 97 bottles of beer.",
            "Take one down and pass it around, 96 bottles of beer on the wall.",
            "",
            "96 bottles of beer on the wall, 96 bottles of beer.",
            "Take one down and pass it around, 95 bottles of beer on the wall.",
            "",
            "95 bottles of beer on the wall, 95 bottles of beer.",
            "Take one down and pass it around, 94 bottles of beer on the wall.",
            "",
            "94 bottles of beer on the wall, 94 bottles of beer.",
            "Take one down and pass it around, 93 bottles of beer on the wall.",
            "",
            "93 bottles of beer on the wall, 93 bottles of beer.",
            "Take one down and pass it around, 92 bottles of beer on the wall.",
            "",
            "92 bottles of beer on the wall, 92 bottles of beer.",
            "Take one down and pass it around, 91 bottles of beer on the wall.",
            "",
            "91 bottles of beer on the wall, 91 bottles of beer.",
            "Take one down and pass it around, 90 bottles of beer on the wall.",
            "",
            "90 bottles of beer on the wall, 90 bottles of beer.",
            "Take one down and pass it around, 89 bottles of beer on the wall.",
            "",
            "89 bottles of beer on the wall, 89 bottles of beer.",
            "Take one down and pass it around, 88 bottles of beer on the wall.",
            "",
            "88 bottles of beer on the wall, 88 bottles of beer.",
            "Take one down and pass it around, 87 bottles of beer on the wall.",
            "",
            "87 bottles of beer on the wall, 87 bottles of beer.",
            "Take one down and pass it around, 86 bottles of beer on the wall.",
            "",
            "86 bottles of beer on the wall, 86 bottles of beer.",
            "Take one down and pass it around, 85 bottles of beer on the wall.",
            "",
            "85 bottles of beer on the wall, 85 bottles of beer.",
            "Take one down and pass it around, 84 bottles of beer on the wall.",
            "",
            "84 bottles of beer on the wall, 84 bottles of beer.",
            "Take one down and pass it around, 83 bottles of beer on the wall.",
            "",
            "83 bottles of beer on the wall, 83 bottles of beer.",
            "Take one down and pass it around, 82 bottles of beer on the wall.",
            "",
            "82 bottles of beer on the wall, 82 bottles of beer.",
            "Take one down and pass it around, 81 bottles of beer on the wall.",
            "",
            "81 bottles of beer on the wall, 81 bottles of beer.",
            "Take one down and pass it around, 80 bottles of beer on the wall.",
            "",
            "80 bottles of beer on the wall, 80 bottles of beer.",
            "Take one down and pass it around, 79 bottles of beer on the wall.",
            "",
            "79 bottles of beer on the wall, 79 bottles of beer.",
            "Take one down and pass it around, 78 bottles of beer on the wall.",
            "",
            "78 bottles of beer on the wall, 78 bottles of beer.",
            "Take one down and pass it around, 77 bottles of beer on the wall.",
            "",
            "77 bottles of beer on the wall, 77 bottles of beer.",
            "Take one down and pass it around, 76 bottles of beer on the wall.",
            "",
            "76 bottles of beer on the wall, 76 bottles of beer.",
            "Take one down and pass it around, 75 bottles of beer on the wall.",
            "",
            "75 bottles of beer on the wall, 75 bottles of beer.",
            "Take one down and pass it around, 74 bottles of beer on the wall.",
            "",
            "74 bottles of beer on the wall, 74 bottles of beer.",
            "Take one down and pass it around, 73 bottles of beer on the wall.",
            "",
            "73 bottles of beer on the wall, 73 bottles of beer.",
            "Take one down and pass it around, 72 bottles of beer on the wall.",
            "",
            "72 bottles of beer on the wall, 72 bottles of beer.",
            "Take one down and pass it around, 71 bottles of beer on the wall.",
            "",
            "71 bottles of beer on the wall, 71 bottles of beer.",
            "Take one down and pass it around, 70 bottles of beer on the wall.",
            "",
            "70 bottles of beer on the wall, 70 bottles of beer.",
            "Take one down and pass it around, 69 bottles of beer on the wall.",
            "",
            "69 bottles of beer on the wall, 69 bottles of beer.",
            "Take one down and pass it around, 68 bottles of beer on the wall.",
            "",
            "68 bottles of beer on the wall, 68 bottles of beer.",
            "Take one down and pass it around, 67 bottles of beer on the wall.",
            "",
            "67 bottles of beer on the wall, 67 bottles of beer.",
            "Take one down and pass it around, 66 bottles of beer on the wall.",
            "",
            "66 bottles of beer on the wall, 66 bottles of beer.",
            "Take one down and pass it around, 65 bottles of beer on the wall.",
            "",
            "65 bottles of beer on the wall, 65 bottles of beer.",
            "Take one down and pass it around, 64 bottles of beer on the wall.",
            "",
            "64 bottles of beer on the wall, 64 bottles of beer.",
            "Take one down and pass it around, 63 bottles of beer on the wall.",
            "",
            "63 bottles of beer on the wall, 63 bottles of beer.",
            "Take one down and pass it around, 62 bottles of beer on the wall.",
            "",
            "62 bottles of beer on the wall, 62 bottles of beer.",
            "Take one down and pass it around, 61 bottles of beer on the wall.",
            "",
            "61 bottles of beer on the wall, 61 bottles of beer.",
            "Take one down and pass it around, 60 bottles of beer on the wall.",
            "",
            "60 bottles of beer on the wall, 60 bottles of beer.",
            "Take one down and pass it around, 59 bottles of beer on the wall.",
            "",
            "59 bottles of beer on the wall, 59 bottles of beer.",
            "Take one down and pass it around, 58 bottles of beer on the wall.",
            "",
            "58 bottles of beer on the wall, 58 bottles of beer.",
            "Take one down and pass it around, 57 bottles of beer on the wall.",
            "",
            "57 bottles of beer on the wall, 57 bottles of beer.",
            "Take one down and pass it around, 56 bottles of beer on the wall.",
            "",
            "56 bottles of beer on the wall, 56 bottles of beer.",
            "Take one down and pass it around, 55 bottles of beer on the wall.",
            "",
            "55 bottles of beer on the wall, 55 bottles of beer.",
            "Take one down and pass it around, 54 bottles of beer on the wall.",
            "",
            "54 bottles of beer on the wall, 54 bottles of beer.",
            "Take one down and pass it around, 53 bottles of beer on the wall.",
            "",
            "53 bottles of beer on the wall, 53 bottles of beer.",
            "Take one down and pass it around, 52 bottles of beer on the wall.",
            "",
            "52 bottles of beer on the wall, 52 bottles of beer.",
            "Take one down and pass it around, 51 bottles of beer on the wall.",
            "",
            "51 bottles of beer on the wall, 51 bottles of beer.",
            "Take one down and pass it around, 50 bottles of beer on the wall.",
            "",
            "50 bottles of beer on the wall, 50 bottles of beer.",
            "Take one down and pass it around, 49 bottles of beer on the wall.",
            "",
            "49 bottles of beer on the wall, 49 bottles of beer.",
            "Take one down and pass it around, 48 bottles of beer on the wall.",
            "",
            "48 bottles of beer on the wall, 48 bottles of beer.",
            "Take one down and pass it around, 47 bottles of beer on the wall.",
            "",
            "47 bottles of beer on the wall, 47 bottles of beer.",
            "Take one down and pass it around, 46 bottles of beer on the wall.",
            "",
            "46 bottles of beer on the wall, 46 bottles of beer.",
            "Take one down and pass it around, 45 bottles of beer on the wall.",
            "",
            "45 bottles of beer on the wall, 45 bottles of beer.",
            "Take one down and pass it around, 44 bottles of beer on the wall.",
            "",
            "44 bottles of beer on the wall, 44 bottles of beer.",
            "Take one down and pass it around, 43 bottles of beer on the wall.",
            "",
            "43 bottles of beer on the wall, 43 bottles of beer.",
            "Take one down and pass it around, 42 bottles of beer on the wall.",
            "",
            "42 bottles of beer on the wall, 42 bottles of beer.",
            "Take one down and pass it around, 41 bottles of beer on the wall.",
            "",
            "41 bottles of beer on the wall, 41 bottles of beer.",
            "Take one down and pass it around, 40 bottles of beer on the wall.",
            "",
            "40 bottles of beer on the wall, 40 bottles of beer.",
            "Take one down and pass it around, 39 bottles of beer on the wall.",
            "",
            "39 bottles of beer on the wall, 39 bottles of beer.",
            "Take one down and pass it around, 38 bottles of beer on the wall.",
            "",
            "38 bottles of beer on the wall, 38 bottles of beer.",
            "Take one down and pass it around, 37 bottles of beer on the wall.",
            "",
            "37 bottles of beer on the wall, 37 bottles of beer.",
            "Take one down and pass it around, 36 bottles of beer on the wall.",
            "",
            "36 bottles of beer on the wall, 36 bottles of beer.",
            "Take one down and pass it around, 35 bottles of beer on the wall.",
            "",
            "35 bottles of beer on the wall, 35 bottles of beer.",
            "Take one down and pass it around, 34 bottles of beer on the wall.",
            "",
            "34 bottles of beer on the wall, 34 bottles of beer.",
            "Take one down and pass it around, 33 bottles of beer on the wall.",
            "",
            "33 bottles of beer on the wall, 33 bottles of beer.",
            "Take one down and pass it around, 32 bottles of beer on the wall.",
            "",
            "32 bottles of beer on the wall, 32 bottles of beer.",
            "Take one down and pass it around, 31 bottles of beer on the wall.",
            "",
            "31 bottles of beer on the wall, 31 bottles of beer.",
            "Take one down and pass it around, 30 bottles of beer on the wall.",
            "",
            "30 bottles of beer on the wall, 30 bottles of beer.",
            "Take one down and pass it around, 29 bottles of beer on the wall.",
            "",
            "29 bottles of beer on the wall, 29 bottles of beer.",
            "Take one down and pass it around, 28 bottles of beer on the wall.",
            "",
            "28 bottles of beer on the wall, 28 bottles of beer.",
            "Take one down and pass it around, 27 bottles of beer on the wall.",
            "",
            "27 bottles of beer on the wall, 27 bottles of beer.",
            "Take one down and pass it around, 26 bottles of beer on the wall.",
            "",
            "26 bottles of beer on the wall, 26 bottles of beer.",
            "Take one down and pass it around, 25 bottles of beer on the wall.",
            "",
            "25 bottles of beer on the wall, 25 bottles of beer.",
            "Take one down and pass it around, 24 bottles of beer on the wall.",
            "",
            "24 bottles of beer on the wall, 24 bottles of beer.",
            "Take one down and pass it around, 23 bottles of beer on the wall.",
            "",
            "23 bottles of beer on the wall, 23 bottles of beer.",
            "Take one down and pass it around, 22 bottles of beer on the wall.",
            "",
            "22 bottles of beer on the wall, 22 bottles of beer.",
            "Take one down and pass it around, 21 bottles of beer on the wall.",
            "",
            "21 bottles of beer on the wall, 21 bottles of beer.",
            "Take one down and pass it around, 20 bottles of beer on the wall.",
            "",
            "20 bottles of beer on the wall, 20 bottles of beer.",
            "Take one down and pass it around, 19 bottles of beer on the wall.",
            "",
            "19 bottles of beer on the wall, 19 bottles of beer.",
            "Take one down and pass it around, 18 bottles of beer on the wall.",
            "",
            "18 bottles of beer on the wall, 18 bottles of beer.",
            "Take one down and pass it around, 17 bottles of beer on the wall.",
            "",
            "17 bottles of beer on the wall, 17 bottles of beer.",
            "Take one down and pass it around, 16 bottles of beer on the wall.",
            "",
            "16 bottles of beer on the wall, 16 bottles of beer.",
            "Take one down and pass it around, 15 bottles of beer on the wall.",
            "",
            "15 bottles of beer on the wall, 15 bottles of beer.",
            "Take one down and pass it around, 14 bottles of beer on the wall.",
            "",
            "14 bottles of beer on the wall, 14 bottles of beer.",
            "Take one down and pass it around, 13 bottles of beer on the wall.",
            "",
            "13 bottles of beer on the wall, 13 bottles of beer.",
            "Take one down and pass it around, 12 bottles of beer on the wall.",
            "",
            "12 bottles of beer on the wall, 12 bottles of beer.",
            "Take one down and pass it around, 11 bottles of beer on the wall.",
            "",
            "11 bottles of beer on the wall, 11 bottles of beer.",
            "Take one down and pass it around, 10 bottles of beer on the wall.",
            "",
            "10 bottles of beer on the wall, 10 bottles of beer.",
            "Take one down and pass it around, 9 bottles of beer on the wall.",
            "",
            "9 bottles of beer on the wall, 9 bottles of beer.",
            "Take one down and pass it around, 8 bottles of beer on the wall.",
            "",
            "8 bottles of beer on the wall, 8 bottles of beer.",
            "Take one down and pass it around, 7 bottles of beer on the wall.",
            "",
            "7 bottles of beer on the wall, 7 bottles of beer.",
            "Take one down and pass it around, 6 bottles of beer on the wall.",
            "",
            "6 bottles of beer on the wall, 6 bottles of beer.",
            "Take one down and pass it around, 5 bottles of beer on the wall.",
            "",
            "5 bottles of beer on the wall, 5 bottles of beer.",
            "Take one down and pass it around, 4 bottles of beer on the wall.",
            "",
            "4 bottles of beer on the wall, 4 bottles of beer.",
            "Take one down and pass it around, 3 bottles of beer on the wall.",
            "",
            "3 bottles of beer on the wall, 3 bottles of beer.",
            "Take one down and pass it around, 2 bottles of beer on the wall.",
            "",
            "2 bottles of beer on the wall, 2 bottles of beer.",
            "Take one down and pass it around, 1 bottle of beer on the wall.",
            "",
            "1 bottle of beer on the wall, 1 bottle of beer.",
            "Take it down and pass it around, no more bottles of beer on the wall.",
            "",
            "No more bottles of beer on the wall, no more bottles of beer.",
            "Go to the store and buy some more, 99 bottles of beer on the wall.",
        ]
>       self.assertEqual(recite(start=99, take=100), expected)
E       AssertionError: '99 bottles of beer on the wall, 99 bottl[12137 chars]all.' != ['99 bottles of beer on the wall, 99 bott[12735 chars]ll.']

beer_song_test.py:373: AssertionError
____________________ BeerSongTest.test_first_generic_verse _____________________

self = <beer_song_test.BeerSongTest testMethod=test_first_generic_verse>

    def test_first_generic_verse(self):
        expected = [
            "99 bottles of beer on the wall, 99 bottles of beer.",
            "Take one down and pass it around, 98 bottles of beer on the wall.",
        ]
>       self.assertEqual(recite(start=99), expected)
E       AssertionError: '99 bottles of beer on the wall, 99 bottl[74 chars]all.' != ['99 bottles of beer on the wall, 99 bott[78 chars]ll.']

beer_song_test.py:18: AssertionError
______________________ BeerSongTest.test_first_two_verses ______________________

self = <beer_song_test.BeerSongTest testMethod=test_first_two_verses>

    def test_first_two_verses(self):
        expected = [
            "99 bottles of beer on the wall, 99 bottles of beer.",
            "Take one down and pass it around, 98 bottles of beer on the wall.",
            "",
            "98 bottles of beer on the wall, 98 bottles of beer.",
            "Take one down and pass it around, 97 bottles of beer on the wall.",
        ]
>       self.assertEqual(recite(start=99, take=2), expected)
E       AssertionError: '99 bottles of beer on the wall, 99 bottl[196 chars]all.' != ['99 bottles of beer on the wall, 99 bott[206 chars]ll.']

beer_song_test.py:56: AssertionError
_____________________ BeerSongTest.test_last_generic_verse _____________________

self = <beer_song_test.BeerSongTest testMethod=test_last_generic_verse>

    def test_last_generic_verse(self):
        expected = [
            "3 bottles of beer on the wall, 3 bottles of beer.",
            "Take one down and pass it around, 2 bottles of beer on the wall.",
        ]
>       self.assertEqual(recite(start=3), expected)
E       AssertionError: '3 bottles of beer on the wall, 3 bottles[71 chars]all.' != ['3 bottles of beer on the wall, 3 bottle[75 chars]ll.']

beer_song_test.py:25: AssertionError
_____________________ BeerSongTest.test_last_three_verses ______________________

self = <beer_song_test.BeerSongTest testMethod=test_last_three_verses>

    def test_last_three_verses(self):
        expected = [
            "2 bottles of beer on the wall, 2 bottles of beer.",
            "Take one down and pass it around, 1 bottle of beer on the wall.",
            "",
            "1 bottle of beer on the wall, 1 bottle of beer.",
            "Take it down and pass it around, no more bottles of beer on the wall.",
            "",
            "No more bottles of beer on the wall, no more bottles of beer.",
            "Go to the store and buy some more, 99 bottles of beer on the wall.",
        ]
>       self.assertEqual(recite(start=2, take=3), expected)
E       AssertionError: '2 bottles of beer on the wall, 2 bottles[325 chars]all.' != ['2 bottles of beer on the wall, 2 bottle[341 chars]ll.']

beer_song_test.py:69: AssertionError
____________________ BeerSongTest.test_verse_with_0_bottles ____________________

self = <beer_song_test.BeerSongTest testMethod=test_verse_with_0_bottles>

    def test_verse_with_0_bottles(self):
        expected = [
            "No more bottles of beer on the wall, no more bottles of beer.",
            "Go to the store and buy some more, 99 bottles of beer on the wall.",
        ]
>       self.assertEqual(recite(start=0), expected)
E       AssertionError: 'No more bottles of beer on the wall, no [85 chars]all.' != ['No more bottles of beer on the wall, no[89 chars]ll.']

beer_song_test.py:46: AssertionError
____________________ BeerSongTest.test_verse_with_1_bottle _____________________

self = <beer_song_test.BeerSongTest testMethod=test_verse_with_1_bottle>

    def test_verse_with_1_bottle(self):
        expected = [
            "1 bottle of beer on the wall, 1 bottle of beer.",
            "Take it down and pass it around, no more bottles of beer on the wall.",
        ]
>       self.assertEqual(recite(start=1), expected)
E       AssertionError: '1 bottle of beer on the wall, 1 bottle o[74 chars]all.' != ['1 bottle of beer on the wall, 1 bottle [78 chars]ll.']

beer_song_test.py:39: AssertionError
____________________ BeerSongTest.test_verse_with_2_bottles ____________________

self = <beer_song_test.BeerSongTest testMethod=test_verse_with_2_bottles>

    def test_verse_with_2_bottles(self):
        expected = [
            "2 bottles of beer on the wall, 2 bottles of beer.",
            "Take one down and pass it around, 1 bottle of beer on the wall.",
        ]
>       self.assertEqual(recite(start=2), expected)
E       AssertionError: '2 bottles of beer on the wall, 2 bottles[70 chars]all.' != ['2 bottles of beer on the wall, 2 bottle[74 chars]ll.']

beer_song_test.py:32: AssertionError
=========================== short test summary info ============================
FAILED beer_song_test.py::BeerSongTest::test_all_verses - AssertionError: '99...
FAILED beer_song_test.py::BeerSongTest::test_first_generic_verse - AssertionE...
FAILED beer_song_test.py::BeerSongTest::test_first_two_verses - AssertionErro...
FAILED beer_song_test.py::BeerSongTest::test_last_generic_verse - AssertionEr...
FAILED beer_song_test.py::BeerSongTest::test_last_three_verses - AssertionErr...
FAILED beer_song_test.py::BeerSongTest::test_verse_with_0_bottles - Assertion...
FAILED beer_song_test.py::BeerSongTest::test_verse_with_1_bottle - AssertionE...
FAILED beer_song_test.py::BeerSongTest::test_verse_with_2_bottles - Assertion...
============================== 8 failed in 0.20s ===============================
