import sys
import pygame
from settings import Settings

def run_game():
    #Initialize game and create a screen object

    pygame.init()   # Initialize the background settings for pygame
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, 
                                        my_settings.screen_height))   # Create a display window 1200 px wide 800 px high

    # A surface in Pygame is where a game element is displayed

    pygame.display.set_caption("Alien Invasion")

    #Start with the main loop for the game

    while True:

        #watch for keyboard and mouse events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redram the screen during each pass through the loop
        screen.fill(my_settings.bg_color)

        #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
