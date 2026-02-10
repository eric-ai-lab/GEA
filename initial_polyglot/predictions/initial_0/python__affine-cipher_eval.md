+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 16 items

affine_cipher_test.py ....F.........F.                                   [100%]

=================================== FAILURES ===================================
_____________ AffineCipherTest.test_decode_with_a_not_coprime_to_m _____________

self = <affine_cipher_test.AffineCipherTest testMethod=test_decode_with_a_not_coprime_to_m>

    def test_decode_with_a_not_coprime_to_m(self):
        with self.assertRaises(ValueError) as err:
            decode("Test", 13, 5)
        self.assertEqual(type(err.exception), ValueError)
>       self.assertEqual(err.exception.args[0], "a and m must be coprime.")
E       AssertionError: '13 and 26 are not coprime. Decryption cannot proceed.' != 'a and m must be coprime.'
E       - 13 and 26 are not coprime. Decryption cannot proceed.
E       + a and m must be coprime.

affine_cipher_test.py:82: AssertionError
_____________ AffineCipherTest.test_encode_with_a_not_coprime_to_m _____________

self = <affine_cipher_test.AffineCipherTest testMethod=test_encode_with_a_not_coprime_to_m>

    def test_encode_with_a_not_coprime_to_m(self):
        with self.assertRaises(ValueError) as err:
            encode("This is a test.", 6, 17)
        self.assertEqual(type(err.exception), ValueError)
>       self.assertEqual(err.exception.args[0], "a and m must be coprime.")
E       AssertionError: '6 and 26 are not coprime. Encryption cannot proceed.' != 'a and m must be coprime.'
E       - 6 and 26 are not coprime. Encryption cannot proceed.
E       + a and m must be coprime.

affine_cipher_test.py:47: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED affine_cipher_test.py::AffineCipherTest::test_decode_a_sentence
PASSED affine_cipher_test.py::AffineCipherTest::test_decode_all_the_letters
PASSED affine_cipher_test.py::AffineCipherTest::test_decode_exercism
PASSED affine_cipher_test.py::AffineCipherTest::test_decode_numbers
PASSED affine_cipher_test.py::AffineCipherTest::test_decode_with_no_spaces_in_input
PASSED affine_cipher_test.py::AffineCipherTest::test_decode_with_too_many_spaces
PASSED affine_cipher_test.py::AffineCipherTest::test_encode_all_the_letters
PASSED affine_cipher_test.py::AffineCipherTest::test_encode_deep_thought
PASSED affine_cipher_test.py::AffineCipherTest::test_encode_mindblowingly
PASSED affine_cipher_test.py::AffineCipherTest::test_encode_no
PASSED affine_cipher_test.py::AffineCipherTest::test_encode_numbers
PASSED affine_cipher_test.py::AffineCipherTest::test_encode_o_m_g
PASSED affine_cipher_test.py::AffineCipherTest::test_encode_omg
PASSED affine_cipher_test.py::AffineCipherTest::test_encode_yes
FAILED affine_cipher_test.py::AffineCipherTest::test_decode_with_a_not_coprime_to_m
FAILED affine_cipher_test.py::AffineCipherTest::test_encode_with_a_not_coprime_to_m
========================= 2 failed, 14 passed in 0.99s =========================
