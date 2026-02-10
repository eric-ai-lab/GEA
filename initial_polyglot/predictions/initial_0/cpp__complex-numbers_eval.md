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
[ 25%] Building CXX object CMakeFiles/complex-numbers.dir/complex_numbers_test.cpp.o
In file included from /testbed/complex_numbers_test.cpp:8:
/testbed/complex_numbers_test.cpp: In function 'void require_approx_equal(const complex_numbers::Complex&, const complex_numbers::Complex&)':
/testbed/complex_numbers_test.cpp:29:26: error: expression cannot be used as a function
   29 |     REQUIRE_THAT(lhs.real(),
      |                  ~~~~~~~~^~
/testbed/complex_numbers_test.cpp:30:53: error: expression cannot be used as a function
   30 |                  Catch::Matchers::WithinAbs(rhs.real(), eps));
      |                                             ~~~~~~~~^~
/testbed/complex_numbers_test.cpp:31:26: error: expression cannot be used as a function
   31 |     REQUIRE_THAT(lhs.imag(),
      |                  ~~~~~~~~^~
/testbed/complex_numbers_test.cpp:32:53: error: expression cannot be used as a function
   32 |                  Catch::Matchers::WithinAbs(rhs.imag(), eps));
      |                                             ~~~~~~~~^~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/complex_numbers_test.cpp:38:24: error: expression cannot be used as a function
   38 |     REQUIRE_THAT(c.real(), Catch::Matchers::WithinAbs(1.0, eps));
      |                  ~~~~~~^~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/complex_numbers_test.cpp:45:24: error: expression cannot be used as a function
   45 |     REQUIRE_THAT(c.real(), Catch::Matchers::WithinAbs(0.0, eps));
      |                  ~~~~~~^~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/complex_numbers_test.cpp:51:24: error: expression cannot be used as a function
   51 |     REQUIRE_THAT(c.real(), Catch::Matchers::WithinAbs(1.0, eps));
      |                  ~~~~~~^~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/complex_numbers_test.cpp:57:24: error: expression cannot be used as a function
   57 |     REQUIRE_THAT(c.imag(), Catch::Matchers::WithinAbs(0.0, eps));
      |                  ~~~~~~^~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/complex_numbers_test.cpp:63:24: error: expression cannot be used as a function
   63 |     REQUIRE_THAT(c.imag(), Catch::Matchers::WithinAbs(1.0, eps));
      |                  ~~~~~~^~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/complex_numbers_test.cpp:69:25: error: expression cannot be used as a function
   69 |     REQUIRE_THAT( c.imag(), Catch::Matchers::WithinAbs(2.0, eps));
      |                   ~~~~~~^~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/complex_numbers_test.cpp:76:49: error: no match for 'operator*' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
   76 |     require_approx_equal(Complex(-1.0, 0.0), c1 * c2);
      |                                              ~~ ^ ~~
      |                                              |    |
      |                                              |    const complex_numbers::Complex
      |                                              const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/complex_numbers_test.cpp:83:48: error: no match for 'operator+' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
   83 |     require_approx_equal(Complex(3.0, 0.0), c1 + c2);
      |                                             ~~ ^ ~~
      |                                             |    |
      |                                             |    const complex_numbers::Complex
      |                                             const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/complex_numbers_test.cpp:90:48: error: no match for 'operator+' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
   90 |     require_approx_equal(Complex(0.0, 3.0), c1 + c2);
      |                                             ~~ ^ ~~
      |                                             |    |
      |                                             |    const complex_numbers::Complex
      |                                             const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/complex_numbers_test.cpp:97:48: error: no match for 'operator+' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
   97 |     require_approx_equal(Complex(4.0, 6.0), c1 + c2);
      |                                             ~~ ^ ~~
      |                                             |    |
      |                                             |    const complex_numbers::Complex
      |                                             const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/complex_numbers_test.cpp:104:49: error: no match for 'operator-' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  104 |     require_approx_equal(Complex(-1.0, 0.0), c1 - c2);
      |                                              ~~ ^ ~~
      |                                              |    |
      |                                              |    const complex_numbers::Complex
      |                                              const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/complex_numbers_test.cpp:111:49: error: no match for 'operator-' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  111 |     require_approx_equal(Complex(0.0, -1.0), c1 - c2);
      |                                              ~~ ^ ~~
      |                                              |    |
      |                                              |    const complex_numbers::Complex
      |                                              const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/complex_numbers_test.cpp:118:50: error: no match for 'operator-' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  118 |     require_approx_equal(Complex(-2.0, -2.0), c1 - c2);
      |                                               ~~ ^ ~~
      |                                               |    |
      |                                               |    const complex_numbers::Complex
      |                                               const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/complex_numbers_test.cpp:125:48: error: no match for 'operator*' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  125 |     require_approx_equal(Complex(2.0, 0.0), c1 * c2);
      |                                             ~~ ^ ~~
      |                                             |    |
      |                                             |    const complex_numbers::Complex
      |                                             const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/complex_numbers_test.cpp:132:49: error: no match for 'operator*' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  132 |     require_approx_equal(Complex(-2.0, 0.0), c1 * c2);
      |                                              ~~ ^ ~~
      |                                              |    |
      |                                              |    const complex_numbers::Complex
      |                                              const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/complex_numbers_test.cpp:139:50: error: no match for 'operator*' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  139 |     require_approx_equal(Complex(-5.0, 10.0), c1 * c2);
      |                                               ~~ ^ ~~
      |                                               |    |
      |                                               |    const complex_numbers::Complex
      |                                               const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/complex_numbers_test.cpp:146:48: error: no match for 'operator/' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  146 |     require_approx_equal(Complex(0.5, 0.0), c1 / c2);
      |                                             ~~ ^ ~~
      |                                             |    |
      |                                             |    const complex_numbers::Complex
      |                                             const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____34()':
/testbed/complex_numbers_test.cpp:153:48: error: no match for 'operator/' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  153 |     require_approx_equal(Complex(0.5, 0.0), c1 / c2);
      |                                             ~~ ^ ~~
      |                                             |    |
      |                                             |    const complex_numbers::Complex
      |                                             const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____36()':
/testbed/complex_numbers_test.cpp:160:50: error: no match for 'operator/' (operand types are 'const complex_numbers::Complex' and 'const complex_numbers::Complex')
  160 |     require_approx_equal(Complex(0.44, 0.08), c1 / c2);
      |                                               ~~ ^ ~~
      |                                               |    |
      |                                               |    const complex_numbers::Complex
      |                                               const complex_numbers::Complex
In file included from /testbed/complex_numbers_test.cpp:8:
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____38()':
/testbed/complex_numbers_test.cpp:166:20: error: 'const struct complex_numbers::Complex' has no member named 'abs'
  166 |     REQUIRE_THAT(c.abs(), Catch::Matchers::WithinAbs(5.0, eps));
      |                    ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____40()':
/testbed/complex_numbers_test.cpp:172:20: error: 'const struct complex_numbers::Complex' has no member named 'abs'
  172 |     REQUIRE_THAT(c.abs(), Catch::Matchers::WithinAbs(5.0, eps));
      |                    ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____42()':
/testbed/complex_numbers_test.cpp:179:20: error: 'const struct complex_numbers::Complex' has no member named 'abs'
  179 |     REQUIRE_THAT(c.abs(), Catch::Matchers::WithinAbs(5.0, eps));
      |                    ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____44()':
/testbed/complex_numbers_test.cpp:186:20: error: 'const struct complex_numbers::Complex' has no member named 'abs'
  186 |     REQUIRE_THAT(c.abs(), Catch::Matchers::WithinAbs(5.0, eps));
      |                    ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____46()':
/testbed/complex_numbers_test.cpp:192:20: error: 'const struct complex_numbers::Complex' has no member named 'abs'
  192 |     REQUIRE_THAT(c.abs(), Catch::Matchers::WithinAbs(5.0, eps));
      |                    ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____48()':
/testbed/complex_numbers_test.cpp:198:47: error: 'const struct complex_numbers::Complex' has no member named 'conj'
  198 |     require_approx_equal(Complex(5.0, 0.0), c.conj());
      |                                               ^~~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____50()':
/testbed/complex_numbers_test.cpp:204:48: error: 'const struct complex_numbers::Complex' has no member named 'conj'
  204 |     require_approx_equal(Complex(0.0, -5.0), c.conj());
      |                                                ^~~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____52()':
/testbed/complex_numbers_test.cpp:210:48: error: 'const struct complex_numbers::Complex' has no member named 'conj'
  210 |     require_approx_equal(Complex(1.0, -1.0), c.conj());
      |                                                ^~~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____54()':
/testbed/complex_numbers_test.cpp:216:48: error: 'const struct complex_numbers::Complex' has no member named 'exp'
  216 |     require_approx_equal(Complex(-1.0, 0.0), c.exp());
      |                                                ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____56()':
/testbed/complex_numbers_test.cpp:222:47: error: 'const struct complex_numbers::Complex' has no member named 'exp'
  222 |     require_approx_equal(Complex(1.0, 0.0), c.exp());
      |                                               ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____58()':
/testbed/complex_numbers_test.cpp:228:47: error: 'const struct complex_numbers::Complex' has no member named 'exp'
  228 |     require_approx_equal(Complex(M_E, 0.0), c.exp());
      |                                               ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____60()':
/testbed/complex_numbers_test.cpp:235:48: error: 'const struct complex_numbers::Complex' has no member named 'exp'
  235 |     require_approx_equal(Complex(-2.0, 0.0), c.exp());
      |                                                ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____62()':
/testbed/complex_numbers_test.cpp:241:47: error: 'const struct complex_numbers::Complex' has no member named 'exp'
  241 |     require_approx_equal(Complex(1.0, 1.0), c.exp());
      |                                               ^~~
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____64()':
/testbed/complex_numbers_test.cpp:247:46: error: no match for 'operator+' (operand types are 'const complex_numbers::Complex' and 'double')
  247 |     require_approx_equal(Complex(6.0,2.0), c + 5.0);
      |                                            ~ ^ ~~~
      |                                            |   |
      |                                            |   double
      |                                            const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____66()':
/testbed/complex_numbers_test.cpp:253:48: error: no match for 'operator+' (operand types are 'double' and 'const complex_numbers::Complex')
  253 |     require_approx_equal(Complex(6.0,2.0), 5.0 + c);
      |                                            ~~~ ^ ~
      |                                            |     |
      |                                            |     const complex_numbers::Complex
      |                                            double
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____68()':
/testbed/complex_numbers_test.cpp:259:46: error: no match for 'operator-' (operand types are 'const complex_numbers::Complex' and 'double')
  259 |     require_approx_equal(Complex(1.0,7.0), c - 4.0 );
      |                                            ~ ^ ~~~
      |                                            |   |
      |                                            |   double
      |                                            const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____70()':
/testbed/complex_numbers_test.cpp:265:50: error: no match for 'operator-' (operand types are 'double' and 'const complex_numbers::Complex')
  265 |     require_approx_equal(Complex(-1.0,-7.0), 4.0 - c);
      |                                              ~~~ ^ ~
      |                                              |     |
      |                                              |     const complex_numbers::Complex
      |                                              double
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____72()':
/testbed/complex_numbers_test.cpp:271:48: error: no match for 'operator*' (operand types are 'const complex_numbers::Complex' and 'double')
  271 |     require_approx_equal(Complex(10.0,25.0), c * 5.0);
      |                                              ~ ^ ~~~
      |                                              |   |
      |                                              |   double
      |                                              const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____74()':
/testbed/complex_numbers_test.cpp:277:50: error: no match for 'operator*' (operand types are 'double' and 'const complex_numbers::Complex')
  277 |     require_approx_equal(Complex(10.0,25.0), 5.0 * c);
      |                                              ~~~ ^ ~
      |                                              |     |
      |                                              |     const complex_numbers::Complex
      |                                              double
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____76()':
/testbed/complex_numbers_test.cpp:283:47: error: no match for 'operator/' (operand types are 'const complex_numbers::Complex' and 'double')
  283 |     require_approx_equal(Complex(1.0,10.0), c / 10.0 );
      |                                             ~ ^ ~~~~
      |                                             |   |
      |                                             |   double
      |                                             const complex_numbers::Complex
/testbed/complex_numbers_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____78()':
/testbed/complex_numbers_test.cpp:289:49: error: no match for 'operator/' (operand types are 'double' and 'const complex_numbers::Complex')
  289 |     require_approx_equal(Complex(2.5,-2.5), 5.0 / c);
      |                                             ~~~ ^ ~
      |                                             |     |
      |                                             |     const complex_numbers::Complex
      |                                             double
/testbed/complex_numbers_test.cpp: At global scope:
/testbed/complex_numbers_test.cpp:28:13: error: 'void require_approx_equal(const complex_numbers::Complex&, const complex_numbers::Complex&)' defined but not used [-Werror=unused-function]
   28 | static void require_approx_equal(const Complex& lhs, const Complex& rhs) {
      |             ^~~~~~~~~~~~~~~~~~~~
cc1plus: all warnings being treated as errors
make[2]: *** [CMakeFiles/complex-numbers.dir/build.make:76: CMakeFiles/complex-numbers.dir/complex_numbers_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/complex-numbers.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
