"""Zaimplementować swoją wersję gry Atari Pong (1972).
Celem gry jest zdobycie 11 punktów. 
Można grać przeciwko drugiemu graczowi lub komputerowi.
"""

import pygame
import random
import math

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)

size = screen_width, screen_height = (1000, 800)
paddle_width = screen_width / 70
paddle_height = screen_height / 5
paddle_speed = 15

ball_diameter = screen_width / 50
paddle_offset = ball_diameter * 1.5

screen = pygame.display.set_mode(size)

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

        self.font = pygame.font.Font(None, 36)

    def run(self, clock, fps):
        while not self.over:
            # HANDLE EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.over = True
                    # ??

            # DRAWING
            if pygame.sprite.spritecollideany(self.ball, self.paddles):
                self.ball.change_direction()

            keys = pygame.key.get_pressed()
            self.sprites.update(keys)

            if self.ball.is_scored:
                self.score_l += 1
                self.ball.is_scored = False # wait to click! 
                if keys[pygame.K_SPACE]:
                    self.ball.init_coords()
                    self.ball.speed = self.ball.rand_spd()
                if self.score_l == self.MAX_SCORE or self.score_r == self.MAX_SCORE:
                    self.end_menu()

            screen.fill(BLACK)
            self.sprites.draw(screen)

            clock.tick(fps)
            score_text = self.font.render(f'left score: {self.score_l} right score: {self.score_r}', True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            pygame.display.flip() # przerysowanie całego okna z bufora na ekran

    def start_menu(self):
        pass

    def end_menu(self):
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
        self.base_speed = [5, 5]
        self.speed = self.rand_spd()
        self.is_scored = False

    def rand_spd(self):
        # so as to avoid movement too vertical or too horizontal
        angle_beg = random.choice([30, 120, 210, 300])
        angle_end = angle_beg + 30
        angle = math.radians(random.uniform(angle_beg, angle_end))
        speedx = self.base_speed[0] * math.sin(angle)
        speedy = self.base_speed[1] * math.cos(angle)
        return [speedx, speedy]
    
    def reset(self):
        self.init_coords()
        self.speed = self.rand_spd()

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
            
def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Pong')

    fps = 120
    clock = pygame.time.Clock()

    # ----------------------- RUN -----------------------
    ball = Ball(RED, ball_diameter)
    paddle1 = Paddle(GREEN, paddle_width, paddle_height, left=True)
    paddle2 = Paddle(GREEN, paddle_width, paddle_height)
    game = Pong(ball, paddle1, paddle2)
    game.run(clock, fps)
    pygame.quit()

if __name__ == "__main__":
    main()