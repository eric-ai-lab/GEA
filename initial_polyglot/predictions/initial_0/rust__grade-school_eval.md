+ cargo test -- --include-ignored
   Compiling grade-school v0.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 1.15s
     Running unittests src/lib.rs (target/debug/deps/grade_school-8406093c39c245f2)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/grade-school.rs (target/debug/deps/grade_school-b702c9656962f796)

running 10 tests
test grade_is_empty_if_no_students_in_that_grade ... ok
test grades_for_empty_school ... ok
test grades_for_one_student ... ok
test grade_is_empty_if_no_students_in_the_roster ... ok
test grades_when_several_students_have_the_same_grade ... ok
test student_not_added_to_same_grade_more_than_once ... FAILED
test student_not_added_to_multiple_grades ... FAILED
test student_not_added_to_other_grade_for_multiple_grades ... FAILED
test grades_for_several_students_are_sorted ... ok
test students_are_sorted_by_name_in_a_grade ... ok

failures:

---- student_not_added_to_same_grade_more_than_once stdout ----

thread 'student_not_added_to_same_grade_more_than_once' panicked at src/lib.rs:19:17:
Student 'James' is already added to the roster
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- student_not_added_to_multiple_grades stdout ----

thread 'student_not_added_to_multiple_grades' panicked at src/lib.rs:19:17:
Student 'James' is already added to the roster

---- student_not_added_to_other_grade_for_multiple_grades stdout ----

thread 'student_not_added_to_other_grade_for_multiple_grades' panicked at src/lib.rs:19:17:
Student 'James' is already added to the roster


failures:
    student_not_added_to_multiple_grades
    student_not_added_to_other_grade_for_multiple_grades
    student_not_added_to_same_grade_more_than_once

test result: FAILED. 7 passed; 3 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

error: test failed, to rerun pass `--test grade-school`
