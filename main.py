# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # initialize the pygame library
    pygame.init()
    # create a window with the specified width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a game loop that runs until the user quits
    running = True
    while running:
        # check for events in the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill the screen with black color
        screen.fill((0, 0, 0))
        # update the display
        pygame.display.flip()
    print("Starting Asteroids!")
    # print screen width and height form Constants.py
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
