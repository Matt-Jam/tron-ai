""" A pygame tron game, compatible with pygbag for web deployment
"""
import asyncio
import pygame

from tron_ai.app.app import App
from tron_ai.config import config
# pygame setup
pygame.init()  # pylint: disable=no-member


screen = pygame.display.set_mode((config.screen_size, config.screen_size))
clock = pygame.time.Clock()


async def main():
    app = App(screen, clock)
    await app.app_loop()
    pygame.quit()  # pylint: disable=no-member


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
