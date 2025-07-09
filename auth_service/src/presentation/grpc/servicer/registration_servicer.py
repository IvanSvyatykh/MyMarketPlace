import grpc
from pydantic import ValidationError

from auth_service.src.presentation.grpc.generated.auth_pb2 import RegisterRequest, RegisterResponse
from auth_service.src.presentation.grpc.generated.auth_pb2_grpc import RegistrationServiceServicer
from auth_service.src.application.command.add_user import AddUserCommand
from auth_service.src.application.dto.user import AddUserRequestDTO
from auth_service.src.domain.exceptions.user_exceptions import EmailAlreadyExistsException
from auth_service.src.presentation.grpc.error_mapping import map_domain_error_to_grpc_status


class RegistrationServicer(RegistrationServiceServicer):

    def __init__(self, add_user_command: AddUserCommand):
        super().__init__()
        self.add_user_command = add_user_command

    async def Register(self, request: RegisterRequest, context: grpc.aio.ServicerContext) -> RegisterResponse:
        try:
            user_dto = AddUserRequestDTO(email=request.email, password=request.password, name=request.name)
        except ValidationError as e:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e.errors()[0]["msg"]))
        try:
            await self.add_user_command.execute(user_dto)
        except EmailAlreadyExistsException as e:
            status_code, details = await map_domain_error_to_grpc_status(e)
            await context.abort(status_code, details)
        return RegisterResponse()
