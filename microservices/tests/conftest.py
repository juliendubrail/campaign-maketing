import pytest
from starlette.testclient import TestClient

from user_service.main import user_service

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(user_service)
    yield client