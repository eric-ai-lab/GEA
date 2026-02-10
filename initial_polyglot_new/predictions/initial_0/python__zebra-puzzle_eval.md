+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 2 items

zebra_puzzle_test.py ..                                                  [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED zebra_puzzle_test.py::ZebraPuzzleTest::test_resident_who_drinks_water
PASSED zebra_puzzle_test.py::ZebraPuzzleTest::test_resident_who_owns_zebra
============================== 2 passed in 0.01s ===============================
