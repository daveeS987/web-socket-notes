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

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1

    try:
        # this will continue to get anything from server
        async for string_obj in websocket:

            # convert back to object
            obj = json.loads(string_obj)
            # do something with object
            #
            #
            #
            #

            # turn back into string and send back
            str_obj = json.dumps({})
            await websocket.send(str_obj)

    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")


start_server = websockets.serve(echo, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
