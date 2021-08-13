# Importing the relevant libraries
import websockets
import asyncio
import json

# The main function that will handle connection and communication
# with the server
async def listen():
    url = "ws://127.0.0.1:7890"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send a greeting message
        # await ws.send("Hello Server!")

        obj1 = {"hello": "davee", "hi": 123, 1: False, "bye": [1, "2", 3]}
        converted = json.dumps(obj1)
        print("converted: ", converted)
        # Stay alive forever, listening to incoming msgs

        while True:
            response = input("> Person1: ")
            if response == "q":
                break
            await ws.send(converted)
            msg = await ws.recv()
            print(msg)


# Start the connection
asyncio.get_event_loop().run_until_complete(listen())
