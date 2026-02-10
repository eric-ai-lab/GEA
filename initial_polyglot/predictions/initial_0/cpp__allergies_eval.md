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
[ 25%] Building CXX object CMakeFiles/allergies.dir/allergies_test.cpp.o
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/allergies_test.cpp:9:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
    9 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("eggs"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:9:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
    9 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("eggs"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:9:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
    9 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("eggs"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/allergies_test.cpp:15:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   15 |         REQUIRE(true == allergies::allergy_test(1).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:15:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   15 |         REQUIRE(true == allergies::allergy_test(1).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:15:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   15 |         REQUIRE(true == allergies::allergy_test(1).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/allergies_test.cpp:19:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   19 |         REQUIRE(true == allergies::allergy_test(3).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:19:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   19 |         REQUIRE(true == allergies::allergy_test(3).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:19:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   19 |         REQUIRE(true == allergies::allergy_test(3).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/allergies_test.cpp:23:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   23 |         REQUIRE(false == allergies::allergy_test(2).is_allergic_to("eggs"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:23:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   23 |         REQUIRE(false == allergies::allergy_test(2).is_allergic_to("eggs"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:23:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   23 |         REQUIRE(false == allergies::allergy_test(2).is_allergic_to("eggs"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/allergies_test.cpp:27:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   27 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:27:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   27 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:27:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   27 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("eggs"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/allergies_test.cpp:31:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   31 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("peanuts"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:31:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   31 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("peanuts"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:31:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   31 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("peanuts"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/allergies_test.cpp:35:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   35 |         REQUIRE(true == allergies::allergy_test(2).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:35:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   35 |         REQUIRE(true == allergies::allergy_test(2).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:35:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   35 |         REQUIRE(true == allergies::allergy_test(2).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/allergies_test.cpp:39:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   39 |         REQUIRE(true == allergies::allergy_test(7).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:39:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   39 |         REQUIRE(true == allergies::allergy_test(7).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:39:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   39 |         REQUIRE(true == allergies::allergy_test(7).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/allergies_test.cpp:43:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   43 |         REQUIRE(false == allergies::allergy_test(5).is_allergic_to("peanuts"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:43:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   43 |         REQUIRE(false == allergies::allergy_test(5).is_allergic_to("peanuts"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:43:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   43 |         REQUIRE(false == allergies::allergy_test(5).is_allergic_to("peanuts"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/allergies_test.cpp:47:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   47 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:47:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   47 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:47:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   47 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("peanuts"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/allergies_test.cpp:51:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   51 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("shellfish"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:51:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   51 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("shellfish"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:51:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   51 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("shellfish"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/allergies_test.cpp:55:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   55 |         REQUIRE(true == allergies::allergy_test(4).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:55:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   55 |         REQUIRE(true == allergies::allergy_test(4).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:55:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   55 |         REQUIRE(true == allergies::allergy_test(4).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/allergies_test.cpp:59:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   59 |         REQUIRE(true == allergies::allergy_test(14).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:59:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   59 |         REQUIRE(true == allergies::allergy_test(14).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:59:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   59 |         REQUIRE(true == allergies::allergy_test(14).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/allergies_test.cpp:63:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   63 |         REQUIRE(false == allergies::allergy_test(10).is_allergic_to("shellfish"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:63:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   63 |         REQUIRE(false == allergies::allergy_test(10).is_allergic_to("shellfish"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:63:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   63 |         REQUIRE(false == allergies::allergy_test(10).is_allergic_to("shellfish"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/allergies_test.cpp:67:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   67 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:67:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   67 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:67:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   67 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("shellfish"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/allergies_test.cpp:71:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   71 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("strawberries"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:71:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   71 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("strawberries"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:71:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   71 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("strawberries"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/allergies_test.cpp:75:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   75 |         REQUIRE(true == allergies::allergy_test(8).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:75:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   75 |         REQUIRE(true == allergies::allergy_test(8).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:75:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   75 |         REQUIRE(true == allergies::allergy_test(8).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____34()':
/testbed/allergies_test.cpp:79:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   79 |         REQUIRE(true == allergies::allergy_test(28).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:79:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   79 |         REQUIRE(true == allergies::allergy_test(28).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:79:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   79 |         REQUIRE(true == allergies::allergy_test(28).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____36()':
/testbed/allergies_test.cpp:83:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   83 |         REQUIRE(false == allergies::allergy_test(20).is_allergic_to("strawberries"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:83:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   83 |         REQUIRE(false == allergies::allergy_test(20).is_allergic_to("strawberries"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:83:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   83 |         REQUIRE(false == allergies::allergy_test(20).is_allergic_to("strawberries"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____38()':
/testbed/allergies_test.cpp:87:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   87 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:87:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   87 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:87:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   87 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("strawberries"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____40()':
/testbed/allergies_test.cpp:91:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   91 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("tomatoes"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:91:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   91 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("tomatoes"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:91:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   91 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("tomatoes"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____42()':
/testbed/allergies_test.cpp:95:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   95 |         REQUIRE(true == allergies::allergy_test(16).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:95:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   95 |         REQUIRE(true == allergies::allergy_test(16).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:95:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   95 |         REQUIRE(true == allergies::allergy_test(16).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____44()':
/testbed/allergies_test.cpp:99:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   99 |         REQUIRE(true == allergies::allergy_test(56).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:99:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   99 |         REQUIRE(true == allergies::allergy_test(56).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:99:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
   99 |         REQUIRE(true == allergies::allergy_test(56).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____46()':
/testbed/allergies_test.cpp:103:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  103 |         REQUIRE(false == allergies::allergy_test(40).is_allergic_to("tomatoes"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:103:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  103 |         REQUIRE(false == allergies::allergy_test(40).is_allergic_to("tomatoes"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:103:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  103 |         REQUIRE(false == allergies::allergy_test(40).is_allergic_to("tomatoes"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____48()':
/testbed/allergies_test.cpp:107:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  107 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:107:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  107 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:107:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  107 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("tomatoes"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____50()':
/testbed/allergies_test.cpp:111:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  111 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("chocolate"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:111:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  111 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("chocolate"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:111:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  111 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("chocolate"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____52()':
/testbed/allergies_test.cpp:115:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  115 |         REQUIRE(true == allergies::allergy_test(32).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:115:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  115 |         REQUIRE(true == allergies::allergy_test(32).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:115:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  115 |         REQUIRE(true == allergies::allergy_test(32).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____54()':
/testbed/allergies_test.cpp:119:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  119 |         REQUIRE(true == allergies::allergy_test(112).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:119:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  119 |         REQUIRE(true == allergies::allergy_test(112).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:119:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  119 |         REQUIRE(true == allergies::allergy_test(112).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____56()':
/testbed/allergies_test.cpp:123:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  123 |         REQUIRE(false == allergies::allergy_test(80).is_allergic_to("chocolate"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:123:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  123 |         REQUIRE(false == allergies::allergy_test(80).is_allergic_to("chocolate"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:123:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  123 |         REQUIRE(false == allergies::allergy_test(80).is_allergic_to("chocolate"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____58()':
/testbed/allergies_test.cpp:127:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  127 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:127:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  127 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:127:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  127 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("chocolate"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____60()':
/testbed/allergies_test.cpp:131:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  131 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("pollen"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:131:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  131 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("pollen"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:131:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  131 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("pollen"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____62()':
/testbed/allergies_test.cpp:135:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  135 |         REQUIRE(true == allergies::allergy_test(64).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:135:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  135 |         REQUIRE(true == allergies::allergy_test(64).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:135:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  135 |         REQUIRE(true == allergies::allergy_test(64).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____64()':
/testbed/allergies_test.cpp:139:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  139 |         REQUIRE(true == allergies::allergy_test(224).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:139:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  139 |         REQUIRE(true == allergies::allergy_test(224).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:139:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  139 |         REQUIRE(true == allergies::allergy_test(224).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____66()':
/testbed/allergies_test.cpp:143:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  143 |         REQUIRE(false == allergies::allergy_test(160).is_allergic_to("pollen"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:143:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  143 |         REQUIRE(false == allergies::allergy_test(160).is_allergic_to("pollen"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:143:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  143 |         REQUIRE(false == allergies::allergy_test(160).is_allergic_to("pollen"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____68()':
/testbed/allergies_test.cpp:147:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  147 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:147:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  147 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:147:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  147 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("pollen"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____70()':
/testbed/allergies_test.cpp:151:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  151 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("cats"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:151:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  151 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("cats"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:151:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  151 |         REQUIRE(false == allergies::allergy_test(0).is_allergic_to("cats"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____72()':
/testbed/allergies_test.cpp:155:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  155 |         REQUIRE(true == allergies::allergy_test(128).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:155:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  155 |         REQUIRE(true == allergies::allergy_test(128).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:155:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  155 |         REQUIRE(true == allergies::allergy_test(128).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____74()':
/testbed/allergies_test.cpp:159:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  159 |         REQUIRE(true == allergies::allergy_test(192).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:159:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  159 |         REQUIRE(true == allergies::allergy_test(192).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:159:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  159 |         REQUIRE(true == allergies::allergy_test(192).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____76()':
/testbed/allergies_test.cpp:163:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  163 |         REQUIRE(false == allergies::allergy_test(64).is_allergic_to("cats"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:163:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  163 |         REQUIRE(false == allergies::allergy_test(64).is_allergic_to("cats"));
      |                                     ^~~~~~~~~~~~
/testbed/allergies_test.cpp:163:37: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  163 |         REQUIRE(false == allergies::allergy_test(64).is_allergic_to("cats"));
      |                                     ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____78()':
/testbed/allergies_test.cpp:167:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  167 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:167:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  167 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp:167:36: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  167 |         REQUIRE(true == allergies::allergy_test(255).is_allergic_to("cats"));
      |                                    ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____80()':
/testbed/allergies_test.cpp:171:14: error: 'unordered_set' is not a member of 'std'
  171 |         std::unordered_set<std::string> expected ={};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:6:1: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
    5 | #include "test/catch.hpp"
  +++ |+#include <unordered_set>
    6 | #endif
/testbed/allergies_test.cpp:171:39: error: expected primary-expression before '>' token
  171 |         std::unordered_set<std::string> expected ={};
      |                                       ^
/testbed/allergies_test.cpp:171:41: error: 'expected' was not declared in this scope
  171 |         std::unordered_set<std::string> expected ={};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:172:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  172 |         REQUIRE(expected == allergies::allergy_test(0).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:172:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  172 |         REQUIRE(expected == allergies::allergy_test(0).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:172:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  172 |         REQUIRE(expected == allergies::allergy_test(0).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____82()':
/testbed/allergies_test.cpp:176:14: error: 'unordered_set' is not a member of 'std'
  176 |         std::unordered_set<std::string> expected ={"eggs"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:176:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:176:39: error: expected primary-expression before '>' token
  176 |         std::unordered_set<std::string> expected ={"eggs"};
      |                                       ^
/testbed/allergies_test.cpp:176:41: error: 'expected' was not declared in this scope
  176 |         std::unordered_set<std::string> expected ={"eggs"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:177:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  177 |         REQUIRE(expected == allergies::allergy_test(1).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:177:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  177 |         REQUIRE(expected == allergies::allergy_test(1).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:177:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  177 |         REQUIRE(expected == allergies::allergy_test(1).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____84()':
/testbed/allergies_test.cpp:181:14: error: 'unordered_set' is not a member of 'std'
  181 |         std::unordered_set<std::string> expected ={"peanuts"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:181:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:181:39: error: expected primary-expression before '>' token
  181 |         std::unordered_set<std::string> expected ={"peanuts"};
      |                                       ^
/testbed/allergies_test.cpp:181:41: error: 'expected' was not declared in this scope
  181 |         std::unordered_set<std::string> expected ={"peanuts"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:182:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  182 |         REQUIRE(expected == allergies::allergy_test(2).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:182:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  182 |         REQUIRE(expected == allergies::allergy_test(2).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:182:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  182 |         REQUIRE(expected == allergies::allergy_test(2).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____86()':
/testbed/allergies_test.cpp:186:14: error: 'unordered_set' is not a member of 'std'
  186 |         std::unordered_set<std::string> expected ={"strawberries"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:186:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:186:39: error: expected primary-expression before '>' token
  186 |         std::unordered_set<std::string> expected ={"strawberries"};
      |                                       ^
/testbed/allergies_test.cpp:186:41: error: 'expected' was not declared in this scope
  186 |         std::unordered_set<std::string> expected ={"strawberries"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:187:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  187 |         REQUIRE(expected == allergies::allergy_test(8).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:187:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  187 |         REQUIRE(expected == allergies::allergy_test(8).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:187:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  187 |         REQUIRE(expected == allergies::allergy_test(8).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____88()':
/testbed/allergies_test.cpp:191:14: error: 'unordered_set' is not a member of 'std'
  191 |         std::unordered_set<std::string> expected ={"eggs", "peanuts"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:191:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:191:39: error: expected primary-expression before '>' token
  191 |         std::unordered_set<std::string> expected ={"eggs", "peanuts"};
      |                                       ^
/testbed/allergies_test.cpp:191:41: error: 'expected' was not declared in this scope
  191 |         std::unordered_set<std::string> expected ={"eggs", "peanuts"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:192:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  192 |         REQUIRE(expected == allergies::allergy_test(3).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:192:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  192 |         REQUIRE(expected == allergies::allergy_test(3).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:192:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  192 |         REQUIRE(expected == allergies::allergy_test(3).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____90()':
/testbed/allergies_test.cpp:196:14: error: 'unordered_set' is not a member of 'std'
  196 |         std::unordered_set<std::string> expected ={"eggs", "shellfish"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:196:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:196:39: error: expected primary-expression before '>' token
  196 |         std::unordered_set<std::string> expected ={"eggs", "shellfish"};
      |                                       ^
/testbed/allergies_test.cpp:196:41: error: 'expected' was not declared in this scope
  196 |         std::unordered_set<std::string> expected ={"eggs", "shellfish"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:197:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  197 |         REQUIRE(expected == allergies::allergy_test(5).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:197:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  197 |         REQUIRE(expected == allergies::allergy_test(5).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:197:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  197 |         REQUIRE(expected == allergies::allergy_test(5).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____92()':
/testbed/allergies_test.cpp:201:14: error: 'unordered_set' is not a member of 'std'
  201 |         std::unordered_set<std::string> expected ={"strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:201:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:201:39: error: expected primary-expression before '>' token
  201 |         std::unordered_set<std::string> expected ={"strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |                                       ^
/testbed/allergies_test.cpp:201:41: error: 'expected' was not declared in this scope
  201 |         std::unordered_set<std::string> expected ={"strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:202:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  202 |         REQUIRE(expected == allergies::allergy_test(248).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:202:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  202 |         REQUIRE(expected == allergies::allergy_test(248).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:202:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  202 |         REQUIRE(expected == allergies::allergy_test(248).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____94()':
/testbed/allergies_test.cpp:206:14: error: 'unordered_set' is not a member of 'std'
  206 |         std::unordered_set<std::string> expected ={"eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:206:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:206:39: error: expected primary-expression before '>' token
  206 |         std::unordered_set<std::string> expected ={"eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |                                       ^
/testbed/allergies_test.cpp:206:41: error: 'expected' was not declared in this scope
  206 |         std::unordered_set<std::string> expected ={"eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:207:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  207 |         REQUIRE(expected == allergies::allergy_test(255).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:207:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  207 |         REQUIRE(expected == allergies::allergy_test(255).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:207:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  207 |         REQUIRE(expected == allergies::allergy_test(255).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____96()':
/testbed/allergies_test.cpp:211:14: error: 'unordered_set' is not a member of 'std'
  211 |         std::unordered_set<std::string> expected ={"eggs", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:211:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:211:39: error: expected primary-expression before '>' token
  211 |         std::unordered_set<std::string> expected ={"eggs", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |                                       ^
/testbed/allergies_test.cpp:211:41: error: 'expected' was not declared in this scope
  211 |         std::unordered_set<std::string> expected ={"eggs", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:212:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  212 |         REQUIRE(expected == allergies::allergy_test(509).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:212:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  212 |         REQUIRE(expected == allergies::allergy_test(509).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:212:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  212 |         REQUIRE(expected == allergies::allergy_test(509).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____98()':
/testbed/allergies_test.cpp:216:14: error: 'unordered_set' is not a member of 'std'
  216 |         std::unordered_set<std::string> expected ={"eggs"};
      |              ^~~~~~~~~~~~~
/testbed/allergies_test.cpp:216:14: note: 'std::unordered_set' is defined in header '<unordered_set>'; did you forget to '#include <unordered_set>'?
/testbed/allergies_test.cpp:216:39: error: expected primary-expression before '>' token
  216 |         std::unordered_set<std::string> expected ={"eggs"};
      |                                       ^
/testbed/allergies_test.cpp:216:41: error: 'expected' was not declared in this scope
  216 |         std::unordered_set<std::string> expected ={"eggs"};
      |                                         ^~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:217:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  217 |         REQUIRE(expected == allergies::allergy_test(257).get_allergies());
      |                                        ^~~~~~~~~~~~
In file included from /testbed/allergies_test.cpp:5:
/testbed/allergies_test.cpp:217:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  217 |         REQUIRE(expected == allergies::allergy_test(257).get_allergies());
      |                                        ^~~~~~~~~~~~
/testbed/allergies_test.cpp:217:40: error: 'allergy_test' is not a member of 'allergies'; did you mean 'Allergies'?
  217 |         REQUIRE(expected == allergies::allergy_test(257).get_allergies());
      |                                        ^~~~~~~~~~~~
make[2]: *** [CMakeFiles/allergies.dir/build.make:76: CMakeFiles/allergies.dir/allergies_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/allergies.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
