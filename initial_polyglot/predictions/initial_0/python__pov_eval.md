+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 15 items

pov_test.py .........FFFF..                                              [100%]

=================================== FAILURES ===================================
______________ PovTest.test_errors_if_destination_does_not_exist _______________

self = <pov_test.PovTest testMethod=test_errors_if_destination_does_not_exist>

    def test_errors_if_destination_does_not_exist(self):
        tree = Tree(
            "parent",
            [
                Tree("x", [Tree("kid-0"), Tree("kid-1")]),
                Tree("sibling-0"),
                Tree("sibling-1"),
            ],
        )
        with self.assertRaises(ValueError) as err:
            tree.path_to("x", "nonexistent")
        self.assertEqual(type(err.exception), ValueError)
    
>       self.assertEqual(err.exception.args[0], "No path found")
E       AssertionError: 'Path from x to nonexistent does not exist.' != 'No path found'
E       - Path from x to nonexistent does not exist.
E       + No path found

pov_test.py:154: AssertionError
_________________ PovTest.test_errors_if_source_does_not_exist _________________

self = <pov_test.PovTest testMethod=test_errors_if_source_does_not_exist>

    def test_errors_if_source_does_not_exist(self):
        tree = Tree(
            "parent",
            [
                Tree("x", [Tree("kid-0"), Tree("kid-1")]),
                Tree("sibling-0"),
                Tree("sibling-1"),
            ],
        )
        with self.assertRaises(ValueError) as err:
            tree.path_to("nonexistent", "x")
        self.assertEqual(type(err.exception), ValueError)
    
>       self.assertEqual(err.exception.args[0], "Tree could not be reoriented")
E       AssertionError: 'Tree does not contain node: nonexistent' != 'Tree could not be reoriented'
E       - Tree does not contain node: nonexistent
E       + Tree could not be reoriented

pov_test.py:169: AssertionError
_________ PovTest.test_errors_if_target_does_not_exist_in_a_large_tree _________

self = <pov_test.PovTest testMethod=test_errors_if_target_does_not_exist_in_a_large_tree>

    def test_errors_if_target_does_not_exist_in_a_large_tree(self):
        tree = Tree(
            "parent",
            [
                Tree("x", [Tree("kid-0"), Tree("kid-1")]),
                Tree("sibling-0"),
                Tree("sibling-1"),
            ],
        )
        with self.assertRaises(ValueError) as err:
            tree.from_pov("nonexistent")
        self.assertEqual(type(err.exception), ValueError)
>       self.assertEqual(err.exception.args[0], "Tree could not be reoriented")
E       AssertionError: 'Tree does not contain node: nonexistent' != 'Tree could not be reoriented'
E       - Tree does not contain node: nonexistent
E       + Tree could not be reoriented

pov_test.py:98: AssertionError
_______ PovTest.test_errors_if_target_does_not_exist_in_a_singleton_tree _______

self = <pov_test.PovTest testMethod=test_errors_if_target_does_not_exist_in_a_singleton_tree>

    def test_errors_if_target_does_not_exist_in_a_singleton_tree(self):
        tree = Tree("x")
        with self.assertRaises(ValueError) as err:
            tree.from_pov("nonexistent")
        self.assertEqual(type(err.exception), ValueError)
>       self.assertEqual(err.exception.args[0], "Tree could not be reoriented")
E       AssertionError: 'Tree does not contain node: nonexistent' != 'Tree could not be reoriented'
E       - Tree does not contain node: nonexistent
E       + Tree could not be reoriented

pov_test.py:84: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED pov_test.py::PovTest::test_can_find_path_from_nodes_other_than_x
PASSED pov_test.py::PovTest::test_can_find_path_not_involving_root
PASSED pov_test.py::PovTest::test_can_find_path_to_cousin
PASSED pov_test.py::PovTest::test_can_find_path_to_parent
PASSED pov_test.py::PovTest::test_can_find_path_to_sibling
PASSED pov_test.py::PovTest::test_can_reroot_a_complex_tree_with_cousins
PASSED pov_test.py::PovTest::test_can_reroot_a_tree_with_a_parent_and_many_siblings
PASSED pov_test.py::PovTest::test_can_reroot_a_tree_with_a_parent_and_one_sibling
PASSED pov_test.py::PovTest::test_can_reroot_a_tree_with_new_root_deeply_nested_in_tree
PASSED pov_test.py::PovTest::test_moves_children_of_the_new_root_to_same_level_as_former_parent
PASSED pov_test.py::PovTest::test_results_in_the_same_tree_if_the_input_tree_is_a_singleton
FAILED pov_test.py::PovTest::test_errors_if_destination_does_not_exist - Asse...
FAILED pov_test.py::PovTest::test_errors_if_source_does_not_exist - Assertion...
FAILED pov_test.py::PovTest::test_errors_if_target_does_not_exist_in_a_large_tree
FAILED pov_test.py::PovTest::test_errors_if_target_does_not_exist_in_a_singleton_tree
========================= 4 failed, 11 passed in 0.45s =========================
