import grpc
from fastapi import APIRouter
from starlette.responses import JSONResponse

import authorization_pb2
import authorization_pb2_grpc
import config
from protantic import make_model, convert_from_proto, convert_to_proto

router = APIRouter()
conf = config.get_config()

gRPC_channel = grpc.insecure_channel(f"{conf['authorization']['host']}:{conf['authorization']['port']}")
stub = authorization_pb2_grpc.AuthorizationStub(gRPC_channel)


@router.post("/login", tags=["Authorization"])
async def login(request: make_model(authorization_pb2.LoginRequest)):
    try:
        response = stub.Login(convert_to_proto(authorization_pb2.LoginRequest, request))
        return JSONResponse(convert_from_proto(response).model_dump(), status_code=200)
    except grpc.RpcError as e:
        return JSONResponse(status_code=400, content={"error": e.details()})


@router.post("/register", tags=["Authorization"], responses={200: {
}})
async def register(request: make_model(authorization_pb2.RegisterRequest)):
    try:
        stub.Register(convert_to_proto(authorization_pb2.RegisterRequest, request))
        return
    except grpc.RpcError as e:
        return JSONResponse(status_code=400, content={"error": e.details()})
