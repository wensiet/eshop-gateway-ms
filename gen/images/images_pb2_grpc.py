# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gen.images import images_pb2 as gen_dot_images_dot_images__pb2


class ImagesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadImage = channel.unary_unary(
                '/images.Images/UploadImage',
                request_serializer=gen_dot_images_dot_images__pb2.UploadImageRequest.SerializeToString,
                response_deserializer=gen_dot_images_dot_images__pb2.Empty.FromString,
                )
        self.GetProductImages = channel.unary_unary(
                '/images.Images/GetProductImages',
                request_serializer=gen_dot_images_dot_images__pb2.GetProductImagesRequest.SerializeToString,
                response_deserializer=gen_dot_images_dot_images__pb2.GetProductImagesResponse.FromString,
                )


class ImagesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProductImages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImagesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadImage': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadImage,
                    request_deserializer=gen_dot_images_dot_images__pb2.UploadImageRequest.FromString,
                    response_serializer=gen_dot_images_dot_images__pb2.Empty.SerializeToString,
            ),
            'GetProductImages': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProductImages,
                    request_deserializer=gen_dot_images_dot_images__pb2.GetProductImagesRequest.FromString,
                    response_serializer=gen_dot_images_dot_images__pb2.GetProductImagesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'images.Images', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Images(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/images.Images/UploadImage',
            gen_dot_images_dot_images__pb2.UploadImageRequest.SerializeToString,
            gen_dot_images_dot_images__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProductImages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/images.Images/GetProductImages',
            gen_dot_images_dot_images__pb2.GetProductImagesRequest.SerializeToString,
            gen_dot_images_dot_images__pb2.GetProductImagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)