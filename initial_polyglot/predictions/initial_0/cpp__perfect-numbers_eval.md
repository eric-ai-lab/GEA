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
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:9:38: error: 'classification' is not a member of 'perfect_numbers'
    9 | CATCH_REGISTER_ENUM(perfect_numbers::classification,
      |                                      ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:9:1: error: template argument 1 is invalid
    9 | CATCH_REGISTER_ENUM(perfect_numbers::classification,
      | ^~~~~~~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/perfect_numbers_test.cpp:15:34: error: 'perfect_numbers::classification' has not been declared
   15 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(6));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:15:34: error: 'perfect_numbers::classification' has not been declared
   15 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(6));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:15:34: error: 'perfect_numbers::classification' has not been declared
   15 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(6));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/perfect_numbers_test.cpp:21:34: error: 'perfect_numbers::classification' has not been declared
   21 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(28));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:21:34: error: 'perfect_numbers::classification' has not been declared
   21 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(28));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:21:34: error: 'perfect_numbers::classification' has not been declared
   21 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(28));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/perfect_numbers_test.cpp:25:34: error: 'perfect_numbers::classification' has not been declared
   25 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(33550336));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:25:34: error: 'perfect_numbers::classification' has not been declared
   25 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(33550336));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:25:34: error: 'perfect_numbers::classification' has not been declared
   25 |         REQUIRE(perfect_numbers::classification::perfect == perfect_numbers::classify(33550336));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/perfect_numbers_test.cpp:29:34: error: 'perfect_numbers::classification' has not been declared
   29 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(12));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:29:34: error: 'perfect_numbers::classification' has not been declared
   29 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(12));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:29:34: error: 'perfect_numbers::classification' has not been declared
   29 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(12));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/perfect_numbers_test.cpp:33:34: error: 'perfect_numbers::classification' has not been declared
   33 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(30));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:33:34: error: 'perfect_numbers::classification' has not been declared
   33 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(30));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:33:34: error: 'perfect_numbers::classification' has not been declared
   33 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(30));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/perfect_numbers_test.cpp:37:34: error: 'perfect_numbers::classification' has not been declared
   37 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(33550335));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:37:34: error: 'perfect_numbers::classification' has not been declared
   37 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(33550335));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:37:34: error: 'perfect_numbers::classification' has not been declared
   37 |         REQUIRE(perfect_numbers::classification::abundant == perfect_numbers::classify(33550335));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/perfect_numbers_test.cpp:41:34: error: 'perfect_numbers::classification' has not been declared
   41 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(2));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:41:34: error: 'perfect_numbers::classification' has not been declared
   41 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(2));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:41:34: error: 'perfect_numbers::classification' has not been declared
   41 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(2));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/perfect_numbers_test.cpp:45:34: error: 'perfect_numbers::classification' has not been declared
   45 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(4));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:45:34: error: 'perfect_numbers::classification' has not been declared
   45 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(4));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:45:34: error: 'perfect_numbers::classification' has not been declared
   45 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(4));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/perfect_numbers_test.cpp:49:34: error: 'perfect_numbers::classification' has not been declared
   49 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(32));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:49:34: error: 'perfect_numbers::classification' has not been declared
   49 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(32));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:49:34: error: 'perfect_numbers::classification' has not been declared
   49 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(32));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/perfect_numbers_test.cpp:53:34: error: 'perfect_numbers::classification' has not been declared
   53 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(33550337));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:53:34: error: 'perfect_numbers::classification' has not been declared
   53 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(33550337));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:53:34: error: 'perfect_numbers::classification' has not been declared
   53 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(33550337));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/perfect_numbers_test.cpp:57:34: error: 'perfect_numbers::classification' has not been declared
   57 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(1));
      |                                  ^~~~~~~~~~~~~~
In file included from /testbed/perfect_numbers_test.cpp:5:
/testbed/perfect_numbers_test.cpp:57:34: error: 'perfect_numbers::classification' has not been declared
   57 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(1));
      |                                  ^~~~~~~~~~~~~~
/testbed/perfect_numbers_test.cpp:57:34: error: 'perfect_numbers::classification' has not been declared
   57 |         REQUIRE(perfect_numbers::classification::deficient == perfect_numbers::classify(1));
      |                                  ^~~~~~~~~~~~~~
make[2]: *** [CMakeFiles/perfect-numbers.dir/build.make:76: CMakeFiles/perfect-numbers.dir/perfect_numbers_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/perfect-numbers.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
