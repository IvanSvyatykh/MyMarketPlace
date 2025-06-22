import uvicorn
from fastapi import FastAPI
from goods_service.src.presentation.rest.v1.goods import goods_router
from config import PORT
from goods_service.src.domain.exceptions.goods_exceptions import DomainException
from goods_service.src.presentation.rest.error_handlers.goods_handlers import domain_error_handler

app = FastAPI()

app.include_router(goods_router)
app.exception_handler(DomainException)(domain_error_handler)
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=PORT)
