from fastapi import FastAPI
from sample_api._router import router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(router, tags=["sample"])

    return app
