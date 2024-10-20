import pygame
from sys import exit
import random
import math

# Variables list #

width, height = 500, 800            # Screen height and width
FPS = 150                           # Screen Rotation rate
back_G_color = ["#90c2ff", "#fffeb0", "#ffe29c", "#212121"]         # background color
sec_tick = 0    #################
game_on = True     # Some Condition
count = False       # Some Condition
player_turn = 0     # Some Condition
SCORE = 0           # Tracking Scores
game_over = False   # Game Over condition
rect_color = (0, 0, 0)      # Color of rectangle
ball_color = (220, 47, 2)   # Color of Ball

initial_rect_x = 0
initial_rect_height = 200
initial_rect_y = height - initial_rect_height
initial_rect_width = 100


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("STICK HERO - IN PYTHON")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

def draw_window():
    clock.tick(FPS)

# -------------------- Class to build rectangle --------------------- #
class Rectangle:
    def __init__(self, fix_height, width, rect_X, rect_Y):
        self.height = fix_height
        self.width = width
        self.rect_X = rect_X
        self.rect_Y = rect_Y

    def build_rectangle(self):
        pygame.draw.rect(screen, rect_color, [self.rect_X, self.rect_Y, self.width, self.height], 0)


# -------------------- Class to build BALL ----------------------- #
class Ball:
    def __init__(self, circle_x1, circle_y1, circle_dia, ball_color):
        self.circle_x1 = circle_x1
        self.circle_y1 = circle_y1
        self.circle_dia = circle_dia
        self.ball_color = ball_color

    def build_ball(self):
        ball = pygame.draw.circle(screen, ball_color, [self.circle_x1, self.circle_y1], self.circle_dia, 0)



rectangle_1 = Rectangle(initial_rect_height, initial_rect_width, initial_rect_x, initial_rect_y)

def draw_window():
    clock.tick(FPS)
    rectangle_1.build_rectangle()

while True:

    for event in pygame.event.get():
        # Event to QUIT the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_on:
        screen.fill(back_G_color[0])
        draw_window()
        pygame.display.update()