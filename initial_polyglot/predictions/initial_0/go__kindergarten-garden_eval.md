+ go test ./...
--- FAIL: TestGarden (0.00s)
    --- FAIL: TestGarden/garden_with_single_student (0.00s)
        kindergarten_garden_test.go:155: Lookup Alice = ["Radishes" "Clover" "Grass" "Grass"], want: ["radishes" "clover" "grass" "grass"]
    --- FAIL: TestGarden/different_garden_with_single_student (0.00s)
        kindergarten_garden_test.go:155: Lookup Alice = ["Violets" "Clover" "Radishes" "Clover"], want: ["violets" "clover" "radishes" "clover"]
    --- FAIL: TestGarden/garden_with_two_students (0.00s)
        kindergarten_garden_test.go:155: Lookup Bob = ["Clover" "Grass" "Radishes" "Clover"], want: ["clover" "grass" "radishes" "clover"]
    --- FAIL: TestGarden/garden_with_three_students (0.00s)
        kindergarten_garden_test.go:155: Lookup Bob = ["Clover" "Clover" "Clover" "Clover"], want: ["clover" "clover" "clover" "clover"]
    --- FAIL: TestGarden/full_garden (0.00s)
        kindergarten_garden_test.go:155: Lookup Alice = ["Violets" "Radishes" "Violets" "Radishes"], want: ["violets" "radishes" "violets" "radishes"]
    --- FAIL: TestGarden/names_out_of_order (0.00s)
        kindergarten_garden_test.go:155: Lookup Patricia = ["Violets" "Clover" "Radishes" "Violets"], want: ["violets" "clover" "radishes" "violets"]
    --- FAIL: TestGarden/wrong_diagram_format (0.00s)
        kindergarten_garden_test.go:145: NewGarden expected error but got nil
    --- FAIL: TestGarden/duplicate_name (0.00s)
        kindergarten_garden_test.go:145: NewGarden expected error but got nil
    --- FAIL: TestGarden/invalid_cup_codes (0.00s)
        kindergarten_garden_test.go:145: NewGarden expected error but got nil
--- FAIL: TestNamesNotModified (0.00s)
    kindergarten_garden_test.go:169: error in test setup: TestNamesNotModified requires valid garden and unsorted children
--- FAIL: TestTwoGardens (0.00s)
    kindergarten_garden_test.go:192: Garden 1 lookup Bob = ["Radishes" "Radishes" "Grass" "Clover"], want ["radishes" "radishes" "grass" "clover"].
FAIL
FAIL	kindergarten	0.109s
FAIL
