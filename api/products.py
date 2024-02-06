import schemas
from services import ProductsService

from fastapi import APIRouter

router = APIRouter()

products_service = ProductsService()


@router.get("/product/info/{pid}", tags=["Products"], responses={
    200: {"model": schemas.Product},
    400: {"model": schemas.ErrorResponse},
    404: {"model": schemas.ErrorResponse},
})
async def get_product(pid: str):
    response = products_service.get_product(pid)
    products_service.logger.info(f"{response.status_code} | GET /product/info/{pid}")
    return response


@router.get("/products", tags=["Products"], responses={
    200: {"model": schemas.GetProductsResponse},
    400: {"model": schemas.ErrorResponse}
})
async def get_products(page: int, limit: int = 10):
    response = products_service.get_products(page, limit)
    products_service.logger.info(f"{response.status_code} | GET /products")
    return response


@router.post("/product", tags=["Products"], responses={
    200: {"model": schemas.CreateProductResponse},
    400: {"model": schemas.ErrorResponse}
})
async def create_product(product: schemas.CreateProductRequest):
    response = products_service.create_product(product.title,
                                               product.description,
                                               product.price,
                                               product.quantity)
    products_service.logger.info(f"{response.status_code} | POST /product")
    return response
