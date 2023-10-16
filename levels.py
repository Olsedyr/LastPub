import pygame
from game_utils import *
from player import *

class AbandonedAlley:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Abandoned Alley"
        self.font = pygame.font.Font(None, 36)
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "character/0.png")

    def update(self, dt):
        self.player.handle_events(dt)  # Call handle_events on the player instance
        self.player.update_bullets(dt)


    def draw (self):
        self.player.draw_bullets(self.screen)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Handle other events as needed
            dt = clock.tick(FPS) / 1000.0  # Calculate delta time (in seconds)
            self.update(dt)  # Update the level, passing dt
            self.screen.fill((255, 255, 255))
            self.player.draw(self.screen)
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()





class BrokenBridge:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Broken Bridge"
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
        self.handle_events()
        # Additional logic for collisions, enemy movement, scoring, etc. goes here

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()



class CreepyCavern:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Creepy Cavern"
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
        self.handle_events()
        # Additional logic for collisions, enemy movement, scoring, etc. goes here

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()

class DecayedDistrict:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Decayed District"
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
        self.handle_events()

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()


class EerieElevator:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Eerie Elevator"
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
        self.handle_events()

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()


class ForgottenFactory:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Forgotten Factory"
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
        self.handle_events()

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()


class HauntedHighway:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Haunted Highway"
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
        self.handle_events()

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()


class InfestedIsland:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Infested Island"
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
        self.handle_events()

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()

class MysteriousMansion:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Mysterious Mansion"
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
        self.handle_events()

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()


class ShadowySewers:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Shadowy Sewers"
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
        self.handle_events()

    def run(self):
        running = True
        while running:
            self.update()
            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), (*self.player_position, 50, 50))
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            pygame.display.flip()