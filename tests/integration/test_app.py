from typing import Dict
from urllib.parse import urlencode

import pytest
from httpx import AsyncClient

from mirror_api import ReflectedResponse

DEFAULT_HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate",
    "host": "test",
    "connection": "keep-alive",
    "user-agent": "python-httpx/0.24.1",
}


@pytest.mark.anyio
async def test_mirrors_get_request(client: AsyncClient):
    params = {
        "q": "test",
        "page": 1,
    }
    headers = {
        "x-test-header": "test",
    }
    response = await client.get("/", params=params, headers=headers)
    assert response.status_code == 200
    response = ReflectedResponse(**response.json())
    assert response.method == "GET"
    assert _has_headers(headers, response.headers)
    assert response.cookies is None
    assert response.json_ is None
    assert response.body == ""
    assert urlencode(params) in response.url
    assert response.form is None


@pytest.mark.anyio
async def test_mirrors_post_form_request(client: AsyncClient):
    params = {
        "q": "test",
        "page": 1,
    }
    headers = {
        "x-test-header": "test",
    }
    form = {
        "test": "test",
    }
    response = await client.post("/", params=params, headers=headers, data=form)
    assert response.status_code == 200
    response = ReflectedResponse(**response.json())
    assert response.method == "POST"
    assert _has_headers(headers, response.headers)
    assert response.cookies is None
    assert response.json_ is None
    assert response.body == "test=test"
    assert urlencode(params) in response.url
    assert response.form == form


def _has_headers(expect_headers: Dict[str, str], headers: Dict[str, str]) -> bool:
    all_headers = {**DEFAULT_HEADERS, **expect_headers}
    for key, value in all_headers.items():
        if key not in headers or headers[key] != value:
            return False
    return True
