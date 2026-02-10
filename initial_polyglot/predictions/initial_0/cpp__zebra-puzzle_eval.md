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
[ 25%] Building CXX object CMakeFiles/zebra-puzzle.dir/zebra_puzzle_test.cpp.o
[ 50%] Building CXX object CMakeFiles/zebra-puzzle.dir/zebra_puzzle.cpp.o
[ 75%] Building CXX object CMakeFiles/zebra-puzzle.dir/test/tests-main.cpp.o
[100%] Linking CXX executable zebra-puzzle
/usr/bin/ld: CMakeFiles/zebra-puzzle.dir/test/tests-main.cpp.o: in function `main':
/testbed/test/catch.hpp:17501: multiple definition of `main'; CMakeFiles/zebra-puzzle.dir/zebra_puzzle.cpp.o:/testbed/zebra_puzzle.cpp:16: first defined here
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/zebra-puzzle.dir/build.make:129: zebra-puzzle] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/zebra-puzzle.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
