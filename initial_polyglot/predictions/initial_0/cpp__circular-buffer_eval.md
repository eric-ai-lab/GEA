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
[ 25%] Building CXX object CMakeFiles/circular-buffer.dir/circular_buffer_test.cpp.o
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/circular_buffer_test.cpp:14:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
   14 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:14:38: error: expected primary-expression before 'int'
   14 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:16:23: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   16 |     REQUIRE_THROWS_AS(buffer.read(), std::domain_error);
      |                       ^~~~~~
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/circular_buffer_test.cpp:22:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
   22 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:22:38: error: expected primary-expression before 'int'
   22 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:24:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   24 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:27:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   27 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:27:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   27 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/circular_buffer_test.cpp:32:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
   32 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:32:38: error: expected primary-expression before 'int'
   32 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:34:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   34 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:37:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   37 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:37:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   37 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/circular_buffer_test.cpp:44:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
   44 |     circular_buffer::circular_buffer<int> buffer(2);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:44:38: error: expected primary-expression before 'int'
   44 |     circular_buffer::circular_buffer<int> buffer(2);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:46:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   46 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:47:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   47 |     REQUIRE_NOTHROW(buffer.write(2));
      |                     ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:50:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   50 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:50:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   50 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/circular_buffer_test.cpp:58:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
   58 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:58:38: error: expected primary-expression before 'int'
   58 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:60:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   60 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:61:23: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   61 |     REQUIRE_THROWS_AS(buffer.write(2), std::domain_error);
      |                       ^~~~~~
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/circular_buffer_test.cpp:66:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
   66 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:66:38: error: expected primary-expression before 'int'
   66 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:68:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   68 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:71:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   71 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:71:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   71 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/circular_buffer_test.cpp:81:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
   81 |     circular_buffer::circular_buffer<int> buffer(3);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:81:38: error: expected primary-expression before 'int'
   81 |     circular_buffer::circular_buffer<int> buffer(3);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:83:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   83 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:84:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   84 |     REQUIRE_NOTHROW(buffer.write(2));
      |                     ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:87:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   87 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:87:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
   87 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/circular_buffer_test.cpp:100:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  100 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:100:38: error: expected primary-expression before 'int'
  100 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:102:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  102 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:104:5: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  104 |     buffer.clear();
      |     ^~~~~~
      |     setbuffer
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/circular_buffer_test.cpp:111:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  111 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:111:38: error: expected primary-expression before 'int'
  111 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:113:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  113 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:115:5: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  115 |     buffer.clear();
      |     ^~~~~~
      |     setbuffer
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/circular_buffer_test.cpp:125:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  125 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:125:38: error: expected primary-expression before 'int'
  125 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
/testbed/circular_buffer_test.cpp:127:5: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  127 |     buffer.clear();
      |     ^~~~~~
      |     setbuffer
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/circular_buffer_test.cpp:137:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  137 |     circular_buffer::circular_buffer<int> buffer(2);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:137:38: error: expected primary-expression before 'int'
  137 |     circular_buffer::circular_buffer<int> buffer(2);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:139:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  139 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:141:5: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  141 |     buffer.overwrite(2);
      |     ^~~~~~
      |     setbuffer
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/circular_buffer_test.cpp:152:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  152 |     circular_buffer::circular_buffer<int> buffer(2);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:152:38: error: expected primary-expression before 'int'
  152 |     circular_buffer::circular_buffer<int> buffer(2);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:154:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  154 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:155:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  155 |     REQUIRE_NOTHROW(buffer.write(2));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:157:5: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  157 |     buffer.overwrite(3);
      |     ^~~~~~
      |     setbuffer
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/circular_buffer_test.cpp:168:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  168 |     circular_buffer::circular_buffer<int> buffer(3);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:168:38: error: expected primary-expression before 'int'
  168 |     circular_buffer::circular_buffer<int> buffer(3);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:170:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  170 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:171:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  171 |     REQUIRE_NOTHROW(buffer.write(2));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:172:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  172 |     REQUIRE_NOTHROW(buffer.write(3));
      |                     ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:175:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  175 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:175:25: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  175 |     REQUIRE(expected == buffer.read());
      |                         ^~~~~~
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/circular_buffer_test.cpp:193:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  193 |     circular_buffer::circular_buffer<int> buffer(1);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:193:38: error: expected primary-expression before 'int'
  193 |     circular_buffer::circular_buffer<int> buffer(1);
      |                                      ^~~
In file included from /testbed/circular_buffer_test.cpp:5:
/testbed/circular_buffer_test.cpp:195:21: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  195 |     REQUIRE_NOTHROW(buffer.write(1));
      |                     ^~~~~~
/testbed/circular_buffer_test.cpp:196:5: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  196 |     buffer.overwrite(2);
      |     ^~~~~~
      |     setbuffer
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/circular_buffer_test.cpp:205:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  205 |     circular_buffer::circular_buffer<std::string> buffer(3);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:205:49: error: expected primary-expression before '>' token
  205 |     circular_buffer::circular_buffer<std::string> buffer(3);
      |                                                 ^
/testbed/circular_buffer_test.cpp:205:51: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  205 |     circular_buffer::circular_buffer<std::string> buffer(3);
      |                                                   ^~~~~~
      |                                                   setbuffer
/testbed/circular_buffer_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/circular_buffer_test.cpp:230:22: error: 'circular_buffer' is not a member of 'circular_buffer'; did you mean 'CircularBuffer'?
  230 |     circular_buffer::circular_buffer<int> buffer(2);
      |                      ^~~~~~~~~~~~~~~
      |                      CircularBuffer
/testbed/circular_buffer_test.cpp:230:38: error: expected primary-expression before 'int'
  230 |     circular_buffer::circular_buffer<int> buffer(2);
      |                                      ^~~
/testbed/circular_buffer_test.cpp:232:5: error: 'buffer' was not declared in this scope; did you mean 'setbuffer'?
  232 |     buffer.clear();
      |     ^~~~~~
      |     setbuffer
make[2]: *** [CMakeFiles/circular-buffer.dir/build.make:76: CMakeFiles/circular-buffer.dir/circular_buffer_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/circular-buffer.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
