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
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/bank_account_test.cpp:12:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   12 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:13:5: error: 'account' was not declared in this scope
   13 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/bank_account_test.cpp:19:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   19 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:20:5: error: 'account' was not declared in this scope
   20 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/bank_account_test.cpp:26:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   26 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:27:5: error: 'account' was not declared in this scope
   27 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/bank_account_test.cpp:34:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   34 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:35:5: error: 'account' was not declared in this scope
   35 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/bank_account_test.cpp:42:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   42 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:43:5: error: 'account' was not declared in this scope
   43 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/bank_account_test.cpp:51:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   51 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:52:5: error: 'account' was not declared in this scope
   52 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/bank_account_test.cpp:62:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   62 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:63:5: error: 'account' was not declared in this scope
   63 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/bank_account_test.cpp:70:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   70 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:71:5: error: 'account' was not declared in this scope
   71 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/bank_account_test.cpp:78:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   78 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:79:23: error: 'account' was not declared in this scope
   79 |     REQUIRE_THROWS_AS(account.deposit(50), std::runtime_error);
      |                       ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/bank_account_test.cpp:83:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   83 |     Bankaccount::Bankaccount account{};
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:84:5: error: 'account' was not declared in this scope
   84 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/bank_account_test.cpp:91:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   91 |     Bankaccount::Bankaccount account;
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:5:
/testbed/bank_account_test.cpp:93:23: error: 'account' was not declared in this scope
   93 |     REQUIRE_THROWS_AS(account.close(), std::runtime_error);
      |                       ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/bank_account_test.cpp:97:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
   97 |     Bankaccount::Bankaccount account;
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:98:5: error: 'account' was not declared in this scope
   98 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/bank_account_test.cpp:105:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
  105 |     Bankaccount::Bankaccount account;
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:106:5: error: 'account' was not declared in this scope
  106 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/bank_account_test.cpp:115:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
  115 |     Bankaccount::Bankaccount account;
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:116:5: error: 'account' was not declared in this scope
  116 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/bank_account_test.cpp:123:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
  123 |     Bankaccount::Bankaccount account;
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:124:5: error: 'account' was not declared in this scope
  124 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/bank_account_test.cpp:130:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
  130 |     Bankaccount::Bankaccount account;
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:131:5: error: 'account' was not declared in this scope
  131 |     account.open();
      |     ^~~~~~~
/testbed/bank_account_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/bank_account_test.cpp:137:18: error: 'Bankaccount' is not a member of 'Bankaccount'; did you mean 'Bankaccount'?
  137 |     Bankaccount::Bankaccount account;
      |                  ^~~~~~~~~~~
In file included from /testbed/bank_account_test.cpp:1:
/testbed/bank_account.h:7:11: note: 'Bankaccount' declared here
    7 | namespace Bankaccount {
      |           ^~~~~~~~~~~
/testbed/bank_account_test.cpp:138:5: error: 'account' was not declared in this scope
  138 |     account.open();
      |     ^~~~~~~
make[2]: *** [CMakeFiles/bank-account.dir/build.make:76: CMakeFiles/bank-account.dir/bank_account_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/bank-account.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
