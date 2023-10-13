import pygame
from game_utils import *
class AbandonedAlley:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Abandoned Alley"
        self.font = pygame.font.Font(None, 36)
        self.player_position = [screen.get_width() // 2, screen.get_height() // 2]
        self.player_speed = 5

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_position[0] -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_position[0] += self.player_speed
        if keys[pygame.K_UP]:
            self.player_position[1] -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.player_position[1] += self.player_speed

    def update(self):
        self.handle_events()  # Handle player input
        # Additional logic for collisions, enemy movement, scoring, etc. goes here

    def run(self):
        running = True
        while running:
            self.update()  # Update game logic
            self.screen.fill((255, 255, 255))  # Set the background color to white for the Abandoned Alley level
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))  # Draw the player as a blue rectangle
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)

            pygame.display.flip()