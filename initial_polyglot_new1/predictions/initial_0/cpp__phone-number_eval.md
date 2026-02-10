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
[ 25%] Building CXX object CMakeFiles/phone-number.dir/phone_number_test.cpp.o
[ 50%] Building CXX object CMakeFiles/phone-number.dir/phone_number.cpp.o
[ 75%] Building CXX object CMakeFiles/phone-number.dir/test/tests-main.cpp.o
[100%] Linking CXX executable phone-number
[100%] Built target phone-number
===============================================================================
All tests passed (18 assertions in 18 test cases)

[100%] Built target test_phone-number
+ cd ../
