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
-- Found Boost: /usr/lib/x86_64-linux-gnu/cmake/Boost-1.74.0/BoostConfig.cmake (found suitable version "1.74.0", minimum required is "1.58") found components: date_time 
-- Configuring done
-- Generating done
-- Build files have been written to: /testbed/build
+ make
[ 25%] Building CXX object CMakeFiles/gigasecond.dir/gigasecond_test.cpp.o
/testbed/gigasecond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/gigasecond_test.cpp:20:45: error: invalid initialization of reference of type 'const time_point&' {aka 'const std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >&'} from expression of type 'boost::posix_time::ptime'
   20 |         gigasecond::advance(time_from_string("2011-04-25 00:00:00"));
      |                             ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~
In file included from /testbed/gigasecond_test.cpp:1:
/testbed/gigasecond.h:9:92: note: in passing argument 1 of 'std::chrono::_V2::system_clock::time_point gigasecond::advance(const time_point&)'
    9 | std::chrono::system_clock::time_point advance(const std::chrono::system_clock::time_point &start);
      |                                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/gigasecond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/gigasecond_test.cpp:30:45: error: invalid initialization of reference of type 'const time_point&' {aka 'const std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >&'} from expression of type 'boost::posix_time::ptime'
   30 |         gigasecond::advance(time_from_string("1977-06-13 00:00:00"));
      |                             ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~
In file included from /testbed/gigasecond_test.cpp:1:
/testbed/gigasecond.h:9:92: note: in passing argument 1 of 'std::chrono::_V2::system_clock::time_point gigasecond::advance(const time_point&)'
    9 | std::chrono::system_clock::time_point advance(const std::chrono::system_clock::time_point &start);
      |                                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/gigasecond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/gigasecond_test.cpp:39:45: error: invalid initialization of reference of type 'const time_point&' {aka 'const std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >&'} from expression of type 'boost::posix_time::ptime'
   39 |         gigasecond::advance(time_from_string("1959-07-19 00:00:00"));
      |                             ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~
In file included from /testbed/gigasecond_test.cpp:1:
/testbed/gigasecond.h:9:92: note: in passing argument 1 of 'std::chrono::_V2::system_clock::time_point gigasecond::advance(const time_point&)'
    9 | std::chrono::system_clock::time_point advance(const std::chrono::system_clock::time_point &start);
      |                                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/gigasecond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/gigasecond_test.cpp:47:45: error: invalid initialization of reference of type 'const time_point&' {aka 'const std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >&'} from expression of type 'boost::posix_time::ptime'
   47 |         gigasecond::advance(time_from_string("2015-01-24 22:00:00"));
      |                             ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~
In file included from /testbed/gigasecond_test.cpp:1:
/testbed/gigasecond.h:9:92: note: in passing argument 1 of 'std::chrono::_V2::system_clock::time_point gigasecond::advance(const time_point&)'
    9 | std::chrono::system_clock::time_point advance(const std::chrono::system_clock::time_point &start);
      |                                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
/testbed/gigasecond_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/gigasecond_test.cpp:56:45: error: invalid initialization of reference of type 'const time_point&' {aka 'const std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >&'} from expression of type 'boost::posix_time::ptime'
   56 |         gigasecond::advance(time_from_string("2015-01-24 23:59:59"));
      |                             ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~
In file included from /testbed/gigasecond_test.cpp:1:
/testbed/gigasecond.h:9:92: note: in passing argument 1 of 'std::chrono::_V2::system_clock::time_point gigasecond::advance(const time_point&)'
    9 | std::chrono::system_clock::time_point advance(const std::chrono::system_clock::time_point &start);
      |                                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
make[2]: *** [CMakeFiles/gigasecond.dir/build.make:76: CMakeFiles/gigasecond.dir/gigasecond_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/gigasecond.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
