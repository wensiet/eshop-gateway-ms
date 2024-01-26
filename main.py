import uvicorn
from fastapi import FastAPI
from api.products import products_router

app = FastAPI()
app.include_router(products_router)

if __name__ == '__main__':
    uvicorn.run(app)
