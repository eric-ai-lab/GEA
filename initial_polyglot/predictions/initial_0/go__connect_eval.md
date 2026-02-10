+ go test ./...
--- FAIL: TestResultOf (0.00s)
    --- FAIL: TestResultOf/an_empty_board_has_no_winner (0.00s)
        connect_test.go:24: ResultOf() returned error invalid token length
            board: 
            . . . . .
             . . . . .
              . . . . .
               . . . . .
                . . . . .
            want: ""
    --- FAIL: TestResultOf/only_edges_does_not_make_a_winner (0.00s)
        connect_test.go:24: ResultOf() returned error invalid token length
            board: 
            O O O X
             X . . X
              X . . X
               X O O O
            want: ""
    --- FAIL: TestResultOf/illegal_diagonal_does_not_make_a_winner (0.00s)
        connect_test.go:24: ResultOf() returned error invalid token length
            board: 
            X O . .
             O X X X
              O X O .
               . O X .
                X X O O
            want: ""
    --- FAIL: TestResultOf/nobody_wins_crossing_adjacent_angles (0.00s)
        connect_test.go:24: ResultOf() returned error invalid token length
            board: 
            X . . .
             . X O .
              O . X O
               . O . X
                . . O .
            want: ""
    --- FAIL: TestResultOf/X_wins_crossing_from_left_to_right (0.00s)
        connect_test.go:24: ResultOf() returned error invalid token length
            board: 
            . O . .
             O X X X
              O X O .
               X X O X
                . O X .
            want: "X"
    --- FAIL: TestResultOf/O_wins_crossing_from_top_to_bottom (0.00s)
        connect_test.go:24: ResultOf() returned error invalid token length
            board: 
            . O . .
             O X X X
              O O O .
               X X O X
                . O X .
            want: "O"
    --- FAIL: TestResultOf/X_wins_using_a_convoluted_path (0.00s)
        connect_test.go:24: ResultOf() returned error invalid token length
            board: 
            . X X . .
             X . X . X
              . X . X .
               . X X . .
                O O O O O
            want: "X"
    --- FAIL: TestResultOf/X_wins_using_a_spiral_path (0.00s)
        connect_test.go:24: ResultOf() returned error invalid token length
            board: 
            O X X X X X X X X
             O X O O O O O O O
              O X O X X X X X O
               O X O X O O O X O
                O X O X X X O X O
                 O X O O O X O X O
                  O X X X X X O X O
                   O O O O O O O X O
                    X X X X X X X X O
            want: "X"
FAIL
FAIL	connect	0.013s
FAIL
