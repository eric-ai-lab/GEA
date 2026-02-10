+ go test ./...
# paasio [paasio.test]
./paasio.go:7:6: WriteCounter redeclared in this block
	./interface.go:26:6: other declaration of WriteCounter
./paasio.go:12:6: ReadCounter redeclared in this block
	./interface.go:12:6: other declaration of ReadCounter
./paasio.go:20:6: ReadWriteCounter redeclared in this block
	./interface.go:37:6: other declaration of ReadWriteCounter
FAIL	paasio [build failed]
FAIL
