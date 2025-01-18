from typing import AsyncIterator, Optional
from grpc.aio import Channel, StreamStreamCall
from . import geyser_pb2

class GeyserStub:
    def __init__(self, channel: Channel) -> None: ...
    def Subscribe(
        self, request_iterator: AsyncIterator[geyser_pb2.SubscribeRequest]
    ) -> StreamStreamCall[geyser_pb2.SubscribeRequest, geyser_pb2.SubscribeUpdate]: ...
    async def Ping(
        self, request: geyser_pb2.PingRequest
    ) -> geyser_pb2.PongResponse: ...
    async def GetLatestBlockhash(
        self, request: geyser_pb2.GetLatestBlockhashRequest
    ) -> geyser_pb2.GetLatestBlockhashResponse: ...
    async def GetBlockHeight(
        self, request: geyser_pb2.GetBlockHeightRequest
    ) -> geyser_pb2.GetBlockHeightResponse: ...
    async def GetSlot(
        self, request: geyser_pb2.GetSlotRequest
    ) -> geyser_pb2.GetSlotResponse: ...
    async def IsBlockhashValid(
        self, request: geyser_pb2.IsBlockhashValidRequest
    ) -> geyser_pb2.IsBlockhashValidResponse: ...
    async def GetVersion(
        self, request: geyser_pb2.GetVersionRequest
    ) -> geyser_pb2.GetVersionResponse: ...
