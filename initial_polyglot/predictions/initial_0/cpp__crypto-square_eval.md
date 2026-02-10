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
[ 25%] Building CXX object CMakeFiles/crypto-square.dir/crypto_square_test.cpp.o
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/crypto_square_test.cpp:10:34: error: 'cipher' is not a member of 'crypto_square'
   10 |     REQUIRE("" == crypto_square::cipher("").normalized_cipher_text());
      |                                  ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp:10:34: error: 'cipher' is not a member of 'crypto_square'
   10 |     REQUIRE("" == crypto_square::cipher("").normalized_cipher_text());
      |                                  ^~~~~~
/testbed/crypto_square_test.cpp:10:34: error: 'cipher' is not a member of 'crypto_square'
   10 |     REQUIRE("" == crypto_square::cipher("").normalized_cipher_text());
      |                                  ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/crypto_square_test.cpp:17:28: error: 'cipher' is not a member of 'crypto_square'
   17 |             crypto_square::cipher("... --- ...").normalized_cipher_text());
      |                            ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp:17:28: error: 'cipher' is not a member of 'crypto_square'
   17 |             crypto_square::cipher("... --- ...").normalized_cipher_text());
      |                            ^~~~~~
/testbed/crypto_square_test.cpp:17:28: error: 'cipher' is not a member of 'crypto_square'
   17 |             crypto_square::cipher("... --- ...").normalized_cipher_text());
      |                            ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/crypto_square_test.cpp:21:35: error: 'cipher' is not a member of 'crypto_square'
   21 |     REQUIRE("a" == crypto_square::cipher("A").normalized_cipher_text());
      |                                   ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp:21:35: error: 'cipher' is not a member of 'crypto_square'
   21 |     REQUIRE("a" == crypto_square::cipher("A").normalized_cipher_text());
      |                                   ^~~~~~
/testbed/crypto_square_test.cpp:21:35: error: 'cipher' is not a member of 'crypto_square'
   21 |     REQUIRE("a" == crypto_square::cipher("A").normalized_cipher_text());
      |                                   ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/crypto_square_test.cpp:25:35: error: 'cipher' is not a member of 'crypto_square'
   25 |     REQUIRE("b" == crypto_square::cipher("  b ").normalized_cipher_text());
      |                                   ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp:25:35: error: 'cipher' is not a member of 'crypto_square'
   25 |     REQUIRE("b" == crypto_square::cipher("  b ").normalized_cipher_text());
      |                                   ^~~~~~
/testbed/crypto_square_test.cpp:25:35: error: 'cipher' is not a member of 'crypto_square'
   25 |     REQUIRE("b" == crypto_square::cipher("  b ").normalized_cipher_text());
      |                                   ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/crypto_square_test.cpp:29:35: error: 'cipher' is not a member of 'crypto_square'
   29 |     REQUIRE("1" == crypto_square::cipher("@1,%!").normalized_cipher_text());
      |                                   ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp:29:35: error: 'cipher' is not a member of 'crypto_square'
   29 |     REQUIRE("1" == crypto_square::cipher("@1,%!").normalized_cipher_text());
      |                                   ^~~~~~
/testbed/crypto_square_test.cpp:29:35: error: 'cipher' is not a member of 'crypto_square'
   29 |     REQUIRE("1" == crypto_square::cipher("@1,%!").normalized_cipher_text());
      |                                   ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/crypto_square_test.cpp:35:28: error: 'cipher' is not a member of 'crypto_square'
   35 |             crypto_square::cipher("This is fun!").normalized_cipher_text());
      |                            ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp:35:28: error: 'cipher' is not a member of 'crypto_square'
   35 |             crypto_square::cipher("This is fun!").normalized_cipher_text());
      |                            ^~~~~~
/testbed/crypto_square_test.cpp:35:28: error: 'cipher' is not a member of 'crypto_square'
   35 |             crypto_square::cipher("This is fun!").normalized_cipher_text());
      |                            ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/crypto_square_test.cpp:44:28: error: 'cipher' is not a member of 'crypto_square'
   44 |             crypto_square::cipher("Chill out.").normalized_cipher_text());
      |                            ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp:44:28: error: 'cipher' is not a member of 'crypto_square'
   44 |             crypto_square::cipher("Chill out.").normalized_cipher_text());
      |                            ^~~~~~
/testbed/crypto_square_test.cpp:44:28: error: 'cipher' is not a member of 'crypto_square'
   44 |             crypto_square::cipher("Chill out.").normalized_cipher_text());
      |                            ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/crypto_square_test.cpp:53:28: error: 'cipher' is not a member of 'crypto_square'
   53 |             crypto_square::cipher("If man was meant to stay on the ground, god "
      |                            ^~~~~~
In file included from /testbed/crypto_square_test.cpp:5:
/testbed/crypto_square_test.cpp:53:28: error: 'cipher' is not a member of 'crypto_square'
   53 |             crypto_square::cipher("If man was meant to stay on the ground, god "
      |                            ^~~~~~
/testbed/crypto_square_test.cpp:53:28: error: 'cipher' is not a member of 'crypto_square'
   53 |             crypto_square::cipher("If man was meant to stay on the ground, god "
      |                            ^~~~~~
make[2]: *** [CMakeFiles/crypto-square.dir/build.make:76: CMakeFiles/crypto-square.dir/crypto_square_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/crypto-square.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
