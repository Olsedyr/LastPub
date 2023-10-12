import pygame
from menu import MainMenu, ResolutionMenu, LevelMenu

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

current_state = RESOLUTION_MENU
resolution_menu = ResolutionMenu(win)
main_menu = MainMenu(win)
level_menu = LevelMenu(win)

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
        print(f"Selected Level: {selected_level}")
        current_state = MAIN_MENU

    pygame.display.flip()  # Update the screen at the end of each frame
    clock.tick(FPS)  # Limit frames per second

pygame.quit()
