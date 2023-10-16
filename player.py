import pygame
from game_utils import *
import math

class Player:
    def __init__(self, x, y, image_path="character/0.png", initial_scale_factor=0.35):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.scale_factor = initial_scale_factor
        self.rect = self.original_image.get_rect(center=(x, y))
        self.speed = 200  # Set initial speed (pixels per second)
        self.bullets = []
        self.shoot_offset = 0

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
        if mouse_buttons[0]:  # Left mouse button
            self.shoot()


    def update(self, dt):
        self.dt = dt  # Store the elapsed time for frame rate independence
        self.handle_events(dt)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate angle between player and mouse position
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)

        # Set the spawn offset distance to move the bullet away from the player's center
        spawn_offset_distance = -20  # Increase this value to move the bullet further away
        spawn_offset_x = spawn_offset_distance * math.cos(angle)
        spawn_offset_y = spawn_offset_distance * math.sin(angle)

        # Apply an additional offset perpendicular to the player's facing angle
        perpendicular_offset = -18  # Adjust this value to move the bullet up or down
        spawn_offset_x += perpendicular_offset * math.sin(angle)
        spawn_offset_y -= perpendicular_offset * math.cos(angle)

        # Adjust spawn offset based on player's width to spawn bullet at the player's side
        spawn_offset_x += self.rect.width / 2 * math.cos(angle)
        spawn_offset_y += self.rect.width / 2 * math.sin(angle)

        # Apply the offset to the bullet's initial position (add to player's position)
        bullet = Bullet(self.rect.centerx + spawn_offset_x, self.rect.centery + spawn_offset_y, angle, self.scale_factor)
        self.bullets.append(bullet)

    def update_bullets(self, dt):
        for bullet in self.bullets:
            bullet.update(dt)
            # Remove bullets that are out of the screen
            if not pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT).colliderect(bullet.rect):
                self.bullets.remove(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        for bullet in self.bullets:
            bullet.draw(screen)


class Bullet:
    def __init__(self, x, y, angle, scale_factor=1.0):
        self.original_image = pygame.Surface((10, 10))  # Create a small black square bullet
        self.original_image.fill((0, 0, 0))
        self.scale_factor = scale_factor
        self.image = pygame.transform.scale(self.original_image, (int(10 * self.scale_factor), int(10 * self.scale_factor)))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 500  # Set bullet speed (pixels per second)
        self.velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * self.speed

    def update(self, dt):
        pixels_per_frame = self.velocity * dt  # Calculate movement based on frame rate
        self.rect.move_ip(pixels_per_frame)

    def is_out_of_screen(self, screen_width, screen_height):
        return not pygame.Rect(0, 0, screen_width, screen_height).colliderect(self.rect)

    def draw(self, screen):
        scaled_bullet = pygame.transform.scale(self.image, (int(self.rect.width * self.scale_factor), int(self.rect.height * self.scale_factor)))
        screen.blit(scaled_bullet, self.rect.topleft)