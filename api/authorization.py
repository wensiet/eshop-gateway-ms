import grpc
from grpc._channel import _InactiveRpcError
from fastapi import APIRouter
from starlette.responses import JSONResponse

import gen.authorization.authorization_pb2 as authorization_pb2
import gen.authorization.authorization_pb2_grpc as authorization_pb2_grpc
import config
from logmod import get_logger
from protantic import make_model, convert_from_proto, convert_to_proto

router = APIRouter()
conf = config.get_config()

gRPC_channel = grpc.insecure_channel(f"{conf['authorization']['host']}:"
                                     f"{conf['authorization']['port']}")
stub = authorization_pb2_grpc.AuthorizationStub(gRPC_channel)
logger = get_logger(f"http://{conf['loki']['host']}:{conf['loki']['port']}/loki/api/v1/push")


# CI CR TEST

@router.post("/login", tags=["Authorization"])
async def login(request: make_model(authorization_pb2.LoginRequest)):
    try:
        response = stub.Login(convert_to_proto(authorization_pb2.LoginRequest, request))
        logger.info(f"user {request.email} logged in")
        return JSONResponse(convert_from_proto(response).model_dump(), status_code=200)
    except _InactiveRpcError as e:
        logger.warning(f"user {request.email} failed to log in")
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return JSONResponse(status_code=404, content={"error": e.details()})
        elif e.code() == grpc.StatusCode.UNAUTHENTICATED:
            return JSONResponse(status_code=400, content={"error": e.details()})
        return JSONResponse(status_code=500, content={"error": e.details()})
    except Exception as e:
        logger.error(f"unexpected error: {e}")
        return JSONResponse(status_code=500, content={"error": "unexpected error"})


@router.post("/register", tags=["Authorization"], responses={200: {
}})
async def register(request: make_model(authorization_pb2.RegisterRequest)):
    try:
        stub.Register(convert_to_proto(authorization_pb2.RegisterRequest, request))
        logger.info(f"user {request.email} registered")
        return
    except _InactiveRpcError as e:
        logger.warning(f"user {request.email} failed to register")
        if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            return JSONResponse(status_code=400, content={"error": e.details()})
        elif e.code() == grpc.StatusCode.ALREADY_EXISTS:
            return JSONResponse(status_code=400, content={"error": e.details()})
        return JSONResponse(status_code=500, content={"error": e.details()})
    except Exception as e:
        logger.error(f"unexpected error: {e}")
        return JSONResponse(status_code=500, content={"error": "unexpected error"})
