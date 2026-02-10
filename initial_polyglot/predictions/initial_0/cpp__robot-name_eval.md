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
[ 25%] Building CXX object CMakeFiles/robot-name.dir/robot_name_test.cpp.o
/testbed/robot_name_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/robot_name_test.cpp:29:23: error: 'robot' in namespace 'robot_name' does not name a type; did you mean 'Robot'?
   29 |     const robot_name::robot robot;
      |                       ^~~~~
      |                       Robot
In file included from /testbed/robot_name_test.cpp:5:
/testbed/robot_name_test.cpp:31:27: error: 'robot' was not declared in this scope
   31 |     REQUIRE(validate_name(robot.name()));
      |                           ^~~~~
In file included from /testbed/robot_name_test.cpp:5:
/testbed/robot_name_test.cpp:31:27: error: 'robot' was not declared in this scope
   31 |     REQUIRE(validate_name(robot.name()));
      |                           ^~~~~
/testbed/robot_name_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/robot_name_test.cpp:37:23: error: 'robot' in namespace 'robot_name' does not name a type; did you mean 'Robot'?
   37 |     const robot_name::robot robot;
      |                       ^~~~~
      |                       Robot
In file included from /testbed/robot_name_test.cpp:5:
/testbed/robot_name_test.cpp:39:13: error: 'robot' was not declared in this scope
   39 |     REQUIRE(robot.name() == robot.name());
      |             ^~~~~
In file included from /testbed/robot_name_test.cpp:5:
/testbed/robot_name_test.cpp:39:13: error: 'robot' was not declared in this scope
   39 |     REQUIRE(robot.name() == robot.name());
      |             ^~~~~
/testbed/robot_name_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/robot_name_test.cpp:44:23: error: 'robot' in namespace 'robot_name' does not name a type; did you mean 'Robot'?
   44 |     const robot_name::robot robot_one;
      |                       ^~~~~
      |                       Robot
/testbed/robot_name_test.cpp:45:23: error: 'robot' in namespace 'robot_name' does not name a type; did you mean 'Robot'?
   45 |     const robot_name::robot robot_two;
      |                       ^~~~~
      |                       Robot
In file included from /testbed/robot_name_test.cpp:5:
/testbed/robot_name_test.cpp:47:13: error: 'robot_one' was not declared in this scope; did you mean 'robot_name'?
   47 |     REQUIRE(robot_one.name() != robot_two.name());
      |             ^~~~~~~~~
/testbed/robot_name_test.cpp:47:33: error: 'robot_two' was not declared in this scope
   47 |     REQUIRE(robot_one.name() != robot_two.name());
      |                                 ^~~~~~~~~
In file included from /testbed/robot_name_test.cpp:5:
/testbed/robot_name_test.cpp:47:13: error: 'robot_one' was not declared in this scope; did you mean 'robot_name'?
   47 |     REQUIRE(robot_one.name() != robot_two.name());
      |             ^~~~~~~~~
/testbed/robot_name_test.cpp:47:33: error: 'robot_two' was not declared in this scope
   47 |     REQUIRE(robot_one.name() != robot_two.name());
      |                                 ^~~~~~~~~
/testbed/robot_name_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/robot_name_test.cpp:52:17: error: 'robot' is not a member of 'robot_name'; did you mean 'Robot'?
   52 |     robot_name::robot robot;
      |                 ^~~~~
      |                 Robot
/testbed/robot_name_test.cpp:53:32: error: 'robot' was not declared in this scope
   53 |     const auto original_name = robot.name();
      |                                ^~~~~
/testbed/robot_name_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/robot_name_test.cpp:62:17: error: 'robot' is not a member of 'robot_name'; did you mean 'Robot'?
   62 |     robot_name::robot robot;
      |                 ^~~~~
      |                 Robot
/testbed/robot_name_test.cpp:64:18: error: 'robot' was not declared in this scope
   64 |     names.insert(robot.name());
      |                  ^~~~~
/testbed/robot_name_test.cpp: At global scope:
/testbed/robot_name_test.cpp:18:13: error: 'bool {anonymous}::validate_name(const string&)' defined but not used [-Werror=unused-function]
   18 | static bool validate_name(const string& name)
      |             ^~~~~~~~~~~~~
cc1plus: all warnings being treated as errors
make[2]: *** [CMakeFiles/robot-name.dir/build.make:76: CMakeFiles/robot-name.dir/robot_name_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/robot-name.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
