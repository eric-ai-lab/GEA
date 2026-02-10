+ set -e
+ '[' '!' -d build ']'
+ mkdir build
+ cd build
+ cmake -DEXERCISM_RUN_ALL_TESTS=1 -G 'Unix Makefiles' ..
-- The CXX compiler identification is GNU 11.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /testbed/build
+ make
[ 25%] Building CXX object CMakeFiles/grade-school.dir/grade_school_test.cpp.o
/testbed/grade_school_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/grade_school_test.cpp:13:25: error: 'school' in namespace 'grade_school' does not name a type; did you mean 'School'?
   13 |     const grade_school::school school_{};
      |                         ^~~~~~
      |                         School
In file included from /testbed/grade_school_test.cpp:6:
/testbed/grade_school_test.cpp:14:13: error: 'school_' was not declared in this scope
   14 |     REQUIRE(school_.roster().empty());
      |             ^~~~~~~
In file included from /testbed/grade_school_test.cpp:6:
/testbed/grade_school_test.cpp:14:13: error: 'school_' was not declared in this scope
   14 |     REQUIRE(school_.roster().empty());
      |             ^~~~~~~
/testbed/grade_school_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/grade_school_test.cpp:20:19: error: 'school' is not a member of 'grade_school'; did you mean 'School'?
   20 |     grade_school::school school_;
      |                   ^~~~~~
      |                   School
/testbed/grade_school_test.cpp:21:5: error: 'school_' was not declared in this scope
   21 |     school_.add("Aimee", 2);
      |     ^~~~~~~
/testbed/grade_school_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/grade_school_test.cpp:31:19: error: 'school' is not a member of 'grade_school'; did you mean 'School'?
   31 |     grade_school::school school_;
      |                   ^~~~~~
      |                   School
/testbed/grade_school_test.cpp:32:5: error: 'school_' was not declared in this scope
   32 |     school_.add("Blair", 2);
      |     ^~~~~~~
/testbed/grade_school_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/grade_school_test.cpp:44:19: error: 'school' is not a member of 'grade_school'; did you mean 'School'?
   44 |     grade_school::school school_;
      |                   ^~~~~~
      |                   School
/testbed/grade_school_test.cpp:45:5: error: 'school_' was not declared in this scope
   45 |     school_.add("Chelsea", 3);
      |     ^~~~~~~
/testbed/grade_school_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/grade_school_test.cpp:56:19: error: 'school' is not a member of 'grade_school'; did you mean 'School'?
   56 |     grade_school::school school_;
      |                   ^~~~~~
      |                   School
/testbed/grade_school_test.cpp:57:5: error: 'school_' was not declared in this scope
   57 |     school_.add("Franklin", 5);
      |     ^~~~~~~
/testbed/grade_school_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/grade_school_test.cpp:69:25: error: 'school' in namespace 'grade_school' does not name a type; did you mean 'School'?
   69 |     const grade_school::school school_{};
      |                         ^~~~~~
      |                         School
/testbed/grade_school_test.cpp:70:25: error: 'school_' was not declared in this scope
   70 |     const auto actual = school_.grade(1);
      |                         ^~~~~~~
/testbed/grade_school_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/grade_school_test.cpp:77:19: error: 'school' is not a member of 'grade_school'; did you mean 'School'?
   77 |     grade_school::school school_;
      |                   ^~~~~~
      |                   School
/testbed/grade_school_test.cpp:78:5: error: 'school_' was not declared in this scope
   78 |     school_.add("Jennifer", 4);
      |     ^~~~~~~
/testbed/grade_school_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/grade_school_test.cpp:95:25: error: 'school' in namespace 'grade_school' does not name a type; did you mean 'School'?
   95 |     const grade_school::school school_{};
      |                         ^~~~~~
      |                         School
/testbed/grade_school_test.cpp:96:5: error: 'school_' was not declared in this scope
   96 |     school_.grade(1);
      |     ^~~~~~~
make[2]: *** [CMakeFiles/grade-school.dir/build.make:76: CMakeFiles/grade-school.dir/grade_school_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/grade-school.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
