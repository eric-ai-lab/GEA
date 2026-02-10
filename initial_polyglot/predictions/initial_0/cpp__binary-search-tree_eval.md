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
[ 25%] Building CXX object CMakeFiles/binary-search-tree.dir/binary_search_tree_test.cpp.o
/testbed/binary_search_tree_test.cpp:12:63: error: 'binary_tree' is not a member of 'binary_search_tree'
   12 | using tree_ptr = typename std::unique_ptr<binary_search_tree::binary_tree<T>>;
      |                                                               ^~~~~~~~~~~
/testbed/binary_search_tree_test.cpp:12:75: error: template argument 1 is invalid
   12 | using tree_ptr = typename std::unique_ptr<binary_search_tree::binary_tree<T>>;
      |                                                                           ^
/testbed/binary_search_tree_test.cpp:12:75: error: template argument 2 is invalid
/testbed/binary_search_tree_test.cpp:12:76: error: expected identifier before '>' token
   12 | using tree_ptr = typename std::unique_ptr<binary_search_tree::binary_tree<T>>;
      |                                                                            ^~
/testbed/binary_search_tree_test.cpp:15:29: error: 'tree_ptr' does not name a type
   15 | static void test_leaf(const tree_ptr<T> &tree,
      |                             ^~~~~~~~
/testbed/binary_search_tree_test.cpp:15:37: error: expected ',' or '...' before '<' token
   15 | static void test_leaf(const tree_ptr<T> &tree,
      |                                     ^
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp: In function 'void test_leaf(int)':
/testbed/binary_search_tree_test.cpp:18:13: error: 'data' was not declared in this scope; did you mean 'std::data'?
   18 |     REQUIRE(data == tree->data());
      |             ^~~~
In file included from /usr/include/c++/11/string:54,
                 from /testbed/test/catch.hpp:475,
                 from /testbed/binary_search_tree_test.cpp:5:
/usr/include/c++/11/bits/range_access.h:319:5: note: 'std::data' declared here
  319 |     data(initializer_list<_Tp> __il) noexcept
      |     ^~~~
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:18:21: error: 'tree' was not declared in this scope; did you mean 'free'?
   18 |     REQUIRE(data == tree->data());
      |                     ^~~~
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:18:13: error: 'data' was not declared in this scope; did you mean 'std::data'?
   18 |     REQUIRE(data == tree->data());
      |             ^~~~
In file included from /usr/include/c++/11/string:54,
                 from /testbed/test/catch.hpp:475,
                 from /testbed/binary_search_tree_test.cpp:5:
/usr/include/c++/11/bits/range_access.h:319:5: note: 'std::data' declared here
  319 |     data(initializer_list<_Tp> __il) noexcept
      |     ^~~~
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:18:21: error: 'tree' was not declared in this scope; did you mean 'free'?
   18 |     REQUIRE(data == tree->data());
      |                     ^~~~
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:19:36: error: 'has_left' was not declared in this scope
   19 |     REQUIRE((bool) tree->left() == has_left);
      |                                    ^~~~~~~~
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:19:36: error: 'has_left' was not declared in this scope
   19 |     REQUIRE((bool) tree->left() == has_left);
      |                                    ^~~~~~~~
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:20:37: error: 'has_right' was not declared in this scope
   20 |     REQUIRE((bool) tree->right() == has_right);
      |                                     ^~~~~~~~~
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:20:37: error: 'has_right' was not declared in this scope
   20 |     REQUIRE((bool) tree->right() == has_right);
      |                                     ^~~~~~~~~
/testbed/binary_search_tree_test.cpp: At global scope:
/testbed/binary_search_tree_test.cpp:24:8: error: 'tree_ptr' does not name a type
   24 | static tree_ptr<T> make_tree(const std::vector<T> &data)
      |        ^~~~~~~~
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/binary_search_tree_test.cpp:43:19: error: 'make_tree' was not declared in this scope
   43 |     auto tested = make_tree<uint32_t>({4});
      |                   ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:43:37: error: expected primary-expression before '>' token
   43 |     auto tested = make_tree<uint32_t>({4});
      |                                     ^
/testbed/binary_search_tree_test.cpp:43:38: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
   43 |     auto tested = make_tree<uint32_t>({4});
      |                                      ^
/testbed/binary_search_tree_test.cpp:43:41: error: expected ';' before '}' token
   43 |     auto tested = make_tree<uint32_t>({4});
      |                                         ^
      |                                         ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/binary_search_tree_test.cpp:51:19: error: 'make_tree' was not declared in this scope
   51 |     auto tested = make_tree<uint32_t>({4, 2});
      |                   ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:51:37: error: expected primary-expression before '>' token
   51 |     auto tested = make_tree<uint32_t>({4, 2});
      |                                     ^
/testbed/binary_search_tree_test.cpp:51:38: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
   51 |     auto tested = make_tree<uint32_t>({4, 2});
      |                                      ^
/testbed/binary_search_tree_test.cpp:51:40: error: left operand of comma operator has no effect [-Werror=unused-value]
   51 |     auto tested = make_tree<uint32_t>({4, 2});
      |                                        ^
/testbed/binary_search_tree_test.cpp:51:44: error: expected ';' before '}' token
   51 |     auto tested = make_tree<uint32_t>({4, 2});
      |                                            ^
      |                                            ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/binary_search_tree_test.cpp:59:19: error: 'make_tree' was not declared in this scope
   59 |     auto tested = make_tree<uint32_t>({4, 4});
      |                   ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:59:37: error: expected primary-expression before '>' token
   59 |     auto tested = make_tree<uint32_t>({4, 4});
      |                                     ^
/testbed/binary_search_tree_test.cpp:59:38: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
   59 |     auto tested = make_tree<uint32_t>({4, 4});
      |                                      ^
/testbed/binary_search_tree_test.cpp:59:40: error: left operand of comma operator has no effect [-Werror=unused-value]
   59 |     auto tested = make_tree<uint32_t>({4, 4});
      |                                        ^
/testbed/binary_search_tree_test.cpp:59:44: error: expected ';' before '}' token
   59 |     auto tested = make_tree<uint32_t>({4, 4});
      |                                            ^
      |                                            ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/binary_search_tree_test.cpp:67:19: error: 'make_tree' was not declared in this scope
   67 |     auto tested = make_tree<uint32_t>({4, 5});
      |                   ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:67:37: error: expected primary-expression before '>' token
   67 |     auto tested = make_tree<uint32_t>({4, 5});
      |                                     ^
/testbed/binary_search_tree_test.cpp:67:38: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
   67 |     auto tested = make_tree<uint32_t>({4, 5});
      |                                      ^
/testbed/binary_search_tree_test.cpp:67:40: error: left operand of comma operator has no effect [-Werror=unused-value]
   67 |     auto tested = make_tree<uint32_t>({4, 5});
      |                                        ^
/testbed/binary_search_tree_test.cpp:67:44: error: expected ';' before '}' token
   67 |     auto tested = make_tree<uint32_t>({4, 5});
      |                                            ^
      |                                            ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/binary_search_tree_test.cpp:75:19: error: 'make_tree' was not declared in this scope
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                   ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:75:37: error: expected primary-expression before '>' token
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                     ^
/testbed/binary_search_tree_test.cpp:75:38: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                      ^
/testbed/binary_search_tree_test.cpp:75:40: error: left operand of comma operator has no effect [-Werror=unused-value]
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                        ^
/testbed/binary_search_tree_test.cpp:75:46: error: right operand of comma operator has no effect [-Werror=unused-value]
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                              ^
/testbed/binary_search_tree_test.cpp:75:49: error: right operand of comma operator has no effect [-Werror=unused-value]
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                                 ^
/testbed/binary_search_tree_test.cpp:75:52: error: right operand of comma operator has no effect [-Werror=unused-value]
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                                    ^
/testbed/binary_search_tree_test.cpp:75:55: error: right operand of comma operator has no effect [-Werror=unused-value]
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                                       ^
/testbed/binary_search_tree_test.cpp:75:58: error: right operand of comma operator has no effect [-Werror=unused-value]
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                                          ^
/testbed/binary_search_tree_test.cpp:75:59: error: expected ';' before '}' token
   75 |     auto tested = make_tree<uint32_t>({4, 2, 6, 1, 3, 5, 7});
      |                                                           ^
      |                                                           ;
/testbed/binary_search_tree_test.cpp: At global scope:
/testbed/binary_search_tree_test.cpp:92:29: error: 'tree_ptr' does not name a type
   92 | static void test_sort(const tree_ptr<T> &tree, const std::vector<T> &expected)
      |                             ^~~~~~~~
/testbed/binary_search_tree_test.cpp:92:37: error: expected ',' or '...' before '<' token
   92 | static void test_sort(const tree_ptr<T> &tree, const std::vector<T> &expected)
      |                                     ^
/testbed/binary_search_tree_test.cpp: In function 'void test_sort(int)':
/testbed/binary_search_tree_test.cpp:95:21: error: 'tree' was not declared in this scope; did you mean 'free'?
   95 |     for (auto& x : *tree) {
      |                     ^~~~
      |                     free
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:98:13: error: 'expected' was not declared in this scope
   98 |     REQUIRE(expected == actual);
      |             ^~~~~~~~
In file included from /testbed/binary_search_tree_test.cpp:5:
/testbed/binary_search_tree_test.cpp:98:13: error: 'expected' was not declared in this scope
   98 |     REQUIRE(expected == actual);
      |             ^~~~~~~~
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/binary_search_tree_test.cpp:104:15: error: 'make_tree' was not declared in this scope
  104 |     test_sort(make_tree<uint32_t>({2}), {2});
      |               ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:104:33: error: expected primary-expression before '>' token
  104 |     test_sort(make_tree<uint32_t>({2}), {2});
      |                                 ^
/testbed/binary_search_tree_test.cpp:104:34: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
  104 |     test_sort(make_tree<uint32_t>({2}), {2});
      |                                  ^
/testbed/binary_search_tree_test.cpp:104:37: error: expected ';' before '}' token
  104 |     test_sort(make_tree<uint32_t>({2}), {2});
      |                                     ^
      |                                     ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/binary_search_tree_test.cpp:109:15: error: 'make_tree' was not declared in this scope
  109 |     test_sort(make_tree<uint32_t>({2, 1}), {1, 2});
      |               ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:109:33: error: expected primary-expression before '>' token
  109 |     test_sort(make_tree<uint32_t>({2, 1}), {1, 2});
      |                                 ^
/testbed/binary_search_tree_test.cpp:109:34: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
  109 |     test_sort(make_tree<uint32_t>({2, 1}), {1, 2});
      |                                  ^
/testbed/binary_search_tree_test.cpp:109:36: error: left operand of comma operator has no effect [-Werror=unused-value]
  109 |     test_sort(make_tree<uint32_t>({2, 1}), {1, 2});
      |                                    ^
/testbed/binary_search_tree_test.cpp:109:40: error: expected ';' before '}' token
  109 |     test_sort(make_tree<uint32_t>({2, 1}), {1, 2});
      |                                        ^
      |                                        ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/binary_search_tree_test.cpp:114:15: error: 'make_tree' was not declared in this scope
  114 |     test_sort(make_tree<uint32_t>({2, 2}), {2, 2});
      |               ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:114:33: error: expected primary-expression before '>' token
  114 |     test_sort(make_tree<uint32_t>({2, 2}), {2, 2});
      |                                 ^
/testbed/binary_search_tree_test.cpp:114:34: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
  114 |     test_sort(make_tree<uint32_t>({2, 2}), {2, 2});
      |                                  ^
/testbed/binary_search_tree_test.cpp:114:36: error: left operand of comma operator has no effect [-Werror=unused-value]
  114 |     test_sort(make_tree<uint32_t>({2, 2}), {2, 2});
      |                                    ^
/testbed/binary_search_tree_test.cpp:114:40: error: expected ';' before '}' token
  114 |     test_sort(make_tree<uint32_t>({2, 2}), {2, 2});
      |                                        ^
      |                                        ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/binary_search_tree_test.cpp:119:15: error: 'make_tree' was not declared in this scope
  119 |     test_sort(make_tree<uint32_t>({2, 3}), {2, 3});
      |               ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:119:33: error: expected primary-expression before '>' token
  119 |     test_sort(make_tree<uint32_t>({2, 3}), {2, 3});
      |                                 ^
/testbed/binary_search_tree_test.cpp:119:34: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
  119 |     test_sort(make_tree<uint32_t>({2, 3}), {2, 3});
      |                                  ^
/testbed/binary_search_tree_test.cpp:119:36: error: left operand of comma operator has no effect [-Werror=unused-value]
  119 |     test_sort(make_tree<uint32_t>({2, 3}), {2, 3});
      |                                    ^
/testbed/binary_search_tree_test.cpp:119:40: error: expected ';' before '}' token
  119 |     test_sort(make_tree<uint32_t>({2, 3}), {2, 3});
      |                                        ^
      |                                        ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/binary_search_tree_test.cpp:124:15: error: 'make_tree' was not declared in this scope
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |               ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:124:33: error: expected primary-expression before '>' token
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |                                 ^
/testbed/binary_search_tree_test.cpp:124:34: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |                                  ^
/testbed/binary_search_tree_test.cpp:124:36: error: left operand of comma operator has no effect [-Werror=unused-value]
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |                                    ^
/testbed/binary_search_tree_test.cpp:124:42: error: right operand of comma operator has no effect [-Werror=unused-value]
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |                                          ^
/testbed/binary_search_tree_test.cpp:124:45: error: right operand of comma operator has no effect [-Werror=unused-value]
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |                                             ^
/testbed/binary_search_tree_test.cpp:124:48: error: right operand of comma operator has no effect [-Werror=unused-value]
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |                                                ^
/testbed/binary_search_tree_test.cpp:124:51: error: right operand of comma operator has no effect [-Werror=unused-value]
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |                                                   ^
/testbed/binary_search_tree_test.cpp:124:52: error: expected ';' before '}' token
  124 |     test_sort(make_tree<uint32_t>({2, 1, 3, 6, 7, 5}), {1, 2, 3, 5, 6, 7});
      |                                                    ^
      |                                                    ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/binary_search_tree_test.cpp:131:19: error: 'make_tree' was not declared in this scope
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                   ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:131:40: error: expected primary-expression before '>' token
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                        ^
/testbed/binary_search_tree_test.cpp:131:41: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                         ^
/testbed/binary_search_tree_test.cpp:131:43: error: left operand of comma operator has no effect [-Werror=unused-value]
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                           ^~~~~~~~~~~
/testbed/binary_search_tree_test.cpp:131:66: error: right operand of comma operator has no effect [-Werror=unused-value]
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                                                  ^~~~~~
/testbed/binary_search_tree_test.cpp:131:74: error: right operand of comma operator has no effect [-Werror=unused-value]
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                                                          ^~~~~~~
/testbed/binary_search_tree_test.cpp:131:83: error: right operand of comma operator has no effect [-Werror=unused-value]
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                                                                   ^~~~~
/testbed/binary_search_tree_test.cpp:131:90: error: right operand of comma operator has no effect [-Werror=unused-value]
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                                                                          ^~~~~~~~~~
/testbed/binary_search_tree_test.cpp:131:102: error: right operand of comma operator has no effect [-Werror=unused-value]
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                                                                                      ^~~~~~~~
/testbed/binary_search_tree_test.cpp:131:110: error: expected ';' before '}' token
  131 |     auto tested = make_tree<std::string>({"delicious", "ballon", "flag", "apple", "cat", "elispsis", "grains"});
      |                                                                                                              ^
      |                                                                                                              ;
/testbed/binary_search_tree_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/binary_search_tree_test.cpp:146:15: error: 'make_tree' was not declared in this scope
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |               ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:146:36: error: expected primary-expression before '>' token
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                    ^
/testbed/binary_search_tree_test.cpp:146:37: error: ISO C++ forbids braced-groups within expressions [-Werror=pedantic]
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                     ^
/testbed/binary_search_tree_test.cpp:146:39: error: left operand of comma operator has no effect [-Werror=unused-value]
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                       ^~~
/testbed/binary_search_tree_test.cpp:146:51: error: right operand of comma operator has no effect [-Werror=unused-value]
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                                   ^~~~~~~~
/testbed/binary_search_tree_test.cpp:146:61: error: right operand of comma operator has no effect [-Werror=unused-value]
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                                             ^~~~~~~~~
/testbed/binary_search_tree_test.cpp:146:72: error: right operand of comma operator has no effect [-Werror=unused-value]
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                                                        ^~~~~~
/testbed/binary_search_tree_test.cpp:146:80: error: right operand of comma operator has no effect [-Werror=unused-value]
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                                                                ^~~~~~~~
/testbed/binary_search_tree_test.cpp:146:90: error: right operand of comma operator has no effect [-Werror=unused-value]
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                                                                          ^~~~
/testbed/binary_search_tree_test.cpp:146:96: error: right operand of comma operator has no effect [-Werror=unused-value]
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                                                                                ^~~~~~~~
/testbed/binary_search_tree_test.cpp:146:104: error: expected ';' before '}' token
  146 |     test_sort(make_tree<std::string>({"A", "few", "random", "strings", "that", "should", "be", "sorted"}), {"A", "be", "few", "random", "should", "sorted", "strings", "that"});
      |                                                                                                        ^
      |                                                                                                        ;
cc1plus: all warnings being treated as errors
make[2]: *** [CMakeFiles/binary-search-tree.dir/build.make:76: CMakeFiles/binary-search-tree.dir/binary_search_tree_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/binary-search-tree.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
