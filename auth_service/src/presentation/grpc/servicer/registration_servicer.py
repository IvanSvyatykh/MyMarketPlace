import grpc

from auth_service.src.presentation.grpc.generated.auth_pb2 import RegisterRequest, RegisterResponse
from auth_service.src.presentation.grpc.generated.auth_pb2_grpc import RegistrationServiceServicer


class RegistrationServicer(RegistrationServiceServicer):

    async def Registration(self, request: RegisterRequest, context: grpc.aio.ServicerContext) -> RegisterResponse:
        pass
