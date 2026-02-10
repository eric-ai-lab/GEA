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
[ 25%] Building CXX object CMakeFiles/linked-list.dir/linked_list_test.cpp.o
[ 50%] Building CXX object CMakeFiles/linked-list.dir/linked_list.cpp.o
[ 75%] Building CXX object CMakeFiles/linked-list.dir/test/tests-main.cpp.o
[100%] Linking CXX executable linked-list
[100%] Built target linked-list
===============================================================================
All tests passed (42 assertions in 19 test cases)

[100%] Built target test_linked-list
+ cd ../
