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

react_test.py .FFFF.F.FF.F.F                                             [100%]

=================================== FAILURES ===================================
______________ ReactTest.test_callback_cells_only_fire_on_change _______________

self = <react_test.ReactTest testMethod=test_callback_cells_only_fire_on_change>

    def test_callback_cells_only_fire_on_change(self):
        input = InputCell(1)
        output = ComputeCell([input], lambda inputs: 111 if inputs[0] < 3 else 222)
        cb1_observer = []
        callback1 = self.callback_factory(cb1_observer)
        output.add_callback(callback1)
        input.value = 2
        self.assertEqual(cb1_observer, [])
        input.value = 4
>       self.assertEqual(cb1_observer[-1], 222)
E       IndexError: list index out of range

react_test.py:105: IndexError
______________ ReactTest.test_callbacks_can_be_added_and_removed _______________

self = <react_test.ReactTest testMethod=test_callbacks_can_be_added_and_removed>

    def test_callbacks_can_be_added_and_removed(self):
        input = InputCell(11)
        output = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] + 1,
        )
        cb1_observer = []
        cb2_observer = []
        cb3_observer = []
        callback1 = self.callback_factory(cb1_observer)
        callback2 = self.callback_factory(cb2_observer)
        callback3 = self.callback_factory(cb3_observer)
        output.add_callback(callback1)
        output.add_callback(callback2)
        input.value = 31
>       self.assertEqual(cb1_observer[-1], 32)
E       IndexError: list index out of range

react_test.py:164: IndexError
____________ ReactTest.test_callbacks_can_fire_from_multiple_cells _____________

self = <react_test.ReactTest testMethod=test_callbacks_can_fire_from_multiple_cells>

    def test_callbacks_can_fire_from_multiple_cells(self):
        input = InputCell(1)
        plus_one = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] + 1,
        )
        minus_one = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] - 1,
        )
        cb1_observer = []
        cb2_observer = []
        callback1 = self.callback_factory(cb1_observer)
        callback2 = self.callback_factory(cb2_observer)
        plus_one.add_callback(callback1)
        minus_one.add_callback(callback2)
        input.value = 10
>       self.assertEqual(cb1_observer[-1], 11)
E       IndexError: list index out of range

react_test.py:144: IndexError
________ ReactTest.test_callbacks_do_not_report_already_reported_values ________

self = <react_test.ReactTest testMethod=test_callbacks_do_not_report_already_reported_values>

    def test_callbacks_do_not_report_already_reported_values(self):
        input = InputCell(1)
        output = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] + 1,
        )
        cb1_observer = []
        callback1 = self.callback_factory(cb1_observer)
        output.add_callback(callback1)
        input.value = 2
>       self.assertEqual(cb1_observer[-1], 3)
E       IndexError: list index out of range

react_test.py:119: IndexError
_ ReactTest.test_callbacks_should_only_be_called_once_even_if_multiple_dependencies_change _

self = <react_test.ReactTest testMethod=test_callbacks_should_only_be_called_once_even_if_multiple_dependencies_change>

    def test_callbacks_should_only_be_called_once_even_if_multiple_dependencies_change(
        self,
    ):
        input = InputCell(1)
        plus_one = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] + 1,
        )
        minus_one1 = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] - 1,
        )
        minus_one2 = ComputeCell(
            [
                minus_one1,
            ],
            lambda inputs: inputs[0] - 1,
        )
        output = ComputeCell(
            [
                plus_one,
                minus_one2,
            ],
            lambda inputs: inputs[0] * inputs[1],
        )
        cb1_observer = []
        callback1 = self.callback_factory(cb1_observer)
        output.add_callback(callback1)
        input.value = 4
>       self.assertEqual(cb1_observer[-1], 10)
E       IndexError: list index out of range

react_test.py:229: IndexError
________ ReactTest.test_compute_cells_can_depend_on_other_compute_cells ________

self = <react_test.ReactTest testMethod=test_compute_cells_can_depend_on_other_compute_cells>

    def test_compute_cells_can_depend_on_other_compute_cells(self):
        input = InputCell(1)
        times_two = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] * 2,
        )
        times_thirty = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] * 30,
        )
        output = ComputeCell(
            [
                times_two,
                times_thirty,
            ],
            lambda inputs: inputs[0] + inputs[1],
        )
        self.assertEqual(output.value, 32)
        input.value = 3
>       self.assertEqual(output.value, 96)
E       AssertionError: 32 != 96

react_test.py:80: AssertionError
_________________ ReactTest.test_compute_cells_fire_callbacks __________________

self = <react_test.ReactTest testMethod=test_compute_cells_fire_callbacks>

    def test_compute_cells_fire_callbacks(self):
        input = InputCell(1)
        output = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] + 1,
        )
        cb1_observer = []
        callback1 = self.callback_factory(cb1_observer)
        output.add_callback(callback1)
        input.value = 3
>       self.assertEqual(cb1_observer[-1], 4)
E       IndexError: list index out of range

react_test.py:94: IndexError
___ ReactTest.test_compute_cells_update_value_when_dependencies_are_changed ____

self = <react_test.ReactTest testMethod=test_compute_cells_update_value_when_dependencies_are_changed>

    def test_compute_cells_update_value_when_dependencies_are_changed(self):
        input = InputCell(1)
        output = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] + 1,
        )
        input.value = 3
>       self.assertEqual(output.value, 4)
E       AssertionError: 2 != 4

react_test.py:55: AssertionError
_ ReactTest.test_removing_a_callback_multiple_times_doesn_t_interfere_with_other_callbacks _

self = <react_test.ReactTest testMethod=test_removing_a_callback_multiple_times_doesn_t_interfere_with_other_callbacks>

    def test_removing_a_callback_multiple_times_doesn_t_interfere_with_other_callbacks(
        self,
    ):
        input = InputCell(1)
        output = ComputeCell(
            [
                input,
            ],
            lambda inputs: inputs[0] + 1,
        )
        cb1_observer = []
        cb2_observer = []
        callback1 = self.callback_factory(cb1_observer)
        callback2 = self.callback_factory(cb2_observer)
        output.add_callback(callback1)
        output.add_callback(callback2)
        output.remove_callback(callback1)
        output.remove_callback(callback1)
        output.remove_callback(callback1)
        input.value = 2
        self.assertEqual(cb1_observer, [])
>       self.assertEqual(cb2_observer[-1], 3)
E       IndexError: list index out of range

react_test.py:194: IndexError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED react_test.py::ReactTest::test_an_input_cell_s_value_can_be_set
PASSED react_test.py::ReactTest::test_callbacks_should_not_be_called_if_dependencies_change_but_output_value_doesn_t_change
PASSED react_test.py::ReactTest::test_compute_cells_calculate_initial_value
PASSED react_test.py::ReactTest::test_compute_cells_take_inputs_in_the_right_order
PASSED react_test.py::ReactTest::test_input_cells_have_a_value
FAILED react_test.py::ReactTest::test_callback_cells_only_fire_on_change - In...
FAILED react_test.py::ReactTest::test_callbacks_can_be_added_and_removed - In...
FAILED react_test.py::ReactTest::test_callbacks_can_fire_from_multiple_cells
FAILED react_test.py::ReactTest::test_callbacks_do_not_report_already_reported_values
FAILED react_test.py::ReactTest::test_callbacks_should_only_be_called_once_even_if_multiple_dependencies_change
FAILED react_test.py::ReactTest::test_compute_cells_can_depend_on_other_compute_cells
FAILED react_test.py::ReactTest::test_compute_cells_fire_callbacks - IndexErr...
FAILED react_test.py::ReactTest::test_compute_cells_update_value_when_dependencies_are_changed
FAILED react_test.py::ReactTest::test_removing_a_callback_multiple_times_doesn_t_interfere_with_other_callbacks
========================= 9 failed, 5 passed in 0.48s ==========================
