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
[ 25%] Building CXX object CMakeFiles/yacht.dir/yacht_test.cpp.o
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/yacht_test.cpp:22:53: error: cannot convert 'const char*' to 'yacht::Category'
   22 |         REQUIRE(50 == yacht::score({5, 5, 5, 5, 5}, "yacht"));
      |                                                     ^~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:22:53: error: cannot convert 'const char*' to 'yacht::Category'
   22 |         REQUIRE(50 == yacht::score({5, 5, 5, 5, 5}, "yacht"));
      |                                                     ^~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:22:53: error: cannot convert 'const char*' to 'yacht::Category'
   22 |         REQUIRE(50 == yacht::score({5, 5, 5, 5, 5}, "yacht"));
      |                                                     ^~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/yacht_test.cpp:28:52: error: cannot convert 'const char*' to 'yacht::Category'
   28 |         REQUIRE(0 == yacht::score({1, 3, 3, 2, 5}, "yacht"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:28:52: error: cannot convert 'const char*' to 'yacht::Category'
   28 |         REQUIRE(0 == yacht::score({1, 3, 3, 2, 5}, "yacht"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:28:52: error: cannot convert 'const char*' to 'yacht::Category'
   28 |         REQUIRE(0 == yacht::score({1, 3, 3, 2, 5}, "yacht"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/yacht_test.cpp:32:52: error: cannot convert 'const char*' to 'yacht::Category'
   32 |         REQUIRE(3 == yacht::score({1, 1, 1, 3, 5}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:32:52: error: cannot convert 'const char*' to 'yacht::Category'
   32 |         REQUIRE(3 == yacht::score({1, 1, 1, 3, 5}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:32:52: error: cannot convert 'const char*' to 'yacht::Category'
   32 |         REQUIRE(3 == yacht::score({1, 1, 1, 3, 5}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/yacht_test.cpp:36:52: error: cannot convert 'const char*' to 'yacht::Category'
   36 |         REQUIRE(3 == yacht::score({3, 1, 1, 5, 1}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:36:52: error: cannot convert 'const char*' to 'yacht::Category'
   36 |         REQUIRE(3 == yacht::score({3, 1, 1, 5, 1}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:36:52: error: cannot convert 'const char*' to 'yacht::Category'
   36 |         REQUIRE(3 == yacht::score({3, 1, 1, 5, 1}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/yacht_test.cpp:40:52: error: cannot convert 'const char*' to 'yacht::Category'
   40 |         REQUIRE(0 == yacht::score({4, 3, 6, 5, 5}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:40:52: error: cannot convert 'const char*' to 'yacht::Category'
   40 |         REQUIRE(0 == yacht::score({4, 3, 6, 5, 5}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:40:52: error: cannot convert 'const char*' to 'yacht::Category'
   40 |         REQUIRE(0 == yacht::score({4, 3, 6, 5, 5}, "ones"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/yacht_test.cpp:44:52: error: cannot convert 'const char*' to 'yacht::Category'
   44 |         REQUIRE(2 == yacht::score({2, 3, 4, 5, 6}, "twos"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:44:52: error: cannot convert 'const char*' to 'yacht::Category'
   44 |         REQUIRE(2 == yacht::score({2, 3, 4, 5, 6}, "twos"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:44:52: error: cannot convert 'const char*' to 'yacht::Category'
   44 |         REQUIRE(2 == yacht::score({2, 3, 4, 5, 6}, "twos"));
      |                                                    ^~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/yacht_test.cpp:48:52: error: cannot convert 'const char*' to 'yacht::Category'
   48 |         REQUIRE(8 == yacht::score({1, 4, 1, 4, 1}, "fours"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:48:52: error: cannot convert 'const char*' to 'yacht::Category'
   48 |         REQUIRE(8 == yacht::score({1, 4, 1, 4, 1}, "fours"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:48:52: error: cannot convert 'const char*' to 'yacht::Category'
   48 |         REQUIRE(8 == yacht::score({1, 4, 1, 4, 1}, "fours"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/yacht_test.cpp:52:53: error: cannot convert 'const char*' to 'yacht::Category'
   52 |         REQUIRE(15 == yacht::score({3, 3, 3, 3, 3}, "threes"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:52:53: error: cannot convert 'const char*' to 'yacht::Category'
   52 |         REQUIRE(15 == yacht::score({3, 3, 3, 3, 3}, "threes"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:52:53: error: cannot convert 'const char*' to 'yacht::Category'
   52 |         REQUIRE(15 == yacht::score({3, 3, 3, 3, 3}, "threes"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/yacht_test.cpp:56:52: error: cannot convert 'const char*' to 'yacht::Category'
   56 |         REQUIRE(0 == yacht::score({3, 3, 3, 3, 3}, "fives"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:56:52: error: cannot convert 'const char*' to 'yacht::Category'
   56 |         REQUIRE(0 == yacht::score({3, 3, 3, 3, 3}, "fives"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:56:52: error: cannot convert 'const char*' to 'yacht::Category'
   56 |         REQUIRE(0 == yacht::score({3, 3, 3, 3, 3}, "fives"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/yacht_test.cpp:60:53: error: cannot convert 'const char*' to 'yacht::Category'
   60 |         REQUIRE(10 == yacht::score({1, 5, 3, 5, 3}, "fives"));
      |                                                     ^~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:60:53: error: cannot convert 'const char*' to 'yacht::Category'
   60 |         REQUIRE(10 == yacht::score({1, 5, 3, 5, 3}, "fives"));
      |                                                     ^~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:60:53: error: cannot convert 'const char*' to 'yacht::Category'
   60 |         REQUIRE(10 == yacht::score({1, 5, 3, 5, 3}, "fives"));
      |                                                     ^~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/yacht_test.cpp:64:52: error: cannot convert 'const char*' to 'yacht::Category'
   64 |         REQUIRE(6 == yacht::score({2, 3, 4, 5, 6}, "sixes"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:64:52: error: cannot convert 'const char*' to 'yacht::Category'
   64 |         REQUIRE(6 == yacht::score({2, 3, 4, 5, 6}, "sixes"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:64:52: error: cannot convert 'const char*' to 'yacht::Category'
   64 |         REQUIRE(6 == yacht::score({2, 3, 4, 5, 6}, "sixes"));
      |                                                    ^~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/yacht_test.cpp:68:53: error: cannot convert 'const char*' to 'yacht::Category'
   68 |         REQUIRE(16 == yacht::score({2, 2, 4, 4, 4}, "full house"));
      |                                                     ^~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:68:53: error: cannot convert 'const char*' to 'yacht::Category'
   68 |         REQUIRE(16 == yacht::score({2, 2, 4, 4, 4}, "full house"));
      |                                                     ^~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:68:53: error: cannot convert 'const char*' to 'yacht::Category'
   68 |         REQUIRE(16 == yacht::score({2, 2, 4, 4, 4}, "full house"));
      |                                                     ^~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/yacht_test.cpp:72:53: error: cannot convert 'const char*' to 'yacht::Category'
   72 |         REQUIRE(19 == yacht::score({5, 3, 3, 5, 3}, "full house"));
      |                                                     ^~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:72:53: error: cannot convert 'const char*' to 'yacht::Category'
   72 |         REQUIRE(19 == yacht::score({5, 3, 3, 5, 3}, "full house"));
      |                                                     ^~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:72:53: error: cannot convert 'const char*' to 'yacht::Category'
   72 |         REQUIRE(19 == yacht::score({5, 3, 3, 5, 3}, "full house"));
      |                                                     ^~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/yacht_test.cpp:76:52: error: cannot convert 'const char*' to 'yacht::Category'
   76 |         REQUIRE(0 == yacht::score({2, 2, 4, 4, 5}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:76:52: error: cannot convert 'const char*' to 'yacht::Category'
   76 |         REQUIRE(0 == yacht::score({2, 2, 4, 4, 5}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:76:52: error: cannot convert 'const char*' to 'yacht::Category'
   76 |         REQUIRE(0 == yacht::score({2, 2, 4, 4, 5}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/yacht_test.cpp:80:52: error: cannot convert 'const char*' to 'yacht::Category'
   80 |         REQUIRE(0 == yacht::score({1, 4, 4, 4, 4}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:80:52: error: cannot convert 'const char*' to 'yacht::Category'
   80 |         REQUIRE(0 == yacht::score({1, 4, 4, 4, 4}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:80:52: error: cannot convert 'const char*' to 'yacht::Category'
   80 |         REQUIRE(0 == yacht::score({1, 4, 4, 4, 4}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/yacht_test.cpp:84:52: error: cannot convert 'const char*' to 'yacht::Category'
   84 |         REQUIRE(0 == yacht::score({2, 2, 2, 2, 2}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:84:52: error: cannot convert 'const char*' to 'yacht::Category'
   84 |         REQUIRE(0 == yacht::score({2, 2, 2, 2, 2}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:84:52: error: cannot convert 'const char*' to 'yacht::Category'
   84 |         REQUIRE(0 == yacht::score({2, 2, 2, 2, 2}, "full house"));
      |                                                    ^~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/yacht_test.cpp:88:53: error: cannot convert 'const char*' to 'yacht::Category'
   88 |         REQUIRE(24 == yacht::score({6, 6, 4, 6, 6}, "four of a kind"));
      |                                                     ^~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:88:53: error: cannot convert 'const char*' to 'yacht::Category'
   88 |         REQUIRE(24 == yacht::score({6, 6, 4, 6, 6}, "four of a kind"));
      |                                                     ^~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:88:53: error: cannot convert 'const char*' to 'yacht::Category'
   88 |         REQUIRE(24 == yacht::score({6, 6, 4, 6, 6}, "four of a kind"));
      |                                                     ^~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____34()':
/testbed/yacht_test.cpp:92:53: error: cannot convert 'const char*' to 'yacht::Category'
   92 |         REQUIRE(12 == yacht::score({3, 3, 3, 3, 3}, "four of a kind"));
      |                                                     ^~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:92:53: error: cannot convert 'const char*' to 'yacht::Category'
   92 |         REQUIRE(12 == yacht::score({3, 3, 3, 3, 3}, "four of a kind"));
      |                                                     ^~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:92:53: error: cannot convert 'const char*' to 'yacht::Category'
   92 |         REQUIRE(12 == yacht::score({3, 3, 3, 3, 3}, "four of a kind"));
      |                                                     ^~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____36()':
/testbed/yacht_test.cpp:96:52: error: cannot convert 'const char*' to 'yacht::Category'
   96 |         REQUIRE(0 == yacht::score({3, 3, 3, 5, 5}, "four of a kind"));
      |                                                    ^~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:96:52: error: cannot convert 'const char*' to 'yacht::Category'
   96 |         REQUIRE(0 == yacht::score({3, 3, 3, 5, 5}, "four of a kind"));
      |                                                    ^~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:96:52: error: cannot convert 'const char*' to 'yacht::Category'
   96 |         REQUIRE(0 == yacht::score({3, 3, 3, 5, 5}, "four of a kind"));
      |                                                    ^~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____38()':
/testbed/yacht_test.cpp:100:53: error: cannot convert 'const char*' to 'yacht::Category'
  100 |         REQUIRE(30 == yacht::score({3, 5, 4, 1, 2}, "little straight"));
      |                                                     ^~~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:100:53: error: cannot convert 'const char*' to 'yacht::Category'
  100 |         REQUIRE(30 == yacht::score({3, 5, 4, 1, 2}, "little straight"));
      |                                                     ^~~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:100:53: error: cannot convert 'const char*' to 'yacht::Category'
  100 |         REQUIRE(30 == yacht::score({3, 5, 4, 1, 2}, "little straight"));
      |                                                     ^~~~~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____40()':
/testbed/yacht_test.cpp:104:52: error: cannot convert 'const char*' to 'yacht::Category'
  104 |         REQUIRE(0 == yacht::score({1, 2, 3, 4, 5}, "big straight"));
      |                                                    ^~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:104:52: error: cannot convert 'const char*' to 'yacht::Category'
  104 |         REQUIRE(0 == yacht::score({1, 2, 3, 4, 5}, "big straight"));
      |                                                    ^~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:104:52: error: cannot convert 'const char*' to 'yacht::Category'
  104 |         REQUIRE(0 == yacht::score({1, 2, 3, 4, 5}, "big straight"));
      |                                                    ^~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____42()':
/testbed/yacht_test.cpp:108:52: error: cannot convert 'const char*' to 'yacht::Category'
  108 |         REQUIRE(0 == yacht::score({1, 1, 2, 3, 4}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:108:52: error: cannot convert 'const char*' to 'yacht::Category'
  108 |         REQUIRE(0 == yacht::score({1, 1, 2, 3, 4}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:108:52: error: cannot convert 'const char*' to 'yacht::Category'
  108 |         REQUIRE(0 == yacht::score({1, 1, 2, 3, 4}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____44()':
/testbed/yacht_test.cpp:112:52: error: cannot convert 'const char*' to 'yacht::Category'
  112 |         REQUIRE(0 == yacht::score({1, 2, 3, 4, 6}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:112:52: error: cannot convert 'const char*' to 'yacht::Category'
  112 |         REQUIRE(0 == yacht::score({1, 2, 3, 4, 6}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:112:52: error: cannot convert 'const char*' to 'yacht::Category'
  112 |         REQUIRE(0 == yacht::score({1, 2, 3, 4, 6}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____46()':
/testbed/yacht_test.cpp:116:52: error: cannot convert 'const char*' to 'yacht::Category'
  116 |         REQUIRE(0 == yacht::score({1, 1, 3, 4, 5}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:116:52: error: cannot convert 'const char*' to 'yacht::Category'
  116 |         REQUIRE(0 == yacht::score({1, 1, 3, 4, 5}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:116:52: error: cannot convert 'const char*' to 'yacht::Category'
  116 |         REQUIRE(0 == yacht::score({1, 1, 3, 4, 5}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____48()':
/testbed/yacht_test.cpp:120:53: error: cannot convert 'const char*' to 'yacht::Category'
  120 |         REQUIRE(30 == yacht::score({4, 6, 2, 5, 3}, "big straight"));
      |                                                     ^~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:120:53: error: cannot convert 'const char*' to 'yacht::Category'
  120 |         REQUIRE(30 == yacht::score({4, 6, 2, 5, 3}, "big straight"));
      |                                                     ^~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:120:53: error: cannot convert 'const char*' to 'yacht::Category'
  120 |         REQUIRE(30 == yacht::score({4, 6, 2, 5, 3}, "big straight"));
      |                                                     ^~~~~~~~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____50()':
/testbed/yacht_test.cpp:124:52: error: cannot convert 'const char*' to 'yacht::Category'
  124 |         REQUIRE(0 == yacht::score({6, 5, 4, 3, 2}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:124:52: error: cannot convert 'const char*' to 'yacht::Category'
  124 |         REQUIRE(0 == yacht::score({6, 5, 4, 3, 2}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:124:52: error: cannot convert 'const char*' to 'yacht::Category'
  124 |         REQUIRE(0 == yacht::score({6, 5, 4, 3, 2}, "little straight"));
      |                                                    ^~~~~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____52()':
/testbed/yacht_test.cpp:128:52: error: cannot convert 'const char*' to 'yacht::Category'
  128 |         REQUIRE(0 == yacht::score({6, 5, 4, 3, 1}, "big straight"));
      |                                                    ^~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:128:52: error: cannot convert 'const char*' to 'yacht::Category'
  128 |         REQUIRE(0 == yacht::score({6, 5, 4, 3, 1}, "big straight"));
      |                                                    ^~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:128:52: error: cannot convert 'const char*' to 'yacht::Category'
  128 |         REQUIRE(0 == yacht::score({6, 5, 4, 3, 1}, "big straight"));
      |                                                    ^~~~~~~~~~~~~~
      |                                                    |
      |                                                    const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____54()':
/testbed/yacht_test.cpp:132:53: error: cannot convert 'const char*' to 'yacht::Category'
  132 |         REQUIRE(23 == yacht::score({3, 3, 5, 6, 6}, "choice"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:132:53: error: cannot convert 'const char*' to 'yacht::Category'
  132 |         REQUIRE(23 == yacht::score({3, 3, 5, 6, 6}, "choice"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:132:53: error: cannot convert 'const char*' to 'yacht::Category'
  132 |         REQUIRE(23 == yacht::score({3, 3, 5, 6, 6}, "choice"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____56()':
/testbed/yacht_test.cpp:136:53: error: cannot convert 'const char*' to 'yacht::Category'
  136 |         REQUIRE(10 == yacht::score({2, 2, 2, 2, 2}, "choice"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:136:53: error: cannot convert 'const char*' to 'yacht::Category'
  136 |         REQUIRE(10 == yacht::score({2, 2, 2, 2, 2}, "choice"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
In file included from /testbed/yacht_test.cpp:5:
/testbed/yacht_test.cpp:136:53: error: cannot convert 'const char*' to 'yacht::Category'
  136 |         REQUIRE(10 == yacht::score({2, 2, 2, 2, 2}, "choice"));
      |                                                     ^~~~~~~~
      |                                                     |
      |                                                     const char*
In file included from /testbed/yacht_test.cpp:1:
/testbed/yacht.h:21:54: note:   initializing argument 2 of 'int yacht::score(const std::vector<int>&, yacht::Category)'
   21 |     int score(const std::vector<int>& dice, Category category);
      |                                             ~~~~~~~~~^~~~~~~~
make[2]: *** [CMakeFiles/yacht.dir/build.make:76: CMakeFiles/yacht.dir/yacht_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/yacht.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
