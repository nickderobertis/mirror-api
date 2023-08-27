"""
A router that for each HTTP method, will return the request as the response
"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from mirror_api._settings import Settings
from mirror_api.reflected_response import ReflectedResponse

router = APIRouter()

settings = Settings()
print("Configured router with settings", settings.json(by_alias=True, indent=2))


@router.api_route(
    "/{path_name:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    response_model=ReflectedResponse,
)
async def get(request: Request, path_name: str):
    data = await ReflectedResponse.from_request(request, f"/{path_name}")
    return JSONResponse(
        content=data.model_dump(by_alias=True), status_code=settings.status_code
    )
