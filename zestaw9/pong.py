"""Zaimplementować swoją wersję gry Atari Pong (1972).
Celem gry jest zdobycie 11 punktów. 
Można grać przeciwko drugiemu graczowi lub komputerowi.
"""

import pygame
import random
import math
from enum import Enum

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)

size = screen_width, screen_height = (1200, 900)
paddle_width = screen_width / 70
paddle_height = screen_height / 5

paddle_speed = 900
ball_speed = [600, 600]

ball_diameter = screen_width / 50
paddle_offset = ball_diameter * 1.5

screen = pygame.display.set_mode(size)

class IsScored(Enum):
    NO = 0
    LEFT = 1
    RIGHT = 2
    WAITING = 3

class Player(Enum):
    LEFT = 0
    RIGHT = 1
    AI = 2

# ----------------------- GAME -----------------------
class Pong:
    def __init__(self, vsAI=True):
        self.ball = Ball(RED, ball_diameter)
        self.paddle1 = Paddle(GREEN, paddle_width, paddle_height, Player.LEFT)
        self.paddle2 = Paddle(GREEN, paddle_width, paddle_height, Player.AI if vsAI else Player.RIGHT)

        self.paddles = pygame.sprite.Group()
        self.paddles.add(self.paddle1) # player 1
        self.paddles.add(self.paddle2) # player 2 / AI
        if (self.paddle1.player == self.paddle2.player): pygame.quit()

        self.sprites = pygame.sprite.Group(self.ball, self.paddles)

        self.score_l = self.score_r = 0
        self.MAX_SCORE = 2 #11
        self.over = False
        self.finished = False

        self.font = pygame.font.Font(None, 72)

    def run(self, fps):
        clock = pygame.time.Clock()
        # choose players here?
        self.start_menu() # does nothing
        while not self.over:
            timedelta = clock.tick(fps)
            c = timedelta / 1000.0 # ms to s
            
            # HANDLE EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.over = True
                    # ??

            # DRAWING
            if pygame.sprite.spritecollideany(self.ball, self.paddles):
                self.ball.change_direction()

            keys = pygame.key.get_pressed()
            self.sprites.update(keys, self.ball.rect.centery, c)

            print (self.ball.state)
            if (s := self.ball.state) == IsScored.LEFT:
                self.score_r += 1 
                self.ball.state = IsScored.WAITING
            elif s == IsScored.RIGHT: 
                self.score_l += 1
                self.ball.state = IsScored.WAITING

            if s == IsScored.WAITING:
                if keys[pygame.K_SPACE]:
                    for sprite in self.sprites:
                        sprite.reset()

            screen.fill(BLACK)
            self.sprites.draw(screen)

            if self.score_l == self.MAX_SCORE or self.score_r == self.MAX_SCORE:
                self.end_menu()
                self.finished = True

            if self.finished:
                if keys[pygame.K_SPACE]:
                    for sprite in self.sprites:
                        sprite.reset()
                    self.score_l = self.score_r = 0
                    self.finished = False
                if keys[pygame.K_RETURN]: # enter
                    self.over = True

            score_text = self.font.render(f"{self.score_l} - {self.score_r}", True, (255, 255, 255))
            screen.blit(score_text, ((screen_width - score_text.get_width()) / 2, screen_height / 50))

            pygame.display.flip() # przerysowanie całego okna z bufora na ekran

    def start_menu(self):
        pass

    def end_menu(self):
        end_text = self.font.render(f"Player 1 won" if self.score_l == self.MAX_SCORE else "Player 2 won", True, (255, 255, 255))
        screen.blit(end_text, ((screen_width - end_text.get_width()) / 2, screen_height / 2))   

# ----------------------- PADDLE -----------------------
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height, player):
        super().__init__()
        self.player = player
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.centery = screen_height / 2
        self.rect.centerx = paddle_offset if self.player == Player.LEFT else screen_width - paddle_offset

    def update(self, keys, ball_y, td):
        if self.player == Player.RIGHT:
            if keys[pygame.K_DOWN] and self.rect.bottom <= screen_height:
                self.rect.y += td * paddle_speed
            if keys[pygame.K_UP] and self.rect.top >= 0:
                self.rect.y -= td * paddle_speed
        elif self.player == Player.LEFT:
            if keys[pygame.K_s] and self.rect.bottom <= screen_height:
                self.rect.y += td * paddle_speed
            if keys[pygame.K_w] and self.rect.top >= 0:
                self.rect.y -= td * paddle_speed
        else: # AI
            if self.rect.centery < ball_y:
                self.rect.y += td * paddle_speed #* random.uniform(0.15, 0.25)
            else:
                self.rect.y -= td * paddle_speed #* random.uniform(0.15, 0.25)

# ----------------------- BALL -----------------------
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, diameter):
        super().__init__()
        self.image = pygame.Surface([diameter, diameter])
        self.image.fill(color) # tylko kolor
        self.rect = self.image.get_rect()
        self.reset()

    def rand_spd(self):
        # so as to avoid movement too vertical or too horizontal
        angle_beg = random.choice([30, 120, 210, 300])
        angle_end = angle_beg + 30
        angle = math.radians(random.uniform(angle_beg, angle_end))
        speedx = ball_speed[0] * math.sin(angle)
        speedy = ball_speed[1] * math.cos(angle)
        return [speedx, speedy]
    
    def reset(self):
        self.state = IsScored.NO
        self.init_coords()
        self.speed = self.rand_spd()

    def init_coords(self):
        self.rect.y = (screen_height - ball_diameter) / 2
        self.rect.x = (screen_width - ball_diameter) / 2

    def change_direction(self):
        self.speed[0] *= -1

    def update(self, keys, ball_y, td):
        self.rect.move_ip(self.speed[0] * td, self.speed[1] * td)

        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed[1] *= -1
        if self.rect.right < paddle_offset and self.state == IsScored.NO: # so that it doesn't change to scored right after setting it to NO
            self.speed = [0, 0]
            self.state = IsScored.LEFT
        elif self.rect.left > screen_width - paddle_offset and self.state == IsScored.NO:
            self.speed = [0, 0]
            self.state = IsScored.RIGHT
            
def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Pong')
    game = Pong(vsAI=False)
    game.run(fps=60)
    pygame.quit()

if __name__ == "__main__":
    main()