import pytest
import pygame

@pytest.fixture
def pygame_init():
    pygame.init()
    yield
    pygame.quit()

@pytest.fixture
def pygame_surface():
    return pygame.Surface((600, 600))

@pytest.fixture
def pygame_clock():
    return pygame.time.Clock()