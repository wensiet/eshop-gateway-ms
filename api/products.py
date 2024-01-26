from fastapi import APIRouter
from fastapi.responses import JSONResponse

import schemas

from protantic import make_model, convert_from_proto, convert_to_proto
import products_pb2

import grpc

import products_pb2_grpc

router = APIRouter()

gRPC_channel = grpc.insecure_channel("products-ms:9090")
stub = products_pb2_grpc.ProductServStub(channel=gRPC_channel)


@router.get("/product/{pid}", tags=["Products"], responses={
    200: {"model": make_model(products_pb2.Product)},
    400: {"model": schemas.ErrorResponse}
})
async def get_product(pid: str):
    try:
        response = stub.GetProduct(products_pb2.GetProductRequest(id=pid))
        return convert_from_proto(response)
    except grpc.RpcError as e:
        print(e)
        return JSONResponse(status_code=400, content={"error": e.details()})


@router.get("/products", tags=["Products"], responses={
    200: {"model": schemas.GetProductsResponse},
    400: {"model": schemas.ErrorResponse}
})
async def get_products(page: int, limit: int = 10):
    response = stub.GetProducts(products_pb2.GetProductsRequest(page=page, limit=limit))
    return schemas.GetProductsResponse(response).model_dump()


@router.post("/product", tags=["Products"], responses={
    200: {"model": make_model(products_pb2.CreateProductResponse)},
    400: {"model": schemas.ErrorResponse}
})
async def create_product(product: make_model(products_pb2.CreateProductRequest)):
    try:
        response = stub.CreateProduct(convert_to_proto(products_pb2.CreateProductRequest, product))
        return convert_from_proto(response).model_dump()
    except grpc.RpcError as e:
        return JSONResponse(status_code=400, content={"error": e.details()})
