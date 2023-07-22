import pytest
from configs.database import engine
from configs.env import env
from faker import Faker
from fastapi.testclient import TestClient
from server import app

from tests.stubs.model import Model

"""
---------------------------------------------------------------------------
API Reference - pytest_sessionstart
---------------------------------------------------------------------------

Called after the Session object has been created and before performing
collection and entering the run test loop.

"""


def pytest_sessionstart(session):
    create_model_table()


def create_model_table():
    Model.metadata.create_all(engine)


"""
---------------------------------------------------------------------------
API Reference - pytest_sessionfinish
---------------------------------------------------------------------------

Called after whole test run finished, right before returning the exit status to
the system.

"""


def pytest_sessionfinish(session):
    drop_all_tables()


def drop_all_tables():
    if env("APP_ENV") == "test" and env("DB_CONNECTION") == "sqlite":
        Model.metadata.drop_all(engine)


"""
---------------------------------------------------------------------------
Fixtures - widely used fixtures
---------------------------------------------------------------------------

Widely used fixtures are the ones used across many layers of test.

"""


@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)


@pytest.fixture(scope="module")
def faker():
    return Faker()
