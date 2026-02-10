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
-- Found Boost: /usr/lib/x86_64-linux-gnu/cmake/Boost-1.74.0/BoostConfig.cmake (found suitable version "1.74.0", minimum required is "1.58") found components: date_time 
-- Configuring done
-- Generating done
-- Build files have been written to: /testbed/build
+ make
[ 25%] Building CXX object CMakeFiles/gigasecond.dir/gigasecond_test.cpp.o
[ 50%] Building CXX object CMakeFiles/gigasecond.dir/gigasecond.cpp.o
[ 75%] Building CXX object CMakeFiles/gigasecond.dir/test/tests-main.cpp.o
[100%] Linking CXX executable gigasecond
[100%] Built target gigasecond
===============================================================================
All tests passed (5 assertions in 5 test cases)

[100%] Built target test_gigasecond
+ cd ../
