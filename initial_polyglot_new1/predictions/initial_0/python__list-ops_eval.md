+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 24 items

list_ops_test.py ............F..F........                                [100%]

=================================== FAILURES ===================================
_ ListOpsTest.test_foldr_direction_dependent_function_applied_to_non_empty_list _

self = <list_ops_test.ListOpsTest testMethod=test_foldr_direction_dependent_function_applied_to_non_empty_list>

    def test_foldr_direction_dependent_function_applied_to_non_empty_list(self):
>       self.assertEqual(foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24), 9)
E       AssertionError: 1.0 != 9

list_ops_test.py:78: AssertionError
___________________ ListOpsTest.test_foldr_foldr_add_string ____________________

self = <list_ops_test.ListOpsTest testMethod=test_foldr_foldr_add_string>

    def test_foldr_foldr_add_string(self):
>       self.assertEqual(
            foldr(
                lambda acc, el: el + acc, ["e", "x", "e", "r", "c", "i", "s", "m"], "!"
            ),
            "exercism!",
        )
E       AssertionError: '!msicrexe' != 'exercism!'
E       - !msicrexe
E       + exercism!

list_ops_test.py:94: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED list_ops_test.py::ListOpsTest::test_append_empty_list_to_list
PASSED list_ops_test.py::ListOpsTest::test_append_empty_lists
PASSED list_ops_test.py::ListOpsTest::test_append_list_to_empty_list
PASSED list_ops_test.py::ListOpsTest::test_append_non_empty_lists
PASSED list_ops_test.py::ListOpsTest::test_concat_empty_list
PASSED list_ops_test.py::ListOpsTest::test_concat_list_of_lists
PASSED list_ops_test.py::ListOpsTest::test_concat_list_of_nested_lists
PASSED list_ops_test.py::ListOpsTest::test_filter_empty_list
PASSED list_ops_test.py::ListOpsTest::test_filter_non_empty_list
PASSED list_ops_test.py::ListOpsTest::test_foldl_direction_dependent_function_applied_to_non_empty_list
PASSED list_ops_test.py::ListOpsTest::test_foldl_direction_independent_function_applied_to_non_empty_list
PASSED list_ops_test.py::ListOpsTest::test_foldl_empty_list
PASSED list_ops_test.py::ListOpsTest::test_foldr_direction_independent_function_applied_to_non_empty_list
PASSED list_ops_test.py::ListOpsTest::test_foldr_empty_list
PASSED list_ops_test.py::ListOpsTest::test_length_empty_list
PASSED list_ops_test.py::ListOpsTest::test_length_non_empty_list
PASSED list_ops_test.py::ListOpsTest::test_map_empty_list
PASSED list_ops_test.py::ListOpsTest::test_map_non_empty_list
PASSED list_ops_test.py::ListOpsTest::test_reverse_empty_list
PASSED list_ops_test.py::ListOpsTest::test_reverse_list_of_lists_is_not_flattened
PASSED list_ops_test.py::ListOpsTest::test_reverse_non_empty_list
PASSED list_ops_test.py::ListOpsTest::test_reverse_reverse_mixed_types
FAILED list_ops_test.py::ListOpsTest::test_foldr_direction_dependent_function_applied_to_non_empty_list
FAILED list_ops_test.py::ListOpsTest::test_foldr_foldr_add_string - Assertion...
========================= 2 failed, 22 passed in 0.05s =========================
