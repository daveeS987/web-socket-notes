import json
import websockets
import asyncio

PORT = 7890
print("Server listening on Port " + str(PORT))

games = {}
idCount = 0


async def echo(websocket, path):
    print("A client just connected: ", websocket)

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
