"""
An API that returns the structure of the request as the response
"""
__version__ = "1.2.0"

from mirror_api.app import create_app  # noqa: F401
from mirror_api.reflected_response import ReflectedResponse  # noqa: F401
