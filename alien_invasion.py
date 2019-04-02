import pygame
from settings import Settings
from ship import Ship 
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    #Initialize game and create a screen object

    pygame.init()   # Initialize the background settings for pygame
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width, 
                                        my_settings.screen_height))   # Create a display window 1200 px wide 800 px high

    # A surface in Pygame is where a game element is displayed
    pygame.display.set_caption("Alien Invasion")

    #Create an instance to store game statistics
    stats = GameStats(my_settings)

    # Make a ship
    ship = Ship(my_settings, screen)

    #Make a group of aliens
    aliens = Group()

    #create the fleet of aliens
    gf.create_fleet(my_settings, screen, aliens, ship)

    # Make a group to store the bullets in
    bullets = Group()

    #Start with the main loop for the game

    while True:
        gf.check_events(my_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, screen, ship, my_settings)
            gf.update_aliens(my_settings, aliens, ship, stats, screen, bullets)
        
        gf.update_screen(my_settings, screen, ship, aliens, bullets)

run_game()
