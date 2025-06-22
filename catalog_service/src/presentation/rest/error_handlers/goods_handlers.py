from fastapi import Request
from fastapi.responses import JSONResponse
from catalog_service.src.domain.exceptions.goods_exceptions import CategoryNotFound


async def domain_error_handler(request: Request, exc: Exception):
    status_code = 500
    if isinstance(exc, CategoryNotFound):
        status_code = 400

    return JSONResponse(
        status_code=status_code,
        content={
            "error": str(exc),
            "type": exc.__class__.__name__
        }
    )
