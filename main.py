import pygame
from menu import MainMenu, ResolutionMenu, LevelMenu
from levels import *  # Import additional level classes
from game_utils import FPS

pygame.init()

pygame.font.init()

# Set up display and clock
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zombie: The Last Pubcrawl")
clock = pygame.time.Clock()

# Game states
MAIN_MENU = 0
RESOLUTION_MENU = 1
LEVEL_MENU = 2


ABANDONED_ALLEY = 3
BROKEN_BRIDGE = 4
CREEPY_CAVERN = 5
DECAYED_DISTRICT = 6
EERIE_ELEVATOR = 7
FORGOTTEN_FACTORY = 8
HAUNTED_HIGHWAY = 9
INFESTED_ISLAND = 10
MYSTERIOUS_MANSION = 11
SHADOWY_SEWERS = 12


current_state = RESOLUTION_MENU
resolution_menu = ResolutionMenu(win)
main_menu = MainMenu(win)
level_menu = LevelMenu(win)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))

    if current_state == MAIN_MENU:
        selected_option = main_menu.run()
        if selected_option == "start":
            current_state = LEVEL_MENU
        elif selected_option == "quit":
            running = False
    elif current_state == RESOLUTION_MENU:
        selected_resolution, fullscreen = resolution_menu.run()
        if fullscreen:
            SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
            win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        else:
            SCREEN_WIDTH, SCREEN_HEIGHT = selected_resolution
            win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        current_state = MAIN_MENU
    elif current_state == LEVEL_MENU:
        selected_level = level_menu.run()
        if selected_level == "Abandoned Alley":
            current_state = ABANDONED_ALLEY
        elif selected_level == "Broken Bridge":
            current_state = BROKEN_BRIDGE
        elif selected_level == "Creepy Cavern":
            current_state = CREEPY_CAVERN
        elif selected_level == "Decayed District":
            current_state = DECAYED_DISTRICT
        elif selected_level == "Eerie Elevator":
            current_state = EERIE_ELEVATOR
        elif selected_level == "Forgotten Factory":
            current_state = FORGOTTEN_FACTORY
        elif selected_level == "Haunted Highway":
            current_state = HAUNTED_HIGHWAY
        elif selected_level == "Infested Island":
            current_state = INFESTED_ISLAND
        elif selected_level == "Mysterious Mansion":
            current_state = MYSTERIOUS_MANSION
        elif selected_level == "Shadowy Sewers":
            current_state = SHADOWY_SEWERS

    elif current_state == ABANDONED_ALLEY:
        abandoned_alley_instance = AbandonedAlley(win)  # Create an instance of AbandonedAlley class
        abandoned_alley_instance.run()
        current_state = MAIN_MENU

    elif current_state == BROKEN_BRIDGE:
        broken_bridge_instance = BrokenBridge(win)
        broken_bridge_instance.run()
        current_state = MAIN_MENU

    elif current_state == CREEPY_CAVERN:
        creepy_cavern_instance = CreepyCavern(win)
        creepy_cavern_instance.run()
        current_state = MAIN_MENU

    elif current_state == DECAYED_DISTRICT:
        decayed_district_instance = DecayedDistrict(win)
        decayed_district_instance.run()
        current_state = MAIN_MENU

    elif current_state == EERIE_ELEVATOR:
        eerie_elevator_instance = EerieElevator(win)
        eerie_elevator_instance.run()
        current_state = MAIN_MENU

    elif current_state == FORGOTTEN_FACTORY:
        forgotten_factory_instance = ForgottenFactory(win)
        forgotten_factory_instance.run()
        current_state = MAIN_MENU

    elif current_state == HAUNTED_HIGHWAY:
        haunted_highway_instance = HAUNTED_HIGHWAY(win)
        haunted_highway_instance.run()
        current_state = MAIN_MENU

    elif current_state == INFESTED_ISLAND:
        infested_island_instance = InfestedIsland(win)
        infested_island_instance.run()
        current_state = MAIN_MENU

    elif current_state == MYSTERIOUS_MANSION:
        mysterious_island_instance = MysteriousMansion(win)
        mysterious_island_instance.run()
        current_state = MAIN_MENU

    elif current_state == SHADOWY_SEWERS:
        shadowy_sewers_instance = ShadowySewers(win)
        shadowy_sewers_instance.run()
        current_state = MAIN_MENU


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
