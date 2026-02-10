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
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Configuring done
-- Generating done
-- Build files have been written to: /testbed/build
+ make
[ 25%] Building CXX object CMakeFiles/bank-account.dir/bank_account_test.cpp.o
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/bank_account_test.cpp:14:28: error: expression cannot be used as a function
   14 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:14:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   14 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:14:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   14 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:14:28: error: expression cannot be used as a function
   14 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:14:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   14 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:14:28: error: expression cannot be used as a function
   14 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/bank_account_test.cpp:22:28: error: expression cannot be used as a function
   22 |     REQUIRE(account.balance() == 100);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:22:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   22 |     REQUIRE(account.balance() == 100);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:22:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   22 |     REQUIRE(account.balance() == 100);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:22:28: error: expression cannot be used as a function
   22 |     REQUIRE(account.balance() == 100);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:22:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   22 |     REQUIRE(account.balance() == 100);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:22:28: error: expression cannot be used as a function
   22 |     REQUIRE(account.balance() == 100);
      |             ~~~~~~~~~~~~~~~^~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/bank_account_test.cpp:30:28: error: expression cannot be used as a function
   30 |     REQUIRE(account.balance() == 150);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:30:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   30 |     REQUIRE(account.balance() == 150);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:30:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   30 |     REQUIRE(account.balance() == 150);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:30:28: error: expression cannot be used as a function
   30 |     REQUIRE(account.balance() == 150);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:30:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   30 |     REQUIRE(account.balance() == 150);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:30:28: error: expression cannot be used as a function
   30 |     REQUIRE(account.balance() == 150);
      |             ~~~~~~~~~~~~~~~^~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/bank_account_test.cpp:38:28: error: expression cannot be used as a function
   38 |     REQUIRE(account.balance() == 25);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:38:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   38 |     REQUIRE(account.balance() == 25);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:38:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   38 |     REQUIRE(account.balance() == 25);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:38:28: error: expression cannot be used as a function
   38 |     REQUIRE(account.balance() == 25);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:38:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   38 |     REQUIRE(account.balance() == 25);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:38:28: error: expression cannot be used as a function
   38 |     REQUIRE(account.balance() == 25);
      |             ~~~~~~~~~~~~~~~^~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/bank_account_test.cpp:47:28: error: expression cannot be used as a function
   47 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:47:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   47 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:47:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   47 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:47:28: error: expression cannot be used as a function
   47 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:47:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   47 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:47:28: error: expression cannot be used as a function
   47 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/bank_account_test.cpp:58:28: error: expression cannot be used as a function
   58 |     REQUIRE(account.balance() == 20);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:58:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   58 |     REQUIRE(account.balance() == 20);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:58:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   58 |     REQUIRE(account.balance() == 20);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:58:28: error: expression cannot be used as a function
   58 |     REQUIRE(account.balance() == 20);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:58:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   58 |     REQUIRE(account.balance() == 20);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:58:28: error: expression cannot be used as a function
   58 |     REQUIRE(account.balance() == 20);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/bank_account_test.cpp:66:31: error: 'int Bankaccount::Bankaccount::balance' is private within this context
   66 |     REQUIRE_THROWS_AS(account.balance(), std::runtime_error);
      |                               ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:66:38: error: expression cannot be used as a function
   66 |     REQUIRE_THROWS_AS(account.balance(), std::runtime_error);
      |                       ~~~~~~~~~~~~~~~^~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/bank_account_test.cpp:111:28: error: expression cannot be used as a function
  111 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:111:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
  111 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:111:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
  111 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:111:28: error: expression cannot be used as a function
  111 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:111:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
  111 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:111:28: error: expression cannot be used as a function
  111 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/bank_account_test.cpp:155:28: error: expression cannot be used as a function
  155 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:155:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
  155 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:155:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
  155 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:155:28: error: expression cannot be used as a function
  155 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
/testbed/bank_account_test.cpp:155:21: error: 'int Bankaccount::Bankaccount::balance' is private within this context
  155 |     REQUIRE(account.balance() == 0);
      |                     ^~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:37:9: note: declared private here
   37 |     int balance;
      |         ^~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:155:28: error: expression cannot be used as a function
  155 |     REQUIRE(account.balance() == 0);
      |             ~~~~~~~~~~~~~~~^~
make[2]: *** [CMakeFiles/bank-account.dir/build.make:76: CMakeFiles/bank-account.dir/bank_account_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/bank-account.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
