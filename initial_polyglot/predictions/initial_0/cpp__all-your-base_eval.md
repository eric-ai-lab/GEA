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
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/all_your_base_test.cpp:15:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   15 |     vector<unsigned int> out_digits = all_your_base::convert(2, in_digits, 10);
      |                                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/all_your_base_test.cpp:24:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   24 |     vector<unsigned int> out_digits = all_your_base::convert(2, in_digits, 10);
      |                                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/all_your_base_test.cpp:32:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   32 |     vector<unsigned int> out_digits = all_your_base::convert(10, in_digits, 2);
      |                                                              ^~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/all_your_base_test.cpp:40:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   40 |     vector<unsigned int> out_digits = all_your_base::convert(2, in_digits, 10);
      |                                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/all_your_base_test.cpp:48:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   48 |     vector<unsigned int> out_digits = all_your_base::convert(10, in_digits, 2);
      |                                                              ^~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/all_your_base_test.cpp:56:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   56 |     vector<unsigned int> out_digits = all_your_base::convert(3, in_digits, 16);
      |                                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/all_your_base_test.cpp:64:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   64 |     vector<unsigned int> out_digits = all_your_base::convert(16, in_digits, 3);
      |                                                              ^~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/all_your_base_test.cpp:72:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   72 |     vector<unsigned int> out_digits = all_your_base::convert(97, in_digits, 73);
      |                                                              ^~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/all_your_base_test.cpp:80:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   80 |     vector<unsigned int> out_digits = all_your_base::convert(2, in_digits, 10);
      |                                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/all_your_base_test.cpp:88:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   88 |     vector<unsigned int> out_digits = all_your_base::convert(10, in_digits, 2);
      |                                                              ^~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/all_your_base_test.cpp:96:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
   96 |     vector<unsigned int> out_digits = all_your_base::convert(10, in_digits, 2);
      |                                                              ^~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/all_your_base_test.cpp:104:62: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
  104 |     vector<unsigned int> out_digits = all_your_base::convert(7, in_digits, 10);
      |                                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/all_your_base_test.cpp:112:46: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
  112 |     REQUIRE_THROWS_AS(all_your_base::convert(1, in_digits, 10), std::invalid_argument);
      |                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/all_your_base_test.cpp:118:49: error: cannot convert 'std::vector<unsigned int>' to 'int'
  118 |     REQUIRE_THROWS_AS(all_your_base::convert(0, in_digits, 10), std::invalid_argument);
      |                                                 ^~~~~~~~~
      |                                                 |
      |                                                 std::vector<unsigned int>
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:52: note:   initializing argument 2 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                                                ~~~~^~~~~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/all_your_base_test.cpp:124:46: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
  124 |     REQUIRE_THROWS_AS(all_your_base::convert(2, in_digits, 10), std::invalid_argument);
      |                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/all_your_base_test.cpp:130:46: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
  130 |     REQUIRE_THROWS_AS(all_your_base::convert(2, in_digits, 1), std::invalid_argument);
      |                                              ^
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
In file included from /testbed/all_your_base_test.cpp:5:
/testbed/all_your_base_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/all_your_base_test.cpp:136:46: error: invalid initialization of reference of type 'const string&' {aka 'const std::__cxx11::basic_string<char>&'} from expression of type 'int'
  136 |     REQUIRE_THROWS_AS(all_your_base::convert(10, in_digits, 0), std::invalid_argument);
      |                                              ^~
In file included from /testbed/all_your_base_test.cpp:1:
/testbed/all_your_base.h:9:40: note: in passing argument 1 of 'std::string all_your_base::convert(const string&, int, int)'
    9 | std::string convert(const std::string& digits, int from_base, int to_base);
      |                     ~~~~~~~~~~~~~~~~~~~^~~~~~
make[2]: *** [CMakeFiles/all-your-base.dir/build.make:76: CMakeFiles/all-your-base.dir/all_your_base_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/all-your-base.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
