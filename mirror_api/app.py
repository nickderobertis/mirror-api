from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mirror_api._router import router


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, tags=["sample"])

    return app
