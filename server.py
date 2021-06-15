# from future import __annotations__
from typing import *

import asyncio
import sys
print(sys.executable)
async def handle_connection(reader, writer):
    addr = writer.get_extra_info('peername')
    # while message := await reader.read(100):
    while True:
        text = message.decode()
        print(f'received {text} from {addr}')
        print(f'sending back {text}')
        writer.write(message)
        await writer.drain()
        if 'quit' in text:
            break
    print('close connection')
    writer.close()


async def main():
    server = await asyncio.start_server(handle_connection, 'localhost', 8888)
    addr = server.sockets[0].getsockname() if server.sockets else 'unknown'
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()


asyncio.run(main)