+ go test ./...
# robot [robot.test]
./robot_simulator.go:10:6: Dir redeclared in this block
	./defs.go:12:6: other declaration of Dir
./robot_simulator.go:72:6: Command redeclared in this block
	./defs.go:18:6: other declaration of Command
./robot_simulator.go:88:6: Step2Robot redeclared in this block
	./defs.go:22:6: other declaration of Step2Robot
./robot_simulator.go:97:6: Rect redeclared in this block
	./defs.go:21:6: other declaration of Rect
./robot_simulator.go:130:24: robot.X undefined (type Step2Robot has no field or method X)
./robot_simulator.go:130:33: robot.Y undefined (type Step2Robot has no field or method Y)
./robot_simulator.go:141:22: extent.MinX undefined (type Rect has no field or method MinX)
./robot_simulator.go:141:45: extent.MaxX undefined (type Rect has no field or method MaxX)
./robot_simulator.go:141:68: extent.MinY undefined (type Rect has no field or method MinY)
./robot_simulator.go:163:6: Step3Robot redeclared in this block
	./defs.go:29:6: other declaration of Step3Robot
./robot_simulator.go:141:68: too many errors
FAIL	robot [build failed]
FAIL
