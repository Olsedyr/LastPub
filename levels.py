import pygame

import enemy
from game_utils import *
from player import *
from enemy import *

class AbandonedAlley:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Abandoned Alley"
        self.font = pygame.font.Font(None, 36)
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "character/0.png")
        self.enemy = Enemy(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.player)

    def update(self, dt):
            self.player.handle_events(dt)  # Call handle_events on the player instance
            self.player.update_bullets(dt, enemies)




    def draw (self):
        print("test")



    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Handle other events as needed

            dt = clock.tick(FPS) / 1000.0  # Calculate delta time (in seconds)


            # Update bullets and check for collisions with enemies
            bullets_to_remove = []
            for bullet in self.player.bullets:
                bullet.update(dt)
                if bullet.check_collision(self.enemy):
                    self.enemy.take_damage(bullet.damage)
                    bullets_to_remove.append(bullet)  # Add bullet to removal list

            # Remove bullets marked for removal from the player's bullets list
            for bullet in bullets_to_remove:
                self.player.bullets.remove(bullet)

            # Update the level, passing dt
            self.update(dt)
            self.player.update(dt)

            # Check if the enemy exists and update it
            if self.enemy:
                self.enemy.update(dt)

                # Check if the enemy is dead and remove it from the enemies list
                if not self.enemy.alive:
                    self.enemy = None  # Set self.enemy to None to prevent further updates

            self.screen.fill((255, 255, 255))
            self.player.draw(self.screen)

            # Draw the enemy and its health bar only if it exists
            if self.enemy:
                self.enemy.draw(self.screen)
                self.enemy.draw_health_bar(self.screen)

            self.player.draw_ammo(self.screen)  # Draw ammo count and magazines
            text = self.font.render(f"Welcome to {self.level_name}!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            self.screen.blit(text, text_rect)
            self.player.draw_health_bar(self.screen)
            pygame.display.flip()
class BrokenBridge:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Broken Bridge"
        self.font = pygame.font.Font(None, 36)
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.player, "enemy/png/female/Attack (1).png")

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




class CreepyCavern:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Creepy Cavern"
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

class DecayedDistrict:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Decayed District"
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


class EerieElevator:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Eerie Elevator"
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


class ForgottenFactory:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Forgotten Factory"
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



class HauntedHighway:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Haunted Highway"
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


class InfestedIsland:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Infested Island"
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


class MysteriousMansion:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Mysterious Mansion"
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


class ShadowySewers:
    def __init__(self, screen):
        self.screen = screen
        self.level_name = "Shadowy Sewers"
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
