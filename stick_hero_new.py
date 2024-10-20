import pygame
from sys import exit
import random
import math

# Variables list #

width, height = 500, 800
FPS = 150
back_G_color = ["#90c2ff", "#fffeb0", "#ffe29c", "#212121"]
sec_tick = 0
game_on = False
count = False
player_turn = 0
SCORE = 0
game_over = False

# Dimension of rectangle
rect_height = 200
rect_width = 100

rect_x = 0
rect_y = 600
random_x = 700
random_width = 200

rect_color = (0, 0, 0)

# Dimension of stick
stick_x1 = rect_width
stick_y1 = height - rect_height
stick_x2 = rect_width
stick_y2 = height - rect_height
stick_width = 4
stick_increment = 3

angle = 0
angular_velocity = math.radians(1)
stick_turn = False

stick_color = (0, 0, 0)

# Dimension of ball
circle_x1 = rect_width - 15
circle_y1 = height - rect_height - 15
circle_dia = 15

ball_color = (220, 47, 2)
ball_forward = False

rewind = False

player_1 = True
player_2 = False

# ----------------------------------- #

# Fundamental Part

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("STICK HERO - IN PYTHON")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)


# ----------------------------------- #

# Class to build random numbers
class RandomNumber:
    def __init__(self):
        pass

    def random_x_build(self):
        random_x = random.randrange(200, 400)
        return random_x

    def random_width_build(self):
        random_width = random.randrange(15, 150)
        return random_width


# ----------------------------------- #

# Class to build rectangle
class Rectangle:
    def __init__(self, fix_height, width, rect_X, rect_Y):
        self.height = fix_height
        self.width = width
        self.rect_X = rect_X
        self.rect_Y = rect_Y

    def build_rectangle(self):
        pygame.draw.rect(screen, rect_color, [self.rect_X, self.rect_Y, self.width, self.height], 0)


# ------------------------------------------ #

# Class to build Ball
class Ball:
    def __init__(self, circle_x1, circle_y1, circle_dia, ball_color):
        self.circle_x1 = circle_x1
        self.circle_y1 = circle_y1
        self.circle_dia = circle_dia
        self.ball_color = ball_color

    def build_ball(self):
        ball = pygame.draw.circle(screen, ball_color, [self.circle_x1, self.circle_y1], self.circle_dia, 0)


# ------------------------------------------ #

# Class to build stick
class Stick:
    def __init__(self, stick_color, stick_x1, stick_y1, stick_x2, stick_y2, stick_width, angle, stick_turn):
        self.stick_color = stick_color
        self.stick_x1 = stick_x1
        self.stick_y1 = stick_y1
        self.stick_x2 = stick_x2
        self.stick_y2 = stick_y2
        self.stick_width = stick_width
        self.angle = angle
        self.stick_turn = stick_turn

    def build_stick(self):
        stick = pygame.draw.line(screen, self.stick_color, (self.stick_x1, self.stick_y1),
                                 (self.stick_x2, self.stick_y2), self.stick_width)

    def turning_stick(self):

        dx = self.stick_x2 - self.stick_x1
        dy = self.stick_y2 - self.stick_y1

        rotated_dx = dx * math.cos(self.angle) - dy * math.sin(self.angle)
        rotated_dy = dx * math.sin(self.angle) + dy * math.cos(self.angle)

        rotated_end_x = rotated_dx + self.stick_x1
        rotated_end_y = rotated_dy + self.stick_y1

        return dx, dy, rotated_dx, rotated_dy, rotated_end_x, rotated_end_y


# ------------------------------------------ #

# Function to display score
def display_score():
    score_surf = test_font.render(f"SCORE: {SCORE}", False, (0, 0, 0))
    score_rect = score_surf.get_rect(topleft=(20, 20))
    screen.blit(score_surf, score_rect)

# ----------------------------------------- #

# Function to display Intro Insructions
def intro_instruction():
    game_name_surf = test_font.render(f"STICK HERO", False, (0, 0, 0))
    game_name_rect = game_name_surf.get_rect(center=(width/2, (height/2)-30))
    screen.blit(game_name_surf, game_name_rect)

    intro_surf_1 = test_font.render(f"PRESS 'S' TO START", False, (0, 0, 0))
    intro_rect_1 = intro_surf_1.get_rect(center=(width / 2, height / 2))
    screen.blit(intro_surf_1, intro_rect_1)

    intro_surf_2 = test_font.render(f"PRESS 'SPACE' TO STICK UP", False, (0, 0, 0))
    intro_rect_2 = intro_surf_2.get_rect(center=(width / 2, (height / 2)+30))
    screen.blit(intro_surf_2, intro_rect_2)

# ----------------------------------------- #

# Function to show gameover screen
def game_over_screen():
    game_over_surf_1 = test_font.render(f"GAME OVER", False, (0, 0, 0))
    game_over_rect_1 = game_over_surf_1.get_rect(center=(width / 2, (height / 2) - 50))
    screen.blit(game_over_surf_1, game_over_rect_1)

    game_over_surf_2 = test_font.render(f"YOUR SCORE : {SCORE}", False, (0, 0, 0))
    game_over_rect_2 = game_over_surf_2.get_rect(center=(width / 2, (height / 2)))
    screen.blit(game_over_surf_2, game_over_rect_2)

# Creating instances from classes

rectangle_1 = Rectangle(rect_height, rect_width, rect_x, rect_y)
rectangle_2 = Rectangle(rect_height, random_width, random_x, rect_y)
gen_random_number = RandomNumber()
ball = Ball(circle_x1, circle_y1, circle_dia, ball_color)
stick = Stick(stick_color, stick_x1, stick_y1, stick_x2, stick_y2, stick_width, angle, stick_turn)


# ----------------------------- #
def draw_window():
    clock.tick(FPS)

    rectangle_1.build_rectangle()
    rectangle_2.build_rectangle()
    ball.build_ball()
    stick.build_stick()
    display_score()

    if not game_on:
        intro_instruction()

    if game_over:
        game_over_screen()

    # pygame.display.update()


while True:
    for event in pygame.event.get():
        # Event to QUIT the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            last_key = event.key
            # Event to catch if 'S' is pressed
            if event.key == pygame.K_s and game_on == False:
                random_x = gen_random_number.random_x_build()
                random_width = gen_random_number.random_width_build()
                rectangle_2.rect_X, rectangle_2.width = random_x, random_width
                print(f"Random X: {random_x}, Random width: {random_width}")
                game_on = True

        if event.type == pygame.KEYUP:
            last_key = None
            # stick_turn = True
            if event.key == pygame.K_SPACE:
                stick_turn = True


    if game_on:
        # print(last_key)
        if last_key == pygame.K_SPACE:
            stick.stick_y2 -= 1
        if last_key == None and stick_turn == True:
            dx, dy, rotated_dx, rotated_dy, rotated_end_x, rotated_end_y = stick.turning_stick()

            if rotated_end_y < stick_y2:
                # Need to factorize properly
                stick.stick_y2 += 1
                stick.stick_x2 += 1
                # angle += 1
                # print(stick.stick_x2, stick.stick_y2)

            if rotated_end_y >= stick.stick_y1:
                ball_forward = True
                # print(f"Rotated end X: {rotated_end_x}")

        if ball_forward and rewind == False:
            # ------------ Logical problem exist ------------ #
                if rectangle_2.rect_X > 0:
                    if rectangle_2.rect_X <= rotated_end_x <= rectangle_2.rect_X + rectangle_2.width:
                        if ball.circle_x1 <= rectangle_2.rect_X + rectangle_2.width - 15:
                            ball.circle_x1 += 1
                            if ball.circle_x1 >= rectangle_2.rect_X + rectangle_2.width - 15:
                                ball_forward = False
                                rewind = True
                                SCORE += 1
                    else:
                        if rotated_end_y >= stick_y1 and ball.circle_x1 < rotated_end_x + 5:
                            ball.circle_x1 += 1
                        if ball.circle_x1 >= rotated_end_x + 5 and ball.circle_y1 < height + 10:
                            ball.circle_y1 += 1
                        if ball.circle_y1 == height + 10:
                            game_over = True
                            # game_on = False

                if rectangle_1.rect_X > 0:
                    if rectangle_1.rect_X <= rotated_end_x <= rectangle_1.rect_X + rectangle_1.width:
                        if ball.circle_x1 <= rectangle_1.rect_X + rectangle_1.width - 15:
                            ball.circle_x1 += 1
                            if ball.circle_x1 >= rectangle_1.rect_X + rectangle_1.width - 15:
                                ball_forward = False
                                rewind = True
                                SCORE += 1
                    else:
                        if rotated_end_y >= stick_y1 and ball.circle_x1 < rotated_end_x + 5:
                            ball.circle_x1 += 1
                        if ball.circle_x1 >= rotated_end_x + 5 and ball.circle_y1 < height + 10:
                            ball.circle_y1 += 1
                        if ball.circle_y1 == height + 10:
                            game_over = True


        if rewind:
            if rectangle_2.rect_X > 0 and player_1 == True:
                rectangle_1.rect_X -= 1
                ball.circle_x1 -= 1
                # stick.stick_x1 = rectangle_2.width
                # stick.stick_x2 = rectangle_2.width
                stick.stick_y2 = stick_y1
                rectangle_2.rect_X -= 1

                stick.stick_x1 = rectangle_1.width
                stick.stick_y1 = 600
                stick.stick_x2 = rectangle_1.width
                stick.stick_y2 = 600

            if rectangle_2.rect_X == 0 and player_1 == True:
                if rectangle_1.rect_X < 0:
                    rectangle_1.rect_X = width + 5
                    random_x = gen_random_number.random_x_build()
                    random_width = gen_random_number.random_width_build()
                    rectangle_1.width = random_width
                    print(f"Random X: {random_x}, Random width: {random_width}")

                    # stick.stick_x1 = -5
                    # stick.stick_y1 = 600
                    # stick.stick_x2 = -5
                    # stick.stick_y2 = 600

                if rectangle_1.rect_X > random_x:
                    rectangle_1.rect_X -= 1

                if rectangle_1.rect_X == random_x:
                    stick.stick_x1 = rectangle_2.width
                    stick.stick_x2 = rectangle_2.width
                    rewind = False
                    ball_forward = False
                    stick_turn = False
                    player_1 = False
                    player_2 = True
                    rotated_end_y = 0
                    # print(f"Stick length: {stick_length}, LDR:{lower_distance_between_rect}, UDR:{upper_distance_between_rect}")
                    print(f"Player-1: {rectangle_1.rect_X, rectangle_2.rect_X, rectangle_2.width, stick.stick_x1}")

            if rectangle_1.rect_X > 0 and player_2 == True:
                rectangle_2.rect_X -= 1
                ball.circle_x1 -= 1
                # stick.stick_x1 = 0
                # stick.stick_x2 = 0
                stick.stick_y2 = stick_y1
                rectangle_1.rect_X -= 1

                stick.stick_x1 = rectangle_2.width
                stick.stick_y1 = 600
                stick.stick_x2 = rectangle_2.width
                stick.stick_y2 = 600

            if rectangle_1.rect_X == 0 and player_2 == True:
                if rectangle_2.rect_X < 0:
                    rectangle_2.rect_X = width + 5
                    random_x = gen_random_number.random_x_build()
                    random_width = gen_random_number.random_width_build()
                    rectangle_2.width = random_width
                    print(f"Random X: {random_x}, Random width: {random_width}")

                if rectangle_2.rect_X > random_x:
                    rectangle_2.rect_X -= 1

                if rectangle_2.rect_X == random_x:
                    stick.stick_x1 = rectangle_1.width
                    stick.stick_x2 = rectangle_1.width
                    rewind = False
                    ball_forward = False
                    stick_turn = False
                    player_1 = True
                    player_2 = False
                    rotated_end_y = 0
                    # print(f"Stick length: {stick_length}, LDR:{lower_distance_between_rect}, UDR:{upper_distance_between_rect}")
                    print(f"Player-2: {rectangle_1.rect_X, rectangle_2.rect_X, rectangle_1.width, stick.stick_x1}")

            # print('rewind work')


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

    draw_window()

    pygame.display.update()
