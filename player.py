import pygame
from game_utils import *
import math

class Player:
    def __init__(self, x, y, image_path="", initial_scale_factor=0.35):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.scale_factor = initial_scale_factor
        self.rect = self.original_image.get_rect(center=(x, y))
        self.speed = 150  # Set initial speed (pixels per second)
        self.bullets = []
        self.shoot_offset = 0
        self.health = 100 # Health
        self.shoot_cooldown = 0.15
        self.time_since_last_shot = 0
        self.ammo = 25  # Initial ammo count
        self.magazines = 3  # Initial number of magazines
        self.reload_time = 1.0  # Time in seconds for reload
        self.reloading = False  # Flag to indicate reloading state
        self.reload_timer = 0  # Timer to track reloading time
        self.ammo_icon = pygame.image.load("character/ammo.png").convert_alpha()
        self.magazine_icon = pygame.image.load("character/magazine.png").convert_alpha()
        self.icon_scale_factor = 0.5  # Adjust the scale factor as needed
        self.icon_spacing = 10  # Spacing between ammo and magazine icons
    def handle_events(self, dt):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_a]:
            dx -= self.speed * dt
        if keys[pygame.K_d]:
            dx += self.speed * dt
        if keys[pygame.K_w]:
            dy -= self.speed * dt
        if keys[pygame.K_s]:
            dy += self.speed * dt

        self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate angle between player and mouse position
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)

        # Convert angle from radians to degrees
        angle_degrees = math.degrees(angle)

        # Rotate the player image to face the mouse cursor
        rotated_image = pygame.transform.rotate(self.original_image, -angle_degrees)

        # Scale the rotated image based on the scale factor
        scaled_image = pygame.transform.scale(rotated_image, (int(rotated_image.get_width() * self.scale_factor),
                                                              int(rotated_image.get_height() * self.scale_factor)))

        self.rect = scaled_image.get_rect(center=self.rect.center)
        self.image = scaled_image

        # Handle mouse events
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] and self.time_since_last_shot >= self.shoot_cooldown:  # Left mouse button and cooldown check
            self.shoot()
            self.time_since_last_shot = 0  # Reset the cooldown timer after shooting
        else:
            self.time_since_last_shot += dt  # Increment the time since the last shot

            # Automatically reload if ammo reaches 0 and there are still magazines available
        if self.ammo <= 0 and self.magazines > 0 and not self.reloading:
            self.reloading = True  # Start the reloading process
    def update(self, dt):
        self.dt = dt  # Store the elapsed time for frame rate independence
        self.handle_events(dt)

        # Update reload timer if reloading
        if self.reloading:
            self.reload_timer += dt
            if self.reload_timer >= self.reload_time:
                self.reload_timer = 0
                self.reloading = False
                self.ammo = 25  # Reload the magazine with 25 bullets
                if self.magazines > 0:
                    self.magazines -= 1  # Reduce the number of magazines by 1 after reloading

        # Automatically reload if ammo reaches 0 and there are still magazines available
        if self.ammo <= 0 and self.magazines > 0 and not self.reloading:
            self.reloading = True  # Start the reloading process
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        for bullet in self.bullets:
            bullet.draw(screen)

    def shoot(self):
        if self.ammo > 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calculate angle between player and mouse position
            angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)

            # Set the spawn offset distance to move the bullet away from the player's center
            spawn_offset_distance = -20  # Increase this value to move the bullet further away
            spawn_offset_x = spawn_offset_distance * math.cos(angle)
            spawn_offset_y = spawn_offset_distance * math.sin(angle)

            # Apply an additional offset perpendicular to the player's facing angle
            perpendicular_offset = -20  # Adjust this value to move the bullet up or down
            spawn_offset_x += perpendicular_offset * math.sin(angle)
            spawn_offset_y -= perpendicular_offset * math.cos(angle)

            # Adjust spawn offset based on player's width to spawn bullet at the player's side
            spawn_offset_x += self.rect.width / 2 * math.cos(angle)
            spawn_offset_y += self.rect.width / 2 * math.sin(angle)

            # Apply the offset to the bullet's initial position (add to player's position)
            bullet = Bullet(self.rect.centerx + spawn_offset_x, self.rect.centery + spawn_offset_y, angle, self.scale_factor)
            self.bullets.append(bullet)
            self.ammo -= 1

    def update_bullets(self, dt, enemies):
        bullets_to_remove = []
        for bullet in self.bullets:
            bullet.update(dt)  # Update the bullet position without passing enemies list here
            for enemy in enemies:
                if bullet.check_collision(enemy):
                    bullets_to_remove.append(bullet)
                    enemy.take_damage(bullet.damage)
                    break  # Exit the loop after hitting one enemy
            # Remove the bullet if it goes out of screen boundaries
            if not pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT).contains(bullet.rect):
                bullets_to_remove.append(bullet)

        # Remove bullets that hit enemies or went out of screen boundaries
        self.bullets = [bullet for bullet in self.bullets if bullet not in bullets_to_remove]
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        for bullet in self.bullets:
            bullet.draw(screen)


    def draw_health_bar(self, screen):
        health_bar_width = 100  # Width of the health bar
        health_bar_height = 10  # Height of the health bar
        lost_health_width = health_bar_width * (1 - self.health / 100)  # Calculate width of lost health (in red)

        # Calculate health bar position (above the player)
        health_bar_x = self.rect.centerx - health_bar_width // 2
        health_bar_y = self.rect.bottom + 10

        # Draw green health bar background
        pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))

        # Draw red lost health overlay
        pygame.draw.rect(screen, (255, 0, 0), (health_bar_x, health_bar_y, lost_health_width, health_bar_height))

    def draw_ammo(self, screen):
        # Calculate scaled size of icons based on the current screen resolution
        icon_size = (int(SCREEN_WIDTH * 0.03), int(SCREEN_HEIGHT * 0.03))  # Adjust the scale factor as needed

        # Scale the icons to the calculated size
        scaled_ammo_icon = pygame.transform.scale(self.ammo_icon, icon_size)
        scaled_magazine_icon = pygame.transform.scale(self.magazine_icon, icon_size)

        # Draw scaled ammo icon
        screen.blit(scaled_ammo_icon, (10, 10))

        # Draw ammo text next to ammo icon
        font = pygame.font.Font(None, 36)
        ammo_text = font.render(str(self.ammo), True, (0, 0, 0))
        screen.blit(ammo_text, (10 + scaled_ammo_icon.get_width() + self.icon_spacing, 10))

        # Draw scaled magazine icon
        screen.blit(scaled_magazine_icon,
                    (10 + scaled_ammo_icon.get_width() + self.icon_spacing + ammo_text.get_width() + self.icon_spacing, 10))

        # Draw magazine text next to magazine icon
        magazine_text = font.render(str(self.magazines), True, (0, 0, 0))
        screen.blit(magazine_text,
                    (10 + scaled_ammo_icon.get_width() + self.icon_spacing * 2 + ammo_text.get_width() +
                     scaled_magazine_icon.get_width() + self.icon_spacing, 10))

    def take_damage(self, damage_amount):
        self.health -= damage_amount

        # Check if the player's health has reached zero
        if self.health <= 0:
            # Handle player death logic (e.g., end the game, reset player position, etc.)
            print("Dead Player")

class Bullet:
    def __init__(self, x, y, angle, scale_factor=1.0):
        self.original_image = pygame.Surface((8, 8))
        self.original_image.fill((0, 0, 0))
        self.scale_factor = scale_factor
        self.image = pygame.transform.scale(self.original_image, (int(32 * self.scale_factor), int(32 * self.scale_factor)))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 1000
        self.velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * self.speed
        self.damage = 25

    def check_collision(self, enemy):
        if enemy is not None and hasattr(enemy, 'rect'):
            return self.rect.colliderect(enemy.rect)
        return False

    def update(self, dt):
        pixels_per_frame = self.velocity * dt  # Calculate movement based on frame rate
        self.rect.move_ip(pixels_per_frame)

        # Remove the bullet if it goes out of screen boundaries
        if not pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT).contains(self.rect):
            return True

        return False

    def draw(self, screen):
        scaled_bullet = pygame.transform.scale(self.image, (int(self.rect.width * self.scale_factor), int(self.rect.height * self.scale_factor)))
        screen.blit(scaled_bullet, self.rect.topleft)



