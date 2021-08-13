import websockets
import asyncio
import json
import pygame

URL = "ws://127.0.0.1:7890"
WIDTH = 500
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))


def redrawWindow(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()


async def listen():
    run = True
    async with websockets.connect(URL) as ws:
        player1 = await ws.recv()
        clock = pygame.time.Clock()
        while run:
            # this is what allows for movements
            clock.tick(60)
            # this will send something
            await ws.send(player1)
            # this will receive player2 position
            result = await ws.recv()
            player2 = "use logic to get player 2"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            player1.move()
            redrawWindow(window, player1, player2)


asyncio.get_event_loop().run_until_complete(listen())
