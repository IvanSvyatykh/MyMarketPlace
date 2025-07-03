from typing import ClassVar as _ClassVar, Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "expires_in")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    expires_in: int
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ("email", "name", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    password: str
    def __init__(self, email: _Optional[str] = ..., name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UpdatePasswordRequest(_message.Message):
    __slots__ = ("email", "name", "current_password", "new_password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    current_password: str
    new_password: str
    def __init__(self, email: _Optional[str] = ..., name: _Optional[str] = ..., current_password: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("email", "name", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    password: str
    def __init__(self, email: _Optional[str] = ..., name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ("access_token",)
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "expires_in")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    expires_in: int
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...
