+ go test ./...
--- FAIL: TestCost (0.00s)
    --- FAIL: TestCost/Only_a_single_book (0.00s)
        book_store_test.go:12: Cost([1]) expected 800, got 0
    --- FAIL: TestCost/Two_of_the_same_book (0.00s)
        book_store_test.go:12: Cost([2 2]) expected 1600, got 800
    --- FAIL: TestCost/Two_different_books (0.00s)
        book_store_test.go:12: Cost([1 2]) expected 1520, got -80
    --- FAIL: TestCost/Three_different_books (0.00s)
        book_store_test.go:12: Cost([1 2 3]) expected 2160, got -240
    --- FAIL: TestCost/Four_different_books (0.00s)
        book_store_test.go:12: Cost([1 2 3 4]) expected 2560, got -640
    --- FAIL: TestCost/Five_different_books (0.00s)
        book_store_test.go:12: Cost([1 2 3 4 5]) expected 3000, got -1000
    --- FAIL: TestCost/Two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three (0.00s)
        book_store_test.go:12: Cost([1 1 2 2 3 3 4 5]) expected 5120, got 1400
    --- FAIL: TestCost/Two_groups_of_four_is_cheaper_than_groups_of_five_and_three (0.00s)
        book_store_test.go:12: Cost([1 1 2 3 4 4 5 5]) expected 5120, got 1400
    --- FAIL: TestCost/Group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three (0.00s)
        book_store_test.go:12: Cost([1 1 2 2 3 4]) expected 4080, got 960
    --- FAIL: TestCost/Two_each_of_first_four_books_and_one_copy_each_of_rest (0.00s)
        book_store_test.go:12: Cost([1 1 2 2 3 3 4 4 5]) expected 5560, got 2200
    --- FAIL: TestCost/Two_copies_of_each_book (0.00s)
        book_store_test.go:12: Cost([1 1 2 2 3 3 4 4 5 5]) expected 6000, got 3000
    --- FAIL: TestCost/Three_copies_of_first_book_and_two_each_of_remaining (0.00s)
        book_store_test.go:12: Cost([1 1 2 2 3 3 4 4 5 5 1]) expected 6800, got 3000
    --- FAIL: TestCost/Three_each_of_first_two_books_and_two_each_of_remaining_books (0.00s)
        book_store_test.go:12: Cost([1 1 2 2 3 3 4 4 5 5 1 2]) expected 7520, got 2920
    --- FAIL: TestCost/Four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three (0.00s)
        book_store_test.go:12: Cost([1 1 2 2 3 3 4 5 1 1 2 2 3 3 4 5]) expected 10240, got 5160
    --- FAIL: TestCost/Check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five (0.00s)
        book_store_test.go:12: Cost([1 1 1 1 1 1 2 2 2 2 2 2 3 3 3 3 3 3 4 4 5 5]) expected 14560, got 7320
    --- FAIL: TestCost/One_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three (0.00s)
        book_store_test.go:12: Cost([1 1 2 3 4]) expected 3360, got 160
    --- FAIL: TestCost/One_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size (0.00s)
        book_store_test.go:12: Cost([1 2 2 3 3 3 4 4 4 4 5 5 5 5 5]) expected 10000, got 3560
FAIL
FAIL	bookstore	0.006s
FAIL
