import random
from typing import NoReturn

from game import GameObject, Game
import pygame


class Player(GameObject):

    """Player object class"""

    def __init__(self):
        pass


class Rocks(GameObject):

    """Rock object class"""
    
    def __init__(self):
        super().__init__(self)
        


    def draw(self, window: pygame.display, COLOUR_PALETTE) -> NoReturn:
        """Method to specify what to draw onto the window"""

        pygame.draw.rect(window, COLOUR_PALETTE["Brown"], (self.x, self.y, 50, 50))


class RockFallGame(Game):

    """Main game class"""

    def __init__(self,
        window_name: str,
        window_width: int,
        window_height: int,
        COLOUR_PALETTE: dict
        ):
        super().__init__(
            window_name,
            window_width,
            window_height,
            COLOUR_PALETTE
            )




def main() -> NoReturn:

    COLOURS = {
        "Black": (0, 0, 0),
        "White": (255, 255, 255),
        "Brown": (100, 50, 20)
    }

    pygame.init()

    game = RockFallGame("Rock Fall", 500, 500, COLOURS)
    rock = Rocks()
    rock.update()
    game.add_object(rock)
    game.main_loop()


if __name__ == "__main__":

    main()
