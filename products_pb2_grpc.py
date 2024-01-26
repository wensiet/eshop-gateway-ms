# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import products_pb2 as products__pb2


class ProductServStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProduct = channel.unary_unary(
                '/product.ProductServ/GetProduct',
                request_serializer=products__pb2.GetProductRequest.SerializeToString,
                response_deserializer=products__pb2.Product.FromString,
                )
        self.GetProducts = channel.unary_unary(
                '/product.ProductServ/GetProducts',
                request_serializer=products__pb2.GetProductsRequest.SerializeToString,
                response_deserializer=products__pb2.GetProductsResponse.FromString,
                )
        self.CreateProduct = channel.unary_unary(
                '/product.ProductServ/CreateProduct',
                request_serializer=products__pb2.CreateProductRequest.SerializeToString,
                response_deserializer=products__pb2.CreateProductResponse.FromString,
                )
        self.UpdateProduct = channel.unary_unary(
                '/product.ProductServ/UpdateProduct',
                request_serializer=products__pb2.UpdateProductRequest.SerializeToString,
                response_deserializer=products__pb2.Product.FromString,
                )
        self.DeleteProduct = channel.unary_unary(
                '/product.ProductServ/DeleteProduct',
                request_serializer=products__pb2.DeleteProductRequest.SerializeToString,
                response_deserializer=products__pb2.DeleteProductResponse.FromString,
                )


class ProductServServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=products__pb2.GetProductRequest.FromString,
                    response_serializer=products__pb2.Product.SerializeToString,
            ),
            'GetProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProducts,
                    request_deserializer=products__pb2.GetProductsRequest.FromString,
                    response_serializer=products__pb2.GetProductsResponse.SerializeToString,
            ),
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=products__pb2.CreateProductRequest.FromString,
                    response_serializer=products__pb2.CreateProductResponse.SerializeToString,
            ),
            'UpdateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProduct,
                    request_deserializer=products__pb2.UpdateProductRequest.FromString,
                    response_serializer=products__pb2.Product.SerializeToString,
            ),
            'DeleteProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProduct,
                    request_deserializer=products__pb2.DeleteProductRequest.FromString,
                    response_serializer=products__pb2.DeleteProductResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'product.ProductServ', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductServ(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.ProductServ/GetProduct',
            products__pb2.GetProductRequest.SerializeToString,
            products__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.ProductServ/GetProducts',
            products__pb2.GetProductsRequest.SerializeToString,
            products__pb2.GetProductsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.ProductServ/CreateProduct',
            products__pb2.CreateProductRequest.SerializeToString,
            products__pb2.CreateProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.ProductServ/UpdateProduct',
            products__pb2.UpdateProductRequest.SerializeToString,
            products__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/product.ProductServ/DeleteProduct',
            products__pb2.DeleteProductRequest.SerializeToString,
            products__pb2.DeleteProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
