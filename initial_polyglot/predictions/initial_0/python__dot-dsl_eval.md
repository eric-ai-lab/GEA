+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 12 items

dot_dsl_test.py FFFFFFFF.FFF                                             [100%]

=================================== FAILURES ===================================
_________________________ DotDslTest.test_empty_graph __________________________

self = <dot_dsl_test.DotDslTest testMethod=test_empty_graph>

    def test_empty_graph(self):
>       g = Graph()

dot_dsl_test.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dot_dsl.Graph object at 0x7ca10224bc10>, data = None

    def __init__(self, data=None):
        # Check for valid data input
        if data is None or not isinstance(data, list) or len(data) == 0:
>           raise TypeError("Graph data malformed")
E           TypeError: Graph data malformed

dot_dsl.py:29: TypeError
____________________ DotDslTest.test_graph_with_attributes _____________________

self = <dot_dsl_test.DotDslTest testMethod=test_graph_with_attributes>

    def test_graph_with_attributes(self):
>       g = Graph([
            (ATTR, "foo", "1"),
            (ATTR, "title", "Testing Attrs"),
            (NODE, "a", {"color": "green"}),
            (NODE, "c", {}),
            (NODE, "b", {"label": "Beta!"}),
            (EDGE, "b", "c", {}),
            (EDGE, "a", "b", {"color": "blue"}),
            (ATTR, "bar", "true")
        ])

dot_dsl_test.py:51: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dot_dsl.Graph object at 0x7ca1020e56d0>
data = [(2, 'foo', '1'), (2, 'title', 'Testing Attrs'), (0, 'a', {'color': 'green'}), (0, 'c', {}), (0, 'b', {'label': 'Beta!'}), (1, 'b', 'c', {}), ...]

    def __init__(self, data=None):
        # Check for valid data input
        if data is None or not isinstance(data, list) or len(data) == 0:
            raise TypeError("Graph data malformed")
    
        self.graph_attributes = {}
        self.nodes = []
        self.edges = []
    
        for item in data:
            # Each item must be a tuple of (graph_attributes, nodes, edges)
            if not (isinstance(item, tuple) and len(item) == 3):
                raise TypeError("Graph data malformed")
    
            g_attr, n_list, e_list = item
    
            # Validate graph attributes
            if not isinstance(g_attr, dict):
>               raise ValueError("ATTRIBUTE malformed")
E               ValueError: ATTRIBUTE malformed

dot_dsl.py:44: ValueError
___________________ DotDslTest.test_graph_with_one_attribute ___________________

self = <dot_dsl_test.DotDslTest testMethod=test_graph_with_one_attribute>

    def test_graph_with_one_attribute(self):
>       g = Graph([
            (ATTR, "foo", "1")
        ])

dot_dsl_test.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dot_dsl.Graph object at 0x7ca1020c6d90>, data = [(2, 'foo', '1')]

    def __init__(self, data=None):
        # Check for valid data input
        if data is None or not isinstance(data, list) or len(data) == 0:
            raise TypeError("Graph data malformed")
    
        self.graph_attributes = {}
        self.nodes = []
        self.edges = []
    
        for item in data:
            # Each item must be a tuple of (graph_attributes, nodes, edges)
            if not (isinstance(item, tuple) and len(item) == 3):
                raise TypeError("Graph data malformed")
    
            g_attr, n_list, e_list = item
    
            # Validate graph attributes
            if not isinstance(g_attr, dict):
>               raise ValueError("ATTRIBUTE malformed")
E               ValueError: ATTRIBUTE malformed

dot_dsl.py:44: ValueError
_____________________ DotDslTest.test_graph_with_one_edge ______________________

self = <dot_dsl_test.DotDslTest testMethod=test_graph_with_one_edge>

    def test_graph_with_one_edge(self):
>       g = Graph([
            (EDGE, "a", "b", {})
        ])

dot_dsl_test.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dot_dsl.Graph object at 0x7ca1020a8f50>, data = [(1, 'a', 'b', {})]

    def __init__(self, data=None):
        # Check for valid data input
        if data is None or not isinstance(data, list) or len(data) == 0:
            raise TypeError("Graph data malformed")
    
        self.graph_attributes = {}
        self.nodes = []
        self.edges = []
    
        for item in data:
            # Each item must be a tuple of (graph_attributes, nodes, edges)
            if not (isinstance(item, tuple) and len(item) == 3):
>               raise TypeError("Graph data malformed")
E               TypeError: Graph data malformed

dot_dsl.py:38: TypeError
_____________________ DotDslTest.test_graph_with_one_node ______________________

self = <dot_dsl_test.DotDslTest testMethod=test_graph_with_one_node>

    def test_graph_with_one_node(self):
>       g = Graph([
            (NODE, "a", {})
        ])

dot_dsl_test.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dot_dsl.Graph object at 0x7ca1021f06d0>, data = [(0, 'a', {})]

    def __init__(self, data=None):
        # Check for valid data input
        if data is None or not isinstance(data, list) or len(data) == 0:
            raise TypeError("Graph data malformed")
    
        self.graph_attributes = {}
        self.nodes = []
        self.edges = []
    
        for item in data:
            # Each item must be a tuple of (graph_attributes, nodes, edges)
            if not (isinstance(item, tuple) and len(item) == 3):
                raise TypeError("Graph data malformed")
    
            g_attr, n_list, e_list = item
    
            # Validate graph attributes
            if not isinstance(g_attr, dict):
>               raise ValueError("ATTRIBUTE malformed")
E               ValueError: ATTRIBUTE malformed

dot_dsl.py:44: ValueError
______________ DotDslTest.test_graph_with_one_node_with_keywords _______________

self = <dot_dsl_test.DotDslTest testMethod=test_graph_with_one_node_with_keywords>

    def test_graph_with_one_node_with_keywords(self):
>       g = Graph([
            (NODE, "a", {"color": "green"})
        ])

dot_dsl_test.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <dot_dsl.Graph object at 0x7ca1020f2350>
data = [(0, 'a', {'color': 'green'})]

    def __init__(self, data=None):
        # Check for valid data input
        if data is None or not isinstance(data, list) or len(data) == 0:
            raise TypeError("Graph data malformed")
    
        self.graph_attributes = {}
        self.nodes = []
        self.edges = []
    
        for item in data:
            # Each item must be a tuple of (graph_attributes, nodes, edges)
            if not (isinstance(item, tuple) and len(item) == 3):
                raise TypeError("Graph data malformed")
    
            g_attr, n_list, e_list = item
    
            # Validate graph attributes
            if not isinstance(g_attr, dict):
>               raise ValueError("ATTRIBUTE malformed")
E               ValueError: ATTRIBUTE malformed

dot_dsl.py:44: ValueError
________________________ DotDslTest.test_malformed_EDGE ________________________

self = <dot_dsl_test.DotDslTest testMethod=test_malformed_EDGE>

    def test_malformed_EDGE(self):
        with self.assertRaises(ValueError) as err:
            Graph([(EDGE, 1, 2)])
        self.assertEqual(type(err.exception), ValueError)
>       self.assertEqual(err.exception.args[0], "Edge is malformed")
E       AssertionError: 'ATTRIBUTE malformed' != 'Edge is malformed'
E       - ATTRIBUTE malformed
E       + Edge is malformed

dot_dsl_test.py:115: AssertionError
________________________ DotDslTest.test_malformed_attr ________________________

self = <dot_dsl_test.DotDslTest testMethod=test_malformed_attr>

    def test_malformed_attr(self):
        with self.assertRaises(ValueError) as err:
>           Graph([(ATTR, 1, 2, 3)])

dot_dsl_test.py:99: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def __init__(self, data=None):
        # Check for valid data input
        if data is None or not isinstance(data, list) or len(data) == 0:
            raise TypeError("Graph data malformed")
    
        self.graph_attributes = {}
        self.nodes = []
        self.edges = []
    
        for item in data:
            # Each item must be a tuple of (graph_attributes, nodes, edges)
            if not (isinstance(item, tuple) and len(item) == 3):
>               raise TypeError("Graph data malformed")
E               TypeError: Graph data malformed

dot_dsl.py:38: TypeError
_____________________ DotDslTest.test_malformed_graph_item _____________________

self = <dot_dsl_test.DotDslTest testMethod=test_malformed_graph_item>

    def test_malformed_graph_item(self):
        with self.assertRaises(TypeError) as err:
            Graph([()])
        self.assertEqual(type(err.exception), TypeError)
>       self.assertEqual(err.exception.args[0], "Graph item incomplete")
E       AssertionError: 'Graph data malformed' != 'Graph item incomplete'
E       - Graph data malformed
E       + Graph item incomplete

dot_dsl_test.py:88: AssertionError
________________________ DotDslTest.test_malformed_node ________________________

self = <dot_dsl_test.DotDslTest testMethod=test_malformed_node>

    def test_malformed_node(self):
        with self.assertRaises(ValueError) as err:
>           Graph([(NODE, 1, 2, 3)])

dot_dsl_test.py:106: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def __init__(self, data=None):
        # Check for valid data input
        if data is None or not isinstance(data, list) or len(data) == 0:
            raise TypeError("Graph data malformed")
    
        self.graph_attributes = {}
        self.nodes = []
        self.edges = []
    
        for item in data:
            # Each item must be a tuple of (graph_attributes, nodes, edges)
            if not (isinstance(item, tuple) and len(item) == 3):
>               raise TypeError("Graph data malformed")
E               TypeError: Graph data malformed

dot_dsl.py:38: TypeError
_________________________ DotDslTest.test_unknown_item _________________________

self = <dot_dsl_test.DotDslTest testMethod=test_unknown_item>

    def test_unknown_item(self):
        with self.assertRaises(ValueError) as err:
            Graph([(99, 1, 2)])
        self.assertEqual(type(err.exception), ValueError)
>       self.assertEqual(err.exception.args[0], "Unknown item")
E       AssertionError: 'ATTRIBUTE malformed' != 'Unknown item'
E       - ATTRIBUTE malformed
E       + Unknown item

dot_dsl_test.py:121: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED dot_dsl_test.py::DotDslTest::test_malformed_graph
FAILED dot_dsl_test.py::DotDslTest::test_empty_graph - TypeError: Graph data ...
FAILED dot_dsl_test.py::DotDslTest::test_graph_with_attributes - ValueError: ...
FAILED dot_dsl_test.py::DotDslTest::test_graph_with_one_attribute - ValueErro...
FAILED dot_dsl_test.py::DotDslTest::test_graph_with_one_edge - TypeError: Gra...
FAILED dot_dsl_test.py::DotDslTest::test_graph_with_one_node - ValueError: AT...
FAILED dot_dsl_test.py::DotDslTest::test_graph_with_one_node_with_keywords - ...
FAILED dot_dsl_test.py::DotDslTest::test_malformed_EDGE - AssertionError: 'AT...
FAILED dot_dsl_test.py::DotDslTest::test_malformed_attr - TypeError: Graph da...
FAILED dot_dsl_test.py::DotDslTest::test_malformed_graph_item - AssertionErro...
FAILED dot_dsl_test.py::DotDslTest::test_malformed_node - TypeError: Graph da...
FAILED dot_dsl_test.py::DotDslTest::test_unknown_item - AssertionError: 'ATTR...
========================= 11 failed, 1 passed in 1.23s =========================
