+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 4 items

robot_name_test.py ...F                                                  [100%]

=================================== FAILURES ===================================
________________________ RobotNameTest.test_reset_name _________________________

self = <robot_name_test.RobotNameTest testMethod=test_reset_name>

    def test_reset_name(self):
        # Set a seed
        seed = "Totally random."
    
        # Initialize RNG using the seed
        random.seed(seed)
    
        # Call the generator
        robot = Robot()
        name = robot.name
    
        # Reinitialize RNG using seed
        random.seed(seed)
    
        # Call the generator again
        robot.reset()
        name2 = robot.name
>       self.assertNotEqual(name, name2)
E       AssertionError: 'EJ348' == 'EJ348'

robot_name_test.py:46: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED robot_name_test.py::RobotNameTest::test_different_robots_have_different_names
PASSED robot_name_test.py::RobotNameTest::test_has_name
PASSED robot_name_test.py::RobotNameTest::test_name_sticks
FAILED robot_name_test.py::RobotNameTest::test_reset_name - AssertionError: '...
========================= 1 failed, 3 passed in 0.53s ==========================
