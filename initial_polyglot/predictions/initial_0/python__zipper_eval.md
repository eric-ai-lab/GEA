+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 14 items

zipper_test.py .FFFFFFFFFFFFF                                            [100%]

=================================== FAILURES ===================================
___________________________ ZipperTest.test_dead_end ___________________________

self = <zipper_test.ZipperTest testMethod=test_dead_end>

    def test_dead_end(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().left()

zipper_test.py:65: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b14cd0>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
________________ ZipperTest.test_different_paths_to_same_zipper ________________

self = <zipper_test.ZipperTest testMethod=test_different_paths_to_same_zipper>

    def test_different_paths_to_same_zipper(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
>       result = Zipper.from_tree(initial).left().up().right().to_tree()

zipper_test.py:306: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021ae8410>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
______________________ ZipperTest.test_left_right_and_up _______________________

self = <zipper_test.ZipperTest testMethod=test_left_right_and_up>

    def test_left_right_and_up(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().up().right().up().left().right().value()

zipper_test.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b1a050>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
_____________________ ZipperTest.test_left_right_and_value _____________________

self = <zipper_test.ZipperTest testMethod=test_left_right_and_value>

    def test_left_right_and_value(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().right().value()

zipper_test.py:50: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b6bd50>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
______________________ ZipperTest.test_set_left_with_leaf ______________________

self = <zipper_test.ZipperTest testMethod=test_set_left_with_leaf>

    def test_set_left_with_leaf(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        expected = {
            "value": 1,
            "left": {
                "value": 2,
                "left": {"value": 5, "left": None, "right": None},
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
        result = (
>           zipper.left().set_left({"value": 5, "left": None, "right": None}).to_tree()
        )

zipper_test.py:211: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b157d0>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
_____________________ ZipperTest.test_set_right_with_null ______________________

self = <zipper_test.ZipperTest testMethod=test_set_right_with_null>

    def test_set_right_with_null(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        expected = {
            "value": 1,
            "left": {"value": 2, "left": None, "right": None},
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().set_right(None).to_tree()

zipper_test.py:233: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b39590>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
____________________ ZipperTest.test_set_right_with_subtree ____________________

self = <zipper_test.ZipperTest testMethod=test_set_right_with_subtree>

    def test_set_right_with_subtree(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        expected = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {
                "value": 6,
                "left": {"value": 7, "left": None, "right": None},
                "right": {"value": 8, "left": None, "right": None},
            },
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.set_right(
            {
                "value": 6,
                "left": {"value": 7, "left": None, "right": None},
                "right": {"value": 8, "left": None, "right": None},
            }
        ).to_tree()

zipper_test.py:262: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b18750>
new_tree = {'left': {'left': None, 'right': None, 'value': 7}, 'right': {'left': None, 'right': None, 'value': 8}, 'value': 6}

    def set_right(self, new_tree):
        """Return a new zipper with the right child replaced by new_tree in the focus node."""
>       new_node = (self.focus[0], self.focus[1], new_tree)
E       KeyError: 0

zipper.py:54: KeyError
__________________________ ZipperTest.test_set_value ___________________________

self = <zipper_test.ZipperTest testMethod=test_set_value>

    def test_set_value(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        expected = {
            "value": 1,
            "left": {
                "value": 5,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().set_value(5).to_tree()

zipper_test.py:160: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b43d50>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
________________ ZipperTest.test_set_value_after_traversing_up _________________

self = <zipper_test.ZipperTest testMethod=test_set_value_after_traversing_up>

    def test_set_value_after_traversing_up(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        expected = {
            "value": 1,
            "left": {
                "value": 5,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().right().up().set_value(5).to_tree()

zipper_test.py:185: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b5e3d0>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
___________________ ZipperTest.test_set_value_on_deep_focus ____________________

self = <zipper_test.ZipperTest testMethod=test_set_value_on_deep_focus>

    def test_set_value_on_deep_focus(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        expected = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 5, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().right().set_value(5).to_tree()

zipper_test.py:293: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b79950>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
______ ZipperTest.test_test_ability_to_descend_multiple_levels_and_return ______

self = <zipper_test.ZipperTest testMethod=test_test_ability_to_descend_multiple_levels_and_return>

    def test_test_ability_to_descend_multiple_levels_and_return(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().right().up().up().value()

zipper_test.py:135: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021af34d0>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
____________________ ZipperTest.test_traversing_up_from_top ____________________

self = <zipper_test.ZipperTest testMethod=test_traversing_up_from_top>

    def test_traversing_up_from_top(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.up()

zipper_test.py:105: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b4b550>

    def up(self):
        """Move the focus up to the parent node. Raise Exception if already at the root."""
        if not self.breadcrumbs:
>           raise Exception("Already at the root of the tree")
E           Exception: Already at the root of the tree

zipper.py:60: Exception
_____________________ ZipperTest.test_tree_from_deep_focus _____________________

self = <zipper_test.ZipperTest testMethod=test_tree_from_deep_focus>

    def test_tree_from_deep_focus(self):
        initial = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        expected = {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {"value": 3, "left": None, "right": None},
            },
            "right": {"value": 4, "left": None, "right": None},
        }
    
        zipper = Zipper.from_tree(initial)
>       result = zipper.left().right().to_tree()

zipper_test.py:90: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <zipper.Zipper object at 0x79f021b06750>

    def left(self):
        """Move the focus to the left child. Raise Exception if left child is None."""
>       left_child = self.focus[1]
E       KeyError: 1

zipper.py:29: KeyError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED zipper_test.py::ZipperTest::test_data_is_retained
FAILED zipper_test.py::ZipperTest::test_dead_end - KeyError: 1
FAILED zipper_test.py::ZipperTest::test_different_paths_to_same_zipper - KeyE...
FAILED zipper_test.py::ZipperTest::test_left_right_and_up - KeyError: 1
FAILED zipper_test.py::ZipperTest::test_left_right_and_value - KeyError: 1
FAILED zipper_test.py::ZipperTest::test_set_left_with_leaf - KeyError: 1
FAILED zipper_test.py::ZipperTest::test_set_right_with_null - KeyError: 1
FAILED zipper_test.py::ZipperTest::test_set_right_with_subtree - KeyError: 0
FAILED zipper_test.py::ZipperTest::test_set_value - KeyError: 1
FAILED zipper_test.py::ZipperTest::test_set_value_after_traversing_up - KeyEr...
FAILED zipper_test.py::ZipperTest::test_set_value_on_deep_focus - KeyError: 1
FAILED zipper_test.py::ZipperTest::test_test_ability_to_descend_multiple_levels_and_return
FAILED zipper_test.py::ZipperTest::test_traversing_up_from_top - Exception: A...
FAILED zipper_test.py::ZipperTest::test_tree_from_deep_focus - KeyError: 1
========================= 13 failed, 1 passed in 0.51s =========================
