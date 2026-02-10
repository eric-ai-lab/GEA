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
[ 25%] Building CXX object CMakeFiles/parallel-letter-frequency.dir/parallel_letter_frequency_test.cpp.o
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/parallel_letter_frequency_test.cpp:18:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
   18 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/parallel_letter_frequency_test.cpp:28:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
   28 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/parallel_letter_frequency_test.cpp:37:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
   37 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/parallel_letter_frequency_test.cpp:49:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
   49 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/parallel_letter_frequency_test.cpp:60:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
   60 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/parallel_letter_frequency_test.cpp:72:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
   72 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/parallel_letter_frequency_test.cpp:83:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
   83 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/parallel_letter_frequency_test.cpp:92:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
   92 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/parallel_letter_frequency_test.cpp:101:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
  101 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/parallel_letter_frequency_test.cpp:116:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
  116 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/parallel_letter_frequency_test.cpp:411:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
  411 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/parallel_letter_frequency_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/parallel_letter_frequency_test.cpp:451:55: error: invalid initialization of reference of type 'const std::vector<std::__cxx11::basic_string<char> >&' from expression of type 'const std::vector<std::basic_string_view<char> >'
  451 |     auto freqs = parallel_letter_frequency::frequency(texts);
      |                                                       ^~~~~
In file included from /testbed/parallel_letter_frequency_test.cpp:1:
/testbed/parallel_letter_frequency.h:11:67: note: in passing argument 1 of 'std::map<char, int> parallel_letter_frequency::frequency(const std::vector<std::__cxx11::basic_string<char> >&)'
   11 |     std::map<char, int> frequency(const std::vector<std::string>& texts);
      |                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
make[2]: *** [CMakeFiles/parallel-letter-frequency.dir/build.make:76: CMakeFiles/parallel-letter-frequency.dir/parallel_letter_frequency_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/parallel-letter-frequency.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
