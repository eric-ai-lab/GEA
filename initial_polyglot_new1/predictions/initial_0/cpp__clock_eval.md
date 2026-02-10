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
[ 25%] Building CXX object CMakeFiles/clock.dir/clock_test.cpp.o
/testbed/clock_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/clock_test.cpp:183:54: error: 'clock' is not a member of 'date_independent'; did you mean 'Clock'?
  183 |         const auto actual = string(date_independent::clock::at(t.hour, t.minute));
      |                                                      ^~~~~
      |                                                      Clock
/testbed/clock_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____3()':
/testbed/clock_test.cpp:194:54: error: 'clock' is not a member of 'date_independent'; did you mean 'Clock'?
  194 |         const auto actual = string(date_independent::clock::at(a.hour, a.minute).plus(a.add));
      |                                                      ^~~~~
      |                                                      Clock
/testbed/clock_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/clock_test.cpp:204:47: error: 'date_independent::clock' has not been declared
  204 |         const auto clock1 = date_independent::clock::at(e.c1.hour, e.c1.minute);
      |                                               ^~~~~
/testbed/clock_test.cpp:205:47: error: 'date_independent::clock' has not been declared
  205 |         const auto clock2 = date_independent::clock::at(e.c2.hour, e.c2.minute);
      |                                               ^~~~~
make[2]: *** [CMakeFiles/clock.dir/build.make:76: CMakeFiles/clock.dir/clock_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/clock.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
