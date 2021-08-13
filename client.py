# Importing the relevant libraries
import websockets
import asyncio
import json
import pygame

width = 500
height = 500
window = pygame.display.set_mode((width, height))


def redrawWindow(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()


async def listen():
    url = "ws://127.0.0.1:7890"
    async with websockets.connect(url) as ws:

        while True:

            # this will send something
            await ws.send("location")
            # this will receive any incoming message
            msg = await ws.recv()
            print(msg)


def main():
    run = True
    clock = pygame.time.Clock()
    player1 = n.getPlayer()

    # Start the connection
    asyncio.get_event_loop().run_until_complete(listen())

    while run:
        clock.tick(60)
        # Send player1 to server to get back player2 object
        player2 = n.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.move()
        redrawWindow(window, player1, player2)


main()
