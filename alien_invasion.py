
import pygame
from settings import Settings
from ship import Ship 
import game_functions as gf
def run_game():
    #Initialize game and create a screen object

    pygame.init()   # Initialize the background settings for pygame
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, 
                                        my_settings.screen_height))   # Create a display window 1200 px wide 800 px high

    # A surface in Pygame is where a game element is displayed
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    #Start with the main loop for the game

    while True:
        gf.check_events(ship)

        gf.update_screen(my_settings, screen, ship)

run_game()
