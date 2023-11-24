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
paddle_height = screen_height / 5
paddle_speed = 15

ball_diameter = screen_width / 50
paddle_offset = ball_diameter * 1.5

ball_init_speed = [8, 8]

# ----------------------- GAME -----------------------
class Pong:
    def __init__(self, ball, paddle_l, paddle_r=None):
        self.paddle_l = paddle_l
        self.paddle_r = paddle_r
        self.ball = ball

        self.paddles = pygame.sprite.Group()
        self.paddles.add(paddle_l) # player 1
        self.paddles.add(paddle_r if paddle_r is not None else paddle_l.copy()) # player 2 / AI

        self.sprites = pygame.sprite.Group(self.ball, self.paddles)

        self.score_l = self.score_r = 0
        self.MAX_SCORE = 11
        self.over = False
        self.point_scored = False

    def run(self):
        # HANDLE EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.over = True

        # DRAWING
        if pygame.sprite.spritecollideany(self.ball, self.paddles):
            ball.change_direction()

        keys = pygame.key.get_pressed()
        self.sprites.update(keys)


        screen.fill(BLACK)
        self.sprites.draw(screen)

        clock.tick(2*fps)
        pygame.display.flip() # przerysowanie całego okna z bufora na ekran

    def update_score(self, score):
        score += 1
        if score == self.MAX_SCORE:
            self.end_game()

    def end_game(self):
        pass

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
        self.init_coords()
        self.is_scored = False
        self.speed = self.rand_spd()

    def rand_spd(self):
        # so as to avoid movement too vertical or too horizontal
        angle_beg = random.choice([30, 120, 210, 300])
        angle_end = angle_beg + 30
        angle = math.radians(random.uniform(angle_beg, angle_end))
        x_speed = ball_init_speed[0] * math.sin(angle)
        y_speed = ball_init_speed[1] * math.cos(angle)
        return [x_speed, y_speed]
    
    def init_coords(self):
        self.rect.y = (screen_height - ball_diameter) / 2
        self.rect.x = (screen_width - ball_diameter) / 2

    def change_direction(self):
        self.speed[0] *= -1

    def update(self, keys):
        self.rect.move_ip(self.speed)

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed[1] *= -1
        if self.rect.right < paddle_offset or self.rect.left > screen_width - paddle_offset:
            self.speed = [0, 0]
            self.is_scored = True
        
        if self.is_scored:
            if keys[pygame.K_SPACE]:
                self.is_scored = False
                self.init_coords()
                self.speed = self.rand_spd()
            
        return self.is_scored

# ----------------------- SPRITES -----------------------
ball = Ball(RED, ball_diameter)
paddle1 = Paddle(GREEN, paddle_width, paddle_height, left=True)
paddle2 = Paddle(GREEN, paddle_width, paddle_height)

# ----------------------- GAME -----------------------
if __name__ == "__main__":
    fps = 60
    clock = pygame.time.Clock()
    game = Pong(ball, paddle1, paddle2)
    game.run()
    pygame.quit()