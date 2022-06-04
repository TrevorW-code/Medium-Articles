import asyncio
import logging
import websockets
from websockets import WebSocketServerProtocol

logging.basicConfig(level=logging.INFO)

class Server:
    clients = set()

    async def register(self, web_socket: WebSocketServerProtocol) -> None:
        self.clients.add(web_socket)
        logging.info(f'{web_socket.remote_address') connects.')

    async def unregister(self, web_socket: WebSocketServerProtocol) -> None:
        self.clients.remove(web_socket)
        logging.info(f'{web_socket.remote_address} disconnects.')

    async def send_to_clients(self, message: str) -> None:
        if self.clients:
            await asyncio.wait([client.send(message) for client in self.clients])

    async def web_socket_handler(self, web_socket: WebSocketProtocol, uri: str) -> None:
        await self.register(web_socket)
        try:
            await self.distribute(web_socket)
        finally:
            await self.unregister(web_socket)

    async def distribute(self, web_socket: WebSocketServerProtocol) -> None:
        async for message in ws:
            await self.send_to_clients(message)

server = Server()
start_server = websocket.serve(server.ws_handler, 'localhost',4000)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()