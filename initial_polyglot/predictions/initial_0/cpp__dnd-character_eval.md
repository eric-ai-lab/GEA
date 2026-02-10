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
[ 25%] Building CXX object CMakeFiles/dnd-character.dir/dnd_character_test.cpp.o
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/dnd_character_test.cpp:31:38: error: 'modifier' is not a member of 'dnd_character'
   31 |         REQUIRE(-4 == dnd_character::modifier(3));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:31:38: error: 'modifier' is not a member of 'dnd_character'
   31 |         REQUIRE(-4 == dnd_character::modifier(3));
      |                                      ^~~~~~~~
/testbed/dnd_character_test.cpp:31:38: error: 'modifier' is not a member of 'dnd_character'
   31 |         REQUIRE(-4 == dnd_character::modifier(3));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/dnd_character_test.cpp:37:38: error: 'modifier' is not a member of 'dnd_character'
   37 |         REQUIRE(-3 == dnd_character::modifier(4));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:37:38: error: 'modifier' is not a member of 'dnd_character'
   37 |         REQUIRE(-3 == dnd_character::modifier(4));
      |                                      ^~~~~~~~
/testbed/dnd_character_test.cpp:37:38: error: 'modifier' is not a member of 'dnd_character'
   37 |         REQUIRE(-3 == dnd_character::modifier(4));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/dnd_character_test.cpp:41:38: error: 'modifier' is not a member of 'dnd_character'
   41 |         REQUIRE(-3 == dnd_character::modifier(5));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:41:38: error: 'modifier' is not a member of 'dnd_character'
   41 |         REQUIRE(-3 == dnd_character::modifier(5));
      |                                      ^~~~~~~~
/testbed/dnd_character_test.cpp:41:38: error: 'modifier' is not a member of 'dnd_character'
   41 |         REQUIRE(-3 == dnd_character::modifier(5));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/dnd_character_test.cpp:45:38: error: 'modifier' is not a member of 'dnd_character'
   45 |         REQUIRE(-2 == dnd_character::modifier(6));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:45:38: error: 'modifier' is not a member of 'dnd_character'
   45 |         REQUIRE(-2 == dnd_character::modifier(6));
      |                                      ^~~~~~~~
/testbed/dnd_character_test.cpp:45:38: error: 'modifier' is not a member of 'dnd_character'
   45 |         REQUIRE(-2 == dnd_character::modifier(6));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/dnd_character_test.cpp:49:38: error: 'modifier' is not a member of 'dnd_character'
   49 |         REQUIRE(-2 == dnd_character::modifier(7));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:49:38: error: 'modifier' is not a member of 'dnd_character'
   49 |         REQUIRE(-2 == dnd_character::modifier(7));
      |                                      ^~~~~~~~
/testbed/dnd_character_test.cpp:49:38: error: 'modifier' is not a member of 'dnd_character'
   49 |         REQUIRE(-2 == dnd_character::modifier(7));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/dnd_character_test.cpp:53:38: error: 'modifier' is not a member of 'dnd_character'
   53 |         REQUIRE(-1 == dnd_character::modifier(8));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:53:38: error: 'modifier' is not a member of 'dnd_character'
   53 |         REQUIRE(-1 == dnd_character::modifier(8));
      |                                      ^~~~~~~~
/testbed/dnd_character_test.cpp:53:38: error: 'modifier' is not a member of 'dnd_character'
   53 |         REQUIRE(-1 == dnd_character::modifier(8));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/dnd_character_test.cpp:57:38: error: 'modifier' is not a member of 'dnd_character'
   57 |         REQUIRE(-1 == dnd_character::modifier(9));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:57:38: error: 'modifier' is not a member of 'dnd_character'
   57 |         REQUIRE(-1 == dnd_character::modifier(9));
      |                                      ^~~~~~~~
/testbed/dnd_character_test.cpp:57:38: error: 'modifier' is not a member of 'dnd_character'
   57 |         REQUIRE(-1 == dnd_character::modifier(9));
      |                                      ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/dnd_character_test.cpp:61:37: error: 'modifier' is not a member of 'dnd_character'
   61 |         REQUIRE(0 == dnd_character::modifier(10));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:61:37: error: 'modifier' is not a member of 'dnd_character'
   61 |         REQUIRE(0 == dnd_character::modifier(10));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:61:37: error: 'modifier' is not a member of 'dnd_character'
   61 |         REQUIRE(0 == dnd_character::modifier(10));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/dnd_character_test.cpp:65:37: error: 'modifier' is not a member of 'dnd_character'
   65 |         REQUIRE(0 == dnd_character::modifier(11));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:65:37: error: 'modifier' is not a member of 'dnd_character'
   65 |         REQUIRE(0 == dnd_character::modifier(11));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:65:37: error: 'modifier' is not a member of 'dnd_character'
   65 |         REQUIRE(0 == dnd_character::modifier(11));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/dnd_character_test.cpp:69:37: error: 'modifier' is not a member of 'dnd_character'
   69 |         REQUIRE(1 == dnd_character::modifier(12));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:69:37: error: 'modifier' is not a member of 'dnd_character'
   69 |         REQUIRE(1 == dnd_character::modifier(12));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:69:37: error: 'modifier' is not a member of 'dnd_character'
   69 |         REQUIRE(1 == dnd_character::modifier(12));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/dnd_character_test.cpp:73:37: error: 'modifier' is not a member of 'dnd_character'
   73 |         REQUIRE(1 == dnd_character::modifier(13));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:73:37: error: 'modifier' is not a member of 'dnd_character'
   73 |         REQUIRE(1 == dnd_character::modifier(13));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:73:37: error: 'modifier' is not a member of 'dnd_character'
   73 |         REQUIRE(1 == dnd_character::modifier(13));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/dnd_character_test.cpp:77:37: error: 'modifier' is not a member of 'dnd_character'
   77 |         REQUIRE(2 == dnd_character::modifier(14));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:77:37: error: 'modifier' is not a member of 'dnd_character'
   77 |         REQUIRE(2 == dnd_character::modifier(14));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:77:37: error: 'modifier' is not a member of 'dnd_character'
   77 |         REQUIRE(2 == dnd_character::modifier(14));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/dnd_character_test.cpp:81:37: error: 'modifier' is not a member of 'dnd_character'
   81 |         REQUIRE(2 == dnd_character::modifier(15));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:81:37: error: 'modifier' is not a member of 'dnd_character'
   81 |         REQUIRE(2 == dnd_character::modifier(15));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:81:37: error: 'modifier' is not a member of 'dnd_character'
   81 |         REQUIRE(2 == dnd_character::modifier(15));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/dnd_character_test.cpp:85:37: error: 'modifier' is not a member of 'dnd_character'
   85 |         REQUIRE(3 == dnd_character::modifier(16));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:85:37: error: 'modifier' is not a member of 'dnd_character'
   85 |         REQUIRE(3 == dnd_character::modifier(16));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:85:37: error: 'modifier' is not a member of 'dnd_character'
   85 |         REQUIRE(3 == dnd_character::modifier(16));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/dnd_character_test.cpp:89:37: error: 'modifier' is not a member of 'dnd_character'
   89 |         REQUIRE(3 == dnd_character::modifier(17));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:89:37: error: 'modifier' is not a member of 'dnd_character'
   89 |         REQUIRE(3 == dnd_character::modifier(17));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:89:37: error: 'modifier' is not a member of 'dnd_character'
   89 |         REQUIRE(3 == dnd_character::modifier(17));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/dnd_character_test.cpp:93:37: error: 'modifier' is not a member of 'dnd_character'
   93 |         REQUIRE(4 == dnd_character::modifier(18));
      |                                     ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:93:37: error: 'modifier' is not a member of 'dnd_character'
   93 |         REQUIRE(4 == dnd_character::modifier(18));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp:93:37: error: 'modifier' is not a member of 'dnd_character'
   93 |         REQUIRE(4 == dnd_character::modifier(18));
      |                                     ^~~~~~~~
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/dnd_character_test.cpp:97:35: error: 'ability' is not a member of 'dnd_character'
   97 |         int result{dnd_character::ability()};
      |                                   ^~~~~~~
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____34()':
/testbed/dnd_character_test.cpp:102:24: error: 'Character' is not a member of 'dnd_character'; did you mean 'character'?
  102 |         dnd_character::Character character;
      |                        ^~~~~~~~~
      |                        character
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:103:20: error: 'character' was not declared in this scope; did you mean 'dnd_character::character'?
  103 |         CHECK_THAT(character.strength, IsBetweenMatcher(3, 18));
      |                    ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:1:
/testbed/dnd_character.h:5:8: note: 'dnd_character::character' declared here
    5 | struct character {
      |        ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:104:20: error: 'character' was not declared in this scope; did you mean 'dnd_character::character'?
  104 |         CHECK_THAT(character.dexterity, IsBetweenMatcher(3, 18));
      |                    ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:1:
/testbed/dnd_character.h:5:8: note: 'dnd_character::character' declared here
    5 | struct character {
      |        ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:105:20: error: 'character' was not declared in this scope; did you mean 'dnd_character::character'?
  105 |         CHECK_THAT(character.constitution, IsBetweenMatcher(3, 18));
      |                    ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:1:
/testbed/dnd_character.h:5:8: note: 'dnd_character::character' declared here
    5 | struct character {
      |        ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:106:20: error: 'character' was not declared in this scope; did you mean 'dnd_character::character'?
  106 |         CHECK_THAT(character.intelligence, IsBetweenMatcher(3, 18));
      |                    ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:1:
/testbed/dnd_character.h:5:8: note: 'dnd_character::character' declared here
    5 | struct character {
      |        ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:107:20: error: 'character' was not declared in this scope; did you mean 'dnd_character::character'?
  107 |         CHECK_THAT(character.wisdom, IsBetweenMatcher(3, 18));
      |                    ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:1:
/testbed/dnd_character.h:5:8: note: 'dnd_character::character' declared here
    5 | struct character {
      |        ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:108:20: error: 'character' was not declared in this scope; did you mean 'dnd_character::character'?
  108 |         CHECK_THAT(character.charisma, IsBetweenMatcher(3, 18));
      |                    ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:1:
/testbed/dnd_character.h:5:8: note: 'dnd_character::character' declared here
    5 | struct character {
      |        ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:109:17: error: 'character' was not declared in this scope; did you mean 'dnd_character::character'?
  109 |         REQUIRE(character.hitpoints == 10 + dnd_character::modifier(character.constitution));
      |                 ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:1:
/testbed/dnd_character.h:5:8: note: 'dnd_character::character' declared here
    5 | struct character {
      |        ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:109:60: error: 'modifier' is not a member of 'dnd_character'
  109 |         REQUIRE(character.hitpoints == 10 + dnd_character::modifier(character.constitution));
      |                                                            ^~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:109:60: error: 'modifier' is not a member of 'dnd_character'
  109 |         REQUIRE(character.hitpoints == 10 + dnd_character::modifier(character.constitution));
      |                                                            ^~~~~~~~
/testbed/dnd_character_test.cpp:109:17: error: 'character' was not declared in this scope; did you mean 'dnd_character::character'?
  109 |         REQUIRE(character.hitpoints == 10 + dnd_character::modifier(character.constitution));
      |                 ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:1:
/testbed/dnd_character.h:5:8: note: 'dnd_character::character' declared here
    5 | struct character {
      |        ^~~~~~~~~
In file included from /testbed/dnd_character_test.cpp:5:
/testbed/dnd_character_test.cpp:109:60: error: 'modifier' is not a member of 'dnd_character'
  109 |         REQUIRE(character.hitpoints == 10 + dnd_character::modifier(character.constitution));
      |                                                            ^~~~~~~~
make[2]: *** [CMakeFiles/dnd-character.dir/build.make:76: CMakeFiles/dnd-character.dir/dnd_character_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/dnd-character.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
