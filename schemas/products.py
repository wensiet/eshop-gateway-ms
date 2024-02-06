from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: str
    title: str
    description: str
    price: float
    quantity: int


class GetProductRequest(BaseModel):
    id: str


class GetProductResponse(BaseModel):
    product: Product


class GetProductsRequest(BaseModel):
    page: int
    limit: int


class GetProductsResponse(BaseModel):
    products: List[Product]
    total: int


class CreateProductRequest(BaseModel):
    title: str
    description: str
    price: float
    quantity: int


class CreateProductResponse(BaseModel):
    id: str
