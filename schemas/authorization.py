from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    token: str


class RegisterRequest(BaseModel):
    email: str
    password: str


class Empty(BaseModel):
    pass
