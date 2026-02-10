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
[ 25%] Building CXX object CMakeFiles/kindergarten-garden.dir/kindergarten_garden_test.cpp.o
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:9:42: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
    9 | CATCH_REGISTER_ENUM(kindergarten_garden::Plants,
      |                                          ^~~~~~
/testbed/kindergarten_garden_test.cpp:9:1: error: template argument 1 is invalid
    9 | CATCH_REGISTER_ENUM(kindergarten_garden::Plants,
      | ^~~~~~~~~~~~~~~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/kindergarten_garden_test.cpp:16:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   16 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:16:44: error: template argument 1 is invalid
   16 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:16:76: error: 'kindergarten_garden::Plants' has not been declared
   16 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:16:115: error: 'kindergarten_garden::Plants' has not been declared
   16 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                                                                                   ^~~~~~
/testbed/kindergarten_garden_test.cpp:16:152: error: 'kindergarten_garden::Plants' has not been declared
   16 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                                                                                                                        ^~~~~~
/testbed/kindergarten_garden_test.cpp:16:188: error: 'kindergarten_garden::Plants' has not been declared
   16 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                                                                                                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:16:46: error: scalar object 'expected' requires one element in initializer
   16 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:17:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   17 |   REQUIRE(kindergarten_garden::plants("RC\nGG", "Alice") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:17:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   17 |   REQUIRE(kindergarten_garden::plants("RC\nGG", "Alice") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:17:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   17 |   REQUIRE(kindergarten_garden::plants("RC\nGG", "Alice") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/kindergarten_garden_test.cpp:23:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   23 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:23:44: error: template argument 1 is invalid
   23 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:23:76: error: 'kindergarten_garden::Plants' has not been declared
   23 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:23:114: error: 'kindergarten_garden::Plants' has not been declared
   23 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                                                                                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp:23:151: error: 'kindergarten_garden::Plants' has not been declared
   23 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                                                                                                                                       ^~~~~~
/testbed/kindergarten_garden_test.cpp:23:190: error: 'kindergarten_garden::Plants' has not been declared
   23 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                                                                                                                                                                              ^~~~~~
/testbed/kindergarten_garden_test.cpp:23:46: error: scalar object 'expected' requires one element in initializer
   23 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:24:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   24 |   REQUIRE(kindergarten_garden::plants("VC\nRC", "Alice") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:24:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   24 |   REQUIRE(kindergarten_garden::plants("VC\nRC", "Alice") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:24:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   24 |   REQUIRE(kindergarten_garden::plants("VC\nRC", "Alice") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/kindergarten_garden_test.cpp:28:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   28 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:28:44: error: template argument 1 is invalid
   28 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:28:76: error: 'kindergarten_garden::Plants' has not been declared
   28 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:28:113: error: 'kindergarten_garden::Plants' has not been declared
   28 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                                                                                                 ^~~~~~
/testbed/kindergarten_garden_test.cpp:28:149: error: 'kindergarten_garden::Plants' has not been declared
   28 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                                                                                                                                     ^~~~~~
/testbed/kindergarten_garden_test.cpp:28:188: error: 'kindergarten_garden::Plants' has not been declared
   28 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                                                                                                                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:28:46: error: scalar object 'expected' requires one element in initializer
   28 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::clover};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:29:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   29 |   REQUIRE(kindergarten_garden::plants("VVCG\nVVRC", "Bob") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:29:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   29 |   REQUIRE(kindergarten_garden::plants("VVCG\nVVRC", "Bob") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:29:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   29 |   REQUIRE(kindergarten_garden::plants("VVCG\nVVRC", "Bob") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/kindergarten_garden_test.cpp:33:37: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   33 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                     ^~~~~~
      |                                     Plant
/testbed/kindergarten_garden_test.cpp:33:46: error: template argument 1 is invalid
   33 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                              ^
/testbed/kindergarten_garden_test.cpp:33:78: error: 'kindergarten_garden::Plants' has not been declared
   33 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                                              ^~~~~~
/testbed/kindergarten_garden_test.cpp:33:115: error: 'kindergarten_garden::Plants' has not been declared
   33 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                                                                                   ^~~~~~
/testbed/kindergarten_garden_test.cpp:33:152: error: 'kindergarten_garden::Plants' has not been declared
   33 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                                                                                                                        ^~~~~~
/testbed/kindergarten_garden_test.cpp:33:189: error: 'kindergarten_garden::Plants' has not been declared
   33 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                                                                                                                                                             ^~~~~~
/testbed/kindergarten_garden_test.cpp:33:48: error: scalar object 'expected' requires one element in initializer
   33 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:34:34: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   34 |     REQUIRE(kindergarten_garden::plants("VVCCGG\nVVCCGG", "Bob") == expected);
      |                                  ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:34:34: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   34 |     REQUIRE(kindergarten_garden::plants("VVCCGG\nVVCCGG", "Bob") == expected);
      |                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp:34:34: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   34 |     REQUIRE(kindergarten_garden::plants("VVCCGG\nVVCCGG", "Bob") == expected);
      |                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/kindergarten_garden_test.cpp:38:37: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   38 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                     ^~~~~~
      |                                     Plant
/testbed/kindergarten_garden_test.cpp:38:46: error: template argument 1 is invalid
   38 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                              ^
/testbed/kindergarten_garden_test.cpp:38:78: error: 'kindergarten_garden::Plants' has not been declared
   38 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                                              ^~~~~~
/testbed/kindergarten_garden_test.cpp:38:114: error: 'kindergarten_garden::Plants' has not been declared
   38 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                                                                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp:38:150: error: 'kindergarten_garden::Plants' has not been declared
   38 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                                                                                                                      ^~~~~~
/testbed/kindergarten_garden_test.cpp:38:186: error: 'kindergarten_garden::Plants' has not been declared
   38 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                                                                                                                                                          ^~~~~~
/testbed/kindergarten_garden_test.cpp:38:48: error: scalar object 'expected' requires one element in initializer
   38 |     std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass};
      |                                                ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:39:34: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   39 |     REQUIRE(kindergarten_garden::plants("VVCCGG\nVVCCGG", "Charlie") == expected);
      |                                  ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:39:34: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   39 |     REQUIRE(kindergarten_garden::plants("VVCCGG\nVVCCGG", "Charlie") == expected);
      |                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp:39:34: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   39 |     REQUIRE(kindergarten_garden::plants("VVCCGG\nVVCCGG", "Charlie") == expected);
      |                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/kindergarten_garden_test.cpp:43:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   43 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:43:44: error: template argument 1 is invalid
   43 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:43:76: error: 'kindergarten_garden::Plants' has not been declared
   43 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:43:114: error: 'kindergarten_garden::Plants' has not been declared
   43 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes};
      |                                                                                                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp:43:153: error: 'kindergarten_garden::Plants' has not been declared
   43 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes};
      |                                                                                                                                                         ^~~~~~
/testbed/kindergarten_garden_test.cpp:43:191: error: 'kindergarten_garden::Plants' has not been declared
   43 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes};
      |                                                                                                                                                                                               ^~~~~~
/testbed/kindergarten_garden_test.cpp:43:46: error: scalar object 'expected' requires one element in initializer
   43 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:44:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   44 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Alice") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:44:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   44 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Alice") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:44:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   44 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Alice") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/kindergarten_garden_test.cpp:48:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   48 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:48:44: error: template argument 1 is invalid
   48 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:48:76: error: 'kindergarten_garden::Plants' has not been declared
   48 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:48:113: error: 'kindergarten_garden::Plants' has not been declared
   48 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                                                                                 ^~~~~~
/testbed/kindergarten_garden_test.cpp:48:149: error: 'kindergarten_garden::Plants' has not been declared
   48 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                                                                                                                     ^~~~~~
/testbed/kindergarten_garden_test.cpp:48:186: error: 'kindergarten_garden::Plants' has not been declared
   48 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                                                                                                                                                                          ^~~~~~
/testbed/kindergarten_garden_test.cpp:48:46: error: scalar object 'expected' requires one element in initializer
   48 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:49:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   49 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Bob") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:49:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   49 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Bob") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:49:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   49 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Bob") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/kindergarten_garden_test.cpp:53:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   53 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:53:44: error: template argument 1 is invalid
   53 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:53:76: error: 'kindergarten_garden::Plants' has not been declared
   53 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:53:114: error: 'kindergarten_garden::Plants' has not been declared
   53 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                                                                                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp:53:152: error: 'kindergarten_garden::Plants' has not been declared
   53 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                                                                                                                                        ^~~~~~
/testbed/kindergarten_garden_test.cpp:53:189: error: 'kindergarten_garden::Plants' has not been declared
   53 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                                                                                                                                                                             ^~~~~~
/testbed/kindergarten_garden_test.cpp:53:46: error: scalar object 'expected' requires one element in initializer
   53 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:54:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   54 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Charlie") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:54:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   54 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Charlie") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:54:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   54 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Charlie") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/kindergarten_garden_test.cpp:58:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   58 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:58:44: error: template argument 1 is invalid
   58 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:58:76: error: 'kindergarten_garden::Plants' has not been declared
   58 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:58:115: error: 'kindergarten_garden::Plants' has not been declared
   58 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes};
      |                                                                                                                   ^~~~~~
/testbed/kindergarten_garden_test.cpp:58:153: error: 'kindergarten_garden::Plants' has not been declared
   58 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes};
      |                                                                                                                                                         ^~~~~~
/testbed/kindergarten_garden_test.cpp:58:190: error: 'kindergarten_garden::Plants' has not been declared
   58 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes};
      |                                                                                                                                                                                              ^~~~~~
/testbed/kindergarten_garden_test.cpp:58:46: error: scalar object 'expected' requires one element in initializer
   58 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::radishes};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:59:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   59 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "David") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:59:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   59 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "David") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:59:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   59 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "David") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/kindergarten_garden_test.cpp:63:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   63 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::grass};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:63:44: error: template argument 1 is invalid
   63 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::grass};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:63:76: error: 'kindergarten_garden::Plants' has not been declared
   63 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::grass};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:63:113: error: 'kindergarten_garden::Plants' has not been declared
   63 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::grass};
      |                                                                                                                 ^~~~~~
/testbed/kindergarten_garden_test.cpp:63:149: error: 'kindergarten_garden::Plants' has not been declared
   63 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::grass};
      |                                                                                                                                                     ^~~~~~
/testbed/kindergarten_garden_test.cpp:63:188: error: 'kindergarten_garden::Plants' has not been declared
   63 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::grass};
      |                                                                                                                                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:63:46: error: scalar object 'expected' requires one element in initializer
   63 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::grass};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:64:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   64 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Eve") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:64:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   64 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Eve") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:64:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   64 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Eve") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/kindergarten_garden_test.cpp:68:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   68 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:68:44: error: template argument 1 is invalid
   68 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:68:76: error: 'kindergarten_garden::Plants' has not been declared
   68 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:68:112: error: 'kindergarten_garden::Plants' has not been declared
   68 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                                                                                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:68:149: error: 'kindergarten_garden::Plants' has not been declared
   68 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                                                                                                                                     ^~~~~~
/testbed/kindergarten_garden_test.cpp:68:187: error: 'kindergarten_garden::Plants' has not been declared
   68 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                                                                                                                                                                           ^~~~~~
/testbed/kindergarten_garden_test.cpp:68:46: error: scalar object 'expected' requires one element in initializer
   68 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:69:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   69 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Fred") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:69:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   69 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Fred") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:69:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   69 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Fred") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/kindergarten_garden_test.cpp:73:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   73 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:73:44: error: template argument 1 is invalid
   73 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:73:76: error: 'kindergarten_garden::Plants' has not been declared
   73 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:73:113: error: 'kindergarten_garden::Plants' has not been declared
   73 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover};
      |                                                                                                                 ^~~~~~
/testbed/kindergarten_garden_test.cpp:73:149: error: 'kindergarten_garden::Plants' has not been declared
   73 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover};
      |                                                                                                                                                     ^~~~~~
/testbed/kindergarten_garden_test.cpp:73:185: error: 'kindergarten_garden::Plants' has not been declared
   73 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover};
      |                                                                                                                                                                                         ^~~~~~
/testbed/kindergarten_garden_test.cpp:73:46: error: scalar object 'expected' requires one element in initializer
   73 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:74:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   74 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Ginny") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:74:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   74 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Ginny") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:74:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   74 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Ginny") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/kindergarten_garden_test.cpp:78:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   78 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:78:44: error: template argument 1 is invalid
   78 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:78:76: error: 'kindergarten_garden::Plants' has not been declared
   78 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:78:114: error: 'kindergarten_garden::Plants' has not been declared
   78 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets};
      |                                                                                                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp:78:153: error: 'kindergarten_garden::Plants' has not been declared
   78 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets};
      |                                                                                                                                                         ^~~~~~
/testbed/kindergarten_garden_test.cpp:78:192: error: 'kindergarten_garden::Plants' has not been declared
   78 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets};
      |                                                                                                                                                                                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:78:46: error: scalar object 'expected' requires one element in initializer
   78 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::radishes, kindergarten_garden::Plants::violets};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:79:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   79 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Harriet") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:79:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   79 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Harriet") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:79:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   79 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Harriet") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/kindergarten_garden_test.cpp:83:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   83 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:83:44: error: template argument 1 is invalid
   83 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:83:76: error: 'kindergarten_garden::Plants' has not been declared
   83 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:83:112: error: 'kindergarten_garden::Plants' has not been declared
   83 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                                                                                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:83:149: error: 'kindergarten_garden::Plants' has not been declared
   83 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                                                                                                                                     ^~~~~~
/testbed/kindergarten_garden_test.cpp:83:187: error: 'kindergarten_garden::Plants' has not been declared
   83 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                                                                                                                                                                           ^~~~~~
/testbed/kindergarten_garden_test.cpp:83:46: error: scalar object 'expected' requires one element in initializer
   83 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:84:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   84 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Ileana") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:84:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   84 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Ileana") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:84:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   84 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Ileana") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/kindergarten_garden_test.cpp:88:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   88 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::grass};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:88:44: error: template argument 1 is invalid
   88 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::grass};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:88:76: error: 'kindergarten_garden::Plants' has not been declared
   88 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::grass};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:88:114: error: 'kindergarten_garden::Plants' has not been declared
   88 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::grass};
      |                                                                                                                  ^~~~~~
/testbed/kindergarten_garden_test.cpp:88:151: error: 'kindergarten_garden::Plants' has not been declared
   88 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::grass};
      |                                                                                                                                                       ^~~~~~
/testbed/kindergarten_garden_test.cpp:88:189: error: 'kindergarten_garden::Plants' has not been declared
   88 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::grass};
      |                                                                                                                                                                                             ^~~~~~
/testbed/kindergarten_garden_test.cpp:88:46: error: scalar object 'expected' requires one element in initializer
   88 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::grass};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:89:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   89 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Joseph") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:89:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   89 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Joseph") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:89:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   89 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Joseph") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/kindergarten_garden_test.cpp:93:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   93 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:93:44: error: template argument 1 is invalid
   93 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:93:76: error: 'kindergarten_garden::Plants' has not been declared
   93 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:93:112: error: 'kindergarten_garden::Plants' has not been declared
   93 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                                                                                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:93:149: error: 'kindergarten_garden::Plants' has not been declared
   93 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                                                                                                                                     ^~~~~~
/testbed/kindergarten_garden_test.cpp:93:186: error: 'kindergarten_garden::Plants' has not been declared
   93 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                                                                                                                                                                          ^~~~~~
/testbed/kindergarten_garden_test.cpp:93:46: error: scalar object 'expected' requires one element in initializer
   93 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::grass};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:94:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   94 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Kincaid") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:94:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   94 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Kincaid") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:94:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   94 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Kincaid") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/kindergarten_garden_test.cpp:98:35: error: 'Plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   98 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets};
      |                                   ^~~~~~
      |                                   Plant
/testbed/kindergarten_garden_test.cpp:98:44: error: template argument 1 is invalid
   98 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets};
      |                                            ^
/testbed/kindergarten_garden_test.cpp:98:76: error: 'kindergarten_garden::Plants' has not been declared
   98 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets};
      |                                                                            ^~~~~~
/testbed/kindergarten_garden_test.cpp:98:112: error: 'kindergarten_garden::Plants' has not been declared
   98 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets};
      |                                                                                                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:98:150: error: 'kindergarten_garden::Plants' has not been declared
   98 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets};
      |                                                                                                                                                      ^~~~~~
/testbed/kindergarten_garden_test.cpp:98:187: error: 'kindergarten_garden::Plants' has not been declared
   98 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets};
      |                                                                                                                                                                                           ^~~~~~
/testbed/kindergarten_garden_test.cpp:98:46: error: scalar object 'expected' requires one element in initializer
   98 |   std::array<kindergarten_garden::Plants, 4> expected{kindergarten_garden::Plants::grass, kindergarten_garden::Plants::violets, kindergarten_garden::Plants::clover, kindergarten_garden::Plants::violets};
      |                                              ^~~~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:99:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   99 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Larry") == expected);
      |                                ^~~~~~
In file included from /testbed/kindergarten_garden_test.cpp:5:
/testbed/kindergarten_garden_test.cpp:99:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   99 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Larry") == expected);
      |                                ^~~~~~
/testbed/kindergarten_garden_test.cpp:99:32: error: 'plants' is not a member of 'kindergarten_garden'; did you mean 'Plant'?
   99 |   REQUIRE(kindergarten_garden::plants("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV", "Larry") == expected);
      |                                ^~~~~~
make[2]: *** [CMakeFiles/kindergarten-garden.dir/build.make:76: CMakeFiles/kindergarten-garden.dir/kindergarten_garden_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/kindergarten-garden.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
