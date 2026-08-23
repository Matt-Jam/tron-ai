import pytest

from tron_ai.app.app import App

@pytest.fixture
def base_app(pygame_init,pygame_surface,pygame_clock):
    return App(pygame_surface,pygame_clock)

def test_app_init(base_app):
    assert True


def test_initial_state(base_app):
    assert base_app.current_state == base_app.playing

def test_state_game_ended(base_app):
    base_app.game_ended()
    assert base_app.current_state == base_app.game_over

def test_start_play_again(base_app):
    base_app.game_ended()
    base_app.play_again()
    assert base_app.current_state == base_app.playing
