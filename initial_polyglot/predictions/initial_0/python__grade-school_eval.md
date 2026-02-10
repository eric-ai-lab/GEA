+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 20 items

grade_school_test.py FFFFF.....FFFFF.....                                [100%]

=================================== FAILURES ===================================
______________________ GradeSchoolTest.test_add_a_student ______________________

self = <grade_school_test.GradeSchoolTest testMethod=test_add_a_student>

    def test_add_a_student(self):
        school = School()
        school.add_student(name="Aimee", grade=2)
        expected = [True]
>       self.assertEqual(school.added(), expected)
E       AssertionError: Lists differ: ['Aimee'] != [True]
E       
E       First differing element 0:
E       'Aimee'
E       True
E       
E       - ['Aimee']
E       + [True]

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
E       AssertionError: Lists differ: ['Blair', 'James', 'Paul'] != [True, True, True]
E       
E       First differing element 0:
E       'Blair'
E       True
E       
E       - ['Blair', 'James', 'Paul']
E       + [True, True, True]

grade_school_test.py:38: AssertionError
___________ GradeSchoolTest.test_adding_students_in_multiple_grades ____________

self = <grade_school_test.GradeSchoolTest testMethod=test_adding_students_in_multiple_grades>

    def test_adding_students_in_multiple_grades(self):
        school = School()
        school.add_student(name="Chelsea", grade=3)
        school.add_student(name="Logan", grade=7)
        expected = [True, True]
>       self.assertEqual(school.added(), expected)
E       AssertionError: Lists differ: ['Chelsea', 'Logan'] != [True, True]
E       
E       First differing element 0:
E       'Chelsea'
E       True
E       
E       - ['Chelsea', 'Logan']
E       + [True, True]

grade_school_test.py:73: AssertionError
_ GradeSchoolTest.test_cannot_add_same_student_to_multiple_grades_in_the_roster _

self = <grade_school_test.GradeSchoolTest testMethod=test_cannot_add_same_student_to_multiple_grades_in_the_roster>

    def test_cannot_add_same_student_to_multiple_grades_in_the_roster(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
>       school.add_student(name="James", grade=3)

grade_school_test.py:87: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <grade_school.School object at 0x7490e1f17190>, name = 'James', grade = 3

    def add_student(self, name, grade):
        # Check for duplicate student name
        if name in self._students:
>           raise ValueError(f"Student '{name}' has already been added")
E           ValueError: Student 'James' has already been added

grade_school.py:11: ValueError
_ GradeSchoolTest.test_cannot_add_student_to_same_grade_in_the_roster_more_than_once _

self = <grade_school_test.GradeSchoolTest testMethod=test_cannot_add_student_to_same_grade_in_the_roster_more_than_once>

    def test_cannot_add_student_to_same_grade_in_the_roster_more_than_once(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
>       school.add_student(name="James", grade=2)

grade_school_test.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <grade_school.School object at 0x7490e1f75fd0>, name = 'James', grade = 2

    def add_student(self, name, grade):
        # Check for duplicate student name
        if name in self._students:
>           raise ValueError(f"Student '{name}' has already been added")
E           ValueError: Student 'James' has already been added

grade_school.py:11: ValueError
__________ GradeSchoolTest.test_student_not_added_to_multiple_grades ___________

self = <grade_school_test.GradeSchoolTest testMethod=test_student_not_added_to_multiple_grades>

    def test_student_not_added_to_multiple_grades(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
>       school.add_student(name="James", grade=3)

grade_school_test.py:160: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <grade_school.School object at 0x7490e1f15e90>, name = 'James', grade = 3

    def add_student(self, name, grade):
        # Check for duplicate student name
        if name in self._students:
>           raise ValueError(f"Student '{name}' has already been added")
E           ValueError: Student 'James' has already been added

grade_school.py:11: ValueError
___ GradeSchoolTest.test_student_not_added_to_multiple_grades_in_the_roster ____

self = <grade_school_test.GradeSchoolTest testMethod=test_student_not_added_to_multiple_grades_in_the_roster>

    def test_student_not_added_to_multiple_grades_in_the_roster(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
>       school.add_student(name="James", grade=3)

grade_school_test.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <grade_school.School object at 0x7490e1f76690>, name = 'James', grade = 3

    def add_student(self, name, grade):
        # Check for duplicate student name
        if name in self._students:
>           raise ValueError(f"Student '{name}' has already been added")
E           ValueError: Student 'James' has already been added

grade_school.py:11: ValueError
__ GradeSchoolTest.test_student_not_added_to_other_grade_for_multiple_grades ___

self = <grade_school_test.GradeSchoolTest testMethod=test_student_not_added_to_other_grade_for_multiple_grades>

    def test_student_not_added_to_other_grade_for_multiple_grades(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
>       school.add_student(name="James", grade=3)

grade_school_test.py:169: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <grade_school.School object at 0x7490e1f174d0>, name = 'James', grade = 3

    def add_student(self, name, grade):
        # Check for duplicate student name
        if name in self._students:
>           raise ValueError(f"Student '{name}' has already been added")
E           ValueError: Student 'James' has already been added

grade_school.py:11: ValueError
_ GradeSchoolTest.test_student_not_added_to_same_grade_in_the_roster_more_than_once _

self = <grade_school_test.GradeSchoolTest testMethod=test_student_not_added_to_same_grade_in_the_roster_more_than_once>

    def test_student_not_added_to_same_grade_in_the_roster_more_than_once(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
>       school.add_student(name="James", grade=2)

grade_school_test.py:62: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <grade_school.School object at 0x7490e1f5e190>, name = 'James', grade = 2

    def add_student(self, name, grade):
        # Check for duplicate student name
        if name in self._students:
>           raise ValueError(f"Student '{name}' has already been added")
E           ValueError: Student 'James' has already been added

grade_school.py:11: ValueError
_____ GradeSchoolTest.test_student_not_added_to_same_grade_more_than_once ______

self = <grade_school_test.GradeSchoolTest testMethod=test_student_not_added_to_same_grade_more_than_once>

    def test_student_not_added_to_same_grade_more_than_once(self):
        school = School()
        school.add_student(name="Blair", grade=2)
        school.add_student(name="James", grade=2)
>       school.add_student(name="James", grade=2)

grade_school_test.py:151: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <grade_school.School object at 0x7490e1f4d050>, name = 'James', grade = 2

    def add_student(self, name, grade):
        # Check for duplicate student name
        if name in self._students:
>           raise ValueError(f"Student '{name}' has already been added")
E           ValueError: Student 'James' has already been added

grade_school.py:11: ValueError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED grade_school_test.py::GradeSchoolTest::test_grade_is_empty_if_no_students_in_that_grade
PASSED grade_school_test.py::GradeSchoolTest::test_grade_is_empty_if_no_students_in_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_multiple_students_in_the_same_grade_are_added_to_the_roster
PASSED grade_school_test.py::GradeSchoolTest::test_roster_is_empty_when_no_student_is_added
PASSED grade_school_test.py::GradeSchoolTest::test_student_is_added_to_the_roster
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
FAILED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_multiple_grades
FAILED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_multiple_grades_in_the_roster
FAILED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_other_grade_for_multiple_grades
FAILED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_same_grade_in_the_roster_more_than_once
FAILED grade_school_test.py::GradeSchoolTest::test_student_not_added_to_same_grade_more_than_once
======================== 10 failed, 10 passed in 0.11s =========================
