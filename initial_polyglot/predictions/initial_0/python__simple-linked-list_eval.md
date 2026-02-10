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

simple_linked_list_test.py F.....FF.F.FFF...F.F                          [100%]

=================================== FAILURES ===================================
____________ SimpleLinkedListTest.test_can_pop_from_non_empty_list _____________

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_can_pop_from_non_empty_list>

    def test_can_pop_from_non_empty_list(self):
        sut = LinkedList([3, 4, 5])
>       self.assertEqual(sut.pop(), 5)
E       AssertionError: 3 != 5

simple_linked_list_test.py:49: AssertionError
_ SimpleLinkedListTest.test_non_empty_linked_list_to_list_is_list_with_all_elements _

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_non_empty_linked_list_to_list_is_list_with_all_elements>

    def test_non_empty_linked_list_to_list_is_list_with_all_elements(self):
        sut = LinkedList([1, 2, 3])
>       self.assertEqual(list(sut), [3, 2, 1])
E       AssertionError: Lists differ: [1, 2, 3] != [3, 2, 1]
E       
E       First differing element 0:
E       1
E       3
E       
E       - [1, 2, 3]
E       ?  ^     ^
E       
E       + [3, 2, 1]
E       ?  ^     ^

simple_linked_list_test.py:102: AssertionError
__________ SimpleLinkedListTest.test_non_empty_list_has_correct_head ___________

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_non_empty_list_has_correct_head>

    def test_non_empty_list_has_correct_head(self):
        sut = LinkedList([1, 2])
>       self.assertEqual(sut.head().value(), 2)
E       AttributeError: 'int' object has no attribute 'value'

simple_linked_list_test.py:34: AttributeError
______________ SimpleLinkedListTest.test_non_empty_list_traverse _______________

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_non_empty_list_traverse>

    def test_non_empty_list_traverse(self):
        sut = LinkedList(range(10))
        current = sut.head()
        for i in range(10):
>           self.assertEqual(current.value(), 9 - i)
E           AttributeError: 'int' object has no attribute 'value'

simple_linked_list_test.py:88: AttributeError
____________________ SimpleLinkedListTest.test_push_and_pop ____________________

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_push_and_pop>

    def test_push_and_pop(self):
        sut = LinkedList([1, 2])
        sut.push(3)
        self.assertEqual(len(sut), 3)
        self.assertEqual(sut.pop(), 3)
>       self.assertEqual(sut.pop(), 2)
E       AssertionError: 1 != 2

simple_linked_list_test.py:73: AssertionError
_________ SimpleLinkedListTest.test_pushing_to_empty_list_changes_head _________

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_pushing_to_empty_list_changes_head>

    def test_pushing_to_empty_list_changes_head(self):
        sut = LinkedList()
        sut.push(5)
        self.assertEqual(len(sut), 1)
>       self.assertEqual(sut.head().value(), 5)
E       AttributeError: 'int' object has no attribute 'value'

simple_linked_list_test.py:45: AttributeError
_______________ SimpleLinkedListTest.test_reverse_non_empty_list _______________

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_reverse_non_empty_list>

    def test_reverse_non_empty_list(self):
        sut = LinkedList([1, 2, 3])
>       self.assertEqual(list(sut.reversed()), [1, 2, 3])
E       AssertionError: Lists differ: [3, 2, 1] != [1, 2, 3]
E       
E       First differing element 0:
E       3
E       1
E       
E       - [3, 2, 1]
E       ?  ^     ^
E       
E       + [1, 2, 3]
E       ?  ^     ^

simple_linked_list_test.py:114: AssertionError
______________ SimpleLinkedListTest.test_singleton_list_has_head _______________

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_singleton_list_has_head>

    def test_singleton_list_has_head(self):
        sut = LinkedList([1])
>       self.assertEqual(sut.head().value(), 1)
E       AttributeError: 'int' object has no attribute 'value'

simple_linked_list_test.py:30: AttributeError
__________ SimpleLinkedListTest.test_singleton_list_head_has_no_next ___________

self = <simple_linked_list_test.SimpleLinkedListTest testMethod=test_singleton_list_head_has_no_next>

    def test_singleton_list_head_has_no_next(self):
        sut = LinkedList([1])
>       self.assertIsNone(sut.head().next())
E       AttributeError: 'int' object has no attribute 'next'

simple_linked_list_test.py:82: AttributeError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_can_push_to_non_empty_list
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_empty_linked_list_to_list_is_empty
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_empty_list_has_len_zero
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_error_on_empty_list_head
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_error_on_empty_list_pop
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_non_empty_list_has_correct_len
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_pop_from_singleton_list_removes_head
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_reversed_empty_list_is_empty_list
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_reversed_singleton_list_is_same_list
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_singleton_linked_list_to_list_list_with_singular_element
PASSED simple_linked_list_test.py::SimpleLinkedListTest::test_singleton_list_has_len_one
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_can_pop_from_non_empty_list
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_non_empty_linked_list_to_list_is_list_with_all_elements
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_non_empty_list_has_correct_head
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_non_empty_list_traverse
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_push_and_pop - ...
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_pushing_to_empty_list_changes_head
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_reverse_non_empty_list
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_singleton_list_has_head
FAILED simple_linked_list_test.py::SimpleLinkedListTest::test_singleton_list_head_has_no_next
========================= 9 failed, 11 passed in 1.09s =========================
