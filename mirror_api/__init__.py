"""
An API that returns the structure of the request as the response
"""
__version__ = "1.0.0"

from mirror_api.app import create_app  # noqa: E402
from mirror_api.reflected_response import ReflectedResponse  # noqa: E402
