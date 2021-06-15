# from future import __annotations__
from typing import *

import asyncio
import sys

async def send_file(file):
    reader, writer = await asyncio.open_connection('localhost', 8888)

    for message in file:
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(100)
        text = data.decode()
        print(f'Received {text!r}')
        if 'quit' in text:
            break
    print('close connection')
    writer.close()



asyncio.run(send_file(sys.stdin))