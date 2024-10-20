import pygame
import os
import random

# Screen width and height
WIDTH, HEIGHT = 500, 600

# Rectangle parameter
rect_height = 150
rect_y_position = HEIGHT - rect_height
circle_radius = 10
circle_y_position = rect_y_position - circle_radius

# Color library
SKY_BLUE = (169, 202, 255)
rectangle_color = (35, 35, 35)
circle_color = (255, 44, 44)
stick_color = (35, 35, 35)

# Defining screen rotation time
FPS = 60

# Loading image
WHITE_CLOUD_IMAGE = pygame.image.load(os.path.join("assets", "cloud_white.png"))
WHITE_CLOUD = pygame.transform.scale(WHITE_CLOUD_IMAGE, (100, 60))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("STICK HERO")

# cloud_position = []


def draw_rect():
    rectangle = pygame.Rect(0, rect_y_position, 100, rect_height)
    pygame.draw.rect(WIN, rectangle_color, rectangle)


def draw_circle():
    pygame.draw.circle(WIN, circle_color, (90, circle_y_position), circle_radius)


def draw_stick(initial_stick_position_x2, initial_stick_position_y2):
    pygame.draw.line(WIN, stick_color, (100, HEIGHT-rect_height), (initial_stick_position_x2, initial_stick_position_y2), 3)


def draw_window(initial_stick_position_x2, initial_stick_position_y2):
    draw_rect()
    draw_circle()
    draw_stick(initial_stick_position_x2, initial_stick_position_y2)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    initial_stick_position_x2 = 100
    initial_stick_position_y2 = HEIGHT - rect_height

    key_up = False

    # Developing clouds in random position
    WIN.fill(SKY_BLUE)
    for i in range(3):
        cloud_x_position = random.randint(100, 400)
        cloud_y_position = random.randint(100, 300)
        # cloud_position.append(cloud_x_position)
        WIN.blit(WHITE_CLOUD, (cloud_x_position, cloud_y_position))
    run = True

    while run:
        clock.tick(FPS)
        all_events = pygame.event.get()
        key_event = pygame.key.get_pressed()
        for event in all_events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                key_up = True
                print(key_up)

        if key_event[pygame.K_UP]:
            initial_stick_position_y2 -= 3
        if key_up:
            WIN.fill(SKY_BLUE)
            initial_stick_position_y2 += 10
            initial_stick_position_x2 += 10
            if initial_stick_position_y2 >= HEIGHT - rect_height:
                key_up = False

        draw_window(initial_stick_position_x2, initial_stick_position_y2)

    pygame.quit()
    # print(cloud_position)


if __name__ == "__main__":
    main()
