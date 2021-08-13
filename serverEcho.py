import json
import websockets
import asyncio

from game import Game

PORT = 7890
print("Server listening on Port " + str(PORT))


async def echo(websocket, path):
    games = {}
    idCount = 0
    print("A client just connected: ", websocket)

    try:
        # this will continue to get anything from server
        async for string_obj in websocket:
            # send back player position 1 or 2
            # receive player position
            # determine who it is
            # send the other player position

            pass

    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")


start_server = websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
