import re
from logging import Logger

from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import config

from protantic import make_model, convert_from_proto, convert_to_proto

import gen.images.images_pb2 as images_pb2
import gen.images.images_pb2_grpc as images_pb2_grpc
import gen.products.products_pb2 as products_pb2
import gen.products.products_pb2_grpc as products_pb2_grpc

import schemas
from logmod import get_logger

import grpc
from grpc.aio._call import AioRpcError

router = APIRouter()
conf = config.get_config()

gRPC_channel = grpc.insecure_channel(f"{conf['products']['host']}:{conf['products']['port']}")
stub = products_pb2_grpc.ProductServStub(channel=gRPC_channel)
images_stub = images_pb2_grpc.ImagesStub(channel=gRPC_channel)

logger: Logger = get_logger(f"http://{conf['loki']['host']}:"
                            f"{conf['loki']['port']}/loki/api/v1/push")


@router.get("/product/info/{pid}", tags=["Products"], responses={
    200: {"model": make_model(products_pb2.Product)},
    400: {"model": schemas.ErrorResponse}
})
async def get_product(pid: str):
    try:
        response = stub.GetProduct(products_pb2.GetProductRequest(id=pid))
        logger.info(f"returned product with id {pid}")
        return convert_from_proto(response)
    except AioRpcError as e:
        logger.warning(f"unable to get product with id {pid}: {e.details()}")
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return JSONResponse(status_code=404, content={"error": e.details()})
        else:
            return JSONResponse(status_code=500, content={"error": e.details()})
    except Exception as e:
        logger.error(f"unexpected error: {e}")
        return JSONResponse(status_code=500, content={"error": "unexpected error"})


@router.get("/products", tags=["Products"], responses={
    200: {"model": schemas.GetProductsResponse},
    400: {"model": schemas.ErrorResponse}
})
async def get_products(page: int, limit: int = 10):
    try:
        response = stub.GetProducts(products_pb2.GetProductsRequest(page=page, limit=limit))
        return schemas.GetProductsResponse(response).model_dump()
    except AioRpcError as e:
        logger.warning(f"unable to get products: {e.details()}")
        return JSONResponse(status_code=500, content={"error": "internal server error"})


@router.post("/product", tags=["Products"], responses={
    200: {"model": make_model(products_pb2.CreateProductResponse)},
    400: {"model": schemas.ErrorResponse}
})
async def create_product(product: make_model(products_pb2.CreateProductRequest)):
    try:
        response = stub.CreateProduct(convert_to_proto(products_pb2.CreateProductRequest, product))
        return convert_from_proto(response).model_dump()
    except AioRpcError as e:
        logger.warning(f"unable to create product: {e.details()}")
        if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            return JSONResponse(status_code=400, content={"error": e.details()})
        return JSONResponse(status_code=500, content={"error": "internal server error"})
    except Exception as e:
        logger.error(f"unexpected error: {e}")
        return JSONResponse(status_code=500, content={"error": "unexpected error"})


@router.post("/product/images/upload", tags=["Products"], responses={})
async def upload_product_images(request_image: UploadFile,
                                request_image_name: str, request_product_id: str):
    if not re.match(r'^[a-zA-Z0-9]+\.png$', request_image.filename):
        return JSONResponse(status_code=400,
                            content={"error": "incorrect file type, use only .png"}
                            )
    try:
        image_bytes = await request_image.read()
        images_stub.UploadImage(
            images_pb2.UploadImageRequest(image=image_bytes,
                                          name=request_image_name,
                                          product_id=request_product_id))
        return JSONResponse(status_code=200, content={"message": "ok"})
    except AioRpcError as e:
        logger.warning(f"unable to upload image: {e.details()}")
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return JSONResponse(status_code=404, content={"error", e.details()})
        return JSONResponse(status_code=500, content={"error": "internal server error"})
    except Exception as e:
        logger.error(f"unexpected error: {e}")
        return JSONResponse(status_code=500, content={"error": "unexpected error"})


@router.get("/product/images", tags=["Products"], responses={})
async def get_product_images(product_id: str):
    try:
        response = images_stub.GetProductImages(
            images_pb2.GetProductImagesRequest(product_id=product_id)
        )
        result: schemas.GetProductImagesResponse | BaseModel = convert_from_proto(
            response,
            schemas.GetProductImagesResponse
        )
        for i, path in enumerate(result.image_paths):
            result.image_paths[i] = conf['domain'] + "/media/products/" + path
        return JSONResponse(status_code=200,
                            content=result.model_dump())
    except AioRpcError as e:
        logger.warning(f"unable to get images: {e.details()}")
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return JSONResponse(status_code=404, content={"error", e.details()})
        return JSONResponse(status_code=500, content={"error": "internal server error"})
    except Exception as e:
        logger.error(f"unexpected error: {e}")
        return JSONResponse(status_code=500, content={"error": "unexpected error"})
