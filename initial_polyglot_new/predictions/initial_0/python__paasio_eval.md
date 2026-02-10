+ pytest -rA --tb=long
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-9.0.2, pluggy-1.6.0
rootdir: /testbed
plugins: anyio-4.12.1, asyncio-1.3.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 25 items

paasio_test.py .........................                                 [100%]

==================================== PASSES ====================================
=========================== short test summary info ============================
PASSED paasio_test.py::PaasioTest::test_meteredfile_context_manager
PASSED paasio_test.py::PaasioTest::test_meteredfile_context_manager_exception_raise
PASSED paasio_test.py::PaasioTest::test_meteredfile_context_manager_exception_suppress
PASSED paasio_test.py::PaasioTest::test_meteredfile_iteration
PASSED paasio_test.py::PaasioTest::test_meteredfile_read_multiple
PASSED paasio_test.py::PaasioTest::test_meteredfile_read_multiple_chunk
PASSED paasio_test.py::PaasioTest::test_meteredfile_read_once
PASSED paasio_test.py::PaasioTest::test_meteredfile_read_under_size
PASSED paasio_test.py::PaasioTest::test_meteredfile_stats_read_only
PASSED paasio_test.py::PaasioTest::test_meteredfile_write_multiple
PASSED paasio_test.py::PaasioTest::test_meteredfile_write_once
PASSED paasio_test.py::PaasioTest::test_meteredfile_write_under_size
PASSED paasio_test.py::PaasioTest::test_meteredsocket_bufsize_required
PASSED paasio_test.py::PaasioTest::test_meteredsocket_context_manager
PASSED paasio_test.py::PaasioTest::test_meteredsocket_context_manager_exception_raise
PASSED paasio_test.py::PaasioTest::test_meteredsocket_context_manager_exception_suppress
PASSED paasio_test.py::PaasioTest::test_meteredsocket_flags_support
PASSED paasio_test.py::PaasioTest::test_meteredsocket_recv_multiple
PASSED paasio_test.py::PaasioTest::test_meteredsocket_recv_multiple_chunk
PASSED paasio_test.py::PaasioTest::test_meteredsocket_recv_once
PASSED paasio_test.py::PaasioTest::test_meteredsocket_recv_under_size
PASSED paasio_test.py::PaasioTest::test_meteredsocket_send_multiple
PASSED paasio_test.py::PaasioTest::test_meteredsocket_send_once
PASSED paasio_test.py::PaasioTest::test_meteredsocket_send_under_size
PASSED paasio_test.py::PaasioTest::test_meteredsocket_stats_read_only
============================== 25 passed in 0.38s ==============================
