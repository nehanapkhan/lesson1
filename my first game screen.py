import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Game loop
running = True
while running:
    # Fill the screen with white
    screen.fill(WHITE)

    # Draw something (a blue rectangle)
    pygame.draw.rect(screen, BLUE, (100, 100, 200, 100))

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
