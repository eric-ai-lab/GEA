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
+ make
-- Build files have been written to: /testbed/build
[ 25%] Building CXX object CMakeFiles/all-your-base.dir/all_your_base_test.cpp.o
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/all_your_base_test.cpp:15:65: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   15 |     vector<unsigned int> out_digits = all_your_base::convert(2, in_digits, 10);
      |                                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/all_your_base_test.cpp:24:65: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   24 |     vector<unsigned int> out_digits = all_your_base::convert(2, in_digits, 10);
      |                                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/all_your_base_test.cpp:32:66: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   32 |     vector<unsigned int> out_digits = all_your_base::convert(10, in_digits, 2);
      |                                                                  ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/all_your_base_test.cpp:40:65: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   40 |     vector<unsigned int> out_digits = all_your_base::convert(2, in_digits, 10);
      |                                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/all_your_base_test.cpp:48:66: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   48 |     vector<unsigned int> out_digits = all_your_base::convert(10, in_digits, 2);
      |                                                                  ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/all_your_base_test.cpp:56:65: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   56 |     vector<unsigned int> out_digits = all_your_base::convert(3, in_digits, 16);
      |                                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/all_your_base_test.cpp:64:66: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   64 |     vector<unsigned int> out_digits = all_your_base::convert(16, in_digits, 3);
      |                                                                  ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/all_your_base_test.cpp:72:66: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   72 |     vector<unsigned int> out_digits = all_your_base::convert(97, in_digits, 73);
      |                                                                  ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/all_your_base_test.cpp:80:65: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   80 |     vector<unsigned int> out_digits = all_your_base::convert(2, in_digits, 10);
      |                                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/all_your_base_test.cpp:88:66: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   88 |     vector<unsigned int> out_digits = all_your_base::convert(10, in_digits, 2);
      |                                                                  ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/all_your_base_test.cpp:96:66: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
   96 |     vector<unsigned int> out_digits = all_your_base::convert(10, in_digits, 2);
      |                                                                  ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/all_your_base_test.cpp:104:65: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
  104 |     vector<unsigned int> out_digits = all_your_base::convert(7, in_digits, 10);
      |                                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/all_your_base_test.cpp:112:49: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
  112 |     REQUIRE_THROWS_AS(all_your_base::convert(1, in_digits, 10), std::invalid_argument);
      |                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/all_your_base_test.cpp:118:49: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
  118 |     REQUIRE_THROWS_AS(all_your_base::convert(0, in_digits, 10), std::invalid_argument);
      |                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/all_your_base_test.cpp:124:49: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
  124 |     REQUIRE_THROWS_AS(all_your_base::convert(2, in_digits, 10), std::invalid_argument);
      |                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/all_your_base_test.cpp:130:49: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
  130 |     REQUIRE_THROWS_AS(all_your_base::convert(2, in_digits, 1), std::invalid_argument);
      |                                                 ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/all_your_base_test.cpp:136:50: error: invalid initialization of reference of type 'const std::vector<int>&' from expression of type 'std::vector<unsigned int>'
  136 |     REQUIRE_THROWS_AS(all_your_base::convert(10, in_digits, 0), std::invalid_argument);
      |                                                  ^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:15:67: note: in passing argument 2 of 'std::vector<int> all_your_base::convert(int, const std::vector<int>&, int)'
   15 | std::vector<int> convert(int source_base, const std::vector<int>& digits, int target_base);
      |                                           ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~
make[2]: *** [CMakeFiles/all-your-base.dir/build.make:76: CMakeFiles/all-your-base.dir/all_your_base_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/all-your-base.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
