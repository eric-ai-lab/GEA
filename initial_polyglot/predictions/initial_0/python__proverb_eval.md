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

proverb_test.py FFFFFFFF                                                 [100%]

=================================== FAILURES ===================================
_____________ ProverbTest.test_an_optional_qualifier_can_be_added ______________

self = <proverb_test.ProverbTest testMethod=test_an_optional_qualifier_can_be_added>

    def test_an_optional_qualifier_can_be_added(self):
        input_data = ["nail"]
>       self.assertEqual(
            proverb(*input_data, qualifier="horseshoe"),
            ["And all for the want of a horseshoe nail."],
        )
E       AssertionError: 'For want of a n the a was lost.\nFor wan[93 chars]e n.' != ['And all for the want of a horseshoe nail.']

proverb_test.py:79: AssertionError
_______ ProverbTest.test_an_optional_qualifier_in_the_final_consequences _______

self = <proverb_test.ProverbTest testMethod=test_an_optional_qualifier_in_the_final_consequences>

    def test_an_optional_qualifier_in_the_final_consequences(self):
        input_data = ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
        self.assertEqual(
>           proverb(*input_data, qualifier="horseshoe"),
            [
                "For want of a nail the shoe was lost.",
                "For want of a shoe the horse was lost.",
                "For want of a horse the rider was lost.",
                "For want of a rider the message was lost.",
                "For want of a message the battle was lost.",
                "For want of a battle the kingdom was lost.",
                "And all for the want of a horseshoe nail.",
            ],
        )
E       TypeError: proverb() got multiple values for argument 'qualifier'

proverb_test.py:87: TypeError
___________________ ProverbTest.test_four_pieces_modernized ____________________

self = <proverb_test.ProverbTest testMethod=test_four_pieces_modernized>

    def test_four_pieces_modernized(self):
        input_data = ["pin", "gun", "soldier", "battle"]
        self.assertEqual(
>           proverb(*input_data, qualifier=None),
            [
                "For want of a pin the gun was lost.",
                "For want of a gun the soldier was lost.",
                "For want of a soldier the battle was lost.",
                "And all for the want of a pin.",
            ],
        )
E       TypeError: proverb() got multiple values for argument 'qualifier'

proverb_test.py:66: TypeError
________________________ ProverbTest.test_full_proverb _________________________

self = <proverb_test.ProverbTest testMethod=test_full_proverb>

    def test_full_proverb(self):
        input_data = ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
        self.assertEqual(
>           proverb(*input_data, qualifier=None),
            [
                "For want of a nail the shoe was lost.",
                "For want of a shoe the horse was lost.",
                "For want of a horse the rider was lost.",
                "For want of a rider the message was lost.",
                "For want of a message the battle was lost.",
                "For want of a battle the kingdom was lost.",
                "And all for the want of a nail.",
            ],
        )
E       TypeError: proverb() got multiple values for argument 'qualifier'

proverb_test.py:51: TypeError
__________________________ ProverbTest.test_one_piece __________________________

self = <proverb_test.ProverbTest testMethod=test_one_piece>

    def test_one_piece(self):
        input_data = ["nail"]
>       self.assertEqual(
            proverb(*input_data, qualifier=None), ["And all for the want of a nail."]
        )
E       AssertionError: 'For want of a n the a was lost.\nFor wan[83 chars]a n.' != ['And all for the want of a nail.']

proverb_test.py:23: AssertionError
________________________ ProverbTest.test_three_pieces _________________________

self = <proverb_test.ProverbTest testMethod=test_three_pieces>

    def test_three_pieces(self):
        input_data = ["nail", "shoe", "horse"]
        self.assertEqual(
>           proverb(*input_data, qualifier=None),
            [
                "For want of a nail the shoe was lost.",
                "For want of a shoe the horse was lost.",
                "And all for the want of a nail.",
            ],
        )
E       TypeError: proverb() got multiple values for argument 'qualifier'

proverb_test.py:40: TypeError
_________________________ ProverbTest.test_two_pieces __________________________

self = <proverb_test.ProverbTest testMethod=test_two_pieces>

    def test_two_pieces(self):
        input_data = ["nail", "shoe"]
        self.assertEqual(
>           proverb(*input_data, qualifier=None),
            [
                "For want of a nail the shoe was lost.",
                "And all for the want of a nail.",
            ],
        )
E       TypeError: proverb() got multiple values for argument 'qualifier'

proverb_test.py:30: TypeError
_________________________ ProverbTest.test_zero_pieces _________________________

self = <proverb_test.ProverbTest testMethod=test_zero_pieces>

    def test_zero_pieces(self):
        input_data = []
>       self.assertEqual(proverb(*input_data, qualifier=None), [])
E       TypeError: proverb() missing 1 required positional argument: 'seq'

proverb_test.py:19: TypeError
=========================== short test summary info ============================
FAILED proverb_test.py::ProverbTest::test_an_optional_qualifier_can_be_added
FAILED proverb_test.py::ProverbTest::test_an_optional_qualifier_in_the_final_consequences
FAILED proverb_test.py::ProverbTest::test_four_pieces_modernized - TypeError:...
FAILED proverb_test.py::ProverbTest::test_full_proverb - TypeError: proverb()...
FAILED proverb_test.py::ProverbTest::test_one_piece - AssertionError: 'For wa...
FAILED proverb_test.py::ProverbTest::test_three_pieces - TypeError: proverb()...
FAILED proverb_test.py::ProverbTest::test_two_pieces - TypeError: proverb() g...
FAILED proverb_test.py::ProverbTest::test_zero_pieces - TypeError: proverb() ...
============================== 8 failed in 0.12s ===============================
