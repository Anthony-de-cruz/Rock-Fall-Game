import os
import sys
from typing import NoReturn

import pygame


class GameObject(pygame.sprite.Sprite):

    """Base game object class"""

    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y


    def draw(self, window: pygame.display) -> None:

        """Method to specify what to draw onto the window"""


class Game():

    """Main game class"""

    def __init__(self,
            window_name: str,
            window_width: int,
            window_height: int,
            COLOUR_PALETTE: dict,
            frame_rate: int
            ):

        self.COLOUR_PALETTE = COLOUR_PALETTE
        self.window_name = window_name
        self.clock = pygame.time.Clock()

        self.window_width = window_width
        self.window_height = window_height

        self.objects: list[GameObject] = []

        self.setup_window()

    def setup_window(self) -> None:

        """Method to setup game window"""

        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height))
        pygame.display.set_caption((self.window_name))
        os.environ["SDL_VIDEO_CENTERED"] = "1"
    
    def draw(self) -> None:

        """Method to draw all objects"""

        self.window.fill(self.COLOUR_PALETTE["Black"])

        for obj in self.objects:
            obj.draw(self.window, self.COLOUR_PALETTE)
    
    def add_object(self, game_object: GameObject) -> None:

        """Method to add a game object to the game object list"""

        self.objects.append(game_object)

    
    def handle_events(self) -> None:

        """Method to handle pygame events"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def main_loop(self) -> None:

        """Method containing the main loop"""

        while True:
            
            self.clock.tick(self.frame_rate)
            self.handle_events()

            self.draw()
            pygame.display.flip()
