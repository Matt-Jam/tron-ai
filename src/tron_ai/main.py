""" A pygame tron game, compatible with pygbag for web deployment
"""
from tron_ai.app.app import App
import asyncio

import pygame

# pygame setup
pygame.init()  # pylint: disable=no-member


screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


async def main():
    app = App(screen, clock)
    await app.app_loop()
    pygame.quit()  # pylint: disable=no-member


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
