from fastapi import UploadFile
from pydantic import BaseModel
from typing import List


class Empty(BaseModel):
    pass


class UploadImageRequest(BaseModel):
    image: UploadFile
    title: str
    pid: str


class GetProductImagesRequest(BaseModel):
    product_id: str


class GetProductImagesResponse(BaseModel):
    total: int
    image_paths: List[str]
