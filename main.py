import random
from typing import NoReturn

from game import GameObject, Game
import pygame

#todo - convert all sets of coords to rect objects
#todo - player input and collision detection
#todo - score
#todo - loss state


class Player(GameObject):

    """Player object class"""

    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)

        self.width = width
        self.height = height
    
    def draw(self, window: pygame.display, COLOUR_PALETTE) -> None:

        """Method to specify what to draw onto the window"""

        pygame.draw.rect(window, COLOUR_PALETTE["White"],
            (self.x, self.y, self.width, self.height))


class Rock(GameObject):

    """Rock object class"""
    
    def __init__(self, game: Game,
                    x: int, y: int,
                    width: int, height: int,
                    velocity: float):
        super().__init__(x, y)

        self.game = game

        self.width = width
        self.height = height
        self.velocity = velocity
        print(self.velocity)

    def draw(self, window: pygame.display, COLOUR_PALETTE) -> None:

        """Method to specify what to draw onto the window"""

        pygame.draw.rect(window, COLOUR_PALETTE["Brown"],
            (self.x, self.y, self.width, self.height))

    def update(self) -> None:

        """Method to update the rock each frame"""

        if self.y >= self.game.window_height:

            self.x = random.randint(0, self.game.window_width - self.width)
            self.y = - self.height - random.randint(0, 100)

        self.y += self.velocity
        

class RockFallGame(Game):

    """Main game class"""

    def __init__(self,
        window_name: str,
        window_width: int,
        window_height: int,
        COLOUR_PALETTE: dict,
        frame_rate: int
        ):
        super().__init__(
            window_name,
            window_width,
            window_height,
            COLOUR_PALETTE,
            frame_rate
            )
        
        self.frame_rate = frame_rate

        player = Player(window_width / 2, window_height * 0.9 - 40, 25, 25)
        self.add_object(player)

        for x in range(10):
            rock_width = random.randint(30, 60)
            rock_height = random.randint(30, 60)
            rock = Rock(self,
                random.randint(0, window_width - rock_width), 
                -rock_height - random.randint(0, 150 * x),
                rock_width, rock_height,
                round(random.uniform(3, 6), 2))
            self.add_object(rock)

    def update_objects(self) -> None:

        """Method to run the update method on all game objects"""

        for x in self.objects:

            x.update() # All objects inherit from pygame.sprite.Sprite
                       # and so should have an empty update method
    
    def main_loop(self) -> None:

        """Method containing the main loop"""

        while True:

            self.clock.tick(self.frame_rate)
            self.handle_events()

            self.update_objects()

            self.draw()
            pygame.display.flip()




def main() -> None:

    COLOURS = {
        "Black": (0, 0, 0),
        "White": (255, 255, 255),
        "Brown": (100, 50, 20)
    }

    pygame.init()

    game = RockFallGame("Rock Fall", 500, 500, COLOURS, 60)

    game.main_loop()


if __name__ == "__main__":

    main()
