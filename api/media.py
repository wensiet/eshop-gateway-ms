from fastapi import APIRouter, UploadFile

import schemas
from services import MediaService

router = APIRouter()
media_service = MediaService()


@router.post("/images/product/upload", tags=["Media"], responses={
    200: {"model": schemas.InfoResponse},
    400: {"model": schemas.ErrorResponse}
})
async def upload_product_images(image: UploadFile,
                                title: str, pid: str):
    response = await media_service.upload_image(title, pid, image)
    media_service.logger.info(f"{response.status_code} | POST /images/product/upload")
    return response


@router.get("/images/product/{pid}", tags=["Media"], responses={
    200: {"model": schemas.GetProductImagesResponse},
    400: {"model": schemas.ErrorResponse}
})
async def get_product_images(pid: str):
    response = media_service.get_product_images(pid)
    media_service.logger.info(f"{response.status_code} | GET /images/product/{pid}")
    return response
