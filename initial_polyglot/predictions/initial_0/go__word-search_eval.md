+ go test ./...
--- FAIL: TestSolve (0.00s)
    --- FAIL: TestSolve/Should_locate_one_word_written_left_to_right (0.00s)
        word_search_test.go:20: Solve([clojure],[clojurermt]) = map[clojure:[[1 1] [1 7]]], want:map[clojure:[[0 0] [6 0]]]
    --- FAIL: TestSolve/Should_locate_the_same_word_written_left_to_right_in_a_different_position (0.00s)
        word_search_test.go:20: Solve([clojure],[mtclojurer]) = map[clojure:[[1 3] [1 9]]], want:map[clojure:[[2 0] [8 0]]]
    --- FAIL: TestSolve/Should_locate_a_different_left_to_right_word (0.00s)
        word_search_test.go:20: Solve([coffee],[coffeelplx]) = map[coffee:[[1 1] [1 6]]], want:map[coffee:[[0 0] [5 0]]]
    --- FAIL: TestSolve/Should_locate_that_different_left_to_right_word_in_a_different_position (0.00s)
        word_search_test.go:20: Solve([coffee],[xcoffeezlp]) = map[coffee:[[1 2] [1 7]]], want:map[coffee:[[1 0] [6 0]]]
    --- FAIL: TestSolve/Should_locate_a_left_to_right_word_in_two_line_grid (0.00s)
        word_search_test.go:20: Solve([clojure],[jefblpepre tclojurerm]) = map[clojure:[[2 2] [2 8]]], want:map[clojure:[[1 1] [7 1]]]
    --- FAIL: TestSolve/Should_locate_a_left_to_right_word_in_three_line_grid (0.00s)
        word_search_test.go:20: Solve([clojure],[camdcimgtc jefblpepre clojurermt]) = map[clojure:[[3 1] [3 7]]], want:map[clojure:[[0 2] [6 2]]]
    --- FAIL: TestSolve/Should_locate_a_left_to_right_word_in_ten_line_grid (0.00s)
        word_search_test.go:20: Solve([clojure],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]]], want:map[clojure:[[0 9] [6 9]]]
    --- FAIL: TestSolve/Should_locate_that_left_to_right_word_in_a_different_position_in_a_ten_line_grid (0.00s)
        word_search_test.go:20: Solve([clojure],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi clojurermt jalaycalmp]) = map[clojure:[[9 1] [9 7]]], want:map[clojure:[[0 8] [6 8]]]
    --- FAIL: TestSolve/Should_locate_a_different_left_to_right_word_in_a_ten_line_grid (0.00s)
        word_search_test.go:20: Solve([fortran],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc fortranftw alxhpburyi clojurermt jalaycalmp]) = map[fortran:[[7 1] [7 7]]], want:map[fortran:[[0 6] [6 6]]]
    --- FAIL: TestSolve/Should_locate_multiple_words (0.00s)
        word_search_test.go:20: Solve([fortran clojure],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc fortranftw alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]] fortran:[[7 1] [7 7]]], want:map[clojure:[[0 9] [6 9]] fortran:[[0 6] [6 6]]]
    --- FAIL: TestSolve/Should_locate_a_single_word_written_right_to_left (0.00s)
        word_search_test.go:20: Solve([elixir],[rixilelhrs]) = map[elixir:[[1 6] [1 1]]], want:map[elixir:[[5 0] [0 0]]]
    --- FAIL: TestSolve/Should_locate_multiple_words_written_in_different_horizontal_directions (0.00s)
        word_search_test.go:20: Solve([elixir clojure],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]] elixir:[[5 6] [5 1]]], want:map[clojure:[[0 9] [6 9]] elixir:[[5 4] [0 4]]]
    --- FAIL: TestSolve/Should_locate_words_written_top_to_bottom (0.00s)
        word_search_test.go:20: Solve([clojure elixir ecmascript],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]] ecmascript:[[1 10] [10 10]] elixir:[[5 6] [5 1]]], want:map[clojure:[[0 9] [6 9]] ecmascript:[[9 0] [9 9]] elixir:[[5 4] [0 4]]]
    --- FAIL: TestSolve/Should_locate_words_written_bottom_to_top (0.00s)
        word_search_test.go:20: Solve([clojure elixir ecmascript rust],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]] ecmascript:[[1 10] [10 10]] elixir:[[5 6] [5 1]] rust:[[5 9] [2 9]]], want:map[clojure:[[0 9] [6 9]] ecmascript:[[9 0] [9 9]] elixir:[[5 4] [0 4]] rust:[[8 4] [8 1]]]
    --- FAIL: TestSolve/Should_locate_words_written_top_left_to_bottom_right (0.00s)
        word_search_test.go:20: Solve([clojure elixir ecmascript rust java],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]] ecmascript:[[1 10] [10 10]] elixir:[[5 6] [5 1]] java:[[1 1] [4 4]] rust:[[5 9] [2 9]]], want:map[clojure:[[0 9] [6 9]] ecmascript:[[9 0] [9 9]] elixir:[[5 4] [0 4]] java:[[0 0] [3 3]] rust:[[8 4] [8 1]]]
    --- FAIL: TestSolve/Should_locate_words_written_bottom_right_to_top_left (0.00s)
        word_search_test.go:20: Solve([clojure elixir ecmascript rust java lua],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]] ecmascript:[[1 10] [10 10]] elixir:[[5 6] [5 1]] java:[[1 1] [4 4]] lua:[[9 8] [7 6]] rust:[[5 9] [2 9]]], want:map[clojure:[[0 9] [6 9]] ecmascript:[[9 0] [9 9]] elixir:[[5 4] [0 4]] java:[[0 0] [3 3]] lua:[[7 8] [5 6]] rust:[[8 4] [8 1]]]
    --- FAIL: TestSolve/Should_locate_words_written_bottom_left_to_top_right (0.00s)
        word_search_test.go:20: Solve([clojure elixir ecmascript rust java lua lisp],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]] ecmascript:[[1 10] [10 10]] elixir:[[5 6] [5 1]] java:[[1 1] [4 4]] lisp:[[6 3] [3 6]] lua:[[9 8] [7 6]] rust:[[5 9] [2 9]]], want:map[clojure:[[0 9] [6 9]] ecmascript:[[9 0] [9 9]] elixir:[[5 4] [0 4]] java:[[0 0] [3 3]] lisp:[[2 5] [5 2]] lua:[[7 8] [5 6]] rust:[[8 4] [8 1]]]
    --- FAIL: TestSolve/Should_locate_words_written_top_right_to_bottom_left (0.00s)
        word_search_test.go:20: Solve([clojure elixir ecmascript rust java lua lisp ruby],[jefblpepre camdcimgtc oivokprjsm pbwasqroua rixilelhrs wolcqlirpc screeaumgr alxhpburyi jalaycalmp clojurermt]) = map[clojure:[[10 1] [10 7]] ecmascript:[[1 10] [10 10]] elixir:[[5 6] [5 1]] java:[[1 1] [4 4]] lisp:[[6 3] [3 6]] lua:[[9 8] [7 6]] ruby:[[6 8] [9 5]] rust:[[5 9] [2 9]]], want:map[clojure:[[0 9] [6 9]] ecmascript:[[9 0] [9 9]] elixir:[[5 4] [0 4]] java:[[0 0] [3 3]] lisp:[[2 5] [5 2]] lua:[[7 8] [5 6]] ruby:[[7 5] [4 8]] rust:[[8 4] [8 1]]]
FAIL
FAIL	wordsearch	0.006s
FAIL
