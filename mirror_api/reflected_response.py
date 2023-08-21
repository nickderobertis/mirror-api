from json import JSONDecodeError
from typing import Dict, Optional, Union

from fastapi import Request
from pydantic import BaseModel, Field


class ReflectedResponse(BaseModel):
    method: str
    url: str
    headers: Union[Dict[str, str], None]
    cookies: Union[Dict[str, str], None]
    json_: Union[dict, list, None] = Field(alias="json")
    body: str
    form: Union[Dict[str, str], None]

    @classmethod
    async def from_request(cls, request: Request) -> "ReflectedResponse":
        body_bytes = await request.body()

        return cls(
            method=request.method,
            url=str(request.url),
            headers=dict(request.headers) if request.headers else None,
            cookies=dict(request.cookies) if request.cookies else None,
            json=await _get_json_from_request(request),
            body=body_bytes.decode(),
            form=await _get_form_from_request(request),
        )


async def _get_json_from_request(request: Request) -> Optional[dict]:
    try:
        return await request.json()
    except JSONDecodeError:
        return None


async def _get_form_from_request(request: Request) -> Optional[dict]:
    data = await request.form()
    if not data:
        return None
    return dict(data)
