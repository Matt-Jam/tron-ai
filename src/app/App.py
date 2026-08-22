import pygame
from statemachine import StateChart, State

import asyncio
from ..game.Game import Game
from ..navscreens.GameOver import GameOver



class App(StateChart):
    #states
    playing = State(initial=True)
    game_over = State()

    #Transitions
    game_ended = playing.to(game_over)
    play_again = game_over.to(playing)


    def __init__(self,screen,clock):
        super().__init__()
        self.screen = screen
        self.clock = clock 
        self.running = True
        self.game_screen = Game(screen)
        self.game_over_screen = GameOver(screen)


    def on_game_ended(self):
        self.game_over_screen.state = self.game_screen.game_state.winner

    def on_play_again(self):
        self.game_screen = Game(self.screen)

    async def app_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()

            match self.current_state:
                case self.playing:
                    if not(self.game_screen.step(keys)):
                        self.game_ended()
                case self.game_over:
                    if not(self.game_over_screen.step(keys)):
                        self.play_again()
                
                    

            pygame.display.flip()

            self.clock.tick(120)
            await asyncio.sleep(0)
