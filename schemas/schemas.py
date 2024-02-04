from typing import List

from fastapi import UploadFile
from pydantic import BaseModel

import gen.products.products_pb2 as products_pb2
from protantic import make_model, convert_from_proto

Product = make_model(products_pb2.Product)


class GetProductsResponse(BaseModel):
    total: int
    products: List[Product]

    def __init__(self, proto_message):
        total = proto_message.total
        products = []
        for product in proto_message.products:
            products.append(convert_from_proto(product, pydantic_model=Product))
        super().__init__(total=total, products=products)


class UploadImageRequest(BaseModel):
    image: UploadFile
    name: str
    product_id: str


class GetProductImagesResponse(BaseModel):
    total: int
    image_paths: List[str]


class ErrorResponse(BaseModel):
    error: str
