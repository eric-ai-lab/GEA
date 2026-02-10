+ go test ./...
--- FAIL: TestCallCloseOnNonFrobError (0.00s)
panic: meh [recovered]
	panic: meh [recovered]
	panic: meh

goroutine 22 [running]:
testing.tRunner.func1.2({0x50f120, 0xc000096510})
	/usr/local/go/src/testing/testing.go:1545 +0x238
testing.tRunner.func1()
	/usr/local/go/src/testing/testing.go:1548 +0x397
panic({0x50f120?, 0xc000096510?})
	/usr/local/go/src/runtime/panic.go:914 +0x21f
erratum.Use.func2()
	/testbed/error_handling.go:40 +0xe5
panic({0x50f120?, 0xc000096510?})
	/usr/local/go/src/runtime/panic.go:914 +0x21f
erratum.TestCallCloseOnNonFrobError.func2({0x522140?, 0x5ad?})
	/testbed/error_handling_test.go:133 +0x3e
erratum.mockResource.Frob(...)
	/testbed/error_handling_test.go:21
erratum.Use(0xc00004c740, {0x530073, 0x5})
	/testbed/error_handling.go:46 +0x126
erratum.TestCallCloseOnNonFrobError(0xc00008b1e0)
	/testbed/error_handling_test.go:137 +0xfa
testing.tRunner(0xc00008b1e0, 0x53bcd8)
	/usr/local/go/src/testing/testing.go:1595 +0xff
created by testing.(*T).Run in goroutine 1
	/usr/local/go/src/testing/testing.go:1648 +0x3ad
FAIL	erratum	0.016s
FAIL
