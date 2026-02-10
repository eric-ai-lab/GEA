+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: asyncio-1.3.0, anyio-4.12.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 20 items

grade_school_test.py FFFFF...............                                [100%]

=================================== FAILURES ===================================
______________________ GradeSchoolTest.test_add_a_student ______________________

self = <grade_school_test.GradeSchoolTest testMethod=test_add_a_student>

    def test_add_a_student(self):
        school = School()
        school.add_student(name="Aimee", grade=2)
        expected = [True]
>       self.assertEqual(school.added(), expected)
E       AssertionError: True != [True]

grade_school_test.py:23: AssertionError
_ GradeSchoolTest.test_adding_multiple_students_in_the_same_grade_in_the_roster _

self = <grade_school_test.GradeSchoolTest testMethod=test_adding_multiple_students_in_the_same_grade_in_the_roster>

    def test_adding_multiple_students_in_the_same_grade_in_the_roster(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
        school.add_student(name="Paul", grade=2)
        expected = [True, True, True]
>       self.assertEqual(school.added(), expected)
E       AssertionError: True != [True, True, True]

grade_school_test.py:38: AssertionError
___________ GradeSchoolTest.test_adding_students_in_multiple_grades ____________

self = <grade_school_test.GradeSchoolTest testMethod=test_adding_students_in_multiple_grades>

    def test_adding_students_in_multiple_grades(self):
        school = School()
        school.add_student(name="Chelsea", grade=3)
        school.add_student(name="Logan", grade=7)
        expected = [True, True]
>       self.assertEqual(school.added(), expected)
E       AssertionError: True != [True, True]

grade_school_test.py:73: AssertionError
_ GradeSchoolTest.test_cannot_add_same_student_to_multiple_grades_in_the_roster _

self = <grade_school_test.GradeSchoolTest testMethod=test_cannot_add_same_student_to_multiple_grades_in_the_roster>

    def test_cannot_add_same_student_to_multiple_grades_in_the_roster(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
        school.add_student(name="James", grade=3)
        school.add_student(name="Paul", grade=3)
        expected = [True, True, False, True]
>       self.assertEqual(school.added(), expected)
E       AssertionError: True != [True, True, False, True]

grade_school_test.py:90: AssertionError
_ GradeSchoolTest.test_cannot_add_student_to_same_grade_in_the_roster_more_than_once _

self = <grade_school_test.GradeSchoolTest testMethod=test_cannot_add_student_to_same_grade_in_the_roster_more_than_once>

    def test_cannot_add_student_to_same_grade_in_the_roster_more_than_once(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
        school.add_student(name="James", grade=2)
        school.add_student(name="Paul", grade=2)
        expected = [True, True, False, True]
>       self.assertEqual(school.added(), expected)
E       AssertionError: True != [True, True, False, True]

grade_school_test.py:56: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED grade_school_test.py::GradeSchoolTest::test_grade_is_empty_if_no_students_in_that_grade
PASSED grade_school_test.py::GradeSchoolTest::test_grade_is_empty_if_no_students_in_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_multiple_students_in_the_same_grade_are_added_to_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_roster_is_empty_when_no_student_is_added
PASSED grade_school_test.py::GradeSchoolTest::test_student_is_added_to_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_multiple_grades
PASSED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_multiple_grades_in_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_other_grade_for_multiple_grades
PASSED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_same_grade_in_the_roster_more_than_once
PASSED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_same_grade_more_than_once
PASSED grade_school_test.py::GradeSchoolTest::test_students_are_sorted_by_grades_and_then_by_name_in_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_students_are_sorted_by_grades_in_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_students_are_sorted_by_name_in_a_grade
PASSED grade_school_test.py::GradeSchoolTest::test_students_are_sorted_by_name_in_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_students_in_multiple_grades_are_added_to_the_roster
FAILED grade_school_test.py::GradeSchoolTest::test_add_a_student - AssertionE...
FAILED grade_school_test.py::GradeSchoolTest::test_adding_multiple_students_in_the_same_grade_in_the_roster
FAILED grade_school_test.py::GradeSchoolTest::test_adding_students_in_multiple_grades
FAILED grade_school_test.py::GradeSchoolTest::test_cannot_add_same_student_to_multiple_grades_in_the_roster
FAILED grade_school_test.py::GradeSchoolTest::test_cannot_add_student_to_same_grade_in_the_roster_more_than_once
========================= 5 failed, 15 passed in 0.05s =========================
