from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from fastapi.testclient import TestClient


def test_root(client: TestClient) -> None:
    """
    Test the root endpoint.

    :param client: fixture to test the FastAPI application.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.template.name == "index.html"
