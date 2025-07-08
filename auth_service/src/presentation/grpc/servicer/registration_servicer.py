import grpc

from auth_service.src.presentation.grpc.generated.auth_pb2 import RegisterRequest, RegisterResponse
from auth_service.src.presentation.grpc.generated.auth_pb2_grpc import RegistrationServiceServicer
from auth_service.src.application.command.add_user import AddUserCommand
from auth_service.src.application.dto.user import AddUserRequestDTO


class RegistrationServicer(RegistrationServiceServicer):

    def __init__(self, add_user_command: AddUserCommand):
        super().__init__()
        self.add_user_command = add_user_command

    async def Register(self, request: RegisterRequest, context: grpc.aio.ServicerContext) -> RegisterResponse:
        print(request.email)
        #user_dto = AddUserRequestDTO(email=request.email, password=request.password, name=request.name)
        return RegisterResponse()

