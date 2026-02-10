+ go test ./...
--- FAIL: TestFromPov (0.01s)
    --- FAIL: TestFromPov/Errors_if_target_does_not_exist_in_a_singleton_tree (0.00s)
        pov_test.go:171: expected: nil, got: x
    --- FAIL: TestFromPov/Errors_if_target_does_not_exist_in_a_large_tree (0.00s)
        pov_test.go:171: expected: nil, got: (parent (x kid-0 kid-1) sibling-0 sibling-1)
--- FAIL: TestPathTo (0.00s)
    --- FAIL: TestPathTo/Errors_if_source_does_not_exist (0.00s)
        pov_test.go:242: expected: [], got: [parent x]
FAIL
FAIL	pov	0.016s
FAIL
