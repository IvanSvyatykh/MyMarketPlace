from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import status
from goods_service.src.domain.exceptions.goods_exceptions import CategoryNotFound, CategoryAlreadyExists, \
    DomainException


async def domain_error_handler(request: Request, exc: DomainException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    if isinstance(exc, CategoryNotFound):
        status_code = status.HTTP_404_NOT_FOUND

    if isinstance(exc, CategoryAlreadyExists):
        status_code = status.HTTP_409_CONFLICT

    return JSONResponse(
        status_code=status_code,
        content={
            "error": str(exc),
            "type": exc.__class__.__name__
        }
    )
