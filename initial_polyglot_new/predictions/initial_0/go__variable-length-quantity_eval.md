+ go test ./...
--- FAIL: TestDecodeVarint (0.00s)
    --- FAIL: TestDecodeVarint/incomplete_sequence_causes_error,_even_if_value_is_zero (0.00s)
        variable_length_quantity_test.go:26: DecodeVarint([]byte{0x80}) expected error, got: []uint32(nil)
FAIL
FAIL	variablelengthquantity	0.007s
FAIL
