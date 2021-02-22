
'''
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE ="DISCONNECT"
SERVER = "192.168.0.108"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length =str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello World!")
'''

import asyncio
import pathlib
import ssl
import websockets


async def hello():
    uri = "wss://192.168.0.108:5050"
    async with websockets.connect(
        uri
    ) as websocket:
        name = input("What's your name? ")
        message = input("Message: ")
        await websocket.send({"message": message, "author": name})
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())