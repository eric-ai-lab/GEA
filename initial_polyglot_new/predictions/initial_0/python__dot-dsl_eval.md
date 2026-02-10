+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: asyncio-1.3.0, anyio-4.12.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 12 items

dot_dsl_test.py ............                                             [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED dot_dsl_test.py::DotDslTest::test_empty_graph
PASSED dot_dsl_test.py::DotDslTest::test_graph_with_attributes
PASSED dot_dsl_test.py::DotDslTest::test_graph_with_one_attribute
PASSED dot_dsl_test.py::DotDslTest::test_graph_with_one_edge
PASSED dot_dsl_test.py::DotDslTest::test_graph_with_one_node
PASSED dot_dsl_test.py::DotDslTest::test_graph_with_one_node_with_keywords
PASSED dot_dsl_test.py::DotDslTest::test_malformed_EDGE
PASSED dot_dsl_test.py::DotDslTest::test_malformed_attr
PASSED dot_dsl_test.py::DotDslTest::test_malformed_graph
PASSED dot_dsl_test.py::DotDslTest::test_malformed_graph_item
PASSED dot_dsl_test.py::DotDslTest::test_malformed_node
PASSED dot_dsl_test.py::DotDslTest::test_unknown_item
============================== 12 passed in 0.02s ==============================
