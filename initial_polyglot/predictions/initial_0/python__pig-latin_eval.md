+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 22 items

pig_latin_test.py ......................                                 [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED pig_latin_test.py::PigLatinTest::test_a_whole_phrase
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_a
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_a_vowel_and_followed_by_a_qu
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_ch
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_e
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_i
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_k
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_o
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_p
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_q_without_a_following_u
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_qu
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_qu_and_a_preceding_consonant
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_sch
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_th
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_thr
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_u
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_x
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_xr
PASSED pig_latin_test.py::PigLatinTest::test_word_beginning_with_yt
PASSED pig_latin_test.py::PigLatinTest::test_y_as_second_letter_in_two_letter_word
PASSED pig_latin_test.py::PigLatinTest::test_y_is_treated_like_a_consonant_at_the_beginning_of_a_word
PASSED pig_latin_test.py::PigLatinTest::test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster
============================== 22 passed in 0.07s ==============================
