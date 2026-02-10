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

paasio_test.py FFFFFFFFFFFFFFFFFFFFFFFFF                                 [100%]

=================================== FAILURES ===================================
_________________ PaasioTest.test_meteredfile_context_manager __________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_context_manager>
super_mock = <SuperMock at 0x7c062cf57790 with mock object: <NonCallableMagicMock id='136365957003856'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_context_manager(self, super_mock):
        wrapped = MockFile(ZEN)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        super_mock.mock_object = mock
>       with MeteredFile() as file:

paasio_test.py:221: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
_________ PaasioTest.test_meteredfile_context_manager_exception_raise __________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_context_manager_exception_raise>
super_mock = <SuperMock at 0x7c062c61d010 with mock object: <NonCallableMagicMock id='136365956261520'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_context_manager_exception_raise(self, super_mock):
        exception = MockException("Should raise")
        wrapped = MockFile(ZEN, exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        super_mock.mock_object = mock
        with self.assertRaisesRegex(MockException, "Should raise") as err:
            with MeteredFile() as file:
                self.assertFalse(mock.__enter__.called)
>               file.read()

paasio_test.py:243: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, size = -1

    def read(self, size=-1):
>       data = super().read(size)

paasio.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.read' id='136365952758096'>, args = (-1,)
kwargs = {}

    def __call__(self, /, *args, **kwargs):
        # can't use self in-case a function / method we are mocking uses self
        # in the signature
        self._mock_check_sig(*args, **kwargs)
        self._increment_mock_call(*args, **kwargs)
>       return self._mock_call(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.read' id='136365952758096'>, args = (-1,)
kwargs = {}

    def _mock_call(self, /, *args, **kwargs):
>       return self._execute_mock_call(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1128: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.read' id='136365952758096'>, args = (-1,)
kwargs = {}, effect = None

    def _execute_mock_call(self, /, *args, **kwargs):
        # separate from _increment_mock_call so that awaited functions are
        # executed separately from their call, also AsyncMock overrides this method
    
        effect = self.side_effect
        if effect is not None:
            if _is_exception(effect):
                raise effect
            elif not _callable(effect):
                result = next(effect)
                if _is_exception(result):
                    raise result
            else:
                result = effect(*args, **kwargs)
    
            if result is not DEFAULT:
                return result
    
        if self._mock_return_value is not DEFAULT:
            return self.return_value
    
        if self._mock_wraps is not None:
>           return self._mock_wraps(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1198: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_utils.MockFile object at 0x7c062c5f9b20>, size = -1

    def read(self, size=-1):
        if self.__exception is not None:
>           raise self.__exception
E           test_utils.MockException: Should raise

test_utils.py:47: MockException

During handling of the above exception, another exception occurred:

self = <paasio_test.PaasioTest testMethod=test_meteredfile_context_manager_exception_raise>
super_mock = <SuperMock at 0x7c062c61d010 with mock object: <NonCallableMagicMock id='136365956261520'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_context_manager_exception_raise(self, super_mock):
        exception = MockException("Should raise")
        wrapped = MockFile(ZEN, exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        super_mock.mock_object = mock
        with self.assertRaisesRegex(MockException, "Should raise") as err:
>           with MeteredFile() as file:

paasio_test.py:241: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
________ PaasioTest.test_meteredfile_context_manager_exception_suppress ________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_context_manager_exception_suppress>
super_mock = <SuperMock at 0x7c062c3284d0 with mock object: <NonCallableMagicMock id='136365953157520'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_context_manager_exception_suppress(self, super_mock):
        exception = MockException("Should suppress")
        wrapped = MockFile(ZEN, exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        super_mock.mock_object = mock
        with MeteredFile() as file:
            self.assertFalse(mock.__enter__.called)
>           file.read()

paasio_test.py:261: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, size = -1

    def read(self, size=-1):
>       data = super().read(size)

paasio.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.read' id='136365952810896'>, args = (-1,)
kwargs = {}

    def __call__(self, /, *args, **kwargs):
        # can't use self in-case a function / method we are mocking uses self
        # in the signature
        self._mock_check_sig(*args, **kwargs)
        self._increment_mock_call(*args, **kwargs)
>       return self._mock_call(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.read' id='136365952810896'>, args = (-1,)
kwargs = {}

    def _mock_call(self, /, *args, **kwargs):
>       return self._execute_mock_call(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1128: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.read' id='136365952810896'>, args = (-1,)
kwargs = {}, effect = None

    def _execute_mock_call(self, /, *args, **kwargs):
        # separate from _increment_mock_call so that awaited functions are
        # executed separately from their call, also AsyncMock overrides this method
    
        effect = self.side_effect
        if effect is not None:
            if _is_exception(effect):
                raise effect
            elif not _callable(effect):
                result = next(effect)
                if _is_exception(result):
                    raise result
            else:
                result = effect(*args, **kwargs)
    
            if result is not DEFAULT:
                return result
    
        if self._mock_return_value is not DEFAULT:
            return self.return_value
    
        if self._mock_wraps is not None:
>           return self._mock_wraps(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1198: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_utils.MockFile object at 0x7c062c3ccdb0>, size = -1

    def read(self, size=-1):
        if self.__exception is not None:
>           raise self.__exception
E           test_utils.MockException: Should suppress

test_utils.py:47: MockException

During handling of the above exception, another exception occurred:

self = <paasio_test.PaasioTest testMethod=test_meteredfile_context_manager_exception_suppress>
super_mock = <SuperMock at 0x7c062c3284d0 with mock object: <NonCallableMagicMock id='136365953157520'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_context_manager_exception_suppress(self, super_mock):
        exception = MockException("Should suppress")
        wrapped = MockFile(ZEN, exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        super_mock.mock_object = mock
>       with MeteredFile() as file:

paasio_test.py:259: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = <class 'test_utils.MockException'>
exc_val = MockException('Should suppress')
exc_tb = <traceback object at 0x7c062c2d1200>

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
____________________ PaasioTest.test_meteredfile_iteration _____________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_iteration>
super_mock = <SuperMock at 0x7c062c34d490 with mock object: <NonCallableMagicMock id='136365953308560'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_iteration(self, super_mock):
        mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
        super_mock.mock_object = mock
        actual_reads = b""
        file = MeteredFile()
>       for line in file:

paasio_test.py:275: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>

    def __next__(self):
>       line = self.readline()
E       ValueError: I/O operation on uninitialized object

paasio.py:32: ValueError
__________________ PaasioTest.test_meteredfile_read_multiple ___________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_read_multiple>
super_mock = <SuperMock at 0x7c062c3f6910 with mock object: <NonCallableMagicMock id='136365954001232'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_read_multiple(self, super_mock):
        wrapped = MockFile(ZEN)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        actual_read = b""
>       with MeteredFile() as file:

paasio_test.py:319: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
_______________ PaasioTest.test_meteredfile_read_multiple_chunk ________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_read_multiple_chunk>
super_mock = <SuperMock at 0x7c062c2fedd0 with mock object: <NonCallableMagicMock id='136365952983184'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_read_multiple_chunk(self, super_mock):
        wrapped = MockFile(ZEN, chunk=20)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        actual_read = b""
>       with MeteredFile() as file:

paasio_test.py:333: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
____________________ PaasioTest.test_meteredfile_read_once _____________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_read_once>
super_mock = <SuperMock at 0x7c062c300850 with mock object: <NonCallableMagicMock id='136365953000784'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_read_once(self, super_mock):
        mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
        super_mock.mock_object = mock
>       with MeteredFile() as file:

paasio_test.py:290: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
_________________ PaasioTest.test_meteredfile_read_under_size __________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_read_under_size>
super_mock = <SuperMock at 0x7c062c3022d0 with mock object: <NonCallableMagicMock id='136365953004560'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_read_under_size(self, super_mock):
        wrapped = MockFile(ZEN, chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
>       with MeteredFile() as file:

paasio_test.py:359: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
_________________ PaasioTest.test_meteredfile_stats_read_only __________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_stats_read_only>
super_mock = <SuperMock at 0x7c062c2e4590 with mock object: <NonCallableMagicMock id='136365952877776'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_stats_read_only(self, super_mock):
        mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
        super_mock.mock_object = mock
>       with MeteredFile() as file:

paasio_test.py:414: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
__________________ PaasioTest.test_meteredfile_write_multiple __________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_write_multiple>
super_mock = <SuperMock at 0x7c062c2fc250 with mock object: <NonCallableMagicMock id='136365952989840'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_write_multiple(self, super_mock):
        wrapped = MockFile()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        write_len = 0
        expected = b"Tomorrow's victory is today's practice."
>       with MeteredFile() as file:

paasio_test.py:386: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
____________________ PaasioTest.test_meteredfile_write_once ____________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_write_once>
super_mock = <SuperMock at 0x7c062c599150 with mock object: <NonCallableMagicMock id='136365955714896'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_write_once(self, super_mock):
        wrapped = MockFile(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
>       with MeteredFile() as file:

paasio_test.py:371: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
_________________ PaasioTest.test_meteredfile_write_under_size _________________

self = <paasio_test.PaasioTest testMethod=test_meteredfile_write_under_size>
super_mock = <SuperMock at 0x7c062c2f3bd0 with mock object: <NonCallableMagicMock id='136365952940624'>>

    @patch("paasio.super", create=True, new_callable=SuperMock)
    def test_meteredfile_write_under_size(self, super_mock):
        wrapped = MockFile(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
>       with MeteredFile() as file:

paasio_test.py:402: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MeteredFile>, exc_type = None, exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self.close()
E       ValueError: I/O operation on uninitialized object

paasio.py:26: ValueError
________________ PaasioTest.test_meteredsocket_bufsize_required ________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_bufsize_required>

    def test_meteredsocket_bufsize_required(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
        with self.assertRaisesRegex(TypeError, "argument"):
            with MeteredSocket(mock) as socket:
>               socket.recv()
E               TypeError: MeteredSocket.recv() missing 1 required positional argument: 'bufsize'

paasio_test.py:145: TypeError

During handling of the above exception, another exception occurred:

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_bufsize_required>

    def test_meteredsocket_bufsize_required(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
        with self.assertRaisesRegex(TypeError, "argument"):
>           with MeteredSocket(mock) as socket:

paasio_test.py:144: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
________________ PaasioTest.test_meteredsocket_context_manager _________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_context_manager>

    def test_meteredsocket_context_manager(self):
        wrapped = MockSock()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
>       with MeteredSocket(mock) as socket:

paasio_test.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c6694d0>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365957106384'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
________ PaasioTest.test_meteredsocket_context_manager_exception_raise _________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_context_manager_exception_raise>

    def test_meteredsocket_context_manager_exception_raise(self):
        exception = MockException("Should raise")
        wrapped = MockSock(exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        with self.assertRaisesRegex(MockException, "Should raise") as err:
            with MeteredSocket(mock) as socket:
                self.assertFalse(mock.__enter__.called)
>               socket.recv(4096)

paasio_test.py:35: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c2c3dd0>, bufsize = 4096
flags = 0

    def recv(self, bufsize, flags=0):
>       data = self._socket.recv(bufsize, flags)

paasio.py:92: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.recv' id='136365965330128'>, args = (4096, 0)
kwargs = {}

    def __call__(self, /, *args, **kwargs):
        # can't use self in-case a function / method we are mocking uses self
        # in the signature
        self._mock_check_sig(*args, **kwargs)
        self._increment_mock_call(*args, **kwargs)
>       return self._mock_call(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.recv' id='136365965330128'>, args = (4096, 0)
kwargs = {}

    def _mock_call(self, /, *args, **kwargs):
>       return self._execute_mock_call(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1128: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.recv' id='136365965330128'>, args = (4096, 0)
kwargs = {}, effect = None

    def _execute_mock_call(self, /, *args, **kwargs):
        # separate from _increment_mock_call so that awaited functions are
        # executed separately from their call, also AsyncMock overrides this method
    
        effect = self.side_effect
        if effect is not None:
            if _is_exception(effect):
                raise effect
            elif not _callable(effect):
                result = next(effect)
                if _is_exception(result):
                    raise result
            else:
                result = effect(*args, **kwargs)
    
            if result is not DEFAULT:
                return result
    
        if self._mock_return_value is not DEFAULT:
            return self.return_value
    
        if self._mock_wraps is not None:
>           return self._mock_wraps(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1198: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_utils.MockSock object at 0x7c062c2c2450>, bufsize = 4096, flags = 0

    def recv(self, bufsize, flags=0):
        if self.__closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        if bufsize is None:
            raise TypeError("'NoneType' object cannot be interpreted as an integer")
        if not isinstance(flags, int):
            raise TypeError(
                "an integer is required (got type {})".format(type(flags).__name__)
            )
        self.flags = flags
        if self.__exception is not None:
>           raise self.__exception
E           test_utils.MockException: Should raise

test_utils.py:93: MockException

During handling of the above exception, another exception occurred:

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_context_manager_exception_raise>

    def test_meteredsocket_context_manager_exception_raise(self):
        exception = MockException("Should raise")
        wrapped = MockSock(exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        with self.assertRaisesRegex(MockException, "Should raise") as err:
>           with MeteredSocket(mock) as socket:

paasio_test.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
_______ PaasioTest.test_meteredsocket_context_manager_exception_suppress _______

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_context_manager_exception_suppress>

    def test_meteredsocket_context_manager_exception_suppress(self):
        exception = MockException("Should suppress")
        wrapped = MockSock(exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        with MeteredSocket(mock) as socket:
            self.assertFalse(mock.__enter__.called)
>           socket.recv(4096)

paasio_test.py:51: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062cf6e390>, bufsize = 4096
flags = 0

    def recv(self, bufsize, flags=0):
>       data = self._socket.recv(bufsize, flags)

paasio.py:92: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.recv' id='136365953384080'>, args = (4096, 0)
kwargs = {}

    def __call__(self, /, *args, **kwargs):
        # can't use self in-case a function / method we are mocking uses self
        # in the signature
        self._mock_check_sig(*args, **kwargs)
        self._increment_mock_call(*args, **kwargs)
>       return self._mock_call(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1124: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.recv' id='136365953384080'>, args = (4096, 0)
kwargs = {}

    def _mock_call(self, /, *args, **kwargs):
>       return self._execute_mock_call(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1128: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='mock.recv' id='136365953384080'>, args = (4096, 0)
kwargs = {}, effect = None

    def _execute_mock_call(self, /, *args, **kwargs):
        # separate from _increment_mock_call so that awaited functions are
        # executed separately from their call, also AsyncMock overrides this method
    
        effect = self.side_effect
        if effect is not None:
            if _is_exception(effect):
                raise effect
            elif not _callable(effect):
                result = next(effect)
                if _is_exception(result):
                    raise result
            else:
                result = effect(*args, **kwargs)
    
            if result is not DEFAULT:
                return result
    
        if self._mock_return_value is not DEFAULT:
            return self.return_value
    
        if self._mock_wraps is not None:
>           return self._mock_wraps(*args, **kwargs)

/opt/miniconda3/lib/python3.11/unittest/mock.py:1198: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_utils.MockSock object at 0x7c062c34f550>, bufsize = 4096, flags = 0

    def recv(self, bufsize, flags=0):
        if self.__closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        if bufsize is None:
            raise TypeError("'NoneType' object cannot be interpreted as an integer")
        if not isinstance(flags, int):
            raise TypeError(
                "an integer is required (got type {})".format(type(flags).__name__)
            )
        self.flags = flags
        if self.__exception is not None:
>           raise self.__exception
E           test_utils.MockException: Should suppress

test_utils.py:93: MockException

During handling of the above exception, another exception occurred:

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_context_manager_exception_suppress>

    def test_meteredsocket_context_manager_exception_suppress(self):
        exception = MockException("Should suppress")
        wrapped = MockSock(exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
>       with MeteredSocket(mock) as socket:

paasio_test.py:49: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062cf6e390>
exc_type = <class 'test_utils.MockException'>
exc_val = MockException('Should suppress')
exc_tb = <traceback object at 0x7c062c35f5c0>

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365953304016'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
_________________ PaasioTest.test_meteredsocket_flags_support __________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_flags_support>

    def test_meteredsocket_flags_support(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
>       with MeteredSocket(mock) as socket:

paasio_test.py:159: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c110dd0>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365950961552'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
_________________ PaasioTest.test_meteredsocket_recv_multiple __________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_recv_multiple>

    def test_meteredsocket_recv_multiple(self):
        wrapped = MockSock()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        actual_recv = b""
>       with MeteredSocket(mock) as socket:

paasio_test.py:72: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c379d90>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365953497552'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
______________ PaasioTest.test_meteredsocket_recv_multiple_chunk _______________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_recv_multiple_chunk>

    def test_meteredsocket_recv_multiple_chunk(self):
        wrapped = MockSock(chunk=20)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        actual_recv = b""
>       with MeteredSocket(mock) as socket:

paasio_test.py:84: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c2f04d0>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365952932688'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
___________________ PaasioTest.test_meteredsocket_recv_once ____________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_recv_once>

    def test_meteredsocket_recv_once(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
>       with MeteredSocket(mock) as socket:

paasio_test.py:61: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062dcf4910>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365953089168'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
________________ PaasioTest.test_meteredsocket_recv_under_size _________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_recv_under_size>

    def test_meteredsocket_recv_under_size(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
>       with MeteredSocket(mock) as socket:

paasio_test.py:96: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c2c4990>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365952756176'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
_________________ PaasioTest.test_meteredsocket_send_multiple __________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_send_multiple>

    def test_meteredsocket_send_multiple(self):
        wrapped = MockSock()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        send_len = 0
        expected = b"Tomorrow's victory is today's practice."
>       with MeteredSocket(mock) as socket:

paasio_test.py:119: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c2f6e90>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365952944144'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
___________________ PaasioTest.test_meteredsocket_send_once ____________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_send_once>

    def test_meteredsocket_send_once(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
>       with MeteredSocket(mock) as socket:

paasio_test.py:106: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c2e8c50>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365952900880'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
________________ PaasioTest.test_meteredsocket_send_under_size _________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_send_under_size>

    def test_meteredsocket_send_under_size(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
>       with MeteredSocket(mock) as socket:

paasio_test.py:133: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c339690>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365953220816'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
________________ PaasioTest.test_meteredsocket_stats_read_only _________________

self = <paasio_test.PaasioTest testMethod=test_meteredsocket_stats_read_only>

    def test_meteredsocket_stats_read_only(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
>       with MeteredSocket(mock) as socket:

paasio_test.py:187: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <paasio.MeteredSocket object at 0x7c062c2b7050>, exc_type = None
exc_val = None, exc_tb = None

    def __exit__(self, exc_type, exc_val, exc_tb):
>       self._socket.close()

paasio.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <NonCallableMagicMock id='136365952691408'>, name = 'close'

    def __getattr__(self, name):
        if name in {'_mock_methods', '_mock_unsafe'}:
            raise AttributeError(name)
        elif self._mock_methods is not None:
            if name not in self._mock_methods or name in _all_magics:
                raise AttributeError("Mock object has no attribute %r" % name)
        elif _is_magic(name):
            raise AttributeError(name)
        if not self._mock_unsafe and (not self._mock_methods or name not in self._mock_methods):
            if name.startswith(('assert', 'assret', 'asert', 'aseert', 'assrt')):
                raise AttributeError(
                    f"{name!r} is not a valid assertion. Use a spec "
                    f"for the mock if {name!r} is meant to be an attribute.")
    
        with NonCallableMock._lock:
            result = self._mock_children.get(name)
            if result is _deleted:
                raise AttributeError(name)
            elif result is None:
                wraps = None
                if self._mock_wraps is not None:
                    # XXXX should we get the attribute without triggering code
                    # execution?
>                   wraps = getattr(self._mock_wraps, name)
E                   AttributeError: 'MockSock' object has no attribute 'close'

/opt/miniconda3/lib/python3.11/unittest/mock.py:671: AttributeError
=========================== short test summary info ============================
FAILED paasio_test.py::PaasioTest::test_meteredfile_context_manager - ValueEr...
FAILED paasio_test.py::PaasioTest::test_meteredfile_context_manager_exception_raise
FAILED paasio_test.py::PaasioTest::test_meteredfile_context_manager_exception_suppress
FAILED paasio_test.py::PaasioTest::test_meteredfile_iteration - ValueError: I...
FAILED paasio_test.py::PaasioTest::test_meteredfile_read_multiple - ValueErro...
FAILED paasio_test.py::PaasioTest::test_meteredfile_read_multiple_chunk - Val...
FAILED paasio_test.py::PaasioTest::test_meteredfile_read_once - ValueError: I...
FAILED paasio_test.py::PaasioTest::test_meteredfile_read_under_size - ValueEr...
FAILED paasio_test.py::PaasioTest::test_meteredfile_stats_read_only - ValueEr...
FAILED paasio_test.py::PaasioTest::test_meteredfile_write_multiple - ValueErr...
FAILED paasio_test.py::PaasioTest::test_meteredfile_write_once - ValueError: ...
FAILED paasio_test.py::PaasioTest::test_meteredfile_write_under_size - ValueE...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_bufsize_required - Attr...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_context_manager - Attri...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_context_manager_exception_raise
FAILED paasio_test.py::PaasioTest::test_meteredsocket_context_manager_exception_suppress
FAILED paasio_test.py::PaasioTest::test_meteredsocket_flags_support - Attribu...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_recv_multiple - Attribu...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_recv_multiple_chunk - A...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_recv_once - AttributeEr...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_recv_under_size - Attri...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_send_multiple - Attribu...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_send_once - AttributeEr...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_send_under_size - Attri...
FAILED paasio_test.py::PaasioTest::test_meteredsocket_stats_read_only - Attri...
============================== 25 failed in 6.59s ==============================
