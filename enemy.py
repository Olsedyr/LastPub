import pygame
import random
import math
from game_utils import *
from player import*

class Enemy:
    def __init__(self, x, y, width, height, walk_left_images, walk_right_images, idle_images, dead_images, attack_images):
        # Initialize your attributes here
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.damage = 5
        self.health = 100
        self.is_dead = False
        self.walk_left_images = walk_left_images
        self.walk_right_images = walk_right_images
        self.idle_images = idle_images
        self.dead_images = dead_images
        self.attack_images = attack_images
        self.current_images = self.idle_images
        self.animation_index = 0
        self.animation_speed = 0.1  # Adjust this value to control animation speed

def update_animation(self, dt):
    if len(self.current_images) > 0:
        self.animation_index += self.animation_speed * dt
        self.animation_index %= len(self.current_images)
        print(f"Animation Index: {self.animation_index}")  # Add this line for debugging
        self.current_image = self.current_images[int(self.animation_index)]
    else:
        print("Warning: Current images list is empty!")
    def update_movement(self, dt, player_x, player_y):
        # Move towards the player if within a certain radius
        distance_to_player = math.sqrt((player_x - self.x) ** 2 + (player_y - self.y) ** 2)

        # Define a speed factor to control the movement speed
        speed = 10
        #print(f"Distance to player: {distance_to_player}")  # Debugging line, remove it later
        if distance_to_player > 50:  # Replace 50 with your desired radius
            # Calculate normalized direction vector towards the player
            dx = player_x - self.x
            dy = player_y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            dx /= distance
            dy /= distance

            # Update enemy position based on the direction vector and speed
            self.x += dx * speed * dt
            self.y += dy * speed * dt


    def attack(self, player):
        # Attack logic: reduce player's health when in range
        distance_to_player = math.sqrt((player.rect.x - self.x) ** 2 + (player.rect.y - self.y) ** 2)
        if distance_to_player < 20:  # Replace 20 with your desired attack range
            player.health -= self.damage
class RegularEnemy:
    @staticmethod
    def load_images():
        walkRight = [pygame.image.load('enemy/png/female/Walk (1).png'),
                     pygame.image.load('enemy/png/female/Walk (2).png'),
                     pygame.image.load('enemy/png/female/Walk (3).png'),
                     pygame.image.load('enemy/png/female/Walk (4).png'),
                     pygame.image.load('enemy/png/female/Walk (5).png'),
                     pygame.image.load('enemy/png/female/Walk (6).png'),
                     pygame.image.load('enemy/png/female/Walk (7).png'),
                     pygame.image.load('enemy/png/female/Walk (8).png'),
                     pygame.image.load('enemy/png/female/Walk (9).png'),
                     pygame.image.load('enemy/png/female/Walk (10).png')]

        walkLeft = [pygame.transform.flip(image, True, False) for image in walkRight]

        Idle = [pygame.image.load('enemy/png/female/Idle (1).png'),
                pygame.image.load('enemy/png/female/Idle (2).png'),
                pygame.image.load('enemy/png/female/Idle (3).png'),
                pygame.image.load('enemy/png/female/Idle (4).png'),
                pygame.image.load('enemy/png/female/Idle (5).png'),
                pygame.image.load('enemy/png/female/Idle (6).png'),
                pygame.image.load('enemy/png/female/Idle (7).png'),
                pygame.image.load('enemy/png/female/Idle (8).png'),
                pygame.image.load('enemy/png/female/Idle (9).png'),
                pygame.image.load('enemy/png/female/Idle (10).png'),
                pygame.image.load('enemy/png/female/Idle (11).png'),
                pygame.image.load('enemy/png/female/Idle (12).png'),
                pygame.image.load('enemy/png/female/Idle (13).png'),
                pygame.image.load('enemy/png/female/Idle (14).png'),
                pygame.image.load('enemy/png/female/Idle (15).png')]

        Dead = [pygame.image.load('enemy/png/female/Dead (1).png'),
                pygame.image.load('enemy/png/female/Dead (2).png'),
                pygame.image.load('enemy/png/female/Dead (3).png'),
                pygame.image.load('enemy/png/female/Dead (4).png'),
                pygame.image.load('enemy/png/female/Dead (5).png'),
                pygame.image.load('enemy/png/female/Dead (6).png'),
                pygame.image.load('enemy/png/female/Dead (7).png'),
                pygame.image.load('enemy/png/female/Dead (8).png'),
                pygame.image.load('enemy/png/female/Dead (9).png'),
                pygame.image.load('enemy/png/female/Dead (10).png')]

        Attack = [pygame.image.load('enemy/png/female/Attack (1).png'),
                  pygame.image.load('enemy/png/female/Attack (2).png'),
                  pygame.image.load('enemy/png/female/Attack (3).png'),
                  pygame.image.load('enemy/png/female/Attack (4).png'),
                  pygame.image.load('enemy/png/female/Attack (5).png'),
                  pygame.image.load('enemy/png/female/Attack (6).png'),
                  pygame.image.load('enemy/png/female/Attack (7).png')]
        return walkRight, walkLeft, Idle, Dead, Attack