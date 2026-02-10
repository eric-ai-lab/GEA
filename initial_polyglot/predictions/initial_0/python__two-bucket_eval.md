+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 9 items

two_bucket_test.py .FFFFFF.F                                             [100%]

=================================== FAILURES ===================================
_ TwoBucketTest.test_measure_one_step_using_bucket_one_of_size_1_and_bucket_two_of_size_3_start_with_bucket_two _

self = <two_bucket_test.TwoBucketTest testMethod=test_measure_one_step_using_bucket_one_of_size_1_and_bucket_two_of_size_3_start_with_bucket_two>

    def test_measure_one_step_using_bucket_one_of_size_1_and_bucket_two_of_size_3_start_with_bucket_two(
        self,
    ):
>       self.assertEqual(measure(1, 3, 3, "two"), (1, "two", 0))
E       AssertionError: {'moves': 1, 'goal_bucket': 'two', 'other_bucket': 0} != (1, 'two', 0)

two_bucket_test.py:36: AssertionError
_ TwoBucketTest.test_measure_using_bucket_one_of_size_2_and_bucket_two_of_size_3_start_with_bucket_one_and_end_with_bucket_two _

self = <two_bucket_test.TwoBucketTest testMethod=test_measure_using_bucket_one_of_size_2_and_bucket_two_of_size_3_start_with_bucket_one_and_end_with_bucket_two>

    def test_measure_using_bucket_one_of_size_2_and_bucket_two_of_size_3_start_with_bucket_one_and_end_with_bucket_two(
        self,
    ):
>       self.assertEqual(measure(2, 3, 3, "one"), (2, "two", 2))
E       AssertionError: {'moves': 4, 'goal_bucket': 'two', 'other_bucket': 1} != (2, 'two', 2)

two_bucket_test.py:41: AssertionError
_ TwoBucketTest.test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_one _

self = <two_bucket_test.TwoBucketTest testMethod=test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_one>

    def test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_one(
        self,
    ):
>       self.assertEqual(measure(3, 5, 1, "one"), (4, "one", 5))
E       AssertionError: {'moves': 4, 'goal_bucket': 'one', 'other_bucket': 5} != (4, 'one', 5)

two_bucket_test.py:16: AssertionError
_ TwoBucketTest.test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_two _

self = <two_bucket_test.TwoBucketTest testMethod=test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_two>

    def test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_two(
        self,
    ):
>       self.assertEqual(measure(3, 5, 1, "two"), (8, "two", 3))
E       AssertionError: {'moves': 8, 'goal_bucket': 'two', 'other_bucket': 3} != (8, 'two', 3)

two_bucket_test.py:21: AssertionError
_ TwoBucketTest.test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_one _

self = <two_bucket_test.TwoBucketTest testMethod=test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_one>

    def test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_one(
        self,
    ):
>       self.assertEqual(measure(7, 11, 2, "one"), (14, "one", 11))
E       AssertionError: {'moves': 14, 'goal_bucket': 'one', 'other_bucket': 11} != (14, 'one', 11)

two_bucket_test.py:26: AssertionError
_ TwoBucketTest.test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_two _

self = <two_bucket_test.TwoBucketTest testMethod=test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_two>

    def test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_two(
        self,
    ):
>       self.assertEqual(measure(7, 11, 2, "two"), (18, "two", 7))
E       AssertionError: {'moves': 18, 'goal_bucket': 'two', 'other_bucket': 7} != (18, 'two', 7)

two_bucket_test.py:31: AssertionError
_ TwoBucketTest.test_with_the_same_buckets_but_a_different_goal_then_it_is_possible _

self = <two_bucket_test.TwoBucketTest testMethod=test_with_the_same_buckets_but_a_different_goal_then_it_is_possible>

    def test_with_the_same_buckets_but_a_different_goal_then_it_is_possible(self):
>       self.assertEqual(measure(6, 15, 9, "one"), (10, "two", 0))
E       AssertionError: {'moves': 10, 'goal_bucket': 'two', 'other_bucket': 0} != (10, 'two', 0)

two_bucket_test.py:48: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED two_bucket_test.py::TwoBucketTest::test_goal_larger_than_both_buckets_is_impossible
PASSED two_bucket_test.py::TwoBucketTest::test_not_possible_to_reach_the_goal
FAILED two_bucket_test.py::TwoBucketTest::test_measure_one_step_using_bucket_one_of_size_1_and_bucket_two_of_size_3_start_with_bucket_two
FAILED two_bucket_test.py::TwoBucketTest::test_measure_using_bucket_one_of_size_2_and_bucket_two_of_size_3_start_with_bucket_one_and_end_with_bucket_two
FAILED two_bucket_test.py::TwoBucketTest::test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_one
FAILED two_bucket_test.py::TwoBucketTest::test_measure_using_bucket_one_of_size_3_and_bucket_two_of_size_5_start_with_bucket_two
FAILED two_bucket_test.py::TwoBucketTest::test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_one
FAILED two_bucket_test.py::TwoBucketTest::test_measure_using_bucket_one_of_size_7_and_bucket_two_of_size_11_start_with_bucket_two
FAILED two_bucket_test.py::TwoBucketTest::test_with_the_same_buckets_but_a_different_goal_then_it_is_possible
========================= 7 failed, 2 passed in 1.11s ==========================
