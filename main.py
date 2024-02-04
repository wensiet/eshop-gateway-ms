import sentry_sdk
import uvicorn

import config
from api import products_router
from api import authorization_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from logmod import get_logger

sentry_sdk.init(
    dsn="https://667b4cfbf3b29df190748ccac1ee04d8@"
        "o4506655030378496.ingest.sentry.io/4506655032147968",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = FastAPI(title="API_NAME",
              description="API_DESC",
              version="0.2.0",
              docs_url='/docs',
              redoc_url='/redoc',
              openapi_url='/openapi.json')
app.include_router(products_router, prefix="")
app.include_router(authorization_router, prefix="")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conf = config.get_config()
logger = get_logger(f"http://{conf['loki']['host']}:{conf['loki']['port']}/loki/api/v1/push")

if __name__ == "__main__":
    PORT = 8000
    logger.info(f"gateway services started on :{PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT, root_path="/api/v1")
