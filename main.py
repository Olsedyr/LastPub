import pygame
from menu import MainMenu, ResolutionMenu, LevelMenu
from levels import AbandonedAlley  # Import the AbandonedAlley class from levels.py

pygame.init()

# Set up display and clock
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Your Game Title")
clock = pygame.time.Clock()

FPS = 60
# Game states
MAIN_MENU = 0
RESOLUTION_MENU = 1
LEVEL_MENU = 2
ABANDONED_ALLEY = 3  # New game state constant for Abandoned Alley level

current_state = RESOLUTION_MENU
resolution_menu = ResolutionMenu(win)
main_menu = MainMenu(win)
level_menu = LevelMenu(win)
abandoned_alley = AbandonedAlley(win)  # Initialize the Abandoned Alley game state with the screen surface (win)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))  # Clear the screen at the beginning of each frame

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
            current_state = ABANDONED_ALLEY  # Transition to the AbandonedAlley game state
        else:
            current_state = MAIN_MENU
    elif current_state == ABANDONED_ALLEY:  # Handle the Abandoned Alley game state
        abandoned_alley.run()
        current_state = MAIN_MENU  # Return to the main menu after the Abandoned Alley level is completed

    pygame.display.flip()  # Update the screen at the end of each frame
    clock.tick(FPS)  # Limit frames per second

pygame.quit()