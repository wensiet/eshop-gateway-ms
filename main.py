import json
import logging

import sentry_sdk
import uvicorn

from loguru import logger
from prometheus_fastapi_instrumentator import Instrumentator

import config
from api import products_router
from api import authorization_router
from api import media_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class Application:
    def __init__(self, routers):
        self.logger = logger

        self.logger.debug("logger initialized")

        self.config = config.get_config()
        self.logger.debug("config loaded")

        self.app = FastAPI(
            title="Gateway API",
            description="This is a gateway API, which is the entry point for the services.",
            docs_url='/docs',
            redoc_url='/redoc',
            openapi_url='/openapi.json'
        )

        for router in routers:
            self.app.include_router(router)

        sentry_sdk.init(
            dsn=self.config['sentry'],
            environment=self.config['env'],
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
        )
        self.logger.debug("sentry initialized")

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3001", "http://localhost:3000"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.logger.debug("exposing prometheus metrics")
        Instrumentator().instrument(self.app).expose(self.app)

    def run(self):
        host = '0.0.0.0'
        self.logger.info(f"starting the gateway service, on {host}:{self.config['port']}")
        uvicorn.run(self.app, host="0.0.0.0", port=self.config['port'],
                    root_path=self.config['path'], log_level=logging.CRITICAL)


def serialize(record):
    subset = {
        "timestamp": record["time"].timestamp(),
        "message": record["message"],
        "level": record["level"].name,
    }
    return json.dumps(subset)


def sink(message):
    serialized = serialize(message.record)
    print(serialized)


if __name__ == "__main__":
    logger.remove()
    logger.add(sink)

    app = Application([products_router, authorization_router, media_router])
    app.run()
