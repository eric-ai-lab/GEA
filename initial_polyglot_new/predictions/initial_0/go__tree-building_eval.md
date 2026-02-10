+ go test ./...
--- FAIL: TestMakeTreeSuccess (0.00s)
    --- FAIL: TestMakeTreeSuccess/three_nodes_in_reverse_order (0.00s)
        tree_building_test.go:264: Build for test case "three nodes in reverse order" returned 0:[2:[] 1:[]] but was expected to return 0:[1:[] 2:[]].
    --- FAIL: TestMakeTreeSuccess/more_than_two_children (0.00s)
        tree_building_test.go:264: Build for test case "more than two children" returned 0:[3:[] 2:[] 1:[]] but was expected to return 0:[1:[] 2:[] 3:[]].
    --- FAIL: TestMakeTreeSuccess/binary_tree (0.00s)
        tree_building_test.go:264: Build for test case "binary tree" returned 0:[2:[3:[] 6:[]] 1:[5:[] 4:[]]] but was expected to return 0:[1:[4:[] 5:[]] 2:[3:[] 6:[]]].
    --- FAIL: TestMakeTreeSuccess/unbalanced_tree (0.00s)
        tree_building_test.go:264: Build for test case "unbalanced tree" returned 0:[2:[5:[] 3:[] 6:[]] 1:[4:[]]] but was expected to return 0:[1:[4:[]] 2:[3:[] 5:[] 6:[]]].
--- FAIL: TestMakeTreeFailure (0.00s)
    --- FAIL: TestMakeTreeFailure/one_root_node_and_has_parent (0.00s)
panic: runtime error: invalid memory address or nil pointer dereference [recovered]
	panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x18 pc=0x4fabb3]

goroutine 177 [running]:
testing.tRunner.func1.2({0x510ca0, 0x61bb90})
	/usr/local/go/src/testing/testing.go:1545 +0x238
testing.tRunner.func1()
	/usr/local/go/src/testing/testing.go:1548 +0x397
panic({0x510ca0?, 0x61bb90?})
	/usr/local/go/src/runtime/panic.go:914 +0x21f
tree.Build(...)
	/testbed/tree_building.go:38
tree.TestMakeTreeFailure.func1(0xc000523520)
	/testbed/tree_building_test.go:274 +0x293
testing.tRunner(0xc000523520, 0xc00019e710)
	/usr/local/go/src/testing/testing.go:1595 +0xff
created by testing.(*T).Run in goroutine 176
	/usr/local/go/src/testing/testing.go:1648 +0x3ad
FAIL	tree	0.017s
FAIL
