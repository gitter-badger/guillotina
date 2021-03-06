from guillotina import testing
from guillotina.async import IAsyncUtility
from guillotina.component import get_all_utilities_registered_for
from guillotina.component import get_utility
from guillotina.content import load_cached_schema
from guillotina.db.storages.cockroach import CockroachStorage
from guillotina.db.transaction import HARD_CACHE
from guillotina.factory import make_app
from guillotina.interfaces import IApplication
from guillotina.tests import docker_containers as containers
from guillotina.tests.utils import ContainerRequesterAsyncContextManager
from guillotina.tests.utils import get_mocked_request

import aiohttp
import asyncio
import os
import pytest


IS_TRAVIS = 'TRAVIS' in os.environ
USE_COCKROACH = 'USE_COCKROACH' in os.environ


def base_settings_configurator(settings):
    settings["utilities"].append({
        "provides": "guillotina.interfaces.ICatalogUtility",
        "factory": "guillotina.catalog.catalog.DefaultSearchUtility"
    })


testing.configure_with(base_settings_configurator)


def get_dummy_settings():
    settings = testing.get_settings()
    settings['databases'][0]['db']['storage'] = 'DUMMY'

    settings['databases'][0]['db']['partition'] = 'guillotina.interfaces.IResource'
    settings['databases'][0]['db']['dsn'] = {}
    return settings


def get_pg_settings():
    settings = testing.get_settings()
    settings['databases'][0]['db']['storage'] = 'postgresql'

    settings['databases'][0]['db']['partition'] = \
        'guillotina.interfaces.IResource'
    settings['databases'][0]['db']['dsn'] = {
        'scheme': 'postgres',
        'dbname': 'guillotina',
        'user': 'postgres',
        'host': getattr(get_pg_settings, 'host', 'localhost'),
        'port': getattr(get_pg_settings, 'port', 5432),
        'password': '',
    }
    if USE_COCKROACH:
        settings['databases'][0]['db']['storage'] = 'cockroach'
        settings['databases'][0]['db']['dsn'].update({
            'user': 'root'
        })
    return settings


@pytest.fixture(scope='session')
def postgres():
    """
    detect travis, use travis's postgres; otherwise, use docker
    """

    if USE_COCKROACH:
        host, port = containers.cockroach_image.run()
    else:
        if not IS_TRAVIS:
            host, port = containers.postgres_image.run()
        else:
            host = 'localhost'
            port = 5432

    # mark the function with the actual host
    setattr(get_pg_settings, 'host', host)
    setattr(get_pg_settings, 'port', port)

    yield host, port  # provide the fixture value

    if USE_COCKROACH:
        containers.cockroach_image.stop()
    elif not IS_TRAVIS:
        containers.postgres_image.stop()


class GuillotinaDBRequester(object):

    def __init__(self, server, loop):
        self.server = server
        self.loop = loop
        self.root = get_utility(IApplication, name='root')
        self.db = self.root['db']

    async def __call__(self, method, path, params=None, data=None, authenticated=True,
                       auth_type='Basic', headers={}, token=testing.ADMIN_TOKEN,
                       accept='application/json'):
        value, status, headers = await self.make_request(
            method, path, params, data, authenticated,
            auth_type, headers, token, accept)
        return value, status

    async def make_request(self, method, path, params=None, data=None,
                           authenticated=True, auth_type='Basic', headers={},
                           token=testing.ADMIN_TOKEN, accept='application/json'):
        settings = {}
        headers = headers.copy()
        settings['headers'] = headers
        if accept is not None:
            settings['headers']['ACCEPT'] = accept
        if authenticated and token is not None:
            settings['headers']['AUTHORIZATION'] = '{} {}'.format(
                auth_type, token)

        settings['params'] = params
        settings['data'] = data

        async with aiohttp.ClientSession(loop=self.loop) as session:
            operation = getattr(session, method.lower(), None)
            async with operation(self.server.make_url(path), **settings) as resp:
                try:
                    value = await resp.json()
                    status = resp.status
                except:  # noqa
                    value = await resp.read()
                    status = resp.status
                return value, status, resp.headers


def close_async_tasks():
    root = get_utility(IApplication, name='root')
    for utility in get_all_utilities_registered_for(IAsyncUtility):
        try:
            root.cancel_async_utility(utility)
        except KeyError:
            pass

@pytest.fixture(scope='function')
def dummy_guillotina(loop):
    from guillotina import test_package  # noqa
    aioapp = make_app(settings=get_dummy_settings(), loop=loop)
    aioapp.config.execute_actions()
    load_cached_schema()
    yield aioapp
    close_async_tasks()


class DummyRequestAsyncContextManager(object):
    def __init__(self, dummy_request, loop):
        self.request = dummy_request
        self.loop = loop

    async def __aenter__(self):
        task = asyncio.Task.current_task(loop=self.loop)
        if task is not None:
            task.request = self.request
        return self.request

    async def __aexit__(self, exc_type, exc, tb):
        task = asyncio.Task.current_task(loop=self.loop)
        del task.request


@pytest.fixture(scope='function')
def dummy_request(dummy_guillotina, monkeypatch):
    HARD_CACHE.clear()
    from guillotina.interfaces import IApplication
    from guillotina.component import get_utility
    root = get_utility(IApplication, name='root')
    db = root['db']

    request = get_mocked_request(db)
    return request


class RootAsyncContextManager(object):
    def __init__(self, request):
        self.request = request
        self.root = None
        self.txn = None

    async def __aenter__(self):
        self.txn = await self.request._tm.begin(request=dummy_request)
        self.root = await self.request._tm.get_root()
        return self.root

    async def __aexit__(self, exc_type, exc, tb):
        await self.txn.abort()


@pytest.fixture(scope='function')
async def dummy_txn_root(dummy_request):
    HARD_CACHE.clear()
    return RootAsyncContextManager(dummy_request)


@pytest.fixture(scope='function')
def guillotina_main(loop):
    HARD_CACHE.clear()
    from guillotina import test_package  # noqa
    aioapp = make_app(settings=get_pg_settings(), loop=loop)
    aioapp.config.execute_actions()
    load_cached_schema()
    yield aioapp
    close_async_tasks()


@pytest.fixture(scope='function')
async def guillotina(test_server, postgres, guillotina_main, loop):
    HARD_CACHE.clear()
    server = await test_server(guillotina_main)
    requester = GuillotinaDBRequester(server=server, loop=loop)
    return requester


@pytest.fixture(scope='function')
async def container_requester(guillotina):
    return ContainerRequesterAsyncContextManager(guillotina)


class CockroachStorageAsyncContextManager(object):
    def __init__(self, request, loop, postgres):
        self.loop = loop
        self.request = request
        self.storage = None
        self.postgres = postgres

    async def __aenter__(self):
        dsn = "postgres://root:@{}:{}/guillotina?sslmode=disable".format(
            self.postgres[0],
            self.postgres[1]
        )
        self.storage = CockroachStorage(
            dsn=dsn, name='db', pool_size=25,
            conn_acquire_timeout=0.1)
        await self.storage.initialize(self.loop)
        return self.storage

    async def __aexit__(self, exc_type, exc, tb):
        await self.storage._read_conn.execute("DROP TABLE IF EXISTS objects;")
        await self.storage._read_conn.execute("DROP TABLE IF EXISTS blobs;")
        await self.storage.create()
        await self.storage.finalize()


@pytest.fixture(scope='function')
async def cockroach_storage(postgres, dummy_request, loop):
    return CockroachStorageAsyncContextManager(dummy_request, loop, postgres)
