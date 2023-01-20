from typing import Union

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(
            self, request: Request, call_next
    ) -> Union[Response, JSONResponse]:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(content={'error': str(e)}, status_code=500)
