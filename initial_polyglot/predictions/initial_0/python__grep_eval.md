+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 25 items

grep_test.py .FFFFFFFFFF.FFFFFFFFFF.FF                                   [100%]

=================================== FAILURES ===================================
________ GrepTest.test_multiple_files_one_match_match_entire_lines_flag ________

self = <grep_test.GrepTest testMethod=test_multiple_files_one_match_match_entire_lines_flag>
mock_file = <MagicMock name='StringIO' id='126178302196688'>
mock_open = <MagicMock name='open' id='126178302201872'>

    def test_multiple_files_one_match_match_entire_lines_flag(
        self, mock_file, mock_open
    ):
>       self.assertMultiLineEqual(
            grep(
                "But I beseech your grace that I may know",
                "-x",
                ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
            ),
            "midsummer-night.txt:But I beseech your grace that I may know\n",
        )
E       AssertionError: 'midsummer-night.txt:But I beseech your grace that I may know' != 'midsummer-night.txt:But I beseech your grace that I may know\n'
E       - midsummer-night.txt:But I beseech your grace that I may know
E       + midsummer-night.txt:But I beseech your grace that I may know
E       
E       ?                                                             
E       +

grep_test.py:221: AssertionError
____________ GrepTest.test_multiple_files_one_match_multiple_flags _____________

self = <grep_test.GrepTest testMethod=test_multiple_files_one_match_multiple_flags>
mock_file = <MagicMock name='StringIO' id='126178302395728'>
mock_open = <MagicMock name='open' id='126178302395792'>

    def test_multiple_files_one_match_multiple_flags(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep(
                "WITH LOSS OF EDEN, TILL ONE GREATER MAN",
                "-n -i -x",
                ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
            ),
            "paradise-lost.txt:4:With loss of Eden, till one greater Man\n",
        )
E       AssertionError: 'paradise-lost.txt:4:With loss of Eden, till one greater Man' != 'paradise-lost.txt:4:With loss of Eden, till one greater Man\n'
E       - paradise-lost.txt:4:With loss of Eden, till one greater Man
E       + paradise-lost.txt:4:With loss of Eden, till one greater Man
E       
E       ?                                                            
E       +

grep_test.py:231: AssertionError
_______________ GrepTest.test_multiple_files_one_match_no_flags ________________

self = <grep_test.GrepTest testMethod=test_multiple_files_one_match_no_flags>
mock_file = <MagicMock name='StringIO' id='126178302378192'>
mock_open = <MagicMock name='open' id='126178302378320'>

    def test_multiple_files_one_match_no_flags(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep(
                "Agamemnon",
                "",
                ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
            ),
            "iliad.txt:Of Atreus, Agamemnon, King of men.\n",
        )
E       AssertionError: 'iliad.txt:Of Atreus, Agamemnon, King of men.' != 'iliad.txt:Of Atreus, Agamemnon, King of men.\n'
E       - iliad.txt:Of Atreus, Agamemnon, King of men.
E       + iliad.txt:Of Atreus, Agamemnon, King of men.
E       
E       ?                                             
E       +

grep_test.py:155: AssertionError
_________ GrepTest.test_multiple_files_one_match_print_file_names_flag _________

self = <grep_test.GrepTest testMethod=test_multiple_files_one_match_print_file_names_flag>
mock_file = <MagicMock name='StringIO' id='126178302428688'>
mock_open = <MagicMock name='open' id='126178302434768'>

    def test_multiple_files_one_match_print_file_names_flag(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep(
                "who", "-l", ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"]
            ),
            "iliad.txt\n" "paradise-lost.txt\n",
        )
E       AssertionError: 'iliad.txt\nparadise-lost.txt' != 'iliad.txt\nparadise-lost.txt\n'
E         iliad.txt
E       - paradise-lost.txt+ paradise-lost.txt
E       ?                  +

grep_test.py:186: AssertionError
______ GrepTest.test_multiple_files_several_matches_case_insensitive_flag ______

self = <grep_test.GrepTest testMethod=test_multiple_files_several_matches_case_insensitive_flag>
mock_file = <MagicMock name='StringIO' id='126178302328208'>
mock_open = <MagicMock name='open' id='126178302314064'>

    def test_multiple_files_several_matches_case_insensitive_flag(
        self, mock_file, mock_open
    ):
>       self.assertMultiLineEqual(
            grep("TO", "-i", ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"]),
            "iliad.txt:Caused to Achaia's host, sent many a soul\n"
            "iliad.txt:Illustrious into Ades premature,\n"
            "iliad.txt:And Heroes gave (so stood the will of Jove)\n"
            "iliad.txt:To dogs and to all ravening fowls a prey,\n"
            "midsummer-night.txt:I do entreat your grace to pardon me.\n"
            "midsummer-night.txt:In such a presence here to plead my thoughts;\n"
            "midsummer-night.txt:If I refuse to wed Demetrius.\n"
            "paradise-lost.txt:Brought Death into the World, and all our woe,\n"
            "paradise-lost.txt:Restore us, and regain the blissful Seat,\n"
            "paradise-lost.txt:Sing Heav'nly Muse, that on the secret top\n",
        )
E       AssertionError: "ilia[505 chars]paradise-lost.txt:Sing Heav'nly Muse, that on the secret top" != "ilia[505 chars]paradise-lost.txt:Sing Heav'nly Muse, that on the secret top\n"
E       Diff is 708 characters long. Set self.maxDiff to None to see it.

grep_test.py:196: AssertionError
_ GrepTest.test_multiple_files_several_matches_file_flag_takes_precedence_over_line_number_flag _

self = <grep_test.GrepTest testMethod=test_multiple_files_several_matches_file_flag_takes_precedence_over_line_number_flag>
mock_file = <MagicMock name='StringIO' id='126178302628688'>
mock_open = <MagicMock name='open' id='126178302633936'>

    def test_multiple_files_several_matches_file_flag_takes_precedence_over_line_number_flag(
        self, mock_file, mock_open
    ):
>       self.assertMultiLineEqual(
            grep(
                "who",
                "-n -l",
                ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
            ),
            "iliad.txt\n" "paradise-lost.txt\n",
        )
E       AssertionError: 'iliad.txt\nparadise-lost.txt' != 'iliad.txt\nparadise-lost.txt\n'
E         iliad.txt
E       - paradise-lost.txt+ paradise-lost.txt
E       ?                  +

grep_test.py:253: AssertionError
_ GrepTest.test_multiple_files_several_matches_inverted_and_match_entire_lines_flags _

self = <grep_test.GrepTest testMethod=test_multiple_files_several_matches_inverted_and_match_entire_lines_flags>
mock_file = <MagicMock name='StringIO' id='126178310627600'>
mock_open = <MagicMock name='open' id='126178302475216'>

    def test_multiple_files_several_matches_inverted_and_match_entire_lines_flags(
        self, mock_file, mock_open
    ):
>       self.assertMultiLineEqual(
            grep(
                "Illustrious into Ades premature,",
                "-x -v",
                ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"],
            ),
            "iliad.txt:Achilles sing, O Goddess! Peleus' son;\n"
            "iliad.txt:His wrath pernicious, who ten thousand woes\n"
            "iliad.txt:Caused to Achaia's host, sent many a soul\n"
            "iliad.txt:And Heroes gave (so stood the will of Jove)\n"
            "iliad.txt:To dogs and to all ravening fowls a prey,\n"
            "iliad.txt:When fierce dispute had separated once\n"
            "iliad.txt:The noble Chief Achilles from the son\n"
            "iliad.txt:Of Atreus, Agamemnon, King of men.\n"
            "midsummer-night.txt:I do entreat your grace to pardon me.\n"
            "midsummer-night.txt:I know not by what power I am made bold,\n"
            "midsummer-night.txt:Nor how it may concern my modesty,\n"
            "midsummer-night.txt:In such a presence here to plead my thoughts;\n"
            "midsummer-night.txt:But I beseech your grace that I may know\n"
            "midsummer-night.txt:The worst that may befall me in this case,\n"
            "midsummer-night.txt:If I refuse to wed Demetrius.\n"
            "paradise-lost.txt:Of Mans First Disobedience, and the Fruit\n"
            "paradise-lost.txt:Of that Forbidden Tree, whose mortal tast\n"
            "paradise-lost.txt:Brought Death into the World, and all our woe,\n"
            "paradise-lost.txt:With loss of Eden, till one greater Man\n"
            "paradise-lost.txt:Restore us, and regain the blissful Seat,\n"
            "paradise-lost.txt:Sing Heav'nly Muse, that on the secret top\n"
            "paradise-lost.txt:Of Oreb, or of Sinai, didst inspire\n"
            "paradise-lost.txt:That Shepherd, who first taught the chosen Seed\n",
        )
E       AssertionError: "ilia[1258 chars]ise-lost.txt:That Shepherd, who first taught the chosen Seed" != "ilia[1258 chars]ise-lost.txt:That Shepherd, who first taught the chosen Seed\n"
E       Diff is 1484 characters long. Set self.maxDiff to None to see it.

grep_test.py:265: AssertionError
__________ GrepTest.test_multiple_files_several_matches_inverted_flag __________

self = <grep_test.GrepTest testMethod=test_multiple_files_several_matches_inverted_flag>
mock_file = <MagicMock name='StringIO' id='126178302379600'>
mock_open = <MagicMock name='open' id='126178302389072'>

    def test_multiple_files_several_matches_inverted_flag(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("a", "-v", ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"]),
            "iliad.txt:Achilles sing, O Goddess! Peleus' son;\n"
            "iliad.txt:The noble Chief Achilles from the son\n"
            "midsummer-night.txt:If I refuse to wed Demetrius.\n",
        )
E       AssertionError: "ilia[84 chars]m the son\nmidsummer-night.txt:If I refuse to wed Demetrius." != "ilia[84 chars]m the son\nmidsummer-night.txt:If I refuse to wed Demetrius.\n"
E         iliad.txt:Achilles sing, O Goddess! Peleus' son;
E         iliad.txt:The noble Chief Achilles from the son
E       - midsummer-night.txt:If I refuse to wed Demetrius.+ midsummer-night.txt:If I refuse to wed Demetrius.
E       ?                                                  +

grep_test.py:211: AssertionError
____________ GrepTest.test_multiple_files_several_matches_no_flags _____________

self = <grep_test.GrepTest testMethod=test_multiple_files_several_matches_no_flags>
mock_file = <MagicMock name='StringIO' id='126178302485776'>
mock_open = <MagicMock name='open' id='126178302407056'>

    def test_multiple_files_several_matches_no_flags(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("may", "", ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"]),
            "midsummer-night.txt:Nor how it may concern my modesty,\n"
            "midsummer-night.txt:But I beseech your grace that I may know\n"
            "midsummer-night.txt:The worst that may befall me in this case,\n",
        )
E       AssertionError: 'mids[116 chars]dsummer-night.txt:The worst that may befall me in this case,' != 'mids[116 chars]dsummer-night.txt:The worst that may befall me in this case,\n'
E         midsummer-night.txt:Nor how it may concern my modesty,
E         midsummer-night.txt:But I beseech your grace that I may know
E       - midsummer-night.txt:The worst that may befall me in this case,+ midsummer-night.txt:The worst that may befall me in this case,
E       ?                                                               +

grep_test.py:165: AssertionError
_____ GrepTest.test_multiple_files_several_matches_print_line_numbers_flag _____

self = <grep_test.GrepTest testMethod=test_multiple_files_several_matches_print_line_numbers_flag>
mock_file = <MagicMock name='StringIO' id='126178301872848'>
mock_open = <MagicMock name='open' id='126178302342992'>

    def test_multiple_files_several_matches_print_line_numbers_flag(
        self, mock_file, mock_open
    ):
>       self.assertMultiLineEqual(
            grep(
                "that", "-n", ["iliad.txt", "midsummer-night.txt", "paradise-lost.txt"]
            ),
            "midsummer-night.txt:5:But I beseech your grace that I may know\n"
            "midsummer-night.txt:6:The worst that may befall me in this case,\n"
            "paradise-lost.txt:2:Of that Forbidden Tree, whose mortal tast\n"
            "paradise-lost.txt:6:Sing Heav'nly Muse, that on the secret top\n",
        )
E       AssertionError: "mids[191 chars]radise-lost.txt:6:Sing Heav'nly Muse, that on the secret top" != "mids[191 chars]radise-lost.txt:6:Sing Heav'nly Muse, that on the secret top\n"
E         midsummer-night.txt:5:But I beseech your grace that I may know
E         midsummer-night.txt:6:The worst that may befall me in this case,
E         paradise-lost.txt:2:Of that Forbidden Tree, whose mortal tast
E       - paradise-lost.txt:6:Sing Heav'nly Muse, that on the secret top+ paradise-lost.txt:6:Sing Heav'nly Muse, that on the secret top
E       ?                                                               +

grep_test.py:175: AssertionError
____________ GrepTest.test_one_file_one_match_case_insensitive_flag ____________

self = <grep_test.GrepTest testMethod=test_one_file_one_match_case_insensitive_flag>
mock_file = <MagicMock name='StringIO' id='126178302428688'>
mock_open = <MagicMock name='open' id='126178302321104'>

    def test_one_file_one_match_case_insensitive_flag(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("FORBIDDEN", "-i", ["paradise-lost.txt"]),
            "Of that Forbidden Tree, whose mortal tast\n",
        )
E       AssertionError: 'Of that Forbidden Tree, whose mortal tast' != 'Of that Forbidden Tree, whose mortal tast\n'
E       - Of that Forbidden Tree, whose mortal tast
E       + Of that Forbidden Tree, whose mortal tast
E       
E       ?                                          
E       +

grep_test.py:66: AssertionError
__ GrepTest.test_one_file_one_match_file_flag_takes_precedence_over_line_flag __

self = <grep_test.GrepTest testMethod=test_one_file_one_match_file_flag_takes_precedence_over_line_flag>
mock_file = <MagicMock name='StringIO' id='126178302589712'>
mock_open = <MagicMock name='open' id='126178302586384'>

    def test_one_file_one_match_file_flag_takes_precedence_over_line_flag(
        self, mock_file, mock_open
    ):
>       self.assertMultiLineEqual(grep("ten", "-n -l", ["iliad.txt"]), "iliad.txt\n")
E       AssertionError: 'iliad.txt' != 'iliad.txt\n'
E       - iliad.txt
E       + iliad.txt
E       
E       ?          
E       +

grep_test.py:136: AssertionError
___________ GrepTest.test_one_file_one_match_match_entire_lines_flag ___________

self = <grep_test.GrepTest testMethod=test_one_file_one_match_match_entire_lines_flag>
mock_file = <MagicMock name='StringIO' id='126178302336720'>
mock_open = <MagicMock name='open' id='126178302292112'>

    def test_one_file_one_match_match_entire_lines_flag(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep(
                "With loss of Eden, till one greater Man", "-x", ["paradise-lost.txt"]
            ),
            "With loss of Eden, till one greater Man\n",
        )
E       AssertionError: 'With loss of Eden, till one greater Man' != 'With loss of Eden, till one greater Man\n'
E       - With loss of Eden, till one greater Man
E       + With loss of Eden, till one greater Man
E       
E       ?                                        
E       +

grep_test.py:77: AssertionError
_______________ GrepTest.test_one_file_one_match_multiple_flags ________________

self = <grep_test.GrepTest testMethod=test_one_file_one_match_multiple_flags>
mock_file = <MagicMock name='StringIO' id='126178302205904'>
mock_open = <MagicMock name='open' id='126178302203472'>

    def test_one_file_one_match_multiple_flags(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("OF ATREUS, Agamemnon, KIng of MEN.", "-n -i -x", ["iliad.txt"]),
            "9:Of Atreus, Agamemnon, King of men.\n",
        )
E       AssertionError: '9:Of Atreus, Agamemnon, King of men.' != '9:Of Atreus, Agamemnon, King of men.\n'
E       - 9:Of Atreus, Agamemnon, King of men.
E       + 9:Of Atreus, Agamemnon, King of men.
E       
E       ?                                     
E       +

grep_test.py:85: AssertionError
__________________ GrepTest.test_one_file_one_match_no_flags ___________________

self = <grep_test.GrepTest testMethod=test_one_file_one_match_no_flags>
mock_file = <MagicMock name='StringIO' id='126178302408336'>
mock_open = <MagicMock name='open' id='126178302407760'>

    def test_one_file_one_match_no_flags(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("Agamemnon", "", ["iliad.txt"]), "Of Atreus, Agamemnon, King of men.\n"
        )
E       AssertionError: 'Of Atreus, Agamemnon, King of men.' != 'Of Atreus, Agamemnon, King of men.\n'
E       - Of Atreus, Agamemnon, King of men.
E       + Of Atreus, Agamemnon, King of men.
E       
E       ?                                   
E       +

grep_test.py:55: AssertionError
____________ GrepTest.test_one_file_one_match_print_file_names_flag ____________

self = <grep_test.GrepTest testMethod=test_one_file_one_match_print_file_names_flag>
mock_file = <MagicMock name='StringIO' id='126178302439248'>
mock_open = <MagicMock name='open' id='126178302196560'>

    def test_one_file_one_match_print_file_names_flag(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("Forbidden", "-l", ["paradise-lost.txt"]), "paradise-lost.txt\n"
        )
E       AssertionError: 'paradise-lost.txt' != 'paradise-lost.txt\n'
E       - paradise-lost.txt
E       + paradise-lost.txt
E       
E       ?                  
E       +

grep_test.py:72: AssertionError
___________ GrepTest.test_one_file_one_match_print_line_numbers_flag ___________

self = <grep_test.GrepTest testMethod=test_one_file_one_match_print_line_numbers_flag>
mock_file = <MagicMock name='StringIO' id='126178301876944'>
mock_open = <MagicMock name='open' id='126178302630544'>

    def test_one_file_one_match_print_line_numbers_flag(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("Forbidden", "-n", ["paradise-lost.txt"]),
            "2:Of that Forbidden Tree, whose mortal tast\n",
        )
E       AssertionError: '2:Of that Forbidden Tree, whose mortal tast' != '2:Of that Forbidden Tree, whose mortal tast\n'
E       - 2:Of that Forbidden Tree, whose mortal tast
E       + 2:Of that Forbidden Tree, whose mortal tast
E       
E       ?                                            
E       +

grep_test.py:60: AssertionError
_________ GrepTest.test_one_file_several_matches_case_insensitive_flag _________

self = <grep_test.GrepTest testMethod=test_one_file_several_matches_case_insensitive_flag>
mock_file = <MagicMock name='StringIO' id='126178302769232'>
mock_open = <MagicMock name='open' id='126178302769936'>

    def test_one_file_several_matches_case_insensitive_flag(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("ACHILLES", "-i", ["iliad.txt"]),
            "Achilles sing, O Goddess! Peleus' son;\n"
            "The noble Chief Achilles from the son\n",
        )
E       AssertionError: "Achi[13 chars]Goddess! Peleus' son;\nThe noble Chief Achilles from the son" != "Achi[13 chars]Goddess! Peleus' son;\nThe noble Chief Achilles from the son\n"
E         Achilles sing, O Goddess! Peleus' son;
E       - The noble Chief Achilles from the son+ The noble Chief Achilles from the son
E       ?                                      +

grep_test.py:114: AssertionError
_ GrepTest.test_one_file_several_matches_inverted_and_match_entire_lines_flags _

self = <grep_test.GrepTest testMethod=test_one_file_several_matches_inverted_and_match_entire_lines_flags>
mock_file = <MagicMock name='StringIO' id='126178302636048'>
mock_open = <MagicMock name='open' id='126178302491856'>

    def test_one_file_several_matches_inverted_and_match_entire_lines_flags(
        self, mock_file, mock_open
    ):
>       self.assertMultiLineEqual(
            grep("Illustrious into Ades premature,", "-x -v", ["iliad.txt"]),
            "Achilles sing, O Goddess! Peleus' son;\n"
            "His wrath pernicious, who ten thousand woes\n"
            "Caused to Achaia's host, sent many a soul\n"
            "And Heroes gave (so stood the will of Jove)\n"
            "To dogs and to all ravening fowls a prey,\n"
            "When fierce dispute had separated once\n"
            "The noble Chief Achilles from the son\n"
            "Of Atreus, Agamemnon, King of men.\n",
        )
E       AssertionError: "Achi[265 chars]ef Achilles from the son\nOf Atreus, Agamemnon, King of men." != "Achi[265 chars]ef Achilles from the son\nOf Atreus, Agamemnon, King of men.\n"
E         Achilles sing, O Goddess! Peleus' son;
E         His wrath pernicious, who ten thousand woes
E         Caused to Achaia's host, sent many a soul
E         And Heroes gave (so stood the will of Jove)
E         To dogs and to all ravening fowls a prey,
E         When fierce dispute had separated once
E         The noble Chief Achilles from the son
E       - Of Atreus, Agamemnon, King of men.+ Of Atreus, Agamemnon, King of men.
E       ?                                   +

grep_test.py:141: AssertionError
_____________ GrepTest.test_one_file_several_matches_inverted_flag _____________

self = <grep_test.GrepTest testMethod=test_one_file_several_matches_inverted_flag>
mock_file = <MagicMock name='StringIO' id='126178302441680'>
mock_open = <MagicMock name='open' id='126178302698128'>

    def test_one_file_several_matches_inverted_flag(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("Of", "-v", ["paradise-lost.txt"]),
            "Brought Death into the World, and all our woe,\n"
            "With loss of Eden, till one greater Man\n"
            "Restore us, and regain the blissful Seat,\n"
            "Sing Heav'nly Muse, that on the secret top\n"
            "That Shepherd, who first taught the chosen Seed\n",
        )
E       AssertionError: "Brou[159 chars] secret top\nThat Shepherd, who first taught the chosen Seed" != "Brou[159 chars] secret top\nThat Shepherd, who first taught the chosen Seed\n"
E         Brought Death into the World, and all our woe,
E         With loss of Eden, till one greater Man
E         Restore us, and regain the blissful Seat,
E         Sing Heav'nly Muse, that on the secret top
E       - That Shepherd, who first taught the chosen Seed+ That Shepherd, who first taught the chosen Seed
E       ?                                                +

grep_test.py:121: AssertionError
_______________ GrepTest.test_one_file_several_matches_no_flags ________________

self = <grep_test.GrepTest testMethod=test_one_file_several_matches_no_flags>
mock_file = <MagicMock name='StringIO' id='126178302208080'>
mock_open = <MagicMock name='open' id='126178302199568'>

    def test_one_file_several_matches_no_flags(self, mock_file, mock_open):
>       self.assertMultiLineEqual(
            grep("may", "", ["midsummer-night.txt"]),
            "Nor how it may concern my modesty,\n"
            "But I beseech your grace that I may know\n"
            "The worst that may befall me in this case,\n",
        )
E       AssertionError: 'Nor [56 chars] that I may know\nThe worst that may befall me in this case,' != 'Nor [56 chars] that I may know\nThe worst that may befall me in this case,\n'
E         Nor how it may concern my modesty,
E         But I beseech your grace that I may know
E       - The worst that may befall me in this case,+ The worst that may befall me in this case,
E       ?                                           +

grep_test.py:91: AssertionError
________ GrepTest.test_one_file_several_matches_print_line_numbers_flag ________

self = <grep_test.GrepTest testMethod=test_one_file_several_matches_print_line_numbers_flag>
mock_file = <MagicMock name='StringIO' id='126178301886160'>
mock_open = <MagicMock name='open' id='126178302195216'>

    def test_one_file_several_matches_print_line_numbers_flag(
        self, mock_file, mock_open
    ):
>       self.assertMultiLineEqual(
            grep("may", "-n", ["midsummer-night.txt"]),
            "3:Nor how it may concern my modesty,\n"
            "5:But I beseech your grace that I may know\n"
            "6:The worst that may befall me in this case,\n",
        )
E       AssertionError: '3:No[62 chars]hat I may know\n6:The worst that may befall me in this case,' != '3:No[62 chars]hat I may know\n6:The worst that may befall me in this case,\n'
E         3:Nor how it may concern my modesty,
E         5:But I beseech your grace that I may know
E       - 6:The worst that may befall me in this case,+ 6:The worst that may befall me in this case,
E       ?                                             +

grep_test.py:101: AssertionError
==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED grep_test.py::GrepTest::test_multiple_files_no_matches_various_flags
PASSED grep_test.py::GrepTest::test_one_file_no_matches_various_flags
PASSED grep_test.py::GrepTest::test_one_file_several_matches_match_entire_lines_flag
FAILED grep_test.py::GrepTest::test_multiple_files_one_match_match_entire_lines_flag
FAILED grep_test.py::GrepTest::test_multiple_files_one_match_multiple_flags
FAILED grep_test.py::GrepTest::test_multiple_files_one_match_no_flags - Asser...
FAILED grep_test.py::GrepTest::test_multiple_files_one_match_print_file_names_flag
FAILED grep_test.py::GrepTest::test_multiple_files_several_matches_case_insensitive_flag
FAILED grep_test.py::GrepTest::test_multiple_files_several_matches_file_flag_takes_precedence_over_line_number_flag
FAILED grep_test.py::GrepTest::test_multiple_files_several_matches_inverted_and_match_entire_lines_flags
FAILED grep_test.py::GrepTest::test_multiple_files_several_matches_inverted_flag
FAILED grep_test.py::GrepTest::test_multiple_files_several_matches_no_flags
FAILED grep_test.py::GrepTest::test_multiple_files_several_matches_print_line_numbers_flag
FAILED grep_test.py::GrepTest::test_one_file_one_match_case_insensitive_flag
FAILED grep_test.py::GrepTest::test_one_file_one_match_file_flag_takes_precedence_over_line_flag
FAILED grep_test.py::GrepTest::test_one_file_one_match_match_entire_lines_flag
FAILED grep_test.py::GrepTest::test_one_file_one_match_multiple_flags - Asser...
FAILED grep_test.py::GrepTest::test_one_file_one_match_no_flags - AssertionEr...
FAILED grep_test.py::GrepTest::test_one_file_one_match_print_file_names_flag
FAILED grep_test.py::GrepTest::test_one_file_one_match_print_line_numbers_flag
FAILED grep_test.py::GrepTest::test_one_file_several_matches_case_insensitive_flag
FAILED grep_test.py::GrepTest::test_one_file_several_matches_inverted_and_match_entire_lines_flags
FAILED grep_test.py::GrepTest::test_one_file_several_matches_inverted_flag - ...
FAILED grep_test.py::GrepTest::test_one_file_several_matches_no_flags - Asser...
FAILED grep_test.py::GrepTest::test_one_file_several_matches_print_line_numbers_flag
========================= 22 failed, 3 passed in 0.69s =========================
