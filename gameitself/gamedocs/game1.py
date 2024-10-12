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
object_image = pygame.image.load('keyboardobject.jpg')    # Replace with an object image yes

# Get the current size of the image
original_width, original_height = object_image.get_size()

# Set the scaling factor (e.g., 0.5 to reduce size by 50%)
scale_factor = 0.2

# Calculate the new size of the image
new_width = int(original_width * scale_factor)
new_height = int(original_height * scale_factor)

# Scale the image
scaled_image = pygame.transform.scale(object_image, (new_width, new_height))

# Object position
object_rect = object_image.get_rect(topleft=(100, 75))  # Adjust the position

# Fonts
font = pygame.font.Font(None, 36)

# Game state variables
clicked = False
message = ""

# Main game loop
def main():
    global clicked, message

    while True:
        screen.fill(WHITE)  
        screen.blit(background, (0, 0))  # Draw the background
        screen.blit(scaled_image, object_rect)  # Draw # Event handling
        for event in pygame.event.get():
            if event.type == pygame:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if object_rect.collidepoint(event.pos):
                    clicked = True
                    message = "You clicked the object!"
                    #click_sound = pygame.mixer.Sound('click.wav')
                else:
                    clicked = False
                    

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