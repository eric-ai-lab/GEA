+ cargo test -- --include-ignored
    Updating crates.io index
     Locking 1 package to latest compatible version
 Downloading crates ...
  Downloaded anyhow v1.0.98
   Compiling anyhow v1.0.98
   Compiling grep v1.3.0 (/testbed)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 3.02s
     Running unittests src/lib.rs (target/debug/deps/grep-e21992db709c85bb)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/grep.rs (target/debug/deps/grep-a004f11243fc8040)

running 27 tests
test grep_returns_result ... ok
test multiple_files_one_match_match_entire_lines_flag ... ok
test multiple_files_several_matches_case_insensitive_flag ... ok
test one_file_no_matches_various_flags ... ok
test multiple_files_no_matches_various_flags ... ok
test multiple_files_one_match_no_flags ... ok
test one_file_one_match_case_insensitive_flag ... ok
test multiple_files_one_match_multiple_flags ... ok
test nonexistent_file_returns_error ... ok
test one_file_one_match_match_entire_lines_flag ... ok
test one_file_one_match_multiple_flags ... ok
test one_file_one_match_no_flags ... ok
test one_file_one_match_print_file_names_flag ... ok
test one_file_several_matches_case_insensitive_flag ... ok
test one_file_several_matches_inverted_flag ... ok
test one_file_one_match_print_line_numbers_flag ... ok
test one_file_several_matches_inverted_and_match_entire_lines_flags ... ok
test one_file_several_matches_match_entire_lines_flag ... ok
test multiple_files_several_matches_no_flags ... ok
test multiple_files_several_matches_inverted_flag ... ok
test one_file_several_matches_no_flags ... ok
test multiple_files_several_matches_inverted_and_match_entire_lines_flags ... ok
test multiple_files_one_match_print_file_names_flag ... ok
test one_file_one_match_file_flag_takes_precedence_over_line_flag ... ok
test multiple_files_several_matches_print_line_numbers_flag ... ok
test multiple_files_several_matches_file_flag_takes_precedence_over_line_number_flag ... ok
test one_file_several_matches_print_line_numbers_flag ... ok

test result: ok. 27 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

   Doc-tests grep

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

