+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 15 items

pov_test.py ...............                                              [100%]

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
PASSED pov_test.py::PovTest::test_errors_if_destination_does_not_exist
PASSED pov_test.py::PovTest::test_errors_if_source_does_not_exist
PASSED pov_test.py::PovTest::test_errors_if_target_does_not_exist_in_a_large_tree
PASSED pov_test.py::PovTest::test_errors_if_target_does_not_exist_in_a_singleton_tree
PASSED pov_test.py::PovTest::test_moves_children_of_the_new_root_to_same_level_as_former_parent
PASSED pov_test.py::PovTest::test_results_in_the_same_tree_if_the_input_tree_is_a_singleton
============================== 15 passed in 0.02s ==============================
