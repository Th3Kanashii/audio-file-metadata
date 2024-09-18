import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client() -> TestClient:
    """
    Fixture to test the FastAPI application.

    :return: TestClient.
    """
    return TestClient(app)
