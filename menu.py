# menu.py
import pygame
from game_utils import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK


def blur_surface(surface, radius):
    temp_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    temp_surface.blit(surface, (0, 0))
    for _ in range(radius):
        temp_surface = pygame.transform.smoothscale(temp_surface, (temp_surface.get_width() // 2, temp_surface.get_height() // 2))
        temp_surface = pygame.transform.smoothscale(temp_surface, (temp_surface.get_width() * 2, temp_surface.get_height() * 2))
    return temp_surface

class ResolutionMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 48)
        self.aspect_ratio = 16 / 9
        self.generate_resolutions()
        self.selected_resolution_index = 0
        self.arrow_left_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 - 25, 50, 50)
        self.arrow_right_rect = pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 - 25, 50, 50)
        self.background = pygame.image.load("backgrounds/background.png").convert()  # Load background image
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = blur_surface(self.background, 10)  # Apply blur effect with radius 10 10




    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def generate_resolutions(self):
        self.resolutions = []
        for width in range(1280, 1921, 160):  # Starting from 1280 up to 1920 with steps of 160
            height = int(width / self.aspect_ratio)
            self.resolutions.append((width, height))
        self.resolutions.append("Fullscreen")





    def draw_options(self):
        self.draw_background()  # Draw the background first

        # Draw title text
        title_text_shadow = self.title_font.render("Resolutions", True, (50, 50, 50))  # Darker color for shadow
        title_rect_shadow = title_text_shadow.get_rect(center=(SCREEN_WIDTH // 2 + 2, SCREEN_HEIGHT // 4 + 2))  # Slightly offset
        self.screen.blit(title_text_shadow, title_rect_shadow)

        title_text = self.title_font.render("Resolutions", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        self.screen.blit(title_text, title_rect)


        # Draw selected resolution
        current_resolution = self.resolutions[self.selected_resolution_index]
        resolution_text_shadow = self.font.render(f"{current_resolution[0]}x{current_resolution[1]}", True, (50, 50, 50))
        resolution_rect_shadow = resolution_text_shadow.get_rect(center=(SCREEN_WIDTH // 2 + 2, SCREEN_HEIGHT // 2 + 2))
        self.screen.blit(resolution_text_shadow, resolution_rect_shadow)

        resolution_text = self.font.render(f"{current_resolution[0]}x{current_resolution[1]}", True, WHITE)
        resolution_rect = resolution_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(resolution_text, resolution_rect)

        # Draw arrows with shadow effect
        arrow_font = pygame.font.Font(None, 48)
        arrow_left_shadow = arrow_font.render("<", True, (50, 50, 50))
        arrow_right_shadow = arrow_font.render(">", True, (50, 50, 50))

        arrow_left_rect_shadow = arrow_left_shadow.get_rect(topleft=self.arrow_left_rect.topleft)
        arrow_right_rect_shadow = arrow_right_shadow.get_rect(topleft=self.arrow_right_rect.topleft)

        self.screen.blit(arrow_left_shadow, arrow_left_rect_shadow.topleft)  # Draw the left arrow shadow
        self.screen.blit(arrow_right_shadow, arrow_right_rect_shadow.topleft)  # Draw the right arrow shadow

        arrow_left = arrow_font.render("<", True, WHITE)
        arrow_right = arrow_font.render(">", True, WHITE)
        self.screen.blit(arrow_left, self.arrow_left_rect.topleft)  # Draw the main left arrow
        self.screen.blit(arrow_right, self.arrow_right_rect.topleft)  # Draw the main right arrow

        # Draw "Apply" text with shadow effect
        apply_text_shadow = self.font.render("Apply", True, (50, 50, 50))
        apply_rect_shadow = apply_text_shadow.get_rect(center=(SCREEN_WIDTH // 2 + 2, SCREEN_HEIGHT - 50))
        self.screen.blit(apply_text_shadow, apply_rect_shadow)

        apply_text = self.font.render("Apply", True, WHITE)
        apply_rect = apply_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.screen.blit(apply_text, apply_rect)

        return arrow_left, arrow_right, apply_rect  # Return the arrow surfaces and apply rectangle
    def run(self):
        while True:
            fullscreen = False  # Initialize fullscreen flag
            self.screen.fill(BLACK)
            arrow_left, arrow_right, apply_rect = self.draw_options()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.arrow_left_rect.collidepoint(mouse_pos):
                        self.selected_resolution_index = max(0, self.selected_resolution_index - 1)
                    elif self.arrow_right_rect.collidepoint(mouse_pos):
                        self.selected_resolution_index = min(len(self.resolutions) - 1, self.selected_resolution_index + 1)
                    elif apply_rect.collidepoint(mouse_pos):
                        selected_option = self.resolutions[self.selected_resolution_index]
                        if selected_option == "Fullscreen":
                            fullscreen = True
                            selected_option = (pygame.display.Info().current_w, pygame.display.Info().current_h)
                        return selected_option, fullscreen

class MainMenu:
    def __init__(self, screen, selected_resolution=None):
        self.screen = screen
        self.selected_resolution = selected_resolution or (1280, 720)
        self.font = pygame.font.Font(None, 48)  # Larger font size

    def run(self):
        while True:
            background = pygame.image.load("backgrounds/background.png").convert()
            background = pygame.transform.scale(background, self.selected_resolution)
            background = blur_surface(background, 10)  # Apply blur effect with radius 10
            self.screen.blit(background, (0, 0))

            # Larger text with hover animation
            start_text = self.font.render("Start", True, WHITE)
            start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

            quit_text = self.font.render("Quit", True, WHITE)
            quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

            # Check for hover animation
            mouse_pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(mouse_pos):
                start_text = self.font.render("Start", True, (255, 0, 0))  # Change color on hover
            if quit_rect.collidepoint(mouse_pos):
                quit_text = self.font.render("Quit", True, (255, 0, 0))  # Change color on hover

            # Draw text on screen
            self.screen.blit(start_text, start_rect)
            self.screen.blit(quit_text, quit_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if start_rect.collidepoint(mouse_pos):
                        return "start"
                    elif quit_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        quit()


class LevelMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.image_size = 300
        self.generate_levels()
        self.selected_level_index = 0
        self.arrow_left_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 - 25, 50, 50)
        self.arrow_right_rect = pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 - 25, 50, 50)
        self.load_images()

    def generate_levels(self):
        self.levels = ["Abandoned Alley", "Broken Bridge", "Creepy Cavern", "Decayed District",
                       "Eerie Elevator", "Forgotten Factory", "Haunted Highway", "Infested Island",
                       "Mysterious Mansion", "Shadowy Sewers"]

    def load_images(self):
        self.images = []
        for i in range(1, 11):
            image_path = f"level_images/level{i}.png"
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (self.image_size, self.image_size))
            self.images.append(image)


    def draw_options(self):
        # Draw selected level image and text with a slight spacing
        image_rect = self.images[self.selected_level_index].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - self.image_size // 4))
        self.screen.blit(self.images[self.selected_level_index], image_rect)

        level_text = self.font.render(self.levels[self.selected_level_index], True, WHITE)
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + self.image_size // 4 + 10))
        self.screen.blit(level_text, level_rect)

        # Draw "Play level" button
        play_level_text = self.font.render("Play Level", True, WHITE)
        play_level_rect = play_level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.screen.blit(play_level_text, play_level_rect)

        # Draw arrows (unchanged)
        arrow_font = pygame.font.Font(None, 48)
        arrow_left = arrow_font.render("<", True, WHITE)
        arrow_right = arrow_font.render(">", True, WHITE)
        self.screen.blit(arrow_left, self.arrow_left_rect)
        self.screen.blit(arrow_right, self.arrow_right_rect)

        return play_level_rect  # Return the rectangle of the "Play level" button

    def run(self):
        while True:
            self.screen.fill(BLACK)
            play_level_rect = self.draw_options()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.arrow_left_rect.collidepoint(mouse_pos):
                        self.selected_level_index = max(0, self.selected_level_index - 1)
                    elif self.arrow_right_rect.collidepoint(mouse_pos):
                        self.selected_level_index = min(len(self.levels) - 1, self.selected_level_index + 1)
                    elif play_level_rect.collidepoint(mouse_pos):
                        selected_level = self.levels[self.selected_level_index]
                        return selected_level