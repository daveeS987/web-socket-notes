import websockets
import asyncio
import json


class Connection:
    def __init__(self):
        self.url = "ws://127.0.0.1:7890"
        self.player = {}
        self.connect()

    def getPlayer(self):
        return self.player

    def connect(self):
        async def listen(self):
            async with websockets.connect(self.url) as ws:

                while True:
                    # this will receive any incoming message
                    msg = await ws.recv()
                    print(msg)
                    # this will send something
                    await ws.send("response")

        # make the connection
        asyncio.get_event_loop().run_until_complete(self.listen())

        # this is returning the Player Instance
        self.player = json.loads("this will need to be the player instance")

    def send(self, data):
        try:
            # send current player location to server
            self.client.send(json.dumps("this will need to be player instance"))
            # return the other players location to client
            return json.loads("this will need to be opponent instance")
        except socket.error as e:
            print(e)
