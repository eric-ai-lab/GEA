+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 20 items

book_store_test.py F.FFFFFFFFFFFFFFFFFF                                  [100%]

=================================== FAILURES ===================================
_ BookStoreTest.test_check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five _

self = <book_store_test.BookStoreTest testMethod=test_check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five>

    def test_check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five(
        self,
    ):
        basket = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5]
>       self.assertEqual(total(basket), 14560)
E       AssertionError: 145.6 != 14560

book_store_test.py:79: AssertionError
___________________ BookStoreTest.test_five_different_books ____________________

self = <book_store_test.BookStoreTest testMethod=test_five_different_books>

    def test_five_different_books(self):
        basket = [1, 2, 3, 4, 5]
>       self.assertEqual(total(basket), 3000)
E       AssertionError: 30.0 != 3000

book_store_test.py:39: AssertionError
___________________ BookStoreTest.test_four_different_books ____________________

self = <book_store_test.BookStoreTest testMethod=test_four_different_books>

    def test_four_different_books(self):
        basket = [1, 2, 3, 4]
>       self.assertEqual(total(basket), 2560)
E       AssertionError: 25.6 != 2560

book_store_test.py:35: AssertionError
_ BookStoreTest.test_four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three _

self = <book_store_test.BookStoreTest testMethod=test_four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three>

    def test_four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three(
        self,
    ):
        basket = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]
>       self.assertEqual(total(basket), 10240)
E       AssertionError: 102.4 != 10240

book_store_test.py:73: AssertionError
_ BookStoreTest.test_group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three _

self = <book_store_test.BookStoreTest testMethod=test_group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three>

    def test_group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three(self):
        basket = [1, 1, 2, 2, 3, 4]
>       self.assertEqual(total(basket), 4080)
E       AssertionError: 40.8 != 4080

book_store_test.py:51: AssertionError
_ BookStoreTest.test_one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three _

self = <book_store_test.BookStoreTest testMethod=test_one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three>

    def test_one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three(self):
        basket = [1, 1, 2, 3, 4]
>       self.assertEqual(total(basket), 3360)
E       AssertionError: 33.6 != 3360

book_store_test.py:83: AssertionError
_ BookStoreTest.test_one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size _

self = <book_store_test.BookStoreTest testMethod=test_one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size>

    def test_one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size(
        self,
    ):
        basket = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
>       self.assertEqual(total(basket), 10000)
E       AssertionError: 100.0 != 10000

book_store_test.py:89: AssertionError
____________________ BookStoreTest.test_only_a_single_book _____________________

self = <book_store_test.BookStoreTest testMethod=test_only_a_single_book>

    def test_only_a_single_book(self):
        basket = [1]
>       self.assertEqual(total(basket), 800)
E       AssertionError: 8 != 800

book_store_test.py:15: AssertionError
____________________ BookStoreTest.test_shuffled_book_order ____________________

self = <book_store_test.BookStoreTest testMethod=test_shuffled_book_order>

    def test_shuffled_book_order(self):
        basket = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
>       self.assertEqual(total(basket), 8120)
E       AssertionError: 81.2 != 8120

book_store_test.py:99: AssertionError
___ BookStoreTest.test_three_copies_of_first_book_and_two_each_of_remaining ____

self = <book_store_test.BookStoreTest testMethod=test_three_copies_of_first_book_and_two_each_of_remaining>

    def test_three_copies_of_first_book_and_two_each_of_remaining(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
>       self.assertEqual(total(basket), 6800)
E       AssertionError: 68.0 != 6800

book_store_test.py:63: AssertionError
___________________ BookStoreTest.test_three_different_books ___________________

self = <book_store_test.BookStoreTest testMethod=test_three_different_books>

    def test_three_different_books(self):
        basket = [1, 2, 3]
>       self.assertEqual(total(basket), 2160)
E       AssertionError: 21.6 != 2160

book_store_test.py:31: AssertionError
_ BookStoreTest.test_three_each_of_first_two_books_and_two_each_of_remaining_books _

self = <book_store_test.BookStoreTest testMethod=test_three_each_of_first_two_books_and_two_each_of_remaining_books>

    def test_three_each_of_first_two_books_and_two_each_of_remaining_books(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2]
>       self.assertEqual(total(basket), 7520)
E       AssertionError: 75.2 != 7520

book_store_test.py:67: AssertionError
__________________ BookStoreTest.test_two_copies_of_each_book __________________

self = <book_store_test.BookStoreTest testMethod=test_two_copies_of_each_book>

    def test_two_copies_of_each_book(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
>       self.assertEqual(total(basket), 6000)
E       AssertionError: 60.0 != 6000

book_store_test.py:59: AssertionError
____________________ BookStoreTest.test_two_different_books ____________________

self = <book_store_test.BookStoreTest testMethod=test_two_different_books>

    def test_two_different_books(self):
        basket = [1, 2]
>       self.assertEqual(total(basket), 1520)
E       AssertionError: 15.2 != 1520

book_store_test.py:27: AssertionError
__ BookStoreTest.test_two_each_of_first_four_books_and_one_copy_each_of_rest ___

self = <book_store_test.BookStoreTest testMethod=test_two_each_of_first_four_books_and_one_copy_each_of_rest>

    def test_two_each_of_first_four_books_and_one_copy_each_of_rest(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5]
>       self.assertEqual(total(basket), 5560)
E       AssertionError: 55.6 != 5560

book_store_test.py:55: AssertionError
__________ BookStoreTest.test_two_groups_of_four_and_a_group_of_five ___________

self = <book_store_test.BookStoreTest testMethod=test_two_groups_of_four_and_a_group_of_five>

    def test_two_groups_of_four_and_a_group_of_five(self):
        basket = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]
>       self.assertEqual(total(basket), 8120)
E       AssertionError: 81.2 != 8120

book_store_test.py:95: AssertionError
_ BookStoreTest.test_two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three _

self = <book_store_test.BookStoreTest testMethod=test_two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three>

    def test_two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 5]
>       self.assertEqual(total(basket), 5120)
E       AssertionError: 51.2 != 5120

book_store_test.py:43: AssertionError
_ BookStoreTest.test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three _

self = <book_store_test.BookStoreTest testMethod=test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three>

    def test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three(self):
        basket = [1, 1, 2, 3, 4, 4, 5, 5]
>       self.assertEqual(total(basket), 5120)
E       AssertionError: 51.2 != 5120

book_store_test.py:47: AssertionError
___________________ BookStoreTest.test_two_of_the_same_book ____________________

self = <book_store_test.BookStoreTest testMethod=test_two_of_the_same_book>

    def test_two_of_the_same_book(self):
        basket = [2, 2]
>       self.assertEqual(total(basket), 1600)
E       AssertionError: 16 != 1600

book_store_test.py:19: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED book_store_test.py::BookStoreTest::test_empty_basket
FAILED book_store_test.py::BookStoreTest::test_check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five
FAILED book_store_test.py::BookStoreTest::test_five_different_books - Asserti...
FAILED book_store_test.py::BookStoreTest::test_four_different_books - Asserti...
FAILED book_store_test.py::BookStoreTest::test_four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three
FAILED book_store_test.py::BookStoreTest::test_group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three
FAILED book_store_test.py::BookStoreTest::test_one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three
FAILED book_store_test.py::BookStoreTest::test_one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size
FAILED book_store_test.py::BookStoreTest::test_only_a_single_book - Assertion...
FAILED book_store_test.py::BookStoreTest::test_shuffled_book_order - Assertio...
FAILED book_store_test.py::BookStoreTest::test_three_copies_of_first_book_and_two_each_of_remaining
FAILED book_store_test.py::BookStoreTest::test_three_different_books - Assert...
FAILED book_store_test.py::BookStoreTest::test_three_each_of_first_two_books_and_two_each_of_remaining_books
FAILED book_store_test.py::BookStoreTest::test_two_copies_of_each_book - Asse...
FAILED book_store_test.py::BookStoreTest::test_two_different_books - Assertio...
FAILED book_store_test.py::BookStoreTest::test_two_each_of_first_four_books_and_one_copy_each_of_rest
FAILED book_store_test.py::BookStoreTest::test_two_groups_of_four_and_a_group_of_five
FAILED book_store_test.py::BookStoreTest::test_two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three
FAILED book_store_test.py::BookStoreTest::test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three
FAILED book_store_test.py::BookStoreTest::test_two_of_the_same_book - Asserti...
========================= 19 failed, 1 passed in 0.71s =========================
