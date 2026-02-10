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
[ 25%] Building CXX object CMakeFiles/perfect-numbers.dir/perfect_numbers_test.cpp.o
[ 50%] Building CXX object CMakeFiles/perfect-numbers.dir/perfect_numbers.cpp.o
[ 75%] Building CXX object CMakeFiles/perfect-numbers.dir/test/tests-main.cpp.o
[100%] Linking CXX executable perfect-numbers
[100%] Built target perfect-numbers
===============================================================================
All tests passed (13 assertions in 13 test cases)

[100%] Built target test_perfect-numbers
+ cd ../
