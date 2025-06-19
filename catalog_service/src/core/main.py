import uvicorn
from fastapi import FastAPI
from catalog_service.src.presentation.rest.v1.goods import goods_router
from config import PORT

app = FastAPI()
app.include_router(goods_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=PORT)
