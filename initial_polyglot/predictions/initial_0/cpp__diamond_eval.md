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
[ 25%] Building CXX object CMakeFiles/diamond.dir/diamond_test.cpp.o
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/diamond_test.cpp:29:26: error: 'rows' is not a member of 'diamond'
   29 |         REQUIRE(diamond::rows('A') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp:29:26: error: 'rows' is not a member of 'diamond'
   29 |         REQUIRE(diamond::rows('A') == expected);
      |                          ^~~~
/testbed/diamond_test.cpp:29:26: error: 'rows' is not a member of 'diamond'
   29 |         REQUIRE(diamond::rows('A') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/diamond_test.cpp:38:26: error: 'rows' is not a member of 'diamond'
   38 |         REQUIRE(diamond::rows('B') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp:38:26: error: 'rows' is not a member of 'diamond'
   38 |         REQUIRE(diamond::rows('B') == expected);
      |                          ^~~~
/testbed/diamond_test.cpp:38:26: error: 'rows' is not a member of 'diamond'
   38 |         REQUIRE(diamond::rows('B') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/diamond_test.cpp:47:26: error: 'rows' is not a member of 'diamond'
   47 |         REQUIRE(diamond::rows('C') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp:47:26: error: 'rows' is not a member of 'diamond'
   47 |         REQUIRE(diamond::rows('C') == expected);
      |                          ^~~~
/testbed/diamond_test.cpp:47:26: error: 'rows' is not a member of 'diamond'
   47 |         REQUIRE(diamond::rows('C') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/diamond_test.cpp:58:26: error: 'rows' is not a member of 'diamond'
   58 |         REQUIRE(diamond::rows('D') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp:58:26: error: 'rows' is not a member of 'diamond'
   58 |         REQUIRE(diamond::rows('D') == expected);
      |                          ^~~~
/testbed/diamond_test.cpp:58:26: error: 'rows' is not a member of 'diamond'
   58 |         REQUIRE(diamond::rows('D') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/diamond_test.cpp:113:26: error: 'rows' is not a member of 'diamond'
  113 |         REQUIRE(diamond::rows('Z') == expected);
      |                          ^~~~
In file included from /testbed/diamond_test.cpp:5:
/testbed/diamond_test.cpp:113:26: error: 'rows' is not a member of 'diamond'
  113 |         REQUIRE(diamond::rows('Z') == expected);
      |                          ^~~~
/testbed/diamond_test.cpp:113:26: error: 'rows' is not a member of 'diamond'
  113 |         REQUIRE(diamond::rows('Z') == expected);
      |                          ^~~~
make[2]: *** [CMakeFiles/diamond.dir/build.make:76: CMakeFiles/diamond.dir/diamond_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/diamond.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
