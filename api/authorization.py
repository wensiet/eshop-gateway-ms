import schemas
from services import AuthService

from fastapi import APIRouter

router = APIRouter()

auth_service = AuthService()


@router.post("/login", tags=["Authorization"], responses={
    200: {"model": schemas.LoginResponse},
    400: {"model": schemas.ErrorResponse},
    404: {"model": schemas.ErrorResponse},
})
async def login(request: schemas.LoginRequest):
    response = auth_service.login(request.email, request.password)
    auth_service.logger.info(f"{response.status_code} | GET /login")
    return response


@router.post("/register", tags=["Authorization"],
             responses={
                 200: {"model": schemas.InfoResponse},
                 400: {"model": schemas.ErrorResponse},
                 409: {"model": schemas.ErrorResponse},
             })
async def register(request: schemas.RegisterRequest):
    response = auth_service.register(request.email, request.password)
    auth_service.logger.info(f"{response.status_code} | POST /register")
    return response
