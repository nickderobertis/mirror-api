import pytest
from fastapi import FastAPI
from httpx import AsyncClient


@pytest.fixture(scope="session")
def app() -> FastAPI:
    from mirror_api import create_app

    app = create_app()

    yield app


@pytest.fixture(scope="session")
async def client(app) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
