import pygame
from game_utils import *
import math
import random

enemies = []

class Enemy():
    def __init__(self, x, y, player, num_frames=16, initial_scale_factor=0.30):

        self.attack_frames = []  # Zombie frames for attacking animation
        for i in range(9):  # Assuming 8 attack frames numbered from 1 to 8
            frame_path = f"enemy/export/skeleton-attack_{i}.png"
            frame_image = pygame.image.load(frame_path).convert_alpha()
            self.attack_frames.append(frame_image)







        self.idle_frames = []  # Zombie frames for idle animation
        for i in range(1, num_frames + 1):
            frame_path = f"enemy/export/skeleton-idle_{i}.png"
            frame_image = pygame.image.load(frame_path).convert_alpha()
            self.idle_frames.append(frame_image)

        self.walk_frames = []  # Zombie frames for walking animation
        for i in range(1, num_frames + 1):
            frame_path = f"enemy/export/skeleton-move_{i}.png"
            frame_image = pygame.image.load(frame_path).convert_alpha()
            self.walk_frames.append(frame_image)

        self.scale_factor = initial_scale_factor
        self.speed = 150  # Set initial speed (pixels per second)
        self.health = 100  # Health
        self.player = player
        self.animation_frames = self.idle_frames  # Start with idle frames
        self.current_frame_index = 0  # Index to keep track of the current frame
        self.animation_speed = 0.008  # Time (in seconds) between frame changes
        self.animation_timer = 0  # Timer to keep track of animation time
        self.detected_player = False  # Flag to track whether the player has been detected

        # Randomly spawn the enemy inside the screen boundaries
        self.rect = self.animation_frames[0].get_rect(center=(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))

        # Radius around the enemy within which it starts following the player
        self.follow_radius = 200

        self.attacking = False
        self.attack_damage = 5
        self.attack_range = 50
        self.attack_cooldown = 0.5  # Set the cooldown time for attack animation in seconds
        self.attack_timer = 0  # Timer to track attack animation time
        enemies.append
        self.alive = True

    def remove_from_list(self):
        enemies.remove(self)  # Remove the enemy from the central enemies list

    def check_collision(self, bullets):
        for bullet in bullets:
            if bullet.check_collision(self):
                return bullet
        return None

    def attack(self):
        # Set the flag to indicate that the enemy is attacking
        self.attacking = True

        # Play attack animation frames
        self.animation_frames = self.attack_frames

        # Reset the current frame index to 0
        self.current_frame_index = 0



    def update(self, dt):
        dt = clock.tick(FPS) / 1000  # Elapsed time in seconds
        self.dt = dt  # Store the elapsed time for frame rate independence

        # Calculate distance to the player
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # If player is detected, maintain the detected state even if player goes out of range
        if distance <= self.follow_radius:
            self.detected_player = True  # Set the flag to True once the player is detected

        # Update animation frames based on player detection and attacking state
        if self.attacking:
            self.update_attack_animation(dt)  # Call update_attack_animation here
            # If attack animation is not complete, keep current frame index
            if self.current_frame_index == len(self.attack_frames) - 1:
                self.current_frame_index = 0
            else:
                self.current_frame_index += 1
        elif distance <= self.attack_range:
            self.attack()
        elif self.detected_player:
            self.animation_frames = self.walk_frames
            self.follow_player()
            # Update the walking animation frames
            self.current_frame_index = (self.current_frame_index + 1) % len(self.walk_frames)
        else:
            self.animation_frames = self.idle_frames
            # Update the idle animation frames
            self.current_frame_index = (self.current_frame_index + 1) % len(self.idle_frames)


        if not self.alive:
            self.remove_from_list()  # Remove the enemy from the list if it's no longer alive

    # Move and clamp the enemy within the screen boundaries
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))


# In the update_animation method
    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            if self.attacking:
                self.current_frame_index = (self.current_frame_index + 1) % len(self.attack_frames)
            else:
                if self.detected_player:
                    self.current_frame_index = (self.current_frame_index + 1) % len(self.walk_frames)
                else:
                    self.current_frame_index = (self.current_frame_index + 1) % len(self.idle_frames)

            # Update animation frames based on attacking state and player detection
            if self.attacking:
                self.animation_frames = self.attack_frames
            else:
                self.animation_frames = self.walk_frames if self.detected_player else self.idle_frames

        # In the update_attack_animation method
    def update_attack_animation(self, dt):
        if self.attacking:
            self.attack_timer += dt
            if self.attack_timer >= self.attack_cooldown:
                self.attack_timer = 0
                self.attacking = False
                self.player.take_damage(self.attack_damage)

                # Reset the animation frames to idle or walking frames based on player detection
                if self.detected_player:
                    self.animation_frames = self.walk_frames
                else:
                    self.animation_frames = self.idle_frames

                # Reset the current frame index to 0
                self.current_frame_index = 0
            else:
                # Keep updating attack frames if attack animation is ongoing
                self.animation_frames = self.attack_frames
                # Ensure current_frame_index doesn't exceed the length of animation frames
                self.current_frame_index = min(self.current_frame_index, len(self.attack_frames) - 1)
        else:
            # If not attacking, set animation frames to idle or walking frames
            if self.detected_player:
                self.animation_frames = self.walk_frames
            else:
                self.animation_frames = self.idle_frames

            # Reset the current frame index to 0
            self.current_frame_index = 0






    def follow_player(self):
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery

        # Calculate the distance to the player
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Normalize the direction vector
        if distance != 0:
            dx /= distance
            dy /= distance

        # Calculate the movement based on the normalized direction vector and fixed speed
        movement_dx = self.speed * dx * self.dt
        movement_dy = self.speed * dy * self.dt

        # Move the enemy
        self.rect.move_ip(movement_dx, movement_dy)

    def draw(self, screen):

        rotated_image = pygame.transform.rotate(self.animation_frames[self.current_frame_index], -math.degrees(math.atan2(self.player.rect.centery - self.rect.centery, self.player.rect.centerx - self.rect.centerx)))
        scaled_image = pygame.transform.scale(rotated_image, (int(rotated_image.get_width() * self.scale_factor),
                                                              int(rotated_image.get_height() * self.scale_factor)))

        self.rect = scaled_image.get_rect(center=self.rect.center)
        screen.blit(scaled_image, self.rect.topleft)



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

    def take_damage(self, damage_amount):
        self.health -= damage_amount
        self.health = max(self.health, 0)  # Ensure health doesn't go below 0

        if self.health <= 0 and self.alive:
            self.alive = False  # Set the alive flag to False to prevent multiple removals
            self.remove_from_list()
            print("Regular Zombie killed")

    def remove_from_list(self):
        if self in enemies:
            enemies.remove(self)