import pygame

# pygame setup
pygame.init()

from src.app.App import App
import asyncio


screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


async def main():
    app = App(screen,clock)
    await app.app_loop()
    pygame.quit()

    

if __name__ == "__main__":
    asyncio.run(main())

