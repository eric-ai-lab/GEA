+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
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
========================= 2 failed, 22 passed in 0.08s =========================
