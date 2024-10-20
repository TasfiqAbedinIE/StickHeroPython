import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
FPS = 60
CENTER = (WIDTH // 2, HEIGHT // 2)
STICK_LENGTH = 100

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Stick")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Main loop
running = True
angle = 0  # Starting angle

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Calculate the stick's end position
    end_x = CENTER[0] + STICK_LENGTH * math.cos(math.radians(angle))
    end_y = CENTER[1] - STICK_LENGTH * math.sin(math.radians(angle))  # Subtract to flip the y-axis

    # Draw the stick
    pygame.draw.line(screen, (0, 0, 0), CENTER, (end_x, end_y), 5)

    # Update the angle for rotation
    angle += 1  # Rotate by 1 degree per frame
    if angle >= 360:
        angle = 0  # Reset angle after a full rotation

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
