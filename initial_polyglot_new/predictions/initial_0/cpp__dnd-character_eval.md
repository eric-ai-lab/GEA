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
/testbed/dnd_character_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/dnd_character_test.cpp:97:35: error: 'ability' is not a member of 'dnd_character'
   97 |         int result{dnd_character::ability()};
      |                                   ^~~~~~~
make[2]: *** [CMakeFiles/dnd-character.dir/build.make:76: CMakeFiles/dnd-character.dir/dnd_character_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/dnd-character.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
