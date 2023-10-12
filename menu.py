# menu.py
import pygame
from game_utils import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

pygame.font.init()  # Initialize font module (needed only once)

# Load the custom font
font_size = 48  # Set the desired font size
custom_font = pygame.font.Font("fonts/Creepster-Regular.ttf", font_size)

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
        self.aspect_ratio = 16 / 9
        self.generate_resolutions()
        self.selected_resolution_index = 0
        self.arrow_left_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 - 25, 50, 50)
        self.arrow_right_rect = pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 - 25, 50, 50)
        self.background = pygame.image.load("backgrounds/background.png").convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = blur_surface(self.background, 10)
        self.hovered_font_size = 52  # Font size when text is hovered
        self.default_font_size = 36
        self.font = pygame.font.Font("fonts/Creepster-Regular.ttf", self.default_font_size)  # Load custom font
        self.hovered_color = (255, 0, 0)  # Color when text is hovered
        self.hovered_apply = False  # Variable to track hover state for "Apply" text

    def generate_resolutions(self):
        self.resolutions = []
        for width in range(1280, 1921, 160):  # Starting from 1280 up to 1920 with steps of 160
            height = int(width / self.aspect_ratio)
            self.resolutions.append((width, height))
        self.resolutions.append("Fullscreen")

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def draw_options(self):
        self.draw_background()  # Draw the background first

        # Draw title text
        title_text_shadow = self.font.render("Resolutions", True, (50, 50, 50))  # Darker color for shadow
        title_rect_shadow = title_text_shadow.get_rect(center=(SCREEN_WIDTH // 2 + 2, SCREEN_HEIGHT // 4 + 2))  # Slightly offset
        self.screen.blit(title_text_shadow, title_rect_shadow)

        title_text = self.font.render("Resolutions", True, WHITE)
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

        # Check for hover animation
        mouse_pos = pygame.mouse.get_pos()
        self.hovered_apply = apply_rect.collidepoint(mouse_pos)

        # Change font size and color on hover
        if self.hovered_apply:
            apply_text = pygame.font.Font("fonts/Creepster-Regular.ttf", self.hovered_font_size).render("Apply", True, self.hovered_color)
        else:
            apply_text = self.font.render("Apply", True, WHITE)

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
        self.default_font_size = 48
        self.hovered_font_size = 52  # Font size when text is hovered
        self.font = pygame.font.Font("fonts/Creepster-Regular.ttf", self.default_font_size)  # Load custom font
        self.start_text = self.font.render("Start", True, WHITE)
        self.quit_text = self.font.render("Quit", True, WHITE)
        self.hovered_color = (255, 0, 0)  # Color when text is hovered

    def run(self):
        while True:
            background = pygame.image.load("backgrounds/background.png").convert()
            background = pygame.transform.scale(background, self.selected_resolution)
            background = blur_surface(background, 10)
            self.screen.blit(background, (0, 0))

            # Larger text with hover animation
            start_rect = self.start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            quit_rect = self.quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

            # Check for hover animation
            mouse_pos = pygame.mouse.get_pos()
            start_hovered = start_rect.collidepoint(mouse_pos)
            quit_hovered = quit_rect.collidepoint(mouse_pos)

            # Change font size and color on hover
            start_text = self.font.render("Start", True, self.hovered_color if start_hovered else WHITE)
            start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            if start_hovered:
                start_text = pygame.font.Font("fonts/Creepster-Regular.ttf", self.hovered_font_size).render("Start", True, self.hovered_color)

            quit_text = self.font.render("Quit", True, self.hovered_color if quit_hovered else WHITE)
            quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            if quit_hovered:
                quit_text = pygame.font.Font("fonts/Creepster-Regular.ttf", self.hovered_font_size).render("Quit", True, self.hovered_color)

            # Draw text on screen
            self.screen.blit(start_text, start_rect)
            self.screen.blit(quit_text, quit_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if start_hovered:
                        return "start"
                    elif quit_hovered:
                        pygame.quit()
                        quit()


class LevelMenu:
    def __init__(self, screen):
        self.screen = screen
        self.image_size = 300
        self.generate_levels()
        self.selected_level_index = 0
        self.arrow_left_rect = pygame.Rect(50, SCREEN_HEIGHT // 2 - 25, 50, 50)
        self.arrow_right_rect = pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT // 2 - 25, 50, 50)
        self.load_images()
        self.background = self.generate_blurred_background()
        self.hovered_font_size = 52  # Font size when text is hovered
        self.default_font_size = 48
        self.font = pygame.font.Font("fonts/Creepster-Regular.ttf", self.default_font_size)  # Load custom font
        self.hovered_color = (255, 0, 0)  # Color when text is hovered
        self.hovered_play = False  # Variable to track hover state for "Play" text

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

    def generate_blurred_background(self):
        background = pygame.image.load("backgrounds/background.png").convert()
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        blurred_background = blur_surface(background, 20)  # Apply blur effect with radius 20
        return blurred_background

    def draw_options(self):
        self.screen.blit(self.background, (0, 0))  # Draw the extra blurred background

        # Draw selected level image and text with a slight spacing
        image_rect = self.images[self.selected_level_index].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - self.image_size // 4))
        self.screen.blit(self.images[self.selected_level_index], image_rect)

        # Draw outline for the picture
        picture_rect = pygame.Rect(image_rect.left - 2, image_rect.top - 2, image_rect.width + 4, image_rect.height + 4)
        pygame.draw.rect(self.screen, BLACK, picture_rect, 2)  # Draw a black outline with thickness 2 around the picture

        level_text = self.font.render(self.levels[self.selected_level_index], True, WHITE)
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + self.image_size // 4 + 30))  # Lowered on the y-axis
        self.screen.blit(level_text, level_rect)

        # Draw arrows with shadows
        arrow_font = pygame.font.Font(None, 48)
        arrow_left_shadow = arrow_font.render("<", True, (50, 50, 50))
        arrow_right_shadow = arrow_font.render(">", True, (50, 50, 50))

        arrow_left_rect_shadow = arrow_left_shadow.get_rect(topleft=(self.arrow_left_rect.left + 2, self.arrow_left_rect.top + 2))
        arrow_right_rect_shadow = arrow_right_shadow.get_rect(topleft=(self.arrow_right_rect.left + 2, self.arrow_right_rect.top + 2))

        self.screen.blit(arrow_left_shadow, arrow_left_rect_shadow.topleft)  # Draw the left arrow shadow
        self.screen.blit(arrow_right_shadow, arrow_right_rect_shadow.topleft)  # Draw the right arrow shadow

        arrow_left = arrow_font.render("<", True, WHITE)
        arrow_right = arrow_font.render(">", True, WHITE)
        self.screen.blit(arrow_left, self.arrow_left_rect.topleft)  # Draw the main left arrow
        self.screen.blit(arrow_right, self.arrow_right_rect.topleft)  # Draw the main right arrow

        # Draw "Play" text with shadow
        play_text_shadow = self.font.render("Play", True, (50, 50, 50))
        play_rect_shadow = play_text_shadow.get_rect(center=(SCREEN_WIDTH // 2 + 2, SCREEN_HEIGHT - 50 + 2))  # Slightly offset
        self.screen.blit(play_text_shadow, play_rect_shadow)

        play_text = self.font.render("Play", True, WHITE)
        play_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

        # Check for hover animation
        mouse_pos = pygame.mouse.get_pos()
        self.hovered_play = play_rect.collidepoint(mouse_pos)

        # Change font size and color on hover
        if self.hovered_play:
            play_text = pygame.font.Font("fonts/Creepster-Regular.ttf", self.hovered_font_size).render("Play", True, self.hovered_color)
        else:
            play_text = self.font.render("Play", True, WHITE)

        self.screen.blit(play_text, play_rect)

        return play_rect  # Return the rectangle of the "Play" button

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