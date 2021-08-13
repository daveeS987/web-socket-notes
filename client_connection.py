import websockets
import asyncio
import json


class Connection:
    def __init__(self):
        self.url = "ws://127.0.0.1:7890"
        self.player = "initialize this with player instance"
        self.connection()

    def getPlayer(self):
        return self.player

    def connection(self):
        async def listen(self):
            async with websockets.connect(self.url) as ws:
                # initialize self.player with instance
                self.player = json.loads("this will need to be the player instance")
                while True:
                    # this will receive any incoming message
                    msg = await ws.recv()
                    print(msg)
                    # this will send something
                    await ws.send("response")

        # make the connection
        asyncio.get_event_loop().run_until_complete(self.listen())

    def send(self, data):

        # send current player location to server
        self.client.send(json.dumps("this will need to be player instance"))
        # return the other players location to client
        return json.loads("this will need to be opponent instance")
