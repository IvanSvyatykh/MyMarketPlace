import grpc
import re
from grpc import aio
from typing import Any, Callable, Awaitable


class EmailValidationInterceptor(aio.ServerInterceptor):
    EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    async def intercept_service(self, continuation, handler_call_details):
        print(getattr(handler_call_details, "_request", None))
        print(handler_call_details.__dir__())
