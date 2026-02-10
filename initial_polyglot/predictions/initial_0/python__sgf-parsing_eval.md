+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 23 items

sgf_parsing_test.py ..FFFFFFF...FF.FF.FF.FF                              [100%]

=================================== FAILURES ===================================
_ SgfParsingTest.test_escaped_backslash_in_property_value_becomes_just_a_backslash _

self = <sgf_parsing_test.SgfParsingTest testMethod=test_escaped_backslash_in_property_value_becomes_just_a_backslash>

    def test_escaped_backslash_in_property_value_becomes_just_a_backslash(self):
        input_string = "(;A[\\\\])"
        expected = SgfTree(properties={"A": ["\\"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2ba89090> != <sgf_parsing.SgfTree object at 0x7d0f2ba89150>

sgf_parsing_test.py:111: AssertionError
_ SgfParsingTest.test_escaped_closing_bracket_within_property_value_becomes_just_a_closing_bracket _

self = <sgf_parsing_test.SgfParsingTest testMethod=test_escaped_closing_bracket_within_property_value_becomes_just_a_closing_bracket>

    def test_escaped_closing_bracket_within_property_value_becomes_just_a_closing_bracket(
        self,
    ):
        input_string = "(;A[\\]])"
        expected = SgfTree(properties={"A": ["]"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2ba7a190> != <sgf_parsing.SgfTree object at 0x7d0f2ba7a310>

sgf_parsing_test.py:106: AssertionError
_ SgfParsingTest.test_escaped_newline_in_property_value_is_converted_to_nothing_at_all _

self = <sgf_parsing_test.SgfParsingTest testMethod=test_escaped_newline_in_property_value_is_converted_to_nothing_at_all>

    def test_escaped_newline_in_property_value_is_converted_to_nothing_at_all(self):
        input_string = "(;A[hello\\\nworld])"
        expected = SgfTree(properties={"A": ["helloworld"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2baa1410> != <sgf_parsing.SgfTree object at 0x7d0f2baa1050>

sgf_parsing_test.py:145: AssertionError
_ SgfParsingTest.test_escaped_t_and_n_in_property_value_are_just_letters_not_whitespace _

self = <sgf_parsing_test.SgfParsingTest testMethod=test_escaped_t_and_n_in_property_value_are_just_letters_not_whitespace>

    def test_escaped_t_and_n_in_property_value_are_just_letters_not_whitespace(self):
        input_string = "(;A[\\t = t and \\n = n])"
        expected = SgfTree(properties={"A": ["t = t and n = n"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2babca50> != <sgf_parsing.SgfTree object at 0x7d0f2babc050>

sgf_parsing_test.py:150: AssertionError
___ SgfParsingTest.test_escaped_tab_in_property_value_is_converted_to_space ____

self = <sgf_parsing_test.SgfParsingTest testMethod=test_escaped_tab_in_property_value_is_converted_to_space>

    def test_escaped_tab_in_property_value_is_converted_to_space(self):
        input_string = "(;A[hello\\\tworld])"
        expected = SgfTree(properties={"A": ["hello world"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2ba8a690> != <sgf_parsing.SgfTree object at 0x7d0f2ba8b410>

sgf_parsing_test.py:140: AssertionError
_ SgfParsingTest.test_mixing_various_kinds_of_whitespace_and_escaped_characters_in_property_value _

self = <sgf_parsing_test.SgfParsingTest testMethod=test_mixing_various_kinds_of_whitespace_and_escaped_characters_in_property_value>

    def test_mixing_various_kinds_of_whitespace_and_escaped_characters_in_property_value(
        self,
    ):
        input_string = "(;A[\\]b\nc\\\nd\t\te\\\\ \\\n\\]])"
        expected = SgfTree(properties={"A": ["]b\ncd  e\\ ]"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2bc20410> != <sgf_parsing.SgfTree object at 0x7d0f2bc20dd0>

sgf_parsing_test.py:157: AssertionError
___________________ SgfParsingTest.test_multiple_properties ____________________

self = <sgf_parsing_test.SgfParsingTest testMethod=test_multiple_properties>

    def test_multiple_properties(self):
        input_string = "(;A[b]C[d])"
        expected = SgfTree(properties={"A": ["b"], "C": ["d"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2baa65d0> != <sgf_parsing.SgfTree object at 0x7d0f2baa6810>

sgf_parsing_test.py:48: AssertionError
_ SgfParsingTest.test_opening_bracket_within_property_value_doesn_t_need_to_be_escaped _

self = <sgf_parsing_test.SgfParsingTest testMethod=test_opening_bracket_within_property_value_doesn_t_need_to_be_escaped>

    def test_opening_bracket_within_property_value_doesn_t_need_to_be_escaped(self):
        input_string = "(;A[x[y\\]z][foo]B[bar];C[baz])"
        expected = SgfTree(
            properties={"A": ["x[y]z", "foo"], "B": ["bar"]},
            children=[SgfTree({"C": ["baz"]})],
        )
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2bacf7d0> != <sgf_parsing.SgfTree object at 0x7d0f2bacf310>

sgf_parsing_test.py:119: AssertionError
__ SgfParsingTest.test_parentheses_in_property_value_don_t_need_to_be_escaped __

self = <sgf_parsing_test.SgfParsingTest testMethod=test_parentheses_in_property_value_don_t_need_to_be_escaped>

    def test_parentheses_in_property_value_don_t_need_to_be_escaped(self):
        input_string = "(;A[x(y)z][foo]B[bar];C[baz])"
        expected = SgfTree(
            properties={"A": ["x(y)z", "foo"], "B": ["bar"]},
            children=[SgfTree({"C": ["baz"]})],
        )
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2bad02d0> != <sgf_parsing.SgfTree object at 0x7d0f2bad0c90>

sgf_parsing_test.py:135: AssertionError
__ SgfParsingTest.test_semicolon_in_property_value_doesn_t_need_to_be_escaped __

self = <sgf_parsing_test.SgfParsingTest testMethod=test_semicolon_in_property_value_doesn_t_need_to_be_escaped>

    def test_semicolon_in_property_value_doesn_t_need_to_be_escaped(self):
        input_string = "(;A[a;b][foo]B[bar];C[baz])"
        expected = SgfTree(
            properties={"A": ["a;b", "foo"], "B": ["bar"]},
            children=[SgfTree({"C": ["baz"]})],
        )
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2babda10> != <sgf_parsing.SgfTree object at 0x7d0f2babfad0>

sgf_parsing_test.py:127: AssertionError
_____________________ SgfParsingTest.test_single_node_tree _____________________

self = <sgf_parsing_test.SgfParsingTest testMethod=test_single_node_tree>

    def test_single_node_tree(self):
        input_string = "(;A[B])"
        expected = SgfTree(properties={"A": ["B"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2ba79290> != <sgf_parsing.SgfTree object at 0x7d0f2ba79f10>

sgf_parsing_test.py:43: AssertionError
_____________________ SgfParsingTest.test_two_child_trees ______________________

self = <sgf_parsing_test.SgfParsingTest testMethod=test_two_child_trees>

    def test_two_child_trees(self):
        input_string = "(;A[B](;B[C])(;C[D]))"
        expected = SgfTree(
            properties={"A": ["B"]},
            children=[SgfTree({"B": ["C"]}), SgfTree({"C": ["D"]})],
        )
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2ba8b310> != <sgf_parsing.SgfTree object at 0x7d0f2ba8be10>

sgf_parsing_test.py:82: AssertionError
________________________ SgfParsingTest.test_two_nodes _________________________

self = <sgf_parsing_test.SgfParsingTest testMethod=test_two_nodes>

    def test_two_nodes(self):
        input_string = "(;A[B];B[C])"
        expected = SgfTree(properties={"A": ["B"]}, children=[SgfTree({"B": ["C"]})])
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2ba781d0> != <sgf_parsing.SgfTree object at 0x7d0f2ba79cd0>

sgf_parsing_test.py:74: AssertionError
____ SgfParsingTest.test_within_property_values_newlines_remain_as_newlines ____

self = <sgf_parsing_test.SgfParsingTest testMethod=test_within_property_values_newlines_remain_as_newlines>

    def test_within_property_values_newlines_remain_as_newlines(self):
        input_string = "(;A[hello\n\nworld])"
        expected = SgfTree(properties={"A": ["hello\n\nworld"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2bacf5d0> != <sgf_parsing.SgfTree object at 0x7d0f2bacf350>

sgf_parsing_test.py:99: AssertionError
_ SgfParsingTest.test_within_property_values_whitespace_characters_such_as_tab_are_converted_to_spaces _

self = <sgf_parsing_test.SgfParsingTest testMethod=test_within_property_values_whitespace_characters_such_as_tab_are_converted_to_spaces>

    def test_within_property_values_whitespace_characters_such_as_tab_are_converted_to_spaces(
        self,
    ):
        input_string = "(;A[hello\t\tworld])"
        expected = SgfTree(properties={"A": ["hello  world"]})
>       self.assertEqual(parse(input_string), expected)
E       AssertionError: <sgf_parsing.SgfTree object at 0x7d0f2bad1f90> != <sgf_parsing.SgfTree object at 0x7d0f2bad2550>

sgf_parsing_test.py:94: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED sgf_parsing_test.py::SgfParsingTest::test_all_lowercase_property
PASSED sgf_parsing_test.py::SgfParsingTest::test_empty_input
PASSED sgf_parsing_test.py::SgfParsingTest::test_multiple_property_values
PASSED sgf_parsing_test.py::SgfParsingTest::test_node_without_properties
PASSED sgf_parsing_test.py::SgfParsingTest::test_node_without_tree
PASSED sgf_parsing_test.py::SgfParsingTest::test_properties_without_delimiter
PASSED sgf_parsing_test.py::SgfParsingTest::test_tree_with_no_nodes
PASSED sgf_parsing_test.py::SgfParsingTest::test_upper_and_lowercase_property
FAILED sgf_parsing_test.py::SgfParsingTest::test_escaped_backslash_in_property_value_becomes_just_a_backslash
FAILED sgf_parsing_test.py::SgfParsingTest::test_escaped_closing_bracket_within_property_value_becomes_just_a_closing_bracket
FAILED sgf_parsing_test.py::SgfParsingTest::test_escaped_newline_in_property_value_is_converted_to_nothing_at_all
FAILED sgf_parsing_test.py::SgfParsingTest::test_escaped_t_and_n_in_property_value_are_just_letters_not_whitespace
FAILED sgf_parsing_test.py::SgfParsingTest::test_escaped_tab_in_property_value_is_converted_to_space
FAILED sgf_parsing_test.py::SgfParsingTest::test_mixing_various_kinds_of_whitespace_and_escaped_characters_in_property_value
FAILED sgf_parsing_test.py::SgfParsingTest::test_multiple_properties - Assert...
FAILED sgf_parsing_test.py::SgfParsingTest::test_opening_bracket_within_property_value_doesn_t_need_to_be_escaped
FAILED sgf_parsing_test.py::SgfParsingTest::test_parentheses_in_property_value_don_t_need_to_be_escaped
FAILED sgf_parsing_test.py::SgfParsingTest::test_semicolon_in_property_value_doesn_t_need_to_be_escaped
FAILED sgf_parsing_test.py::SgfParsingTest::test_single_node_tree - Assertion...
FAILED sgf_parsing_test.py::SgfParsingTest::test_two_child_trees - AssertionE...
FAILED sgf_parsing_test.py::SgfParsingTest::test_two_nodes - AssertionError: ...
FAILED sgf_parsing_test.py::SgfParsingTest::test_within_property_values_newlines_remain_as_newlines
FAILED sgf_parsing_test.py::SgfParsingTest::test_within_property_values_whitespace_characters_such_as_tab_are_converted_to_spaces
========================= 15 failed, 8 passed in 0.44s =========================
