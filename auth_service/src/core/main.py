import asyncio

from grpc.aio import server as grpc_server

from config import AUTH_SERVICE_PORT


async def serve():
    server = grpc_server()
    server.add_insecure_port(f"[::]:{AUTH_SERVICE_PORT}")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
