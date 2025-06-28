from fastapi import Response, Request, HTTPException
from typing import Callable, Awaitable

ALLOWED_MIME_TYPES = {"image/jpeg", "image/png"}


async def file_validation_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]):
    path = request.url.path
    if path == "/good/photo":
        form_data = await request.form()
        for file in form_data.values():
            if hasattr(file, "content_type") and file.content_type not in ALLOWED_MIME_TYPES:
                raise HTTPException(400, detail=f"Недопустимый тип файла. Разрешены: {ALLOWED_MIME_TYPES}")
    return await call_next(request)
