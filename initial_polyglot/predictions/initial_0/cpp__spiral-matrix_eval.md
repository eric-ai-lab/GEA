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
[ 25%] Building CXX object CMakeFiles/spiral-matrix.dir/spiral_matrix_test.cpp.o
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/spiral_matrix_test.cpp:14:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   14 |     REQUIRE(expected == spiral_matrix::spiral_matrix(0));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:14:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   14 |     REQUIRE(expected == spiral_matrix::spiral_matrix(0));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:14:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   14 |     REQUIRE(expected == spiral_matrix::spiral_matrix(0));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/spiral_matrix_test.cpp:20:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   20 |     REQUIRE(expected == spiral_matrix::spiral_matrix(1));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:20:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   20 |     REQUIRE(expected == spiral_matrix::spiral_matrix(1));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:20:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   20 |     REQUIRE(expected == spiral_matrix::spiral_matrix(1));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/spiral_matrix_test.cpp:28:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   28 |     REQUIRE(expected == spiral_matrix::spiral_matrix(2));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:28:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   28 |     REQUIRE(expected == spiral_matrix::spiral_matrix(2));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:28:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   28 |     REQUIRE(expected == spiral_matrix::spiral_matrix(2));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/spiral_matrix_test.cpp:37:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   37 |     REQUIRE(expected == spiral_matrix::spiral_matrix(3));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:37:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   37 |     REQUIRE(expected == spiral_matrix::spiral_matrix(3));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:37:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   37 |     REQUIRE(expected == spiral_matrix::spiral_matrix(3));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/spiral_matrix_test.cpp:47:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   47 |     REQUIRE(expected == spiral_matrix::spiral_matrix(4));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:47:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   47 |     REQUIRE(expected == spiral_matrix::spiral_matrix(4));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:47:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   47 |     REQUIRE(expected == spiral_matrix::spiral_matrix(4));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/spiral_matrix_test.cpp:58:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   58 |     REQUIRE(expected == spiral_matrix::spiral_matrix(5));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:58:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   58 |     REQUIRE(expected == spiral_matrix::spiral_matrix(5));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:6:
/testbed/spiral_matrix_test.cpp:58:40: error: 'spiral_matrix' is not a member of 'spiral_matrix'; did you mean 'spiral_matrix'?
   58 |     REQUIRE(expected == spiral_matrix::spiral_matrix(5));
      |                                        ^~~~~~~~~~~~~
In file included from /testbed/spiral_matrix_test.cpp:1:
/testbed/spiral_matrix.h:6:11: note: 'spiral_matrix' declared here
    6 | namespace spiral_matrix {
      |           ^~~~~~~~~~~~~
make[2]: *** [CMakeFiles/spiral-matrix.dir/build.make:76: CMakeFiles/spiral-matrix.dir/spiral_matrix_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/spiral-matrix.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
