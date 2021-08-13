# Communicates with a client and server
# Importing the relevant libraries
import json
import websockets
import asyncio

PORT = 7890
print("Server listening on Port " + str(PORT))


async def echo(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            print("message: ", message)
            converted = json.loads(message)
            print("converted: ", converted)
            await websocket.send("Pong: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")


start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
