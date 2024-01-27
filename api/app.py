import uvicorn
from fastapi import FastAPI

from api.products import router as products_router
from api.authorization import router as authorization_router
import sentry_sdk

sentry_sdk.init(
    dsn="https://glet_05f1d570dd5b0f3ed16431f86bac28ca@observe.gitlab.com:443/errortracking/api/v1/projects/54282896",

    # Enable performance monitoring
    enable_tracing=True,
)

app = FastAPI(title="API_NAME",
              description="API_DESC",
              version="0.2.0",
              docs_url='/docs',
              redoc_url='/redoc',
              openapi_url='/openapi.json')
app.include_router(products_router, prefix="")
app.include_router(authorization_router, prefix="")

if __name__ == "__main__":
    uvicorn.run(app)
