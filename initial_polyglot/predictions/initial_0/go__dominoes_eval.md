+ go test ./...
--- FAIL: TestMakeChain (0.00s)
    --- FAIL: TestMakeChain/need_backtrack (0.00s)
        dominoes_test.go:20: MakeChain([[1 2] [2 3] [3 1] [2 4] [2 4]])
            verifying chain failed with error: chain is not legal - adjacent mismatch
            chain: [[1 2] [2 3] [3 1] [2 4] [4 2]]
    --- FAIL: TestMakeChain/separate_loops (0.00s)
        dominoes_test.go:20: MakeChain([[1 2] [2 3] [3 1] [1 1] [2 2] [3 3]])
            verifying chain failed with error: chain is not legal - adjacent mismatch
            chain: [[1 2] [2 3] [3 1] [1 1] [3 3] [2 2]]
    --- FAIL: TestMakeChain/nine_elements (0.00s)
        dominoes_test.go:20: MakeChain([[1 2] [5 3] [3 1] [1 2] [2 4] [1 6] [2 3] [3 4] [5 6]])
            verifying chain failed with error: chain is not legal - adjacent mismatch
            chain: [[1 2] [2 1] [1 3] [3 5] [5 6] [6 1] [3 2] [2 4] [4 3]]
FAIL
FAIL	dominoes	0.007s
FAIL
