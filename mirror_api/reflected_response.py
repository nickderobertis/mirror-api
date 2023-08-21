from json import JSONDecodeError
from typing import Dict, Optional, Union

from fastapi import Request
from pydantic import BaseModel, Field


class ReflectedResponse(BaseModel):
    method: str
    url: str
    headers: Dict[str, str]
    cookies: Dict[str, str]
    json_: Union[dict, list, None] = Field(alias="json")
    body: str
    form: Dict[str, str]

    @classmethod
    async def from_request(cls, request: Request) -> "ReflectedResponse":
        body_bytes = await request.body()

        return cls(
            method=request.method,
            url=str(request.url),
            headers=dict(request.headers),
            cookies=dict(request.cookies),
            json=await _get_json_from_request(request),
            body=body_bytes.decode(),
            form=dict(await request.form()),
        )


async def _get_json_from_request(request: Request) -> Optional[dict]:
    try:
        return await request.json()
    except JSONDecodeError:
        return None
