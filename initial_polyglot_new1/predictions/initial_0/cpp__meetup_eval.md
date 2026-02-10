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
[ 25%] Building CXX object CMakeFiles/meetup.dir/meetup_test.cpp.o
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____0()':
/testbed/meetup_test.cpp:17:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   17 |     const meetup::scheduler meetup{boost::gregorian::May, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:20:31: error: expected primary-expression before '.' token
   20 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:20:31: error: expected primary-expression before '.' token
   20 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
/testbed/meetup_test.cpp:20:31: error: expected primary-expression before '.' token
   20 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____2()':
/testbed/meetup_test.cpp:26:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   26 |     const meetup::scheduler meetup{boost::gregorian::Aug, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:29:31: error: expected primary-expression before '.' token
   29 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:29:31: error: expected primary-expression before '.' token
   29 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
/testbed/meetup_test.cpp:29:31: error: expected primary-expression before '.' token
   29 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____4()':
/testbed/meetup_test.cpp:34:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   34 |     const meetup::scheduler meetup{boost::gregorian::Sep, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:37:31: error: expected primary-expression before '.' token
   37 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:37:31: error: expected primary-expression before '.' token
   37 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
/testbed/meetup_test.cpp:37:31: error: expected primary-expression before '.' token
   37 |     REQUIRE(expected == meetup.monteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____6()':
/testbed/meetup_test.cpp:42:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   42 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:45:31: error: expected primary-expression before '.' token
   45 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:45:31: error: expected primary-expression before '.' token
   45 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
/testbed/meetup_test.cpp:45:31: error: expected primary-expression before '.' token
   45 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____8()':
/testbed/meetup_test.cpp:50:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   50 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:53:31: error: expected primary-expression before '.' token
   53 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:53:31: error: expected primary-expression before '.' token
   53 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
/testbed/meetup_test.cpp:53:31: error: expected primary-expression before '.' token
   53 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____10()':
/testbed/meetup_test.cpp:58:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   58 |     const meetup::scheduler meetup{boost::gregorian::Aug, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:61:31: error: expected primary-expression before '.' token
   61 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:61:31: error: expected primary-expression before '.' token
   61 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
/testbed/meetup_test.cpp:61:31: error: expected primary-expression before '.' token
   61 |     REQUIRE(expected == meetup.tuesteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____12()':
/testbed/meetup_test.cpp:66:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   66 |     const meetup::scheduler meetup{boost::gregorian::Jan, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:69:31: error: expected primary-expression before '.' token
   69 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:69:31: error: expected primary-expression before '.' token
   69 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
/testbed/meetup_test.cpp:69:31: error: expected primary-expression before '.' token
   69 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____14()':
/testbed/meetup_test.cpp:74:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   74 |     const meetup::scheduler meetup{boost::gregorian::Feb, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:77:31: error: expected primary-expression before '.' token
   77 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:77:31: error: expected primary-expression before '.' token
   77 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
/testbed/meetup_test.cpp:77:31: error: expected primary-expression before '.' token
   77 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____16()':
/testbed/meetup_test.cpp:82:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   82 |     const meetup::scheduler meetup{boost::gregorian::Jun, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:85:31: error: expected primary-expression before '.' token
   85 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:85:31: error: expected primary-expression before '.' token
   85 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
/testbed/meetup_test.cpp:85:31: error: expected primary-expression before '.' token
   85 |     REQUIRE(expected == meetup.wednesteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____18()':
/testbed/meetup_test.cpp:90:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   90 |     const meetup::scheduler meetup{boost::gregorian::May, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:93:31: error: expected primary-expression before '.' token
   93 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:93:31: error: expected primary-expression before '.' token
   93 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
/testbed/meetup_test.cpp:93:31: error: expected primary-expression before '.' token
   93 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____20()':
/testbed/meetup_test.cpp:98:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
   98 |     const meetup::scheduler meetup{boost::gregorian::Jun, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:101:31: error: expected primary-expression before '.' token
  101 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:101:31: error: expected primary-expression before '.' token
  101 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
/testbed/meetup_test.cpp:101:31: error: expected primary-expression before '.' token
  101 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____22()':
/testbed/meetup_test.cpp:106:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  106 |     const meetup::scheduler meetup{boost::gregorian::Sep, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:109:31: error: expected primary-expression before '.' token
  109 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:109:31: error: expected primary-expression before '.' token
  109 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
/testbed/meetup_test.cpp:109:31: error: expected primary-expression before '.' token
  109 |     REQUIRE(expected == meetup.thursteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____24()':
/testbed/meetup_test.cpp:114:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  114 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:117:31: error: expected primary-expression before '.' token
  117 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:117:31: error: expected primary-expression before '.' token
  117 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
/testbed/meetup_test.cpp:117:31: error: expected primary-expression before '.' token
  117 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____26()':
/testbed/meetup_test.cpp:122:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  122 |     const meetup::scheduler meetup{boost::gregorian::Aug, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:125:31: error: expected primary-expression before '.' token
  125 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:125:31: error: expected primary-expression before '.' token
  125 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
/testbed/meetup_test.cpp:125:31: error: expected primary-expression before '.' token
  125 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____28()':
/testbed/meetup_test.cpp:130:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  130 |     const meetup::scheduler meetup{boost::gregorian::Sep, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:133:31: error: expected primary-expression before '.' token
  133 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:133:31: error: expected primary-expression before '.' token
  133 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
/testbed/meetup_test.cpp:133:31: error: expected primary-expression before '.' token
  133 |     REQUIRE(expected == meetup.friteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____30()':
/testbed/meetup_test.cpp:138:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  138 |     const meetup::scheduler meetup{boost::gregorian::Feb, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:141:31: error: expected primary-expression before '.' token
  141 |     REQUIRE(expected == meetup.saturteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:141:31: error: expected primary-expression before '.' token
  141 |     REQUIRE(expected == meetup.saturteenth());
      |                               ^
/testbed/meetup_test.cpp:141:31: error: expected primary-expression before '.' token
  141 |     REQUIRE(expected == meetup.saturteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____32()':
/testbed/meetup_test.cpp:146:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  146 |     const meetup::scheduler meetup{boost::gregorian::Oct, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:149:31: error: expected primary-expression before '.' token
  149 |     REQUIRE(expected == meetup.saturteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:149:31: error: expected primary-expression before '.' token
  149 |     REQUIRE(expected == meetup.saturteenth());
      |                               ^
/testbed/meetup_test.cpp:149:31: error: expected primary-expression before '.' token
  149 |     REQUIRE(expected == meetup.saturteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____34()':
/testbed/meetup_test.cpp:154:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  154 |     const meetup::scheduler meetup{boost::gregorian::May, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:157:31: error: expected primary-expression before '.' token
  157 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:157:31: error: expected primary-expression before '.' token
  157 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
/testbed/meetup_test.cpp:157:31: error: expected primary-expression before '.' token
  157 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____36()':
/testbed/meetup_test.cpp:162:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  162 |     const meetup::scheduler meetup{boost::gregorian::Jun, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:165:31: error: expected primary-expression before '.' token
  165 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:165:31: error: expected primary-expression before '.' token
  165 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
/testbed/meetup_test.cpp:165:31: error: expected primary-expression before '.' token
  165 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____38()':
/testbed/meetup_test.cpp:170:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  170 |     const meetup::scheduler meetup{boost::gregorian::Oct, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:173:31: error: expected primary-expression before '.' token
  173 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:173:31: error: expected primary-expression before '.' token
  173 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
/testbed/meetup_test.cpp:173:31: error: expected primary-expression before '.' token
  173 |     REQUIRE(expected == meetup.sunteenth());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____40()':
/testbed/meetup_test.cpp:178:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  178 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:181:31: error: expected primary-expression before '.' token
  181 |     REQUIRE(expected == meetup.first_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:181:31: error: expected primary-expression before '.' token
  181 |     REQUIRE(expected == meetup.first_monday());
      |                               ^
/testbed/meetup_test.cpp:181:31: error: expected primary-expression before '.' token
  181 |     REQUIRE(expected == meetup.first_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____42()':
/testbed/meetup_test.cpp:186:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  186 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:189:31: error: expected primary-expression before '.' token
  189 |     REQUIRE(expected == meetup.first_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:189:31: error: expected primary-expression before '.' token
  189 |     REQUIRE(expected == meetup.first_monday());
      |                               ^
/testbed/meetup_test.cpp:189:31: error: expected primary-expression before '.' token
  189 |     REQUIRE(expected == meetup.first_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____44()':
/testbed/meetup_test.cpp:194:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  194 |     const meetup::scheduler meetup{boost::gregorian::May, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:197:31: error: expected primary-expression before '.' token
  197 |     REQUIRE(expected == meetup.first_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:197:31: error: expected primary-expression before '.' token
  197 |     REQUIRE(expected == meetup.first_tuesday());
      |                               ^
/testbed/meetup_test.cpp:197:31: error: expected primary-expression before '.' token
  197 |     REQUIRE(expected == meetup.first_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____46()':
/testbed/meetup_test.cpp:202:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  202 |     const meetup::scheduler meetup{boost::gregorian::Jun, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:205:31: error: expected primary-expression before '.' token
  205 |     REQUIRE(expected == meetup.first_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:205:31: error: expected primary-expression before '.' token
  205 |     REQUIRE(expected == meetup.first_tuesday());
      |                               ^
/testbed/meetup_test.cpp:205:31: error: expected primary-expression before '.' token
  205 |     REQUIRE(expected == meetup.first_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____48()':
/testbed/meetup_test.cpp:210:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  210 |     const meetup::scheduler meetup{boost::gregorian::Jul, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:213:31: error: expected primary-expression before '.' token
  213 |     REQUIRE(expected == meetup.first_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:213:31: error: expected primary-expression before '.' token
  213 |     REQUIRE(expected == meetup.first_wednesday());
      |                               ^
/testbed/meetup_test.cpp:213:31: error: expected primary-expression before '.' token
  213 |     REQUIRE(expected == meetup.first_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____50()':
/testbed/meetup_test.cpp:218:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  218 |     const meetup::scheduler meetup{boost::gregorian::Aug, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:221:31: error: expected primary-expression before '.' token
  221 |     REQUIRE(expected == meetup.first_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:221:31: error: expected primary-expression before '.' token
  221 |     REQUIRE(expected == meetup.first_wednesday());
      |                               ^
/testbed/meetup_test.cpp:221:31: error: expected primary-expression before '.' token
  221 |     REQUIRE(expected == meetup.first_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____52()':
/testbed/meetup_test.cpp:226:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  226 |     const meetup::scheduler meetup{boost::gregorian::Sep, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:229:31: error: expected primary-expression before '.' token
  229 |     REQUIRE(expected == meetup.first_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:229:31: error: expected primary-expression before '.' token
  229 |     REQUIRE(expected == meetup.first_thursday());
      |                               ^
/testbed/meetup_test.cpp:229:31: error: expected primary-expression before '.' token
  229 |     REQUIRE(expected == meetup.first_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____54()':
/testbed/meetup_test.cpp:234:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  234 |     const meetup::scheduler meetup{boost::gregorian::Oct, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:237:31: error: expected primary-expression before '.' token
  237 |     REQUIRE(expected == meetup.first_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:237:31: error: expected primary-expression before '.' token
  237 |     REQUIRE(expected == meetup.first_thursday());
      |                               ^
/testbed/meetup_test.cpp:237:31: error: expected primary-expression before '.' token
  237 |     REQUIRE(expected == meetup.first_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____56()':
/testbed/meetup_test.cpp:242:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  242 |     const meetup::scheduler meetup{boost::gregorian::Nov, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:245:31: error: expected primary-expression before '.' token
  245 |     REQUIRE(expected == meetup.first_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:245:31: error: expected primary-expression before '.' token
  245 |     REQUIRE(expected == meetup.first_friday());
      |                               ^
/testbed/meetup_test.cpp:245:31: error: expected primary-expression before '.' token
  245 |     REQUIRE(expected == meetup.first_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____58()':
/testbed/meetup_test.cpp:250:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  250 |     const meetup::scheduler meetup{boost::gregorian::Dec, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:253:31: error: expected primary-expression before '.' token
  253 |     REQUIRE(expected == meetup.first_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:253:31: error: expected primary-expression before '.' token
  253 |     REQUIRE(expected == meetup.first_friday());
      |                               ^
/testbed/meetup_test.cpp:253:31: error: expected primary-expression before '.' token
  253 |     REQUIRE(expected == meetup.first_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____60()':
/testbed/meetup_test.cpp:258:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  258 |     const meetup::scheduler meetup{boost::gregorian::Jan, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:261:31: error: expected primary-expression before '.' token
  261 |     REQUIRE(expected == meetup.first_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:261:31: error: expected primary-expression before '.' token
  261 |     REQUIRE(expected == meetup.first_saturday());
      |                               ^
/testbed/meetup_test.cpp:261:31: error: expected primary-expression before '.' token
  261 |     REQUIRE(expected == meetup.first_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____62()':
/testbed/meetup_test.cpp:266:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  266 |     const meetup::scheduler meetup{boost::gregorian::Feb, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:269:31: error: expected primary-expression before '.' token
  269 |     REQUIRE(expected == meetup.first_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:269:31: error: expected primary-expression before '.' token
  269 |     REQUIRE(expected == meetup.first_saturday());
      |                               ^
/testbed/meetup_test.cpp:269:31: error: expected primary-expression before '.' token
  269 |     REQUIRE(expected == meetup.first_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____64()':
/testbed/meetup_test.cpp:274:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  274 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:277:31: error: expected primary-expression before '.' token
  277 |     REQUIRE(expected == meetup.first_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:277:31: error: expected primary-expression before '.' token
  277 |     REQUIRE(expected == meetup.first_sunday());
      |                               ^
/testbed/meetup_test.cpp:277:31: error: expected primary-expression before '.' token
  277 |     REQUIRE(expected == meetup.first_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____66()':
/testbed/meetup_test.cpp:282:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  282 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:285:31: error: expected primary-expression before '.' token
  285 |     REQUIRE(expected == meetup.first_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:285:31: error: expected primary-expression before '.' token
  285 |     REQUIRE(expected == meetup.first_sunday());
      |                               ^
/testbed/meetup_test.cpp:285:31: error: expected primary-expression before '.' token
  285 |     REQUIRE(expected == meetup.first_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____68()':
/testbed/meetup_test.cpp:290:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  290 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:293:31: error: expected primary-expression before '.' token
  293 |     REQUIRE(expected == meetup.second_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:293:31: error: expected primary-expression before '.' token
  293 |     REQUIRE(expected == meetup.second_monday());
      |                               ^
/testbed/meetup_test.cpp:293:31: error: expected primary-expression before '.' token
  293 |     REQUIRE(expected == meetup.second_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____70()':
/testbed/meetup_test.cpp:298:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  298 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:301:31: error: expected primary-expression before '.' token
  301 |     REQUIRE(expected == meetup.second_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:301:31: error: expected primary-expression before '.' token
  301 |     REQUIRE(expected == meetup.second_monday());
      |                               ^
/testbed/meetup_test.cpp:301:31: error: expected primary-expression before '.' token
  301 |     REQUIRE(expected == meetup.second_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____72()':
/testbed/meetup_test.cpp:306:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  306 |     const meetup::scheduler meetup{boost::gregorian::May, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:309:31: error: expected primary-expression before '.' token
  309 |     REQUIRE(expected == meetup.second_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:309:31: error: expected primary-expression before '.' token
  309 |     REQUIRE(expected == meetup.second_tuesday());
      |                               ^
/testbed/meetup_test.cpp:309:31: error: expected primary-expression before '.' token
  309 |     REQUIRE(expected == meetup.second_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____74()':
/testbed/meetup_test.cpp:314:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  314 |     const meetup::scheduler meetup{boost::gregorian::Jun, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:317:31: error: expected primary-expression before '.' token
  317 |     REQUIRE(expected == meetup.second_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:317:31: error: expected primary-expression before '.' token
  317 |     REQUIRE(expected == meetup.second_tuesday());
      |                               ^
/testbed/meetup_test.cpp:317:31: error: expected primary-expression before '.' token
  317 |     REQUIRE(expected == meetup.second_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____76()':
/testbed/meetup_test.cpp:322:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  322 |     const meetup::scheduler meetup{boost::gregorian::Jul, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:325:31: error: expected primary-expression before '.' token
  325 |     REQUIRE(expected == meetup.second_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:325:31: error: expected primary-expression before '.' token
  325 |     REQUIRE(expected == meetup.second_wednesday());
      |                               ^
/testbed/meetup_test.cpp:325:31: error: expected primary-expression before '.' token
  325 |     REQUIRE(expected == meetup.second_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____78()':
/testbed/meetup_test.cpp:330:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  330 |     const meetup::scheduler meetup{boost::gregorian::Aug, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:333:31: error: expected primary-expression before '.' token
  333 |     REQUIRE(expected == meetup.second_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:333:31: error: expected primary-expression before '.' token
  333 |     REQUIRE(expected == meetup.second_wednesday());
      |                               ^
/testbed/meetup_test.cpp:333:31: error: expected primary-expression before '.' token
  333 |     REQUIRE(expected == meetup.second_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____80()':
/testbed/meetup_test.cpp:338:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  338 |     const meetup::scheduler meetup{boost::gregorian::Sep, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:341:31: error: expected primary-expression before '.' token
  341 |     REQUIRE(expected == meetup.second_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:341:31: error: expected primary-expression before '.' token
  341 |     REQUIRE(expected == meetup.second_thursday());
      |                               ^
/testbed/meetup_test.cpp:341:31: error: expected primary-expression before '.' token
  341 |     REQUIRE(expected == meetup.second_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____82()':
/testbed/meetup_test.cpp:346:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  346 |     const meetup::scheduler meetup{boost::gregorian::Oct, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:349:31: error: expected primary-expression before '.' token
  349 |     REQUIRE(expected == meetup.second_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:349:31: error: expected primary-expression before '.' token
  349 |     REQUIRE(expected == meetup.second_thursday());
      |                               ^
/testbed/meetup_test.cpp:349:31: error: expected primary-expression before '.' token
  349 |     REQUIRE(expected == meetup.second_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____84()':
/testbed/meetup_test.cpp:354:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  354 |     const meetup::scheduler meetup{boost::gregorian::Nov, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:357:31: error: expected primary-expression before '.' token
  357 |     REQUIRE(expected == meetup.second_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:357:31: error: expected primary-expression before '.' token
  357 |     REQUIRE(expected == meetup.second_friday());
      |                               ^
/testbed/meetup_test.cpp:357:31: error: expected primary-expression before '.' token
  357 |     REQUIRE(expected == meetup.second_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____86()':
/testbed/meetup_test.cpp:362:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  362 |     const meetup::scheduler meetup{boost::gregorian::Dec, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:365:31: error: expected primary-expression before '.' token
  365 |     REQUIRE(expected == meetup.second_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:365:31: error: expected primary-expression before '.' token
  365 |     REQUIRE(expected == meetup.second_friday());
      |                               ^
/testbed/meetup_test.cpp:365:31: error: expected primary-expression before '.' token
  365 |     REQUIRE(expected == meetup.second_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____88()':
/testbed/meetup_test.cpp:370:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  370 |     const meetup::scheduler meetup{boost::gregorian::Jan, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:373:31: error: expected primary-expression before '.' token
  373 |     REQUIRE(expected == meetup.second_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:373:31: error: expected primary-expression before '.' token
  373 |     REQUIRE(expected == meetup.second_saturday());
      |                               ^
/testbed/meetup_test.cpp:373:31: error: expected primary-expression before '.' token
  373 |     REQUIRE(expected == meetup.second_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____90()':
/testbed/meetup_test.cpp:378:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  378 |     const meetup::scheduler meetup{boost::gregorian::Feb, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:381:31: error: expected primary-expression before '.' token
  381 |     REQUIRE(expected == meetup.second_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:381:31: error: expected primary-expression before '.' token
  381 |     REQUIRE(expected == meetup.second_saturday());
      |                               ^
/testbed/meetup_test.cpp:381:31: error: expected primary-expression before '.' token
  381 |     REQUIRE(expected == meetup.second_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____92()':
/testbed/meetup_test.cpp:386:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  386 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:389:31: error: expected primary-expression before '.' token
  389 |     REQUIRE(expected == meetup.second_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:389:31: error: expected primary-expression before '.' token
  389 |     REQUIRE(expected == meetup.second_sunday());
      |                               ^
/testbed/meetup_test.cpp:389:31: error: expected primary-expression before '.' token
  389 |     REQUIRE(expected == meetup.second_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____94()':
/testbed/meetup_test.cpp:394:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  394 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:397:31: error: expected primary-expression before '.' token
  397 |     REQUIRE(expected == meetup.second_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:397:31: error: expected primary-expression before '.' token
  397 |     REQUIRE(expected == meetup.second_sunday());
      |                               ^
/testbed/meetup_test.cpp:397:31: error: expected primary-expression before '.' token
  397 |     REQUIRE(expected == meetup.second_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____96()':
/testbed/meetup_test.cpp:402:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  402 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:405:31: error: expected primary-expression before '.' token
  405 |     REQUIRE(expected == meetup.third_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:405:31: error: expected primary-expression before '.' token
  405 |     REQUIRE(expected == meetup.third_monday());
      |                               ^
/testbed/meetup_test.cpp:405:31: error: expected primary-expression before '.' token
  405 |     REQUIRE(expected == meetup.third_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____98()':
/testbed/meetup_test.cpp:410:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  410 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:413:31: error: expected primary-expression before '.' token
  413 |     REQUIRE(expected == meetup.third_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:413:31: error: expected primary-expression before '.' token
  413 |     REQUIRE(expected == meetup.third_monday());
      |                               ^
/testbed/meetup_test.cpp:413:31: error: expected primary-expression before '.' token
  413 |     REQUIRE(expected == meetup.third_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____100()':
/testbed/meetup_test.cpp:418:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  418 |     const meetup::scheduler meetup{boost::gregorian::May, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:421:31: error: expected primary-expression before '.' token
  421 |     REQUIRE(expected == meetup.third_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:421:31: error: expected primary-expression before '.' token
  421 |     REQUIRE(expected == meetup.third_tuesday());
      |                               ^
/testbed/meetup_test.cpp:421:31: error: expected primary-expression before '.' token
  421 |     REQUIRE(expected == meetup.third_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____102()':
/testbed/meetup_test.cpp:426:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  426 |     const meetup::scheduler meetup{boost::gregorian::Jun, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:429:31: error: expected primary-expression before '.' token
  429 |     REQUIRE(expected == meetup.third_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:429:31: error: expected primary-expression before '.' token
  429 |     REQUIRE(expected == meetup.third_tuesday());
      |                               ^
/testbed/meetup_test.cpp:429:31: error: expected primary-expression before '.' token
  429 |     REQUIRE(expected == meetup.third_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____104()':
/testbed/meetup_test.cpp:434:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  434 |     const meetup::scheduler meetup{boost::gregorian::Jul, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:437:31: error: expected primary-expression before '.' token
  437 |     REQUIRE(expected == meetup.third_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:437:31: error: expected primary-expression before '.' token
  437 |     REQUIRE(expected == meetup.third_wednesday());
      |                               ^
/testbed/meetup_test.cpp:437:31: error: expected primary-expression before '.' token
  437 |     REQUIRE(expected == meetup.third_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____106()':
/testbed/meetup_test.cpp:442:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  442 |     const meetup::scheduler meetup{boost::gregorian::Aug, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:445:31: error: expected primary-expression before '.' token
  445 |     REQUIRE(expected == meetup.third_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:445:31: error: expected primary-expression before '.' token
  445 |     REQUIRE(expected == meetup.third_wednesday());
      |                               ^
/testbed/meetup_test.cpp:445:31: error: expected primary-expression before '.' token
  445 |     REQUIRE(expected == meetup.third_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____108()':
/testbed/meetup_test.cpp:450:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  450 |     const meetup::scheduler meetup{boost::gregorian::Sep, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:453:31: error: expected primary-expression before '.' token
  453 |     REQUIRE(expected == meetup.third_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:453:31: error: expected primary-expression before '.' token
  453 |     REQUIRE(expected == meetup.third_thursday());
      |                               ^
/testbed/meetup_test.cpp:453:31: error: expected primary-expression before '.' token
  453 |     REQUIRE(expected == meetup.third_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____110()':
/testbed/meetup_test.cpp:458:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  458 |     const meetup::scheduler meetup{boost::gregorian::Oct, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:461:31: error: expected primary-expression before '.' token
  461 |     REQUIRE(expected == meetup.third_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:461:31: error: expected primary-expression before '.' token
  461 |     REQUIRE(expected == meetup.third_thursday());
      |                               ^
/testbed/meetup_test.cpp:461:31: error: expected primary-expression before '.' token
  461 |     REQUIRE(expected == meetup.third_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____112()':
/testbed/meetup_test.cpp:466:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  466 |     const meetup::scheduler meetup{boost::gregorian::Nov, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:469:31: error: expected primary-expression before '.' token
  469 |     REQUIRE(expected == meetup.third_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:469:31: error: expected primary-expression before '.' token
  469 |     REQUIRE(expected == meetup.third_friday());
      |                               ^
/testbed/meetup_test.cpp:469:31: error: expected primary-expression before '.' token
  469 |     REQUIRE(expected == meetup.third_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____114()':
/testbed/meetup_test.cpp:474:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  474 |     const meetup::scheduler meetup{boost::gregorian::Dec, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:477:31: error: expected primary-expression before '.' token
  477 |     REQUIRE(expected == meetup.third_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:477:31: error: expected primary-expression before '.' token
  477 |     REQUIRE(expected == meetup.third_friday());
      |                               ^
/testbed/meetup_test.cpp:477:31: error: expected primary-expression before '.' token
  477 |     REQUIRE(expected == meetup.third_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____116()':
/testbed/meetup_test.cpp:482:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  482 |     const meetup::scheduler meetup{boost::gregorian::Jan, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:485:31: error: expected primary-expression before '.' token
  485 |     REQUIRE(expected == meetup.third_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:485:31: error: expected primary-expression before '.' token
  485 |     REQUIRE(expected == meetup.third_saturday());
      |                               ^
/testbed/meetup_test.cpp:485:31: error: expected primary-expression before '.' token
  485 |     REQUIRE(expected == meetup.third_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____118()':
/testbed/meetup_test.cpp:490:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  490 |     const meetup::scheduler meetup{boost::gregorian::Feb, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:493:31: error: expected primary-expression before '.' token
  493 |     REQUIRE(expected == meetup.third_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:493:31: error: expected primary-expression before '.' token
  493 |     REQUIRE(expected == meetup.third_saturday());
      |                               ^
/testbed/meetup_test.cpp:493:31: error: expected primary-expression before '.' token
  493 |     REQUIRE(expected == meetup.third_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____120()':
/testbed/meetup_test.cpp:498:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  498 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:501:31: error: expected primary-expression before '.' token
  501 |     REQUIRE(expected == meetup.third_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:501:31: error: expected primary-expression before '.' token
  501 |     REQUIRE(expected == meetup.third_sunday());
      |                               ^
/testbed/meetup_test.cpp:501:31: error: expected primary-expression before '.' token
  501 |     REQUIRE(expected == meetup.third_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____122()':
/testbed/meetup_test.cpp:506:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  506 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:509:31: error: expected primary-expression before '.' token
  509 |     REQUIRE(expected == meetup.third_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:509:31: error: expected primary-expression before '.' token
  509 |     REQUIRE(expected == meetup.third_sunday());
      |                               ^
/testbed/meetup_test.cpp:509:31: error: expected primary-expression before '.' token
  509 |     REQUIRE(expected == meetup.third_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____124()':
/testbed/meetup_test.cpp:514:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  514 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:517:31: error: expected primary-expression before '.' token
  517 |     REQUIRE(expected == meetup.fourth_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:517:31: error: expected primary-expression before '.' token
  517 |     REQUIRE(expected == meetup.fourth_monday());
      |                               ^
/testbed/meetup_test.cpp:517:31: error: expected primary-expression before '.' token
  517 |     REQUIRE(expected == meetup.fourth_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____126()':
/testbed/meetup_test.cpp:522:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  522 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:525:31: error: expected primary-expression before '.' token
  525 |     REQUIRE(expected == meetup.fourth_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:525:31: error: expected primary-expression before '.' token
  525 |     REQUIRE(expected == meetup.fourth_monday());
      |                               ^
/testbed/meetup_test.cpp:525:31: error: expected primary-expression before '.' token
  525 |     REQUIRE(expected == meetup.fourth_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____128()':
/testbed/meetup_test.cpp:530:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  530 |     const meetup::scheduler meetup{boost::gregorian::May, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:533:31: error: expected primary-expression before '.' token
  533 |     REQUIRE(expected == meetup.fourth_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:533:31: error: expected primary-expression before '.' token
  533 |     REQUIRE(expected == meetup.fourth_tuesday());
      |                               ^
/testbed/meetup_test.cpp:533:31: error: expected primary-expression before '.' token
  533 |     REQUIRE(expected == meetup.fourth_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____130()':
/testbed/meetup_test.cpp:538:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  538 |     const meetup::scheduler meetup{boost::gregorian::Jun, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:541:31: error: expected primary-expression before '.' token
  541 |     REQUIRE(expected == meetup.fourth_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:541:31: error: expected primary-expression before '.' token
  541 |     REQUIRE(expected == meetup.fourth_tuesday());
      |                               ^
/testbed/meetup_test.cpp:541:31: error: expected primary-expression before '.' token
  541 |     REQUIRE(expected == meetup.fourth_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____132()':
/testbed/meetup_test.cpp:546:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  546 |     const meetup::scheduler meetup{boost::gregorian::Jul, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:549:31: error: expected primary-expression before '.' token
  549 |     REQUIRE(expected == meetup.fourth_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:549:31: error: expected primary-expression before '.' token
  549 |     REQUIRE(expected == meetup.fourth_wednesday());
      |                               ^
/testbed/meetup_test.cpp:549:31: error: expected primary-expression before '.' token
  549 |     REQUIRE(expected == meetup.fourth_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____134()':
/testbed/meetup_test.cpp:554:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  554 |     const meetup::scheduler meetup{boost::gregorian::Aug, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:557:31: error: expected primary-expression before '.' token
  557 |     REQUIRE(expected == meetup.fourth_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:557:31: error: expected primary-expression before '.' token
  557 |     REQUIRE(expected == meetup.fourth_wednesday());
      |                               ^
/testbed/meetup_test.cpp:557:31: error: expected primary-expression before '.' token
  557 |     REQUIRE(expected == meetup.fourth_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____136()':
/testbed/meetup_test.cpp:562:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  562 |     const meetup::scheduler meetup{boost::gregorian::Sep, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:565:31: error: expected primary-expression before '.' token
  565 |     REQUIRE(expected == meetup.fourth_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:565:31: error: expected primary-expression before '.' token
  565 |     REQUIRE(expected == meetup.fourth_thursday());
      |                               ^
/testbed/meetup_test.cpp:565:31: error: expected primary-expression before '.' token
  565 |     REQUIRE(expected == meetup.fourth_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____138()':
/testbed/meetup_test.cpp:570:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  570 |     const meetup::scheduler meetup{boost::gregorian::Oct, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:573:31: error: expected primary-expression before '.' token
  573 |     REQUIRE(expected == meetup.fourth_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:573:31: error: expected primary-expression before '.' token
  573 |     REQUIRE(expected == meetup.fourth_thursday());
      |                               ^
/testbed/meetup_test.cpp:573:31: error: expected primary-expression before '.' token
  573 |     REQUIRE(expected == meetup.fourth_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____140()':
/testbed/meetup_test.cpp:578:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  578 |     const meetup::scheduler meetup{boost::gregorian::Nov, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:581:31: error: expected primary-expression before '.' token
  581 |     REQUIRE(expected == meetup.fourth_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:581:31: error: expected primary-expression before '.' token
  581 |     REQUIRE(expected == meetup.fourth_friday());
      |                               ^
/testbed/meetup_test.cpp:581:31: error: expected primary-expression before '.' token
  581 |     REQUIRE(expected == meetup.fourth_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____142()':
/testbed/meetup_test.cpp:586:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  586 |     const meetup::scheduler meetup{boost::gregorian::Dec, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:589:31: error: expected primary-expression before '.' token
  589 |     REQUIRE(expected == meetup.fourth_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:589:31: error: expected primary-expression before '.' token
  589 |     REQUIRE(expected == meetup.fourth_friday());
      |                               ^
/testbed/meetup_test.cpp:589:31: error: expected primary-expression before '.' token
  589 |     REQUIRE(expected == meetup.fourth_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____144()':
/testbed/meetup_test.cpp:594:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  594 |     const meetup::scheduler meetup{boost::gregorian::Jan, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:597:31: error: expected primary-expression before '.' token
  597 |     REQUIRE(expected == meetup.fourth_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:597:31: error: expected primary-expression before '.' token
  597 |     REQUIRE(expected == meetup.fourth_saturday());
      |                               ^
/testbed/meetup_test.cpp:597:31: error: expected primary-expression before '.' token
  597 |     REQUIRE(expected == meetup.fourth_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____146()':
/testbed/meetup_test.cpp:602:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  602 |     const meetup::scheduler meetup{boost::gregorian::Feb, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:605:31: error: expected primary-expression before '.' token
  605 |     REQUIRE(expected == meetup.fourth_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:605:31: error: expected primary-expression before '.' token
  605 |     REQUIRE(expected == meetup.fourth_saturday());
      |                               ^
/testbed/meetup_test.cpp:605:31: error: expected primary-expression before '.' token
  605 |     REQUIRE(expected == meetup.fourth_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____148()':
/testbed/meetup_test.cpp:610:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  610 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:613:31: error: expected primary-expression before '.' token
  613 |     REQUIRE(expected == meetup.fourth_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:613:31: error: expected primary-expression before '.' token
  613 |     REQUIRE(expected == meetup.fourth_sunday());
      |                               ^
/testbed/meetup_test.cpp:613:31: error: expected primary-expression before '.' token
  613 |     REQUIRE(expected == meetup.fourth_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____150()':
/testbed/meetup_test.cpp:618:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  618 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:621:31: error: expected primary-expression before '.' token
  621 |     REQUIRE(expected == meetup.fourth_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:621:31: error: expected primary-expression before '.' token
  621 |     REQUIRE(expected == meetup.fourth_sunday());
      |                               ^
/testbed/meetup_test.cpp:621:31: error: expected primary-expression before '.' token
  621 |     REQUIRE(expected == meetup.fourth_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____152()':
/testbed/meetup_test.cpp:626:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  626 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:629:31: error: expected primary-expression before '.' token
  629 |     REQUIRE(expected == meetup.last_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:629:31: error: expected primary-expression before '.' token
  629 |     REQUIRE(expected == meetup.last_monday());
      |                               ^
/testbed/meetup_test.cpp:629:31: error: expected primary-expression before '.' token
  629 |     REQUIRE(expected == meetup.last_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____154()':
/testbed/meetup_test.cpp:634:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  634 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:637:31: error: expected primary-expression before '.' token
  637 |     REQUIRE(expected == meetup.last_monday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:637:31: error: expected primary-expression before '.' token
  637 |     REQUIRE(expected == meetup.last_monday());
      |                               ^
/testbed/meetup_test.cpp:637:31: error: expected primary-expression before '.' token
  637 |     REQUIRE(expected == meetup.last_monday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____156()':
/testbed/meetup_test.cpp:642:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  642 |     const meetup::scheduler meetup{boost::gregorian::May, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:645:31: error: expected primary-expression before '.' token
  645 |     REQUIRE(expected == meetup.last_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:645:31: error: expected primary-expression before '.' token
  645 |     REQUIRE(expected == meetup.last_tuesday());
      |                               ^
/testbed/meetup_test.cpp:645:31: error: expected primary-expression before '.' token
  645 |     REQUIRE(expected == meetup.last_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____158()':
/testbed/meetup_test.cpp:650:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  650 |     const meetup::scheduler meetup{boost::gregorian::Jun, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:653:31: error: expected primary-expression before '.' token
  653 |     REQUIRE(expected == meetup.last_tuesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:653:31: error: expected primary-expression before '.' token
  653 |     REQUIRE(expected == meetup.last_tuesday());
      |                               ^
/testbed/meetup_test.cpp:653:31: error: expected primary-expression before '.' token
  653 |     REQUIRE(expected == meetup.last_tuesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____160()':
/testbed/meetup_test.cpp:658:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  658 |     const meetup::scheduler meetup{boost::gregorian::Jul, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:661:31: error: expected primary-expression before '.' token
  661 |     REQUIRE(expected == meetup.last_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:661:31: error: expected primary-expression before '.' token
  661 |     REQUIRE(expected == meetup.last_wednesday());
      |                               ^
/testbed/meetup_test.cpp:661:31: error: expected primary-expression before '.' token
  661 |     REQUIRE(expected == meetup.last_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____162()':
/testbed/meetup_test.cpp:666:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  666 |     const meetup::scheduler meetup{boost::gregorian::Aug, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:669:31: error: expected primary-expression before '.' token
  669 |     REQUIRE(expected == meetup.last_wednesday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:669:31: error: expected primary-expression before '.' token
  669 |     REQUIRE(expected == meetup.last_wednesday());
      |                               ^
/testbed/meetup_test.cpp:669:31: error: expected primary-expression before '.' token
  669 |     REQUIRE(expected == meetup.last_wednesday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____164()':
/testbed/meetup_test.cpp:674:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  674 |     const meetup::scheduler meetup{boost::gregorian::Sep, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:677:31: error: expected primary-expression before '.' token
  677 |     REQUIRE(expected == meetup.last_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:677:31: error: expected primary-expression before '.' token
  677 |     REQUIRE(expected == meetup.last_thursday());
      |                               ^
/testbed/meetup_test.cpp:677:31: error: expected primary-expression before '.' token
  677 |     REQUIRE(expected == meetup.last_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____166()':
/testbed/meetup_test.cpp:682:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  682 |     const meetup::scheduler meetup{boost::gregorian::Oct, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:685:31: error: expected primary-expression before '.' token
  685 |     REQUIRE(expected == meetup.last_thursday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:685:31: error: expected primary-expression before '.' token
  685 |     REQUIRE(expected == meetup.last_thursday());
      |                               ^
/testbed/meetup_test.cpp:685:31: error: expected primary-expression before '.' token
  685 |     REQUIRE(expected == meetup.last_thursday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____168()':
/testbed/meetup_test.cpp:690:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  690 |     const meetup::scheduler meetup{boost::gregorian::Nov, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:693:31: error: expected primary-expression before '.' token
  693 |     REQUIRE(expected == meetup.last_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:693:31: error: expected primary-expression before '.' token
  693 |     REQUIRE(expected == meetup.last_friday());
      |                               ^
/testbed/meetup_test.cpp:693:31: error: expected primary-expression before '.' token
  693 |     REQUIRE(expected == meetup.last_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____170()':
/testbed/meetup_test.cpp:698:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  698 |     const meetup::scheduler meetup{boost::gregorian::Dec, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:701:31: error: expected primary-expression before '.' token
  701 |     REQUIRE(expected == meetup.last_friday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:701:31: error: expected primary-expression before '.' token
  701 |     REQUIRE(expected == meetup.last_friday());
      |                               ^
/testbed/meetup_test.cpp:701:31: error: expected primary-expression before '.' token
  701 |     REQUIRE(expected == meetup.last_friday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____172()':
/testbed/meetup_test.cpp:706:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  706 |     const meetup::scheduler meetup{boost::gregorian::Jan, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:709:31: error: expected primary-expression before '.' token
  709 |     REQUIRE(expected == meetup.last_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:709:31: error: expected primary-expression before '.' token
  709 |     REQUIRE(expected == meetup.last_saturday());
      |                               ^
/testbed/meetup_test.cpp:709:31: error: expected primary-expression before '.' token
  709 |     REQUIRE(expected == meetup.last_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____174()':
/testbed/meetup_test.cpp:714:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  714 |     const meetup::scheduler meetup{boost::gregorian::Feb, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:717:31: error: expected primary-expression before '.' token
  717 |     REQUIRE(expected == meetup.last_saturday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:717:31: error: expected primary-expression before '.' token
  717 |     REQUIRE(expected == meetup.last_saturday());
      |                               ^
/testbed/meetup_test.cpp:717:31: error: expected primary-expression before '.' token
  717 |     REQUIRE(expected == meetup.last_saturday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____176()':
/testbed/meetup_test.cpp:722:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  722 |     const meetup::scheduler meetup{boost::gregorian::Mar, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:725:31: error: expected primary-expression before '.' token
  725 |     REQUIRE(expected == meetup.last_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:725:31: error: expected primary-expression before '.' token
  725 |     REQUIRE(expected == meetup.last_sunday());
      |                               ^
/testbed/meetup_test.cpp:725:31: error: expected primary-expression before '.' token
  725 |     REQUIRE(expected == meetup.last_sunday());
      |                               ^
/testbed/meetup_test.cpp: In function 'void ____C_A_T_C_H____T_E_S_T____178()':
/testbed/meetup_test.cpp:730:19: error: 'scheduler' in namespace 'meetup' does not name a type; did you mean 'schedule'?
  730 |     const meetup::scheduler meetup{boost::gregorian::Apr, 2013};
      |                   ^~~~~~~~~
      |                   schedule
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:733:31: error: expected primary-expression before '.' token
  733 |     REQUIRE(expected == meetup.last_sunday());
      |                               ^
In file included from /testbed/meetup_test.cpp:6:
/testbed/meetup_test.cpp:733:31: error: expected primary-expression before '.' token
  733 |     REQUIRE(expected == meetup.last_sunday());
      |                               ^
/testbed/meetup_test.cpp:733:31: error: expected primary-expression before '.' token
  733 |     REQUIRE(expected == meetup.last_sunday());
      |                               ^
make[2]: *** [CMakeFiles/meetup.dir/build.make:76: CMakeFiles/meetup.dir/meetup_test.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:85: CMakeFiles/meetup.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
