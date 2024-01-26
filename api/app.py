import uvicorn
from fastapi import FastAPI

from api.products import router as products_router
from api.authorization import router as authorization_router

app = FastAPI(title="API_NAME",
              description="API_DESC",
              version="0.2.0",
              docs_url='/docs',
              redoc_url='/redoc',
              openapi_url='/openapi.json')
app.include_router(products_router, prefix="")
app.include_router(authorization_router)

if __name__ == "__main__":
    uvicorn.run(app)
