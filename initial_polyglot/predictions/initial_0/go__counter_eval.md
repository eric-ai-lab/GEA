+ go test ./...
# counter [counter.test]
./interface.go:3:6: Counter redeclared in this block
	./counter.go:8:6: other declaration of Counter
./maker.go:16:10: cannot use &Impl1{} (value of type *Impl1) as Counter value in return statement
./maker.go:18:10: cannot use &Impl2{} (value of type *Impl2) as Counter value in return statement
./maker.go:20:10: cannot use &Impl3{} (value of type *Impl3) as Counter value in return statement
./maker.go:22:10: cannot use &Impl4{} (value of type *Impl4) as Counter value in return statement
FAIL	counter [build failed]
FAIL
