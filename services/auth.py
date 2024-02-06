import grpc
from grpc._channel import _InactiveRpcError
from loguru import logger
from fastapi.responses import JSONResponse

import config
import schemas
from gen.authorization import authorization_pb2_grpc, authorization_pb2
from services.generic import GenericGRPC


class AuthService:
    def __init__(self):
        self.config = config.get_config()
        self.channel = grpc.insecure_channel(
            f"{self.config['authorization']['host']}:{self.config['authorization']['port']}"
        )
        self.stub = authorization_pb2_grpc.AuthorizationStub(channel=self.channel)
        self.logger = logger

    def login(self, email: str, password: str):
        try:
            response = self.stub.Login(
                authorization_pb2.LoginRequest(email=email, password=password)
            )
            schema = schemas.LoginResponse(
                token=response.token,
            )
            self.logger.info(f"user {email} logged in")
            return JSONResponse(schema.model_dump(), status_code=200)
        except _InactiveRpcError as e:
            self.logger.warning(f"user {email} failed to log in")
            return JSONResponse(status_code=GenericGRPC.get_http_code_from_grpc_code(e),
                                content={"error": e.details()})
        except Exception as e:
            self.logger.error(f"unexpected error: {e}")
            return JSONResponse(status_code=500, content={"error": "unexpected error"})

    def register(self, email: str, password: str):
        try:
            self.stub.Register(
                authorization_pb2.RegisterRequest(email=email, password=password)
            )
            self.logger.info(f"user {email} registered")
            return JSONResponse(status_code=200,
                                content={"message": "user registered successfully"})
        except _InactiveRpcError as e:
            self.logger.warning(f"user {email} failed to register")
            return JSONResponse(status_code=GenericGRPC.get_http_code_from_grpc_code(e),
                                content={"error": e.details()})
        except Exception as e:
            self.logger.error(f"unexpected error: {e}")
            return JSONResponse(status_code=500, content={"error": "unexpected error"})
