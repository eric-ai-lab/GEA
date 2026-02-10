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
[ 25%] Building CXX object CMakeFiles/queen-attack.dir/queen_attack_test.cpp.o
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/queen_attack_test.cpp:14:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
   14 |     const queen_attack::chess_board board{white, black};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:16:22: error: 'board' was not declared in this scope
   16 |     REQUIRE(white == board.white());
      |                      ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:16:22: error: 'board' was not declared in this scope
   16 |     REQUIRE(white == board.white());
      |                      ^~~~~
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/queen_attack_test.cpp:26:38: error: 'chess_board' is not a member of 'queen_attack'
   26 |     REQUIRE_THROWS_AS((queen_attack::chess_board{white, black}), std::domain_error);
      |                                      ^~~~~~~~~~~
/testbed/queen_attack_test.cpp:26:49: error: expected ')' before '{' token
   26 |     REQUIRE_THROWS_AS((queen_attack::chess_board{white, black}), std::domain_error);
      |                       ~                         ^
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/queen_attack_test.cpp:34:38: error: 'chess_board' is not a member of 'queen_attack'
   34 |     REQUIRE_THROWS_AS((queen_attack::chess_board{white, black}), std::domain_error);
      |                                      ^~~~~~~~~~~
/testbed/queen_attack_test.cpp:34:49: error: expected ')' before '{' token
   34 |     REQUIRE_THROWS_AS((queen_attack::chess_board{white, black}), std::domain_error);
      |                       ~                         ^
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/queen_attack_test.cpp:42:38: error: 'chess_board' is not a member of 'queen_attack'
   42 |     REQUIRE_THROWS_AS((queen_attack::chess_board{white, black}), std::domain_error);
      |                                      ^~~~~~~~~~~
/testbed/queen_attack_test.cpp:42:49: error: expected ')' before '{' token
   42 |     REQUIRE_THROWS_AS((queen_attack::chess_board{white, black}), std::domain_error);
      |                       ~                         ^
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/queen_attack_test.cpp:50:38: error: 'chess_board' is not a member of 'queen_attack'
   50 |     REQUIRE_THROWS_AS((queen_attack::chess_board{white, black}), std::domain_error);
      |                                      ^~~~~~~~~~~
/testbed/queen_attack_test.cpp:50:49: error: expected ')' before '{' token
   50 |     REQUIRE_THROWS_AS((queen_attack::chess_board{white, black}), std::domain_error);
      |                       ~                         ^
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/queen_attack_test.cpp:57:38: error: 'chess_board' is not a member of 'queen_attack'
   57 |     REQUIRE_THROWS_AS((queen_attack::chess_board{pos, pos}), std::domain_error);
      |                                      ^~~~~~~~~~~
/testbed/queen_attack_test.cpp:57:49: error: expected ')' before '{' token
   57 |     REQUIRE_THROWS_AS((queen_attack::chess_board{pos, pos}), std::domain_error);
      |                       ~                         ^
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/queen_attack_test.cpp:62:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
   62 |     const queen_attack::chess_board board{std::make_pair(2, 4), std::make_pair(6, 6)};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:64:19: error: 'board' was not declared in this scope
   64 |     REQUIRE_FALSE(board.can_attack());
      |                   ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:64:19: error: 'board' was not declared in this scope
   64 |     REQUIRE_FALSE(board.can_attack());
      |                   ^~~~~
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/queen_attack_test.cpp:69:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
   69 |     const queen_attack::chess_board board{std::make_pair(2, 4), std::make_pair(2, 6)};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:71:13: error: 'board' was not declared in this scope
   71 |     REQUIRE(board.can_attack());
      |             ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:71:13: error: 'board' was not declared in this scope
   71 |     REQUIRE(board.can_attack());
      |             ^~~~~
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/queen_attack_test.cpp:76:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
   76 |     const queen_attack::chess_board board{std::make_pair(4, 5), std::make_pair(2, 5)};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:78:13: error: 'board' was not declared in this scope
   78 |     REQUIRE(board.can_attack());
      |             ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:78:13: error: 'board' was not declared in this scope
   78 |     REQUIRE(board.can_attack());
      |             ^~~~~
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/queen_attack_test.cpp:83:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
   83 |     const queen_attack::chess_board board{std::make_pair(2, 2), std::make_pair(0, 4)};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:85:13: error: 'board' was not declared in this scope
   85 |     REQUIRE(board.can_attack());
      |             ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:85:13: error: 'board' was not declared in this scope
   85 |     REQUIRE(board.can_attack());
      |             ^~~~~
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/queen_attack_test.cpp:90:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
   90 |     const queen_attack::chess_board board{std::make_pair(2, 2), std::make_pair(3, 1)};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:92:13: error: 'board' was not declared in this scope
   92 |     REQUIRE(board.can_attack());
      |             ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:92:13: error: 'board' was not declared in this scope
   92 |     REQUIRE(board.can_attack());
      |             ^~~~~
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/queen_attack_test.cpp:97:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
   97 |     const queen_attack::chess_board board{std::make_pair(2, 2), std::make_pair(1, 1)};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:99:13: error: 'board' was not declared in this scope
   99 |     REQUIRE(board.can_attack());
      |             ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:99:13: error: 'board' was not declared in this scope
   99 |     REQUIRE(board.can_attack());
      |             ^~~~~
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/queen_attack_test.cpp:104:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
  104 |     const queen_attack::chess_board board{std::make_pair(1, 7), std::make_pair(0, 6)};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:106:13: error: 'board' was not declared in this scope
  106 |     REQUIRE(board.can_attack());
      |             ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:106:13: error: 'board' was not declared in this scope
  106 |     REQUIRE(board.can_attack());
      |             ^~~~~
/testbed/queen_attack_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/queen_attack_test.cpp:111:25: error: 'chess_board' in namespace 'queen_attack' does not name a type
  111 |     const queen_attack::chess_board board{std::make_pair(4, 1), std::make_pair(2, 5)};
      |                         ^~~~~~~~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:113:19: error: 'board' was not declared in this scope
  113 |     REQUIRE_FALSE(board.can_attack());
      |                   ^~~~~
In file included from /testbed/queen_attack_test.cpp:5:
/testbed/queen_attack_test.cpp:113:19: error: 'board' was not declared in this scope
  113 |     REQUIRE_FALSE(board.can_attack());
      |                   ^~~~~
make[2]: *** [CMakeFiles/queen-attack.dir/build.make:76: CMakeFiles/queen-attack.dir/queen_attack_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/queen-attack.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
