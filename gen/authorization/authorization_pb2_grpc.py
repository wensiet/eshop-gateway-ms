# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gen.authorization import authorization_pb2 as gen_dot_authorization_dot_authorization__pb2


class AuthorizationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/Authorization/Login',
                request_serializer=gen_dot_authorization_dot_authorization__pb2.LoginRequest.SerializeToString,
                response_deserializer=gen_dot_authorization_dot_authorization__pb2.LoginResponse.FromString,
                )
        self.Register = channel.unary_unary(
                '/Authorization/Register',
                request_serializer=gen_dot_authorization_dot_authorization__pb2.RegisterRequest.SerializeToString,
                response_deserializer=gen_dot_authorization_dot_authorization__pb2.Empty.FromString,
                )


class AuthorizationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthorizationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=gen_dot_authorization_dot_authorization__pb2.LoginRequest.FromString,
                    response_serializer=gen_dot_authorization_dot_authorization__pb2.LoginResponse.SerializeToString,
            ),
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=gen_dot_authorization_dot_authorization__pb2.RegisterRequest.FromString,
                    response_serializer=gen_dot_authorization_dot_authorization__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Authorization', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Authorization(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Authorization/Login',
            gen_dot_authorization_dot_authorization__pb2.LoginRequest.SerializeToString,
            gen_dot_authorization_dot_authorization__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Authorization/Register',
            gen_dot_authorization_dot_authorization__pb2.RegisterRequest.SerializeToString,
            gen_dot_authorization_dot_authorization__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)