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
[ 25%] Building CXX object CMakeFiles/all-your-base.dir/all_your_base_test.cpp.o
[ 50%] Building CXX object CMakeFiles/all-your-base.dir/all_your_base.cpp.o
[ 75%] Building CXX object CMakeFiles/all-your-base.dir/test/tests-main.cpp.o
[100%] Linking CXX executable all-your-base
[100%] Built target all-your-base
===============================================================================
All tests passed (17 assertions in 17 test cases)

[100%] Built target test_all-your-base
+ cd ../
