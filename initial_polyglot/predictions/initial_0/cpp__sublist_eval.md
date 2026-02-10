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
[ 25%] Building CXX object CMakeFiles/sublist.dir/sublist_test.cpp.o
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:23:30: error: 'List_comparison' is not a member of 'sublist'
   23 | CATCH_REGISTER_ENUM(sublist::List_comparison,
      |                              ^~~~~~~~~~~~~~~
/testbed/sublist_test.cpp:23:1: error: template argument 1 is invalid
   23 | CATCH_REGISTER_ENUM(sublist::List_comparison,
      | ^~~~~~~~~~~~~~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/sublist_test.cpp:30:18: error: 'List_comparison' is not a member of 'sublist'
   30 |         sublist::List_comparison expected = sublist::List_comparison::equal;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:31:17: error: 'expected' was not declared in this scope
   31 |         REQUIRE(expected == sublist::sublist({}, {}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:31:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   31 |         REQUIRE(expected == sublist::sublist({}, {}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:31:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   31 |         REQUIRE(expected == sublist::sublist({}, {}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:31:17: error: 'expected' was not declared in this scope
   31 |         REQUIRE(expected == sublist::sublist({}, {}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:31:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   31 |         REQUIRE(expected == sublist::sublist({}, {}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/sublist_test.cpp:37:18: error: 'List_comparison' is not a member of 'sublist'
   37 |         sublist::List_comparison expected = sublist::List_comparison::sublist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:38:17: error: 'expected' was not declared in this scope
   38 |         REQUIRE(expected == sublist::sublist({}, {1, 2, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:38:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   38 |         REQUIRE(expected == sublist::sublist({}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:38:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   38 |         REQUIRE(expected == sublist::sublist({}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:38:17: error: 'expected' was not declared in this scope
   38 |         REQUIRE(expected == sublist::sublist({}, {1, 2, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:38:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   38 |         REQUIRE(expected == sublist::sublist({}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/sublist_test.cpp:42:18: error: 'List_comparison' is not a member of 'sublist'
   42 |         sublist::List_comparison expected = sublist::List_comparison::superlist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:43:17: error: 'expected' was not declared in this scope
   43 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:43:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   43 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:43:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   43 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:43:17: error: 'expected' was not declared in this scope
   43 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:43:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   43 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/sublist_test.cpp:47:18: error: 'List_comparison' is not a member of 'sublist'
   47 |         sublist::List_comparison expected = sublist::List_comparison::equal;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:48:17: error: 'expected' was not declared in this scope
   48 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 2, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:48:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   48 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:48:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   48 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:48:17: error: 'expected' was not declared in this scope
   48 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 2, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:48:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   48 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/sublist_test.cpp:52:18: error: 'List_comparison' is not a member of 'sublist'
   52 |         sublist::List_comparison expected = sublist::List_comparison::unequal;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:53:17: error: 'expected' was not declared in this scope
   53 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {2, 3, 4}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:53:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   53 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {2, 3, 4}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:53:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   53 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {2, 3, 4}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:53:17: error: 'expected' was not declared in this scope
   53 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {2, 3, 4}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:53:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   53 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {2, 3, 4}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/sublist_test.cpp:57:18: error: 'List_comparison' is not a member of 'sublist'
   57 |         sublist::List_comparison expected = sublist::List_comparison::sublist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:58:17: error: 'expected' was not declared in this scope
   58 |         REQUIRE(expected == sublist::sublist({1, 2, 5}, {0, 1, 2, 3, 1, 2, 5, 6}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:58:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   58 |         REQUIRE(expected == sublist::sublist({1, 2, 5}, {0, 1, 2, 3, 1, 2, 5, 6}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:58:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   58 |         REQUIRE(expected == sublist::sublist({1, 2, 5}, {0, 1, 2, 3, 1, 2, 5, 6}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:58:17: error: 'expected' was not declared in this scope
   58 |         REQUIRE(expected == sublist::sublist({1, 2, 5}, {0, 1, 2, 3, 1, 2, 5, 6}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:58:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   58 |         REQUIRE(expected == sublist::sublist({1, 2, 5}, {0, 1, 2, 3, 1, 2, 5, 6}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/sublist_test.cpp:62:18: error: 'List_comparison' is not a member of 'sublist'
   62 |         sublist::List_comparison expected = sublist::List_comparison::sublist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:63:17: error: 'expected' was not declared in this scope
   63 |         REQUIRE(expected == sublist::sublist({1, 1, 2}, {0, 1, 1, 1, 2, 1, 2}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:63:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   63 |         REQUIRE(expected == sublist::sublist({1, 1, 2}, {0, 1, 1, 1, 2, 1, 2}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:63:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   63 |         REQUIRE(expected == sublist::sublist({1, 1, 2}, {0, 1, 1, 1, 2, 1, 2}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:63:17: error: 'expected' was not declared in this scope
   63 |         REQUIRE(expected == sublist::sublist({1, 1, 2}, {0, 1, 1, 1, 2, 1, 2}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:63:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   63 |         REQUIRE(expected == sublist::sublist({1, 1, 2}, {0, 1, 1, 1, 2, 1, 2}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/sublist_test.cpp:67:18: error: 'List_comparison' is not a member of 'sublist'
   67 |         sublist::List_comparison expected = sublist::List_comparison::sublist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:68:17: error: 'expected' was not declared in this scope
   68 |         REQUIRE(expected == sublist::sublist({0, 1, 2}, {0, 1, 2, 3, 4, 5}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:68:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   68 |         REQUIRE(expected == sublist::sublist({0, 1, 2}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:68:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   68 |         REQUIRE(expected == sublist::sublist({0, 1, 2}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:68:17: error: 'expected' was not declared in this scope
   68 |         REQUIRE(expected == sublist::sublist({0, 1, 2}, {0, 1, 2, 3, 4, 5}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:68:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   68 |         REQUIRE(expected == sublist::sublist({0, 1, 2}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/sublist_test.cpp:72:18: error: 'List_comparison' is not a member of 'sublist'
   72 |         sublist::List_comparison expected = sublist::List_comparison::sublist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:73:17: error: 'expected' was not declared in this scope
   73 |         REQUIRE(expected == sublist::sublist({2, 3, 4}, {0, 1, 2, 3, 4, 5}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:73:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   73 |         REQUIRE(expected == sublist::sublist({2, 3, 4}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:73:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   73 |         REQUIRE(expected == sublist::sublist({2, 3, 4}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:73:17: error: 'expected' was not declared in this scope
   73 |         REQUIRE(expected == sublist::sublist({2, 3, 4}, {0, 1, 2, 3, 4, 5}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:73:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   73 |         REQUIRE(expected == sublist::sublist({2, 3, 4}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/sublist_test.cpp:77:18: error: 'List_comparison' is not a member of 'sublist'
   77 |         sublist::List_comparison expected = sublist::List_comparison::sublist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:78:17: error: 'expected' was not declared in this scope
   78 |         REQUIRE(expected == sublist::sublist({3, 4, 5}, {0, 1, 2, 3, 4, 5}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:78:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   78 |         REQUIRE(expected == sublist::sublist({3, 4, 5}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:78:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   78 |         REQUIRE(expected == sublist::sublist({3, 4, 5}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:78:17: error: 'expected' was not declared in this scope
   78 |         REQUIRE(expected == sublist::sublist({3, 4, 5}, {0, 1, 2, 3, 4, 5}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:78:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   78 |         REQUIRE(expected == sublist::sublist({3, 4, 5}, {0, 1, 2, 3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/sublist_test.cpp:82:18: error: 'List_comparison' is not a member of 'sublist'
   82 |         sublist::List_comparison expected = sublist::List_comparison::superlist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:83:17: error: 'expected' was not declared in this scope
   83 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {0, 1, 2}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:83:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   83 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {0, 1, 2}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:83:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   83 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {0, 1, 2}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:83:17: error: 'expected' was not declared in this scope
   83 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {0, 1, 2}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:83:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   83 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {0, 1, 2}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/sublist_test.cpp:87:18: error: 'List_comparison' is not a member of 'sublist'
   87 |         sublist::List_comparison expected = sublist::List_comparison::superlist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:88:17: error: 'expected' was not declared in this scope
   88 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {2, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:88:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   88 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:88:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   88 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:88:17: error: 'expected' was not declared in this scope
   88 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {2, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:88:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   88 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/sublist_test.cpp:92:18: error: 'List_comparison' is not a member of 'sublist'
   92 |         sublist::List_comparison expected = sublist::List_comparison::superlist;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:93:17: error: 'expected' was not declared in this scope
   93 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {3, 4, 5}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:93:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   93 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:93:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   93 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:93:17: error: 'expected' was not declared in this scope
   93 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {3, 4, 5}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:93:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   93 |         REQUIRE(expected == sublist::sublist({0, 1, 2, 3, 4, 5}, {3, 4, 5}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/sublist_test.cpp:97:18: error: 'List_comparison' is not a member of 'sublist'
   97 |         sublist::List_comparison expected = sublist::List_comparison::unequal;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:98:17: error: 'expected' was not declared in this scope
   98 |         REQUIRE(expected == sublist::sublist({1, 3}, {1, 2, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:98:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   98 |         REQUIRE(expected == sublist::sublist({1, 3}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:98:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   98 |         REQUIRE(expected == sublist::sublist({1, 3}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:98:17: error: 'expected' was not declared in this scope
   98 |         REQUIRE(expected == sublist::sublist({1, 3}, {1, 2, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:98:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
   98 |         REQUIRE(expected == sublist::sublist({1, 3}, {1, 2, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/sublist_test.cpp:102:18: error: 'List_comparison' is not a member of 'sublist'
  102 |         sublist::List_comparison expected = sublist::List_comparison::unequal;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:103:17: error: 'expected' was not declared in this scope
  103 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:103:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  103 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:103:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  103 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:103:17: error: 'expected' was not declared in this scope
  103 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 3}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:103:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  103 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {1, 3}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/sublist_test.cpp:107:18: error: 'List_comparison' is not a member of 'sublist'
  107 |         sublist::List_comparison expected = sublist::List_comparison::unequal;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:108:17: error: 'expected' was not declared in this scope
  108 |         REQUIRE(expected == sublist::sublist({1, 2}, {1, 22}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:108:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  108 |         REQUIRE(expected == sublist::sublist({1, 2}, {1, 22}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:108:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  108 |         REQUIRE(expected == sublist::sublist({1, 2}, {1, 22}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:108:17: error: 'expected' was not declared in this scope
  108 |         REQUIRE(expected == sublist::sublist({1, 2}, {1, 22}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:108:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  108 |         REQUIRE(expected == sublist::sublist({1, 2}, {1, 22}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/sublist_test.cpp:112:18: error: 'List_comparison' is not a member of 'sublist'
  112 |         sublist::List_comparison expected = sublist::List_comparison::unequal;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:113:17: error: 'expected' was not declared in this scope
  113 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {3, 2, 1}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:113:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  113 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {3, 2, 1}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:113:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  113 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {3, 2, 1}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:113:17: error: 'expected' was not declared in this scope
  113 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {3, 2, 1}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:113:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  113 |         REQUIRE(expected == sublist::sublist({1, 2, 3}, {3, 2, 1}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
/testbed/sublist_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____34()':
/testbed/sublist_test.cpp:117:18: error: 'List_comparison' is not a member of 'sublist'
  117 |         sublist::List_comparison expected = sublist::List_comparison::unequal;
      |                  ^~~~~~~~~~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:118:17: error: 'expected' was not declared in this scope
  118 |         REQUIRE(expected == sublist::sublist({1, 0, 1}, {10, 1}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:118:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  118 |         REQUIRE(expected == sublist::sublist({1, 0, 1}, {10, 1}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:118:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  118 |         REQUIRE(expected == sublist::sublist({1, 0, 1}, {10, 1}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
In file included from /testbed/sublist_test.cpp:5:
/testbed/sublist_test.cpp:118:17: error: 'expected' was not declared in this scope
  118 |         REQUIRE(expected == sublist::sublist({1, 0, 1}, {10, 1}));
      |                 ^~~~~~~~
/testbed/sublist_test.cpp:118:38: error: 'sublist' is not a member of 'sublist'; did you mean 'sublist'?
  118 |         REQUIRE(expected == sublist::sublist({1, 0, 1}, {10, 1}));
      |                                      ^~~~~~~
In file included from /testbed/sublist_test.cpp:1:
/testbed/sublist.h:6:11: note: 'sublist' declared here
    6 | namespace sublist {
      |           ^~~~~~~
make[2]: *** [CMakeFiles/sublist.dir/build.make:76: CMakeFiles/sublist.dir/sublist_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/sublist.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
