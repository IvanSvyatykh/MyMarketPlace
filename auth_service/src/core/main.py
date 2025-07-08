import asyncio
import signal
from grpc.aio import server as grpc_server, Server
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import AUTH_SERVICE_PORT, DATABASE_URL
from auth_service.src.presentation.grpc.generated.auth_pb2_grpc import add_RegistrationServiceServicer_to_server
from auth_service.src.application.command.add_user import AddUserCommand
from auth_service.src.infrastructure.db.repositories.user_repository import UserRepository
from auth_service.src.presentation.grpc.servicer.registration_servicer import RegistrationServicer


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


async def main():
    app = Application()

    user_repository = await app.create_repository()

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
