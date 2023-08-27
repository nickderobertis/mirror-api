import json
from typing import Dict
from unittest.mock import patch
from urllib.parse import urlencode

import pytest
from httpx import AsyncClient

from mirror_api import ReflectedResponse
from mirror_api._router import settings

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
    cookies = {
        "cookie1": "test",
    }
    response = await client.get("/", params=params, headers=headers, cookies=cookies)
    assert response.status_code == 200
    response = ReflectedResponse(**response.json())
    assert response.method == "GET"
    assert _has_headers(headers, response.headers)
    assert response.cookies == cookies
    assert response.json_ is None
    assert response.body == ""
    assert urlencode(params) in response.url
    assert response.form is None
    assert response.api_path == "/"


@pytest.mark.anyio
async def test_mirrors_get_request_at_sub_url(client: AsyncClient):
    params = {
        "q": "test",
        "page": 1,
    }
    headers = {
        "x-test-header": "test",
    }
    cookies = {
        "cookie1": "test",
    }
    response = await client.get(
        "/nested/url", params=params, headers=headers, cookies=cookies
    )
    assert response.status_code == 200
    response = ReflectedResponse(**response.json())
    assert response.method == "GET"
    assert _has_headers(headers, response.headers)
    assert response.cookies == cookies
    assert response.json_ is None
    assert response.body == ""
    assert urlencode(params) in response.url
    assert response.form is None
    assert response.api_path == "/nested/url"


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
    assert response.api_path == "/"


@pytest.fixture(params=["PUT", "DELETE", "POST", "PATCH", "OPTIONS"])
def method(request):
    return request.param


@pytest.fixture(params=[200, 400, 500])
def status_code(request):
    return request.param


@pytest.mark.anyio
async def test_mirrors_json_request(client: AsyncClient, method: str, status_code: int):
    await _standard_json_test(method, status_code, client)


async def _standard_json_test(method: str, status_code: int, client: AsyncClient):
    with patch.object(settings, "status_code", status_code):
        params = {
            "q": "test",
            "page": 1,
        }
        headers = {
            "x-test-header": "test",
        }
        json_data = {
            "test": "test",
        }
        response = await client.request(
            method, "/", params=params, headers=headers, json=json_data
        )
        assert response.status_code == status_code
        response = ReflectedResponse(**response.json())
        assert response.method == method
        assert _has_headers(headers, response.headers)
        assert response.cookies is None
        assert response.json_ == json_data
        assert response.body == json.dumps(json_data)
        assert urlencode(params) in response.url
        assert response.form is None
        assert response.api_path == "/"


def _has_headers(expect_headers: Dict[str, str], headers: Dict[str, str]) -> bool:
    all_headers = {**DEFAULT_HEADERS, **expect_headers}
    for key, value in all_headers.items():
        if key not in headers or headers[key] != value:
            return False
    return True
