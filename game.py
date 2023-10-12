import pygame

class Game:
    def __init__(self, screen, level, screen_width, screen_height):
        self.screen = screen
        self.level = level
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clock = pygame.time.Clock()


    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # Limit frames per second

# End of game.py
