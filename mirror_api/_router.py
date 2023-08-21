"""
A router that for each HTTP method, will return the request as the response
"""
from fastapi import APIRouter, Request
from sample_api.reflected_response import ReflectedResponse

router = APIRouter()


@router.api_route("/{path_name:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def get(request: Request, path_name: str):
    return await ReflectedResponse.from_request(request)
