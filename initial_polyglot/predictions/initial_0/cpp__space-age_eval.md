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
[ 25%] Building CXX object CMakeFiles/space-age.dir/space_age_test.cpp.o
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/space_age_test.cpp:10:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   10 |     const space_age::space_age age(1000000);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:12:13: error: 'age' was not declared in this scope
   12 |     REQUIRE(age.seconds() == 1000000);
      |             ^~~
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:12:13: error: 'age' was not declared in this scope
   12 |     REQUIRE(age.seconds() == 1000000);
      |             ^~~
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/space_age_test.cpp:23:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   23 |     const space_age::space_age age(1000000000);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:25:18: error: 'age' was not declared in this scope
   25 |     REQUIRE_THAT(age.on_earth(), Catch::Matchers::WithinAbs(31.69, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/space_age_test.cpp:30:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   30 |     const space_age::space_age age(2134835688);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:32:18: error: 'age' was not declared in this scope
   32 |     REQUIRE_THAT(age.on_earth(), Catch::Matchers::WithinAbs(67.65, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp:33:18: error: 'age' was not declared in this scope
   33 |     REQUIRE_THAT(age.on_mercury(), Catch::Matchers::WithinAbs(280.88, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/space_age_test.cpp:38:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   38 |     const space_age::space_age age(189839836);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:40:18: error: 'age' was not declared in this scope
   40 |     REQUIRE_THAT(age.on_earth(), Catch::Matchers::WithinAbs(6.02, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp:41:18: error: 'age' was not declared in this scope
   41 |     REQUIRE_THAT(age.on_venus(), Catch::Matchers::WithinAbs(9.78, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/space_age_test.cpp:46:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   46 |     const space_age::space_age age(2329871239);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:48:18: error: 'age' was not declared in this scope
   48 |     REQUIRE_THAT(age.on_earth(), Catch::Matchers::WithinAbs(73.83, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp:49:18: error: 'age' was not declared in this scope
   49 |     REQUIRE_THAT(age.on_mars(), Catch::Matchers::WithinAbs(39.25, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/space_age_test.cpp:54:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   54 |     const space_age::space_age age(901876382);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:56:18: error: 'age' was not declared in this scope
   56 |     REQUIRE_THAT(age.on_earth(), Catch::Matchers::WithinAbs(28.58, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp:57:18: error: 'age' was not declared in this scope
   57 |     REQUIRE_THAT(age.on_jupiter(), Catch::Matchers::WithinAbs(2.41, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/space_age_test.cpp:62:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   62 |     const space_age::space_age age(3000000000);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:64:18: error: 'age' was not declared in this scope
   64 |     REQUIRE_THAT(age.on_earth(), Catch::Matchers::WithinAbs(95.06, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp:65:18: error: 'age' was not declared in this scope
   65 |     REQUIRE_THAT(age.on_saturn(), Catch::Matchers::WithinAbs(3.23, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/space_age_test.cpp:70:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   70 |     const space_age::space_age age(3210123456);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:72:18: error: 'age' was not declared in this scope
   72 |     REQUIRE_THAT(age.on_earth(), Catch::Matchers::WithinAbs(101.72, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp:73:18: error: 'age' was not declared in this scope
   73 |     REQUIRE_THAT(age.on_uranus(), Catch::Matchers::WithinAbs(1.21, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/space_age_test.cpp:78:22: error: 'space_age' in namespace 'space_age' does not name a type; did you mean 'SpaceAge'?
   78 |     const space_age::space_age age(8210123456);
      |                      ^~~~~~~~~
      |                      SpaceAge
In file included from /testbed/space_age_test.cpp:5:
/testbed/space_age_test.cpp:80:18: error: 'age' was not declared in this scope
   80 |     REQUIRE_THAT(age.on_earth(), Catch::Matchers::WithinAbs(260.16, accuracy));
      |                  ^~~
/testbed/space_age_test.cpp:81:18: error: 'age' was not declared in this scope
   81 |     REQUIRE_THAT(age.on_neptune(), Catch::Matchers::WithinAbs(1.58, accuracy));
      |                  ^~~
make[2]: *** [CMakeFiles/space-age.dir/build.make:76: CMakeFiles/space-age.dir/space_age_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/space-age.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
