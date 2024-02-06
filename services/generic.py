import grpc
from grpc._channel import _InactiveRpcError


class GenericGRPC:
    @staticmethod
    def get_http_code_from_grpc_code(e: _InactiveRpcError):
        if e.code() == grpc.StatusCode.OK:
            return 200
        elif e.code() == grpc.StatusCode.CANCELLED:
            return 499
        elif e.code() == grpc.StatusCode.UNKNOWN:
            return 500
        elif e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            return 400
        elif e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
            return 504
        elif e.code() == grpc.StatusCode.NOT_FOUND:
            return 404
        elif e.code() == grpc.StatusCode.ALREADY_EXISTS:
            return 409
        elif e.code() == grpc.StatusCode.PERMISSION_DENIED:
            return 403
        elif e.code() == grpc.StatusCode.RESOURCE_EXHAUSTED:
            return 429
        elif e.code() == grpc.StatusCode.FAILED_PRECONDITION:
            return 400
        elif e.code() == grpc.StatusCode.ABORTED:
            return 409
        elif e.code() == grpc.StatusCode.OUT_OF_RANGE:
            return 400
        elif e.code() == grpc.StatusCode.UNIMPLEMENTED:
            return 501
        elif e.code() == grpc.StatusCode.INTERNAL:
            return 500
        elif e.code() == grpc.StatusCode.UNAVAILABLE:
            return 503
        elif e.code() == grpc.StatusCode.DATA_LOSS:
            return 500
        elif e.code() == grpc.StatusCode.UNAUTHENTICATED:
            return 401
        return 500
