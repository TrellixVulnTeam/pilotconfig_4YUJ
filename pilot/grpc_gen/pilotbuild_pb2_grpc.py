# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import pilotbuild_pb2 as pilotbuild__pb2

class PilotBuildStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Build = channel.unary_stream(
                '/PilotBuild/Build',
                request_serializer=pilotbuild__pb2.BuildRequest.SerializeToString,
                response_deserializer=pilotbuild__pb2.BuildStatus.FromString,
                )


class PilotBuildServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Build(self, request, context):
        """Build firmware for the given modules
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PilotBuildServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Build': grpc.unary_stream_rpc_method_handler(
                    servicer.Build,
                    request_deserializer=pilotbuild__pb2.BuildRequest.FromString,
                    response_serializer=pilotbuild__pb2.BuildStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PilotBuild', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PilotBuild(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Build(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/PilotBuild/Build',
            pilotbuild__pb2.BuildRequest.SerializeToString,
            pilotbuild__pb2.BuildStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
