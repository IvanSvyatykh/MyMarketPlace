import asyncio
import signal
import logging
from logging.handlers import RotatingFileHandler
import sys
import colorlog
from grpc.aio import server as grpc_server, Server
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import AUTH_SERVICE_PORT, DATABASE_URL
from auth_service.src.presentation.grpc.generated.auth_pb2_grpc import add_RegistrationServiceServicer_to_server
from auth_service.src.application.command.add_user import AddUserCommand
from auth_service.src.infrastructure.db.repositories.user_repository import UserRepository
from auth_service.src.presentation.grpc.servicer.registration_servicer import RegistrationServicer
from auth_service.src.presentation.grpc.interceptors.email_interceptor import EmailValidationInterceptor


class Application:
    def __init__(self):
        self.engine = create_async_engine(
            DATABASE_URL,
            pool_size=10,
            max_overflow=20,
            echo=True
        )

        self.async_session_maker = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def create_repository(self):
        session = self.async_session_maker()
        return UserRepository(session)

    async def close(self):
        await self.engine.dispose()


async def serve(server: Server, app: Application):
    loop = asyncio.get_running_loop()

    async def shutdown_handler():
        print("\nStarting graceful shutdown...")
        await server.stop(5)
        await app.close()
        print("Server stopped successfully")

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown_handler()))

    await server.start()
    print(f"Server started on port {AUTH_SERVICE_PORT}")

    try:
        await server.wait_for_termination()
    except asyncio.CancelledError:
        await shutdown_handler()


def setup_logging():
    # Форматтеры
    console_format = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Логгер для gRPC (возьмём root, но можно указать конкретный, например 'grpc')
    logger = logging.getLogger()  # Или 'grpc' для точечного логирования
    logger.setLevel(logging.INFO)

    # Обработчик для консоли (с цветами)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # Обработчик для файла (с ротацией)
    file_handler = RotatingFileHandler(
        'grpc_server.log',
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    # Опционально: подавление лишних логов от зависимостей
    logging.getLogger("grpc").setLevel(logging.INFO)


async def main():
    app = Application()
    setup_logging()
    user_repository = await app.create_repository()
    # interceptors=[EmailValidationInterceptor()]
    server = grpc_server()
    registration_servicer = RegistrationServicer(
        add_user_command=AddUserCommand(user_repository=user_repository)
    )
    add_RegistrationServiceServicer_to_server(registration_servicer, server)

    server.add_insecure_port(f"[::]:{AUTH_SERVICE_PORT}")
    await serve(server, app)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user")
