import asyncio
import signal
from grpc.aio import server as grpc_server, Server
from config import AUTH_SERVICE_PORT
from logging import getLogger


async def serve(server: Server):
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(
            sig,
            lambda: asyncio.create_task(graceful_shutdown())
        )

    await server.start()
    print(f"Server started on port {AUTH_SERVICE_PORT}")

    try:
        await server.wait_for_termination()
    except asyncio.CancelledError:
        await graceful_shutdown()


async def graceful_shutdown(self):
    print("\nShutting down server gracefully...")
    await self.server.stop(5)  # 5 секунд на graceful shutdown
    print("Server stopped successfully")


async def main():

    server = grpc_server()
    await serve(server)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user")
