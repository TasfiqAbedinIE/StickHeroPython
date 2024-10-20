import pygame
from sys import exit
import random
import math

# Variables list #
width, height = 500, 800
FPS = 60
back_G_color = ["#90c2ff", "#fffeb0", "#ffe29c", "#212121"]
sec_tick = 0
game_on = False
count = False

# Dimension of rectangle
rect_height = 200
ini_rect_width = 100

ini_rect_x = 0
ini_rect_y = 600
main_x = 700
main_width = 200

rect_color = (0, 0, 0)

# Dimension of stick
x1 = ini_rect_width
y1 = height - rect_height
x2 = ini_rect_width
y2 = height - rect_height
stick_width = 3
stick_increment = 3

angle = 0
angular_velocity = math.radians(1)

# Dimension of circle
circle_x1 = ini_rect_width - 15
circle_y1 = height - rect_height - 15
circle_dia = 15

last_key = None

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("STICK HERO - IN PYTHON")
clock = pygame.time.Clock()

# RECT = pygame.Rect(0, 0, 50, 100)
# building_1 = pygame.draw.rect(screen, color="#ffffff", rect=RECT)


def random_x_build2():
    main_x = random.randrange(200, 400)
    return main_x


def random_width_build2():
    main_width = random.randrange(15, 150)
    return main_width


def stick_rotation(angle=0):
    dx = x2 - x1
    dy = y2 - y1

    rotated_dx = dx * math.cos(angle) - dy * math.sin(angle)
    rotated_dy = dx * math.sin(angle) + dy * math.cos(angle)
    rotated_end_x = x1 + rotated_dx
    rotated_end_y = y1 + rotated_dy

    stick = pygame.draw.line(screen, (0, 0, 0), (x1, y1), (rotated_end_x, rotated_end_y))
    pygame.display.flip()

    # angle += angular_velocity
    pygame.time.delay(10)


def draw_window(main_x, main_width, circle_x1):
    clock.tick(FPS)
    # Initial Rectangle
    # RECT = pygame.Rect(ini_rect_x, ini_rect_y, ini_rect_width, rect_height)
    building_1 = pygame.draw.rect(screen, rect_color, [ini_rect_x, ini_rect_y, ini_rect_width, rect_height], 0)

    # Second Rectangle
    # RECT = pygame.Rect(main_x, ini_rect_y, main_width, rect_height)
    building_2 = pygame.draw.rect(screen, rect_color, [main_x, ini_rect_y, main_width, rect_height], 0)

    # Building Stick
    stick = pygame.draw.line(screen, (0, 0, 0), [x1, y1], [x2, y2], stick_width)

    # Build the ball
    ball = pygame.draw.circle(screen, (0, 255, 0), [circle_x1, circle_y1], circle_dia, 0)

    pygame.display.update()


while True:
    for event in pygame.event.get():
        # Event to QUIT the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Event to catch the KEY down press
        if event.type == pygame.KEYDOWN:
            last_key = event.key
            # Event to catch if 'S' is pressed
            if event.key == pygame.K_s:
                main_x = random_x_build2()
                main_width = random_width_build2()
                game_on = True
        # Event to check if the KEY is UP
        if event.type == pygame.KEYUP:
            last_key = None
            if event.key == pygame.K_SPACE:
                count = True
            # print(ini_rect_width - main_width)

    if game_on:
        if last_key == pygame.K_SPACE:
            # print("space pressed")
            y2 -= stick_increment

        if last_key == None and count == True:
            lower_distance_between_rect = main_x - ini_rect_width
            upper_distance_between_rect = main_x - ini_rect_width + main_width
            stick_length = y1 - y2



            dx = x2 - x1
            dy = y2 - y1

            rotated_dx = dx * math.cos(angle) - dy * math.sin(angle)
            rotated_dy = dx * math.sin(angle) + dy * math.cos(angle)
            rotated_end_x = x1 + rotated_dx
            rotated_end_y = y1 + rotated_dy
            print(rotated_end_x, rotated_end_y)
            if rotated_end_y < y1:
                # print("YEs")
                pygame.draw.line(screen, (0, 0, 0), (x1, y1), (rotated_end_x, rotated_end_y), stick_width)
                pygame.display.flip()
                angle += angular_velocity
                pygame.time.delay(10)
            if rotated_end_y >= y1:
                pygame.draw.line(screen, (0, 0, 0), (x1, y1), (rotated_end_x, rotated_end_y), stick_width)
                pygame.display.flip()
                if lower_distance_between_rect < stick_length < upper_distance_between_rect and circle_x1 < main_x + main_width - 15:
                    circle_x1 += 3
                if stick_length < lower_distance_between_rect or stick_length > upper_distance_between_rect:
                    circle_x1 += 3



            # print(lower_distance_between_rect)
            # print(stick_length)
            # print(upper_distance_between_rect)
            # print(circle_x1)

            # if lower_distance_between_rect < stick_length < upper_distance_between_rect and circle_x1 < main_x + main_width - 15:
            #     circle_x1 += 3
            # if stick_length < lower_distance_between_rect or stick_length > upper_distance_between_rect:
            #     circle_x1 += 3





    # Changing background color based on time
    sec_tick += 1 / 10
    # print(sec_tick)
    if sec_tick < 30:
        screen.fill(back_G_color[0])
    elif 30 < sec_tick < 60:
        screen.fill(back_G_color[1])
    elif 60 < sec_tick < 90:
        screen.fill(back_G_color[2])
    elif 90 < sec_tick < 120:
        screen.fill(back_G_color[3])
    if sec_tick > 120:
        sec_tick = 0

    draw_window(main_x, main_width, circle_x1)