+ go test ./...
--- FAIL: TestFormatLedgerSuccess (0.00s)
    --- FAIL: TestFormatLedgerSuccess/empty_ledger (0.00s)
        ledger_test.go:259: FormatLedger for input named "empty ledger" failed
            got:
            Date       | Description              | Change
            
            want:
            Date       | Description               | Change
    --- FAIL: TestFormatLedgerSuccess/one_entry (0.00s)
        ledger_test.go:259: FormatLedger for input named "one entry" failed
            got:
            Date       | Description              | Change
            01/01/2015 | Buy present               |      ($10.00)
            
            want:
            Date       | Description               | Change
            01/01/2015 | Buy present               |      ($10.00)
    --- FAIL: TestFormatLedgerSuccess/credit_and_debit (0.00s)
        ledger_test.go:259: FormatLedger for input named "credit and debit" failed
            got:
            Date       | Description              | Change
            01/01/2015 | Buy present               |      ($10.00)
            01/02/2015 | Get present               |       $10.00 
            
            want:
            Date       | Description               | Change
            01/01/2015 | Buy present               |      ($10.00)
            01/02/2015 | Get present               |       $10.00 
    --- FAIL: TestFormatLedgerSuccess/multiple_entries_on_same_date_ordered_by_description (0.00s)
        ledger_test.go:259: FormatLedger for input named "multiple entries on same date ordered by description" failed
            got:
            Date       | Description              | Change
            01/01/2015 | Buy present               |      ($10.00)
            01/01/2015 | Get present               |       $10.00 
            
            want:
            Date       | Description               | Change
            01/01/2015 | Buy present               |      ($10.00)
            01/01/2015 | Get present               |       $10.00 
    --- FAIL: TestFormatLedgerSuccess/final_order_tie_breaker_is_change (0.00s)
        ledger_test.go:259: FormatLedger for input named "final order tie breaker is change" failed
            got:
            Date       | Description              | Change
            01/01/2015 | Something                 |       ($0.01)
            01/01/2015 | Something                 |        $0.00 
            01/01/2015 | Something                 |        $0.01 
            
            want:
            Date       | Description               | Change
            01/01/2015 | Something                 |       ($0.01)
            01/01/2015 | Something                 |        $0.00 
            01/01/2015 | Something                 |        $0.01 
    --- FAIL: TestFormatLedgerSuccess/overlong_descriptions (0.00s)
        ledger_test.go:259: FormatLedger for input named "overlong descriptions" failed
            got:
            Date       | Description              | Change
            01/01/2015 | Freude schoner Gotterf... |   ($1,234.56)
            
            want:
            Date       | Description               | Change
            01/01/2015 | Freude schoner Gotterf... |   ($1,234.56)
    --- FAIL: TestFormatLedgerSuccess/euros (0.00s)
        ledger_test.go:259: FormatLedger for input named "euros" failed
            got:
            Date       | Description              | Change
            01/01/2015 | Buy present               |    (€10.00)
            
            want:
            Date       | Description               | Change
            01/01/2015 | Buy present               |      (€10.00)
    --- FAIL: TestFormatLedgerSuccess/Dutch_locale (0.00s)
        ledger_test.go:259: FormatLedger for input named "Dutch locale" failed
            got:
            Datum      | Omschrijving             | Verandering
            12-03-2015 | Buy present               |   $ 1.234,56 
            
            want:
            Datum      | Omschrijving              | Verandering
            12-03-2015 | Buy present               |   $ 1.234,56 
    --- FAIL: TestFormatLedgerSuccess/Dutch_negative_number_with_3_digits_before_decimal_point (0.00s)
        ledger_test.go:259: FormatLedger for input named "Dutch negative number with 3 digits before decimal point" failed
            got:
            Datum      | Omschrijving             | Verandering
            12-03-2015 | Buy present               |     $ 123,45-
            
            want:
            Datum      | Omschrijving              | Verandering
            12-03-2015 | Buy present               |     $ 123,45-
    --- FAIL: TestFormatLedgerSuccess/American_negative_number_with_3_digits_before_decimal_point (0.00s)
        ledger_test.go:259: FormatLedger for input named "American negative number with 3 digits before decimal point" failed
            got:
            Date       | Description              | Change
            03/12/2015 | Buy present               |     ($123.45)
            
            want:
            Date       | Description               | Change
            03/12/2015 | Buy present               |     ($123.45)
FAIL
FAIL	ledger	0.155s
FAIL
