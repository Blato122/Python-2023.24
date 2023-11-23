"""Zaimplementować swoją wersję gry Atari Pong (1972).
Celem gry jest zdobycie 11 punktów. 
Można grać przeciwko drugiemu graczowi lub komputerowi.
"""

import pygame
import random
import math

# ----------------------- COLORS -----------------------
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)

# ----------------------- INIT -----------------------
pygame.init()
size = screen_width, screen_height = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong')

# ----------------------- VARIABLES -----------------------
paddle_width = screen_width / 70
paddle_height = screen_height / 7
paddle_speed = 15

ball_diameter = paddle_height / 5
paddle_offset = ball_diameter * 1.5

ball_init_speed = [8, 8]

# ----------------------- PADDLE -----------------------
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, left=False):
        super().__init__()
        self.left = left
        self.image = pygame.Surface([width, height])
        self.image.fill(color) # tylko kolor
        self.rect = self.image.get_rect()
        self.rect.centery = screen_height / 2
        self.rect.centerx = paddle_offset if left else screen_width - paddle_offset

    def update(self, keys):
        if self.left:
            if keys[pygame.K_s] and self.rect.bottom <= screen_height:
                self.rect.y += paddle_speed
            if keys[pygame.K_w] and self.rect.top >= 0:
                self.rect.y -= paddle_speed
        else:
            if keys[pygame.K_DOWN] and self.rect.bottom <= screen_height:
                self.rect.y += paddle_speed
            if keys[pygame.K_UP] and self.rect.top >= 0:
                self.rect.y -= paddle_speed

# ----------------------- BALL -----------------------
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, diameter):
        super().__init__()
        self.image = pygame.Surface([diameter, diameter])
        self.image.fill(color) # tylko kolor
        self.rect = self.image.get_rect()
        self.rect.y = (screen_height - ball_diameter) / 2
        self.rect.x = (screen_width - ball_diameter) / 2
        
        # so as to avoid movement too vertical or too horizontal
        angle_beg = random.choice([20, 110, 200, 290])
        angle_end = angle_beg + 50
        angle = math.radians(random.uniform(angle_beg, angle_end))
        x_speed = ball_init_speed[0] * math.sin(angle)
        y_speed = ball_init_speed[1] * math.cos(angle)
        self.speed = [x_speed, y_speed]

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed[1] *= -1

# ----------------------- SPRITES -----------------------
ball = Ball(RED, ball_diameter)
balls = pygame.sprite.Group()
balls.add(ball)

paddle1 = Paddle(GREEN, paddle_width, paddle_height)
paddle2 = Paddle(GREEN, paddle_width, paddle_height, left=True)
paddles = pygame.sprite.Group()
paddles.add(paddle1, paddle2)

# ----------------------- CLOCK -----------------------
fps = 60
clock = pygame.time.Clock()

# ----------------------- MAIN GAME LOOP -----------------------
score = 0
done = False
while not done:
    clock.tick(fps)
    screen.fill(BLACK)

    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # DRAWING
    # Rysowanie różnych obiektów, sprawdzanie przekrywania, itp.
    keys = pygame.key.get_pressed()
    paddles.update(keys)
    paddles.draw(screen)
    balls.update()
    balls.draw(screen)
    pygame.display.flip() # przerysowanie całego okna z bufora na ekran

pygame.quit()
# dalsze instrukcje programu bez pygame