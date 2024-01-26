from typing import List

from pydantic import BaseModel

import products_pb2
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


class ErrorResponse(BaseModel):
    error: str
