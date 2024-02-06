import re

import grpc
from grpc._channel import _InactiveRpcError
from loguru import logger

import config
import schemas
from caching import get_response, cache_response
from gen.images import images_pb2_grpc, images_pb2

from fastapi.responses import JSONResponse
from fastapi import UploadFile

from services.generic import GenericGRPC


class MediaService:

    def __init__(self):
        self.config = config.get_config()
        self.channel = grpc.insecure_channel(f"{self.config['products']['host']}"
                                             f":{self.config['products']['port']}")
        self.images_stub = images_pb2_grpc.ImagesStub(channel=self.channel)
        self.logger = logger

    async def upload_image(self, title: str, pid: str, image: UploadFile) -> JSONResponse:
        if not re.match(r'^[a-zA-Z0-9]+\.png$', image.filename):
            self.logger.info("incorrect file extension, only .png is allowed")
            return JSONResponse(status_code=400,
                                content={"error": "incorrect file extension, only .png is allowed"})
        try:
            image_bytes = await image.read()
            self.images_stub.UploadImage(images_pb2.UploadImageRequest(image=image_bytes,
                                                                       name=title,
                                                                       product_id=pid))
            self.logger.info(f"uploaded image {title} for product {pid}")
            return JSONResponse(status_code=200, content={"message": "image uploaded successfully"})
        except _InactiveRpcError as e:
            self.logger.error(f"failed to upload image: {e.details()}")
            return JSONResponse(status_code=GenericGRPC.get_http_code_from_grpc_code(e),
                                content={"error": e.details()})
        except Exception as e:
            self.logger.error(f"unexpected error: {e}")
            return JSONResponse(status_code=500, content={"error": "unexpected error"})

    def get_product_images(self, pid: str) -> JSONResponse:
        try:
            cached = get_response("MediaService:get_product_images:" + pid)
            if cached:
                self.logger.info(f"returned cached images for product {pid}")
                return JSONResponse(status_code=200, content=cached)
            response = self.images_stub.GetProductImages(
                images_pb2.GetProductImagesRequest(product_id=pid)
            )
            image_paths = [self.config['domain'] + "/products/" +
                           path for path in response.image_paths]
            schema = schemas.GetProductImagesResponse(total=response.total, image_paths=image_paths)
            cache_response("MediaService:get_product_images:"
                           + pid, schema.model_dump(), 30)
            self.logger.info(f"got images for product {pid}")
            return JSONResponse(status_code=200, content=schema.model_dump())
        except _InactiveRpcError as e:
            self.logger.error(f"failed to get images for product {pid}: {e.details()}")
            return JSONResponse(status_code=GenericGRPC.get_http_code_from_grpc_code(e),
                                content={"error": e.details()})
        except Exception as e:
            self.logger.error(f"unexpected error: {e}")
            return JSONResponse(status_code=500, content={"error": "unexpected error"})
