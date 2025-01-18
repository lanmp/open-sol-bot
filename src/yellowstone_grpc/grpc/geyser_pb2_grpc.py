# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
import warnings

import yellowstone_grpc.grpc.geyser_pb2 as geyser__pb2

GRPC_GENERATED_VERSION = "1.68.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in geyser_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class GeyserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.stream_stream(
            "/geyser.Geyser/Subscribe",
            request_serializer=geyser__pb2.SubscribeRequest.SerializeToString,
            response_deserializer=geyser__pb2.SubscribeUpdate.FromString,
            _registered_method=True,
        )
        self.Ping = channel.unary_unary(
            "/geyser.Geyser/Ping",
            request_serializer=geyser__pb2.PingRequest.SerializeToString,
            response_deserializer=geyser__pb2.PongResponse.FromString,
            _registered_method=True,
        )
        self.GetLatestBlockhash = channel.unary_unary(
            "/geyser.Geyser/GetLatestBlockhash",
            request_serializer=geyser__pb2.GetLatestBlockhashRequest.SerializeToString,
            response_deserializer=geyser__pb2.GetLatestBlockhashResponse.FromString,
            _registered_method=True,
        )
        self.GetBlockHeight = channel.unary_unary(
            "/geyser.Geyser/GetBlockHeight",
            request_serializer=geyser__pb2.GetBlockHeightRequest.SerializeToString,
            response_deserializer=geyser__pb2.GetBlockHeightResponse.FromString,
            _registered_method=True,
        )
        self.GetSlot = channel.unary_unary(
            "/geyser.Geyser/GetSlot",
            request_serializer=geyser__pb2.GetSlotRequest.SerializeToString,
            response_deserializer=geyser__pb2.GetSlotResponse.FromString,
            _registered_method=True,
        )
        self.IsBlockhashValid = channel.unary_unary(
            "/geyser.Geyser/IsBlockhashValid",
            request_serializer=geyser__pb2.IsBlockhashValidRequest.SerializeToString,
            response_deserializer=geyser__pb2.IsBlockhashValidResponse.FromString,
            _registered_method=True,
        )
        self.GetVersion = channel.unary_unary(
            "/geyser.Geyser/GetVersion",
            request_serializer=geyser__pb2.GetVersionRequest.SerializeToString,
            response_deserializer=geyser__pb2.GetVersionResponse.FromString,
            _registered_method=True,
        )


class GeyserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Subscribe(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetLatestBlockhash(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetBlockHeight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetSlot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def IsBlockhashValid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GeyserServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Subscribe": grpc.stream_stream_rpc_method_handler(
            servicer.Subscribe,
            request_deserializer=geyser__pb2.SubscribeRequest.FromString,
            response_serializer=geyser__pb2.SubscribeUpdate.SerializeToString,
        ),
        "Ping": grpc.unary_unary_rpc_method_handler(
            servicer.Ping,
            request_deserializer=geyser__pb2.PingRequest.FromString,
            response_serializer=geyser__pb2.PongResponse.SerializeToString,
        ),
        "GetLatestBlockhash": grpc.unary_unary_rpc_method_handler(
            servicer.GetLatestBlockhash,
            request_deserializer=geyser__pb2.GetLatestBlockhashRequest.FromString,
            response_serializer=geyser__pb2.GetLatestBlockhashResponse.SerializeToString,
        ),
        "GetBlockHeight": grpc.unary_unary_rpc_method_handler(
            servicer.GetBlockHeight,
            request_deserializer=geyser__pb2.GetBlockHeightRequest.FromString,
            response_serializer=geyser__pb2.GetBlockHeightResponse.SerializeToString,
        ),
        "GetSlot": grpc.unary_unary_rpc_method_handler(
            servicer.GetSlot,
            request_deserializer=geyser__pb2.GetSlotRequest.FromString,
            response_serializer=geyser__pb2.GetSlotResponse.SerializeToString,
        ),
        "IsBlockhashValid": grpc.unary_unary_rpc_method_handler(
            servicer.IsBlockhashValid,
            request_deserializer=geyser__pb2.IsBlockhashValidRequest.FromString,
            response_serializer=geyser__pb2.IsBlockhashValidResponse.SerializeToString,
        ),
        "GetVersion": grpc.unary_unary_rpc_method_handler(
            servicer.GetVersion,
            request_deserializer=geyser__pb2.GetVersionRequest.FromString,
            response_serializer=geyser__pb2.GetVersionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "geyser.Geyser", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("geyser.Geyser", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Geyser(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Subscribe(
        request_iterator,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            "/geyser.Geyser/Subscribe",
            geyser__pb2.SubscribeRequest.SerializeToString,
            geyser__pb2.SubscribeUpdate.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Ping(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/geyser.Geyser/Ping",
            geyser__pb2.PingRequest.SerializeToString,
            geyser__pb2.PongResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def GetLatestBlockhash(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/geyser.Geyser/GetLatestBlockhash",
            geyser__pb2.GetLatestBlockhashRequest.SerializeToString,
            geyser__pb2.GetLatestBlockhashResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def GetBlockHeight(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/geyser.Geyser/GetBlockHeight",
            geyser__pb2.GetBlockHeightRequest.SerializeToString,
            geyser__pb2.GetBlockHeightResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def GetSlot(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/geyser.Geyser/GetSlot",
            geyser__pb2.GetSlotRequest.SerializeToString,
            geyser__pb2.GetSlotResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def IsBlockhashValid(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/geyser.Geyser/IsBlockhashValid",
            geyser__pb2.IsBlockhashValidRequest.SerializeToString,
            geyser__pb2.IsBlockhashValidResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def GetVersion(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/geyser.Geyser/GetVersion",
            geyser__pb2.GetVersionRequest.SerializeToString,
            geyser__pb2.GetVersionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
