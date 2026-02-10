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
[ 25%] Building CXX object CMakeFiles/knapsack.dir/knapsack_test.cpp.o
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/knapsack_test.cpp:13:23: error: 'maximum_value' is not a member of 'knapsack'
   13 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 0);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp:13:23: error: 'maximum_value' is not a member of 'knapsack'
   13 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 0);
      |                       ^~~~~~~~~~~~~
/testbed/knapsack_test.cpp:13:23: error: 'maximum_value' is not a member of 'knapsack'
   13 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 0);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/knapsack_test.cpp:22:23: error: 'maximum_value' is not a member of 'knapsack'
   22 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 0);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp:22:23: error: 'maximum_value' is not a member of 'knapsack'
   22 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 0);
      |                       ^~~~~~~~~~~~~
/testbed/knapsack_test.cpp:22:23: error: 'maximum_value' is not a member of 'knapsack'
   22 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 0);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/knapsack_test.cpp:30:23: error: 'maximum_value' is not a member of 'knapsack'
   30 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 21);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp:30:23: error: 'maximum_value' is not a member of 'knapsack'
   30 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 21);
      |                       ^~~~~~~~~~~~~
/testbed/knapsack_test.cpp:30:23: error: 'maximum_value' is not a member of 'knapsack'
   30 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 21);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/knapsack_test.cpp:38:23: error: 'maximum_value' is not a member of 'knapsack'
   38 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 80);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp:38:23: error: 'maximum_value' is not a member of 'knapsack'
   38 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 80);
      |                       ^~~~~~~~~~~~~
/testbed/knapsack_test.cpp:38:23: error: 'maximum_value' is not a member of 'knapsack'
   38 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 80);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/knapsack_test.cpp:46:23: error: 'maximum_value' is not a member of 'knapsack'
   46 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 90);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp:46:23: error: 'maximum_value' is not a member of 'knapsack'
   46 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 90);
      |                       ^~~~~~~~~~~~~
/testbed/knapsack_test.cpp:46:23: error: 'maximum_value' is not a member of 'knapsack'
   46 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 90);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/knapsack_test.cpp:55:23: error: 'maximum_value' is not a member of 'knapsack'
   55 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 900);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp:55:23: error: 'maximum_value' is not a member of 'knapsack'
   55 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 900);
      |                       ^~~~~~~~~~~~~
/testbed/knapsack_test.cpp:55:23: error: 'maximum_value' is not a member of 'knapsack'
   55 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 900);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/knapsack_test.cpp:65:23: error: 'maximum_value' is not a member of 'knapsack'
   65 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 1458);
      |                       ^~~~~~~~~~~~~
In file included from /testbed/knapsack_test.cpp:6:
/testbed/knapsack_test.cpp:65:23: error: 'maximum_value' is not a member of 'knapsack'
   65 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 1458);
      |                       ^~~~~~~~~~~~~
/testbed/knapsack_test.cpp:65:23: error: 'maximum_value' is not a member of 'knapsack'
   65 |     REQUIRE(knapsack::maximum_value(max_weight, items) == 1458);
      |                       ^~~~~~~~~~~~~
make[2]: *** [CMakeFiles/knapsack.dir/build.make:76: CMakeFiles/knapsack.dir/knapsack_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/knapsack.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
