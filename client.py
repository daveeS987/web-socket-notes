# Importing the relevant libraries
import websockets
import asyncio
import json

# The main function that will handle connection and communication
# with the server
async def listen():
    url = "ws://127.0.0.1:7890"
    async with websockets.connect(url) as ws:

        while True:

            # this will send something
            await ws.send("location")
            # this will receive any incoming message
            msg = await ws.recv()
            print(msg)


# Start the connection
asyncio.get_event_loop().run_until_complete(listen())
