+ pytest -rA --tb=long
/opt/miniconda3/lib/python3.11/site-packages/pytest_asyncio/plugin.py:217: PytestDeprecationWarning: The configuration option "asyncio_default_fixture_loop_scope" is unset.
The event loop scope for asynchronous fixtures will default to the fixture caching scope. Future versions of pytest-asyncio will default the loop scope for asynchronous fixtures to function scope. Set the default fixture loop scope explicitly in order to avoid unexpected behavior in the future. Valid fixture loop scopes are: "function", "class", "module", "package", "session"

  warnings.warn(PytestDeprecationWarning(_DEFAULT_FIXTURE_LOOP_SCOPE_UNSET))
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-8.3.5, pluggy-1.5.0
rootdir: /testbed
plugins: asyncio-0.26.0, anyio-4.9.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 9 items

rest_api_test.py FFFFFFFFF                                               [100%]

=================================== FAILURES ===================================
__________________________ RestApiTest.test_add_user ___________________________

self = <rest_api_test.RestApiTest testMethod=test_add_user>

    def test_add_user(self):
        database = {"users": []}
        api = RestAPI(database)
        payload = json.dumps({"user": "Adam"})
>       response = api.post("/add", payload)

rest_api_test.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <rest_api.RestAPI object at 0x7b2199d87610>, url = '/add'
payload = '{"user": "Adam"}'

    def post(self, url, payload=None):
        if url == "/add":
            # Create a new user if not exists
>           user_name = payload["user"]
E           TypeError: string indices must be integers, not 'str'

rest_api.py:44: TypeError
________________ RestApiTest.test_borrower_has_negative_balance ________________

self = <rest_api_test.RestApiTest testMethod=test_borrower_has_negative_balance>

    def test_borrower_has_negative_balance(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {"Chuck": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Chuck", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
>       response = api.post("/iou", payload)

rest_api_test.py:73: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <rest_api.RestAPI object at 0x7b2199d30a10>, url = '/iou'
payload = '{"lender": "Adam", "borrower": "Bob", "amount": 3.0}'

    def post(self, url, payload=None):
        if url == "/add":
            # Create a new user if not exists
            user_name = payload["user"]
            if self.find_user(user_name) is None:
                new_user = {
                    "name": user_name,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
                self.database["users"].append(new_user)
                return new_user
            else:
                # If user exists, return the existing user
                return self.find_user(user_name)
    
        elif url == "/iou":
>           lender_name = payload["lender"]
E           TypeError: string indices must be integers, not 'str'

rest_api.py:59: TypeError
__________________ RestApiTest.test_both_users_have_0_balance __________________

self = <rest_api_test.RestApiTest testMethod=test_both_users_have_0_balance>

    def test_both_users_have_0_balance(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
>       response = api.post("/iou", payload)

rest_api_test.py:54: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <rest_api.RestAPI object at 0x7b2199ca6710>, url = '/iou'
payload = '{"lender": "Adam", "borrower": "Bob", "amount": 3.0}'

    def post(self, url, payload=None):
        if url == "/add":
            # Create a new user if not exists
            user_name = payload["user"]
            if self.find_user(user_name) is None:
                new_user = {
                    "name": user_name,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
                self.database["users"].append(new_user)
                return new_user
            else:
                # If user exists, return the existing user
                return self.find_user(user_name)
    
        elif url == "/iou":
>           lender_name = payload["lender"]
E           TypeError: string indices must be integers, not 'str'

rest_api.py:59: TypeError
_______________________ RestApiTest.test_get_single_user _______________________

self = <rest_api_test.RestApiTest testMethod=test_get_single_user>

    def test_get_single_user(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"users": ["Bob"]})
>       response = api.get("/users", payload)

rest_api_test.py:39: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <rest_api.RestAPI object at 0x7b2199d85dd0>, url = '/users'
payload = '{"users": ["Bob"]}'

    def get(self, url, payload=None):
        if url == "/users":
            # If payload specifies which users to return
            if payload and "users" in payload:
>               names = payload["users"]
E               TypeError: string indices must be integers, not 'str'

rest_api.py:29: TypeError
_________________ RestApiTest.test_lender_has_negative_balance _________________

self = <rest_api_test.RestApiTest testMethod=test_lender_has_negative_balance>

    def test_lender_has_negative_balance(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {"Chuck": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Chuck", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Bob", "borrower": "Adam", "amount": 3.0})
>       response = api.post("/iou", payload)

rest_api_test.py:97: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <rest_api.RestAPI object at 0x7b2199befa10>, url = '/iou'
payload = '{"lender": "Bob", "borrower": "Adam", "amount": 3.0}'

    def post(self, url, payload=None):
        if url == "/add":
            # Create a new user if not exists
            user_name = payload["user"]
            if self.find_user(user_name) is None:
                new_user = {
                    "name": user_name,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
                self.database["users"].append(new_user)
                return new_user
            else:
                # If user exists, return the existing user
                return self.find_user(user_name)
    
        elif url == "/iou":
>           lender_name = payload["lender"]
E           TypeError: string indices must be integers, not 'str'

rest_api.py:59: TypeError
____________________ RestApiTest.test_lender_owes_borrower _____________________

self = <rest_api_test.RestApiTest testMethod=test_lender_owes_borrower>

    def test_lender_owes_borrower(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 2.0})
>       response = api.post("/iou", payload)

rest_api_test.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <rest_api.RestAPI object at 0x7b2199bf4a50>, url = '/iou'
payload = '{"lender": "Adam", "borrower": "Bob", "amount": 2.0}'

    def post(self, url, payload=None):
        if url == "/add":
            # Create a new user if not exists
            user_name = payload["user"]
            if self.find_user(user_name) is None:
                new_user = {
                    "name": user_name,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
                self.database["users"].append(new_user)
                return new_user
            else:
                # If user exists, return the existing user
                return self.find_user(user_name)
    
        elif url == "/iou":
>           lender_name = payload["lender"]
E           TypeError: string indices must be integers, not 'str'

rest_api.py:59: TypeError
___________ RestApiTest.test_lender_owes_borrower_less_than_new_loan ___________

self = <rest_api_test.RestApiTest testMethod=test_lender_owes_borrower_less_than_new_loan>

    def test_lender_owes_borrower_less_than_new_loan(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 4.0})
>       response = api.post("/iou", payload)

rest_api_test.py:138: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <rest_api.RestAPI object at 0x7b2199d843d0>, url = '/iou'
payload = '{"lender": "Adam", "borrower": "Bob", "amount": 4.0}'

    def post(self, url, payload=None):
        if url == "/add":
            # Create a new user if not exists
            user_name = payload["user"]
            if self.find_user(user_name) is None:
                new_user = {
                    "name": user_name,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
                self.database["users"].append(new_user)
                return new_user
            else:
                # If user exists, return the existing user
                return self.find_user(user_name)
    
        elif url == "/iou":
>           lender_name = payload["lender"]
E           TypeError: string indices must be integers, not 'str'

rest_api.py:59: TypeError
____________ RestApiTest.test_lender_owes_borrower_same_as_new_loan ____________

self = <rest_api_test.RestApiTest testMethod=test_lender_owes_borrower_same_as_new_loan>

    def test_lender_owes_borrower_same_as_new_loan(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
>       response = api.post("/iou", payload)

rest_api_test.py:156: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <rest_api.RestAPI object at 0x7b2199ca4a50>, url = '/iou'
payload = '{"lender": "Adam", "borrower": "Bob", "amount": 3.0}'

    def post(self, url, payload=None):
        if url == "/add":
            # Create a new user if not exists
            user_name = payload["user"]
            if self.find_user(user_name) is None:
                new_user = {
                    "name": user_name,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
                self.database["users"].append(new_user)
                return new_user
            else:
                # If user exists, return the existing user
                return self.find_user(user_name)
    
        elif url == "/iou":
>           lender_name = payload["lender"]
E           TypeError: string indices must be integers, not 'str'

rest_api.py:59: TypeError
__________________________ RestApiTest.test_no_users ___________________________

self = <rest_api_test.RestApiTest testMethod=test_no_users>

    def test_no_users(self):
        database = {"users": []}
        api = RestAPI(database)
    
        response = api.get("/users")
        expected = {"users": []}
>       self.assertDictEqual(json.loads(response), expected)

rest_api_test.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = {'users': []}, cls = None, object_hook = None, parse_float = None
parse_int = None, parse_constant = None, object_pairs_hook = None, kw = {}

    def loads(s, *, cls=None, object_hook=None, parse_float=None,
            parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
        """Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance
        containing a JSON document) to a Python object.
    
        ``object_hook`` is an optional function that will be called with the
        result of any object literal decode (a ``dict``). The return value of
        ``object_hook`` will be used instead of the ``dict``. This feature
        can be used to implement custom decoders (e.g. JSON-RPC class hinting).
    
        ``object_pairs_hook`` is an optional function that will be called with the
        result of any object literal decoded with an ordered list of pairs.  The
        return value of ``object_pairs_hook`` will be used instead of the ``dict``.
        This feature can be used to implement custom decoders.  If ``object_hook``
        is also defined, the ``object_pairs_hook`` takes priority.
    
        ``parse_float``, if specified, will be called with the string
        of every JSON float to be decoded. By default this is equivalent to
        float(num_str). This can be used to use another datatype or parser
        for JSON floats (e.g. decimal.Decimal).
    
        ``parse_int``, if specified, will be called with the string
        of every JSON int to be decoded. By default this is equivalent to
        int(num_str). This can be used to use another datatype or parser
        for JSON integers (e.g. float).
    
        ``parse_constant``, if specified, will be called with one of the
        following strings: -Infinity, Infinity, NaN.
        This can be used to raise an exception if invalid JSON numbers
        are encountered.
    
        To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
        kwarg; otherwise ``JSONDecoder`` is used.
        """
        if isinstance(s, str):
            if s.startswith('\ufeff'):
                raise JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)",
                                      s, 0)
        else:
            if not isinstance(s, (bytes, bytearray)):
>               raise TypeError(f'the JSON object must be str, bytes or bytearray, '
                                f'not {s.__class__.__name__}')
E               TypeError: the JSON object must be str, bytes or bytearray, not dict

/opt/miniconda3/lib/python3.11/json/__init__.py:339: TypeError
=========================== short test summary info ============================
FAILED rest_api_test.py::RestApiTest::test_add_user - TypeError: string indic...
FAILED rest_api_test.py::RestApiTest::test_borrower_has_negative_balance - Ty...
FAILED rest_api_test.py::RestApiTest::test_both_users_have_0_balance - TypeEr...
FAILED rest_api_test.py::RestApiTest::test_get_single_user - TypeError: strin...
FAILED rest_api_test.py::RestApiTest::test_lender_has_negative_balance - Type...
FAILED rest_api_test.py::RestApiTest::test_lender_owes_borrower - TypeError: ...
FAILED rest_api_test.py::RestApiTest::test_lender_owes_borrower_less_than_new_loan
FAILED rest_api_test.py::RestApiTest::test_lender_owes_borrower_same_as_new_loan
FAILED rest_api_test.py::RestApiTest::test_no_users - TypeError: the JSON obj...
============================== 9 failed in 0.80s ===============================
