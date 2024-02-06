import grpc
from grpc._channel import _InactiveRpcError
from loguru import logger

import config
import schemas.products
from caching import get_response, cache_response
from gen.products import products_pb2_grpc, products_pb2
from fastapi.responses import Response, JSONResponse

from services.generic import GenericGRPC


class ProductsService:
    def __init__(self):
        self.config = config.get_config()
        self.channel = grpc.insecure_channel(f"{self.config['products']['host']}:"
                                             f"{self.config['products']['port']}")
        self.stub = products_pb2_grpc.ProductServStub(channel=self.channel)
        self.logger = logger

    def get_product(self, pid: str) -> Response:
        try:
            cached = get_response(f"ProductsService:get_product:{pid}")
            if cached:
                self.logger.info(f"returned cached product with id {pid}")
                return JSONResponse(status_code=200, content=cached)
            response = self.stub.GetProduct(products_pb2.GetProductRequest(id=pid))
            schema = schemas.products.Product(
                id=response.id,
                title=response.title,
                description=response.description,
                price=response.price,
                quantity=response.quantity
            )
            cache_response(f"ProductsService:get_product:{pid}", schema.model_dump(), 30)
            self.logger.info(f"returned product with id {pid}")
            return JSONResponse(status_code=200, content=schema.dict())
        except _InactiveRpcError as e:
            logger.warning(f"failed to get product with id {pid}: {e.details()}")
            return JSONResponse(status_code=GenericGRPC.get_http_code_from_grpc_code(e),
                                content={"error": e.details()})
        except Exception as e:
            logger.error(f"unexpected error: {e}")
            return JSONResponse(status_code=500, content={"error": "unexpected error"})

    def get_products(self, page: int, limit: int) -> Response:
        try:
            cached = get_response(f"ProductsService:get_products:{page}:{limit}")
            if cached:
                self.logger.info(f"returned cached products with request:"
                                 f" ProductsService:get_products:{page}:{limit}")
                return JSONResponse(status_code=200, content=cached)
            response = self.stub.GetProducts(products_pb2.GetProductsRequest(
                page=page,
                limit=limit
            ))
            schema = schemas.products.GetProductsResponse(
                products=[
                    schemas.products.Product(
                        id=product.id,
                        title=product.title,
                        description=product.description,
                        price=product.price,
                        quantity=product.quantity
                    ) for product in response.products
                ],
                total=response.total
            )
            cache_response(f"ProductsService:get_products:{page}:{limit}", schema.model_dump(), 30)
            self.logger.info(f"returned products with request: "
                             f"ProductsService:get_products:{page}:{limit}")
            return JSONResponse(status_code=200, content=schema.model_dump())
        except _InactiveRpcError as e:
            self.logger.warning(f"unable to get products: {e.details()}")
            return JSONResponse(status_code=GenericGRPC.get_http_code_from_grpc_code(e),
                                content={"error": e.details()})
        except Exception as e:
            self.logger.error(f"unexpected error: {e}")
            return JSONResponse(status_code=500, content={"error": "unexpected error"})

    def create_product(self, title: str, description: str, price: float, quantity: int) -> Response:
        try:
            response = self.stub.CreateProduct(products_pb2.CreateProductRequest(
                title=title, description=description, price=price, quantity=quantity
            ))
            return JSONResponse(status_code=200, content={"id": response.id})
        except _InactiveRpcError as e:
            self.logger.warning(f"unable to create product: {e.details()}")
            return JSONResponse(status_code=GenericGRPC.get_http_code_from_grpc_code(e),
                                content={"error": e.details()})
        except Exception as e:
            self.logger.error(f"unexpected error: {e}")
            return JSONResponse(status_code=500, content={"error": "unexpected error"})
