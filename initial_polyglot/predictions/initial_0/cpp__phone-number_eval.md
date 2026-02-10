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
[ 25%] Building CXX object CMakeFiles/phone-number.dir/phone_number_test.cpp.o
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/phone_number_test.cpp:10:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   10 |             phone_number::phone_number("(223) 456-7890").number());
      |                           ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp:10:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   10 |             phone_number::phone_number("(223) 456-7890").number());
      |                           ^~~~~~~~~~~~
/testbed/phone_number_test.cpp:10:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   10 |             phone_number::phone_number("(223) 456-7890").number());
      |                           ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/phone_number_test.cpp:18:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   18 |             phone_number::phone_number("223.456.7890").number());
      |                           ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp:18:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   18 |             phone_number::phone_number("223.456.7890").number());
      |                           ^~~~~~~~~~~~
/testbed/phone_number_test.cpp:18:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   18 |             phone_number::phone_number("223.456.7890").number());
      |                           ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/phone_number_test.cpp:24:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   24 |             phone_number::phone_number("223 456   7890   ").number());
      |                           ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp:24:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   24 |             phone_number::phone_number("223 456   7890   ").number());
      |                           ^~~~~~~~~~~~
/testbed/phone_number_test.cpp:24:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   24 |             phone_number::phone_number("223 456   7890   ").number());
      |                           ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/phone_number_test.cpp:28:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   28 |     REQUIRE_THROWS_AS(phone_number::phone_number("123456789"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/phone_number_test.cpp:34:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   34 |     REQUIRE_THROWS_AS(phone_number::phone_number("22234567890"),
      |                                     ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/phone_number_test.cpp:40:43: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   40 |     REQUIRE("2234567890" == phone_number::phone_number("12234567890").number());
      |                                           ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp:40:43: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   40 |     REQUIRE("2234567890" == phone_number::phone_number("12234567890").number());
      |                                           ^~~~~~~~~~~~
/testbed/phone_number_test.cpp:40:43: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   40 |     REQUIRE("2234567890" == phone_number::phone_number("12234567890").number());
      |                                           ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/phone_number_test.cpp:46:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   46 |             phone_number::phone_number("+1 (223) 456-7890").number());
      |                           ^~~~~~~~~~~~
In file included from /testbed/phone_number_test.cpp:5:
/testbed/phone_number_test.cpp:46:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   46 |             phone_number::phone_number("+1 (223) 456-7890").number());
      |                           ^~~~~~~~~~~~
/testbed/phone_number_test.cpp:46:27: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   46 |             phone_number::phone_number("+1 (223) 456-7890").number());
      |                           ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/phone_number_test.cpp:51:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   51 |     REQUIRE_THROWS_AS(phone_number::phone_number("321234567890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/phone_number_test.cpp:56:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   56 |     REQUIRE_THROWS_AS(phone_number::phone_number("123-abc-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/phone_number_test.cpp:62:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   62 |     REQUIRE_THROWS_AS(phone_number::phone_number("123-@:!-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/phone_number_test.cpp:68:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   68 |     REQUIRE_THROWS_AS(phone_number::phone_number("(023) 456-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/phone_number_test.cpp:74:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   74 |     REQUIRE_THROWS_AS(phone_number::phone_number("(123) 456-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/phone_number_test.cpp:80:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   80 |     REQUIRE_THROWS_AS(phone_number::phone_number("(223) 056-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/phone_number_test.cpp:86:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   86 |     REQUIRE_THROWS_AS(phone_number::phone_number("(223) 156-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/phone_number_test.cpp:92:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   92 |     REQUIRE_THROWS_AS(phone_number::phone_number("1 (023) 456-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/phone_number_test.cpp:98:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
   98 |     REQUIRE_THROWS_AS(phone_number::phone_number("1 (123) 456-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/phone_number_test.cpp:104:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
  104 |     REQUIRE_THROWS_AS(phone_number::phone_number("1 (223) 056-7890"),
      |                                     ^~~~~~~~~~~~
/testbed/phone_number_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____34()':
/testbed/phone_number_test.cpp:110:37: error: 'phone_number' is not a member of 'phone_number'; did you mean 'PhoneNumber'?
  110 |     REQUIRE_THROWS_AS(phone_number::phone_number("1 (223) 156-7890"),
      |                                     ^~~~~~~~~~~~
make[2]: *** [CMakeFiles/phone-number.dir/build.make:76: CMakeFiles/phone-number.dir/phone_number_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/phone-number.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
