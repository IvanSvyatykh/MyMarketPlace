from auth_service.src.domain.exceptions.user_exceptions import DomainException , EmailAlreadyExistsException
from grpc import StatusCode

async def map_domain_error_to_grpc_status(error: DomainException) -> tuple[StatusCode, str]:
    if isinstance(error, EmailAlreadyExistsException):
        return StatusCode.ALREADY_EXISTS, "Email already exists"
    else:
        return StatusCode.UNKNOWN , "Something went wrong"
