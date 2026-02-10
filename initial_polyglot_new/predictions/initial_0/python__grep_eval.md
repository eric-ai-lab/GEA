+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 25 items

grep_test.py .........................                                   [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED grep_test.py::GrepTest::test_multiple_files_no_matches_various_flags
PASSED grep_test.py::GrepTest::test_multiple_files_one_match_match_entire_lines_flag
PASSED grep_test.py::GrepTest::test_multiple_files_one_match_multiple_flags
PASSED grep_test.py::GrepTest::test_multiple_files_one_match_no_flags
PASSED grep_test.py::GrepTest::test_multiple_files_one_match_print_file_names_flag
PASSED grep_test.py::GrepTest::test_multiple_files_several_matches_case_insensitive_flag
PASSED grep_test.py::GrepTest::test_multiple_files_several_matches_file_flag_takes_precedence_over_line_number_flag
PASSED grep_test.py::GrepTest::test_multiple_files_several_matches_inverted_and_match_entire_lines_flags
PASSED grep_test.py::GrepTest::test_multiple_files_several_matches_inverted_flag
PASSED grep_test.py::GrepTest::test_multiple_files_several_matches_no_flags
PASSED grep_test.py::GrepTest::test_multiple_files_several_matches_print_line_numbers_flag
PASSED grep_test.py::GrepTest::test_one_file_no_matches_various_flags
PASSED grep_test.py::GrepTest::test_one_file_one_match_case_insensitive_flag
PASSED grep_test.py::GrepTest::test_one_file_one_match_file_flag_takes_precedence_over_line_flag
PASSED grep_test.py::GrepTest::test_one_file_one_match_match_entire_lines_flag
PASSED grep_test.py::GrepTest::test_one_file_one_match_multiple_flags
PASSED grep_test.py::GrepTest::test_one_file_one_match_no_flags
PASSED grep_test.py::GrepTest::test_one_file_one_match_print_file_names_flag
PASSED grep_test.py::GrepTest::test_one_file_one_match_print_line_numbers_flag
PASSED grep_test.py::GrepTest::test_one_file_several_matches_case_insensitive_flag
PASSED grep_test.py::GrepTest::test_one_file_several_matches_inverted_and_match_entire_lines_flags
PASSED grep_test.py::GrepTest::test_one_file_several_matches_inverted_flag
PASSED grep_test.py::GrepTest::test_one_file_several_matches_match_entire_lines_flag
PASSED grep_test.py::GrepTest::test_one_file_several_matches_no_flags
PASSED grep_test.py::GrepTest::test_one_file_several_matches_print_line_numbers_flag
============================== 25 passed in 0.04s ==============================
