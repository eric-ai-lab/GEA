+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items

food_chain_test.py FFFFFFFFFF                                            [100%]

=================================== FAILURES ===================================
___________________________ FoodChainTest.test_bird ____________________________

self = <food_chain_test.FoodChainTest testMethod=test_bird>

    def test_bird(self):
>       self.assertEqual(
            recite(3, 3),
            [
                "I know an old lady who swallowed a bird.",
                "How absurd to swallow a bird!",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a bird.[226 chars]die." != ['I know an old lady who swallowed a bird[236 chars]ie."]

food_chain_test.py:34: AssertionError
____________________________ FoodChainTest.test_cat ____________________________

self = <food_chain_test.FoodChainTest testMethod=test_cat>

    def test_cat(self):
>       self.assertEqual(
            recite(4, 4),
            [
                "I know an old lady who swallowed a cat.",
                "Imagine that, to swallow a cat!",
                "She swallowed the cat to catch the bird.",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a cat.\[269 chars]die." != ['I know an old lady who swallowed a cat.[281 chars]ie."]

food_chain_test.py:46: AssertionError
____________________________ FoodChainTest.test_cow ____________________________

self = <food_chain_test.FoodChainTest testMethod=test_cow>

    def test_cow(self):
>       self.assertEqual(
            recite(7, 7),
            [
                "I know an old lady who swallowed a cow.",
                "I don't know how she swallowed a cow!",
                "She swallowed the cow to catch the goat.",
                "She swallowed the goat to catch the dog.",
                "She swallowed the dog to catch the cat.",
                "She swallowed the cat to catch the bird.",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a cow.\[400 chars]die." != ['I know an old lady who swallowed a cow.[418 chars]ie."]

food_chain_test.py:88: AssertionError
____________________________ FoodChainTest.test_dog ____________________________

self = <food_chain_test.FoodChainTest testMethod=test_dog>

    def test_dog(self):
>       self.assertEqual(
            recite(5, 5),
            [
                "I know an old lady who swallowed a dog.",
                "What a hog, to swallow a dog!",
                "She swallowed the dog to catch the cat.",
                "She swallowed the cat to catch the bird.",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a dog.\[308 chars]die." != ['I know an old lady who swallowed a dog.[322 chars]ie."]

food_chain_test.py:59: AssertionError
____________________________ FoodChainTest.test_fly ____________________________

self = <food_chain_test.FoodChainTest testMethod=test_fly>

    def test_fly(self):
>       self.assertEqual(
            recite(1, 1),
            [
                "I know an old lady who swallowed a fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a fly.\[56 chars]die." != ['I know an old lady who swallowed a fly.[60 chars]ie."]

food_chain_test.py:14: AssertionError
_________________________ FoodChainTest.test_full_song _________________________

self = <food_chain_test.FoodChainTest testMethod=test_full_song>

    def test_full_song(self):
>       self.assertEqual(
            recite(1, 8),
            [
                "I know an old lady who swallowed a fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a spider.",
                "It wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a bird.",
                "How absurd to swallow a bird!",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a cat.",
                "Imagine that, to swallow a cat!",
                "She swallowed the cat to catch the bird.",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a dog.",
                "What a hog, to swallow a dog!",
                "She swallowed the dog to catch the cat.",
                "She swallowed the cat to catch the bird.",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a goat.",
                "Just opened her throat and swallowed a goat!",
                "She swallowed the goat to catch the dog.",
                "She swallowed the dog to catch the cat.",
                "She swallowed the cat to catch the bird.",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a cow.",
                "I don't know how she swallowed a cow!",
                "She swallowed the cow to catch the goat.",
                "She swallowed the goat to catch the dog.",
                "She swallowed the dog to catch the cat.",
                "She swallowed the cat to catch the bird.",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a horse.",
                "She's dead, of course!",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a fly.\[2134 chars]rse!" != ['I know an old lady who swallowed a fly.[2234 chars]se!"]

food_chain_test.py:130: AssertionError
___________________________ FoodChainTest.test_goat ____________________________

self = <food_chain_test.FoodChainTest testMethod=test_goat>

    def test_goat(self):
>       self.assertEqual(
            recite(6, 6),
            [
                "I know an old lady who swallowed a goat.",
                "Just opened her throat and swallowed a goat!",
                "She swallowed the goat to catch the dog.",
                "She swallowed the dog to catch the cat.",
                "She swallowed the cat to catch the bird.",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a goat.[366 chars]die." != ['I know an old lady who swallowed a goat[382 chars]ie."]

food_chain_test.py:73: AssertionError
___________________________ FoodChainTest.test_horse ___________________________

self = <food_chain_test.FoodChainTest testMethod=test_horse>

    def test_horse(self):
>       self.assertEqual(
            recite(8, 8),
            ["I know an old lady who swallowed a horse.", "She's dead, of course!"],
        )
E       AssertionError: "I know an old lady who swallowed a horse.\nShe's dead, of course!" != ['I know an old lady who swallowed a horse.', "She's dead, of course!"]

food_chain_test.py:104: AssertionError
______________________ FoodChainTest.test_multiple_verses ______________________

self = <food_chain_test.FoodChainTest testMethod=test_multiple_verses>

    def test_multiple_verses(self):
>       self.assertEqual(
            recite(1, 3),
            [
                "I know an old lady who swallowed a fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a spider.",
                "It wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
                "",
                "I know an old lady who swallowed a bird.",
                "How absurd to swallow a bird!",
                "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a fly.\[530 chars]die." != ['I know an old lady who swallowed a fly.[556 chars]ie."]

food_chain_test.py:110: AssertionError
__________________________ FoodChainTest.test_spider ___________________________

self = <food_chain_test.FoodChainTest testMethod=test_spider>

    def test_spider(self):
>       self.assertEqual(
            recite(2, 2),
            [
                "I know an old lady who swallowed a spider.",
                "It wriggled and jiggled and tickled inside her.",
                "She swallowed the spider to catch the fly.",
                "I don't know why she swallowed the fly. Perhaps she'll die.",
            ],
        )
E       AssertionError: "I know an old lady who swallowed a spide[152 chars]die." != ['I know an old lady who swallowed a spid[160 chars]ie."]

food_chain_test.py:23: AssertionError
=========================== short test summary info ============================
FAILED food_chain_test.py::FoodChainTest::test_bird - AssertionError: "I know...
FAILED food_chain_test.py::FoodChainTest::test_cat - AssertionError: "I know ...
FAILED food_chain_test.py::FoodChainTest::test_cow - AssertionError: "I know ...
FAILED food_chain_test.py::FoodChainTest::test_dog - AssertionError: "I know ...
FAILED food_chain_test.py::FoodChainTest::test_fly - AssertionError: "I know ...
FAILED food_chain_test.py::FoodChainTest::test_full_song - AssertionError: "I...
FAILED food_chain_test.py::FoodChainTest::test_goat - AssertionError: "I know...
FAILED food_chain_test.py::FoodChainTest::test_horse - AssertionError: "I kno...
FAILED food_chain_test.py::FoodChainTest::test_multiple_verses - AssertionErr...
FAILED food_chain_test.py::FoodChainTest::test_spider - AssertionError: "I kn...
============================== 10 failed in 0.18s ==============================
