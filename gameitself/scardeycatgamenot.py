import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Point and Click Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets (images for objects)
background = pygame.image.load('background.jpg')  # Replace with your own background
object_image = pygame.image.load('object.png')    # Replace with an object image

# Object position
object_rect = object_image.get_rect(topleft=(300, 200))  # Adjust the position

# Fonts
font = pygame.font.Font(None, 36)

# Game state variables
clicked = False
message = ""

# Main game loop
def main():
    global clicked, message

    while True:
        screen.fill(WHITE)  # Clear screen
        screen.blit(background, (0, 0))  # Draw the background
        screen.blit(object_image, object_rect)  # Draw the object

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if object_rect.collidepoint(event.pos):
                    clicked = True
                    message = "You clicked the object!"
                    click_sound = pygame.mixer.Sound('click.wav')
                else:
                    clicked = False
                    message = ""

        # Display message if object is clicked
        if clicked:
            display_message(screen, message, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

        pygame.display.flip()  # Update the display

# Function to display messages
def display_message(surface, text, x, y):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

if __name__ == '__main__':
    main()
