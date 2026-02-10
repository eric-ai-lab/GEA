+ go test ./...
runtime: goroutine stack exceeds 1000000000-byte limit
runtime: sp=0xc0201e0388 stack=[0xc0201e0000, 0xc0401e0000]
fatal error: stack overflow

runtime stack:
runtime.throw({0x5371ac?, 0x2030000?})
	/usr/local/go/src/runtime/panic.go:1077 +0x5c fp=0xc000525e18 sp=0xc000525de8 pc=0x4367bc
runtime.newstack()
	/usr/local/go/src/runtime/stack.go:1107 +0x5ac fp=0xc000525fc8 sp=0xc000525e18 pc=0x44f2ac
traceback: unexpected SPWRITE function runtime.morestack
runtime.morestack()
	/usr/local/go/src/runtime/asm_amd64.s:593 +0x8f fp=0xc000525fd0 sp=0xc000525fc8 pc=0x466f6f

goroutine 57 [running]:
runtime.deductAssistCredit(0x3?)
	/usr/local/go/src/runtime/malloc.go:1275 +0x70 fp=0xc0201e0398 sp=0xc0201e0390 pc=0x40cf50
runtime.mallocgc(0x3, 0x0, 0x0)
	/usr/local/go/src/runtime/malloc.go:1006 +0xc9 fp=0xc0201e0400 sp=0xc0201e0398 pc=0x40c769
runtime.slicebytetostring(0xc0009c2930?, 0xc0201e0460, 0x3)
	/usr/local/go/src/runtime/string.go:112 +0x77 fp=0xc0201e0430 sp=0xc0201e0400 pc=0x450eb7
strconv.cloneString(...)
	/usr/local/go/src/strconv/atoi.go:50
strconv.syntaxError(...)
	/usr/local/go/src/strconv/atoi.go:53
strconv.Atoi({0x5373de?, 0xc0201e04f0?})
	/usr/local/go/src/strconv/atoi.go:266 +0x1aa fp=0xc0201e04c0 sp=0xc0201e0430 pc=0x489cca
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:91 +0xa6 fp=0xc0201e0550 sp=0xc0201e04c0 pc=0x4ff4e6
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e05e0 sp=0xc0201e0550 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0670 sp=0xc0201e05e0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0700 sp=0xc0201e0670 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0790 sp=0xc0201e0700 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0820 sp=0xc0201e0790 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e08b0 sp=0xc0201e0820 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0940 sp=0xc0201e08b0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e09d0 sp=0xc0201e0940 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0a60 sp=0xc0201e09d0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0af0 sp=0xc0201e0a60 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0b80 sp=0xc0201e0af0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0c10 sp=0xc0201e0b80 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0ca0 sp=0xc0201e0c10 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0d30 sp=0xc0201e0ca0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0dc0 sp=0xc0201e0d30 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0e50 sp=0xc0201e0dc0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0ee0 sp=0xc0201e0e50 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e0f70 sp=0xc0201e0ee0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1000 sp=0xc0201e0f70 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1090 sp=0xc0201e1000 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1120 sp=0xc0201e1090 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e11b0 sp=0xc0201e1120 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1240 sp=0xc0201e11b0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e12d0 sp=0xc0201e1240 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1360 sp=0xc0201e12d0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e13f0 sp=0xc0201e1360 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1480 sp=0xc0201e13f0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1510 sp=0xc0201e1480 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e15a0 sp=0xc0201e1510 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1630 sp=0xc0201e15a0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e16c0 sp=0xc0201e1630 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1750 sp=0xc0201e16c0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e17e0 sp=0xc0201e1750 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1870 sp=0xc0201e17e0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1900 sp=0xc0201e1870 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1990 sp=0xc0201e1900 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1a20 sp=0xc0201e1990 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1ab0 sp=0xc0201e1a20 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1b40 sp=0xc0201e1ab0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1bd0 sp=0xc0201e1b40 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1c60 sp=0xc0201e1bd0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1cf0 sp=0xc0201e1c60 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0201e1d80 sp=0xc0201e1cf0 pc=0x4ffa29
...3728167 frames elided...
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de400 sp=0xc0401de370 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de490 sp=0xc0401de400 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de520 sp=0xc0401de490 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de5b0 sp=0xc0401de520 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de640 sp=0xc0401de5b0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de6d0 sp=0xc0401de640 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de760 sp=0xc0401de6d0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de7f0 sp=0xc0401de760 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de880 sp=0xc0401de7f0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de910 sp=0xc0401de880 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401de9a0 sp=0xc0401de910 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401dea30 sp=0xc0401de9a0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401deac0 sp=0xc0401dea30 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401deb50 sp=0xc0401deac0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401debe0 sp=0xc0401deb50 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401dec70 sp=0xc0401debe0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401ded00 sp=0xc0401dec70 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401ded90 sp=0xc0401ded00 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401dee20 sp=0xc0401ded90 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401deeb0 sp=0xc0401dee20 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401def40 sp=0xc0401deeb0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401defd0 sp=0xc0401def40 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df060 sp=0xc0401defd0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df0f0 sp=0xc0401df060 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df180 sp=0xc0401df0f0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df210 sp=0xc0401df180 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df2a0 sp=0xc0401df210 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df330 sp=0xc0401df2a0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df3c0 sp=0xc0401df330 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df450 sp=0xc0401df3c0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df4e0 sp=0xc0401df450 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df570 sp=0xc0401df4e0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df600 sp=0xc0401df570 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df690 sp=0xc0401df600 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df720 sp=0xc0401df690 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df7b0 sp=0xc0401df720 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df840 sp=0xc0401df7b0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df8d0 sp=0xc0401df840 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df960 sp=0xc0401df8d0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401df9f0 sp=0xc0401df960 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401dfa80 sp=0xc0401df9f0 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401dfb10 sp=0xc0401dfa80 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x5373de?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401dfba0 sp=0xc0401dfb10 pc=0x4ffa29
forth.evalTokens({0xc0000af5c0, 0x3, 0x534eac?}, 0x3?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401dfc30 sp=0xc0401dfba0 pc=0x4ffa29
forth.evalTokens({0xc0000978f0, 0x1, 0x607f00?}, 0x6165e0?, 0xc0401dfd00)
	/testbed/forth.go:99 +0x5e9 fp=0xc0401dfcc0 sp=0xc0401dfc30 pc=0x4ffa29
forth.Forth({0x625fa0?, 0x5ac?, 0x4c0a20?})
	/testbed/forth.go:26 +0xcb fp=0xc0401dfea8 sp=0xc0401dfcc0 pc=0x4fed8b
forth.TestForth.func1(0xc0000eeea0)
	/testbed/forth_test.go:11 +0x3f fp=0xc0401dff70 sp=0xc0401dfea8 pc=0x4ffdff
testing.tRunner(0xc0000eeea0, 0xc000097860)
	/usr/local/go/src/testing/testing.go:1595 +0xff fp=0xc0401dffc0 sp=0xc0401dff70 pc=0x4c0b1f
testing.(*T).Run.func1()
	/usr/local/go/src/testing/testing.go:1648 +0x25 fp=0xc0401dffe0 sp=0xc0401dffc0 pc=0x4c1aa5
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc0401dffe8 sp=0xc0401dffe0 pc=0x468c81
created by testing.(*T).Run in goroutine 18
	/usr/local/go/src/testing/testing.go:1648 +0x3ad

goroutine 1 [chan receive]:
runtime.gopark(0xc00009e9e8?, 0x40cca5?, 0x90?, 0x20?, 0x18?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00009e980 sp=0xc00009e960 pc=0x43960e
runtime.chanrecv(0xc0000d6070, 0xc00009ea67, 0x1)
	/usr/local/go/src/runtime/chan.go:583 +0x3cd fp=0xc00009e9f8 sp=0xc00009e980 pc=0x40662d
runtime.chanrecv1(0x62eea0?, 0x50e220?)
	/usr/local/go/src/runtime/chan.go:442 +0x12 fp=0xc00009ea20 sp=0xc00009e9f8 pc=0x406252
testing.(*T).Run(0xc00008a820, {0x535b25?, 0x4c085c?}, 0x5414a0)
	/usr/local/go/src/testing/testing.go:1649 +0x3c8 fp=0xc00009eae0 sp=0xc00009ea20 pc=0x4c1948
testing.runTests.func1(0x62f8c0?)
	/usr/local/go/src/testing/testing.go:2054 +0x3e fp=0xc00009eb30 sp=0xc00009eae0 pc=0x4c39fe
testing.tRunner(0xc00008a820, 0xc00009ec48)
	/usr/local/go/src/testing/testing.go:1595 +0xff fp=0xc00009eb80 sp=0xc00009eb30 pc=0x4c0b1f
testing.runTests(0xc0000a80a0?, {0x624fa0, 0x1, 0x1}, {0x41293f?, 0xc00009ed08?, 0x62f0a0?})
	/usr/local/go/src/testing/testing.go:2052 +0x445 fp=0xc00009ec78 sp=0xc00009eb80 pc=0x4c38e5
testing.(*M).Run(0xc0000a80a0)
	/usr/local/go/src/testing/testing.go:1925 +0x636 fp=0xc00009eec0 sp=0xc00009ec78 pc=0x4c22d6
main.main()
	_testmain.go:49 +0x19c fp=0xc00009ef40 sp=0xc00009eec0 pc=0x50041c
runtime.main()
	/usr/local/go/src/runtime/proc.go:267 +0x2bb fp=0xc00009efe0 sp=0xc00009ef40 pc=0x43919b
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00009efe8 sp=0xc00009efe0 pc=0x468c81

goroutine 2 [force gc (idle)]:
runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000050fa8 sp=0xc000050f88 pc=0x43960e
runtime.goparkunlock(...)
	/usr/local/go/src/runtime/proc.go:404
runtime.forcegchelper()
	/usr/local/go/src/runtime/proc.go:322 +0xb3 fp=0xc000050fe0 sp=0xc000050fa8 pc=0x439473
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc000050fe8 sp=0xc000050fe0 pc=0x468c81
created by runtime.init.6 in goroutine 1
	/usr/local/go/src/runtime/proc.go:310 +0x1a

goroutine 3 [GC sweep wait]:
runtime.gopark(0x1?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000051778 sp=0xc000051758 pc=0x43960e
runtime.goparkunlock(...)
	/usr/local/go/src/runtime/proc.go:404
runtime.bgsweep(0x0?)
	/usr/local/go/src/runtime/mgcsweep.go:321 +0xdf fp=0xc0000517c8 sp=0xc000051778 pc=0x42411f
runtime.gcenable.func1()
	/usr/local/go/src/runtime/mgc.go:200 +0x25 fp=0xc0000517e0 sp=0xc0000517c8 pc=0x419285
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc0000517e8 sp=0xc0000517e0 pc=0x468c81
created by runtime.gcenable in goroutine 1
	/usr/local/go/src/runtime/mgc.go:200 +0x66

goroutine 4 [GC scavenge wait]:
runtime.gopark(0x37bef8?, 0x1dd1cf?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000051f70 sp=0xc000051f50 pc=0x43960e
runtime.goparkunlock(...)
	/usr/local/go/src/runtime/proc.go:404
runtime.(*scavengerState).park(0x62f120)
	/usr/local/go/src/runtime/mgcscavenge.go:425 +0x49 fp=0xc000051fa0 sp=0xc000051f70 pc=0x4219a9
runtime.bgscavenge(0x0?)
	/usr/local/go/src/runtime/mgcscavenge.go:658 +0x59 fp=0xc000051fc8 sp=0xc000051fa0 pc=0x421f59
runtime.gcenable.func2()
	/usr/local/go/src/runtime/mgc.go:201 +0x25 fp=0xc000051fe0 sp=0xc000051fc8 pc=0x419225
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc000051fe8 sp=0xc000051fe0 pc=0x468c81
created by runtime.gcenable in goroutine 1
	/usr/local/go/src/runtime/mgc.go:201 +0xa5

goroutine 17 [finalizer wait]:
runtime.gopark(0x40c53e?, 0x400000?, 0x70?, 0x6?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000050620 sp=0xc000050600 pc=0x43960e
runtime.runfinq()
	/usr/local/go/src/runtime/mfinal.go:193 +0x107 fp=0xc0000507e0 sp=0xc000050620 pc=0x4182a7
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc0000507e8 sp=0xc0000507e0 pc=0x468c81
created by runtime.createfing in goroutine 1
	/usr/local/go/src/runtime/mfinal.go:163 +0x3d

goroutine 18 [chan receive]:
runtime.gopark(0xc00009fe20?, 0x40cca5?, 0x90?, 0x2c?, 0x18?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00009fdb8 sp=0xc00009fd98 pc=0x43960e
runtime.chanrecv(0xc0000d7180, 0xc00009fe9f, 0x1)
	/usr/local/go/src/runtime/chan.go:583 +0x3cd fp=0xc00009fe30 sp=0xc00009fdb8 pc=0x40662d
runtime.chanrecv1(0x62eea0?, 0x50e220?)
	/usr/local/go/src/runtime/chan.go:442 +0x12 fp=0xc00009fe58 sp=0xc00009fe30 pc=0x406252
testing.(*T).Run(0xc00008a9c0, {0x53f5b9?, 0xc00004c760?}, 0xc000097860)
	/usr/local/go/src/testing/testing.go:1649 +0x3c8 fp=0xc00009ff18 sp=0xc00009fe58 pc=0x4c1948
forth.TestForth(0x0?)
	/testbed/forth_test.go:10 +0x5a fp=0xc00009ff70 sp=0xc00009ff18 pc=0x4ffcda
testing.tRunner(0xc00008a9c0, 0x5414a0)
	/usr/local/go/src/testing/testing.go:1595 +0xff fp=0xc00009ffc0 sp=0xc00009ff70 pc=0x4c0b1f
testing.(*T).Run.func1()
	/usr/local/go/src/testing/testing.go:1648 +0x25 fp=0xc00009ffe0 sp=0xc00009ffc0 pc=0x4c1aa5
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00009ffe8 sp=0xc00009ffe0 pc=0x468c81
created by testing.(*T).Run in goroutine 1
	/usr/local/go/src/testing/testing.go:1648 +0x3ad

goroutine 58 [GC worker (idle)]:
runtime.gopark(0xc00004c760?, 0x47894f?, 0xb0?, 0xc7?, 0x4c0b1f?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00004c750 sp=0xc00004c730 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc00004c7e0 sp=0xc00004c750 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00004c7e8 sp=0xc00004c7e0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 5 [GC worker (idle)]:
runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000052750 sp=0xc000052730 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc0000527e0 sp=0xc000052750 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc0000527e8 sp=0xc0000527e0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 59 [GC worker (idle)]:
runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00004cf50 sp=0xc00004cf30 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc00004cfe0 sp=0xc00004cf50 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00004cfe8 sp=0xc00004cfe0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 60 [GC worker (idle)]:
runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00004d750 sp=0xc00004d730 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc00004d7e0 sp=0xc00004d750 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00004d7e8 sp=0xc00004d7e0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 61 [GC worker (idle)]:
runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00004df50 sp=0xc00004df30 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc00004dfe0 sp=0xc00004df50 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00004dfe8 sp=0xc00004dfe0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 6 [GC worker (idle)]:
runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000052f50 sp=0xc000052f30 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc000052fe0 sp=0xc000052f50 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc000052fe8 sp=0xc000052fe0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 7 [GC worker (idle)]:
runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000053750 sp=0xc000053730 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc0000537e0 sp=0xc000053750 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc0000537e8 sp=0xc0000537e0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 8 [GC worker (idle)]:
runtime.gopark(0x0?, 0x0?, 0x0?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000053f50 sp=0xc000053f30 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc000053fe0 sp=0xc000053f50 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc000053fe8 sp=0xc000053fe0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 9 [GC worker (idle)]:
runtime.gopark(0xc0000af5c0?, 0x3?, 0xde?, 0x73?, 0x3?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000504750 sp=0xc000504730 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc0005047e0 sp=0xc000504750 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc0005047e8 sp=0xc0005047e0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 65 [GC worker (idle)]:
runtime.gopark(0xc0005dfd00?, 0x7982976c2030?, 0x66?, 0x6f?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc000500750 sp=0xc000500730 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc0005007e0 sp=0xc000500750 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc0005007e8 sp=0xc0005007e0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 81 [GC worker (idle)]:
runtime.gopark(0x3?, 0x0?, 0x3?, 0x0?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00050e750 sp=0xc00050e730 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc00050e7e0 sp=0xc00050e750 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00050e7e8 sp=0xc00050e7e0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 62 [GC worker (idle)]:
runtime.gopark(0x65d8c0?, 0x1?, 0x3c?, 0xcc?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00004e750 sp=0xc00004e730 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc00004e7e0 sp=0xc00004e750 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00004e7e8 sp=0xc00004e7e0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 82 [GC worker (idle)]:
runtime.gopark(0xd9aaab5b5066f?, 0x1?, 0xd8?, 0x4d?, 0xc0005dfd18?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00050ef50 sp=0xc00050ef30 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc00050efe0 sp=0xc00050ef50 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00050efe8 sp=0xc00050efe0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c

goroutine 63 [GC worker (idle)]:
runtime.gopark(0x65d8c0?, 0x1?, 0xe6?, 0xd2?, 0x0?)
	/usr/local/go/src/runtime/proc.go:398 +0xce fp=0xc00004ef50 sp=0xc00004ef30 pc=0x43960e
runtime.gcBgMarkWorker()
	/usr/local/go/src/runtime/mgc.go:1295 +0xe5 fp=0xc00004efe0 sp=0xc00004ef50 pc=0x41ae05
runtime.goexit()
	/usr/local/go/src/runtime/asm_amd64.s:1650 +0x1 fp=0xc00004efe8 sp=0xc00004efe0 pc=0x468c81
created by runtime.gcBgMarkStartWorkers in goroutine 57
	/usr/local/go/src/runtime/mgc.go:1219 +0x1c
FAIL	forth	7.362s
FAIL
