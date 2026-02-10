+ cargo test -- --include-ignored
   Compiling grade-school v0.0.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 0.52s
     Running unittests src/lib.rs (target/debug/deps/grade_school-2324a25c6248b9be)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/grade-school.rs (target/debug/deps/grade_school-9cb83f373f9f5703)

running 10 tests
test grade_is_empty_if_no_students_in_that_grade ... ok
test grade_is_empty_if_no_students_in_the_roster ... ok
test grades_for_empty_school ... ok
test grades_for_one_student ... ok
test grades_for_several_students_are_sorted ... ok
test grades_when_several_students_have_the_same_grade ... ok
test student_not_added_to_multiple_grades ... ok
test student_not_added_to_other_grade_for_multiple_grades ... ok
test student_not_added_to_same_grade_more_than_once ... ok
test students_are_sorted_by_name_in_a_grade ... ok

test result: ok. 10 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests grade_school

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

