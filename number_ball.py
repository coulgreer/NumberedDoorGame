import pygame
import constants as c


class NumberBall(pygame.sprite.Sprite):
    def __init__(self, pos_index, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        diameter = self.rect.width
        radius = diameter / 2
        total_circle_width = c.MAX_BALLS * diameter
        margin = (c.SCREEN_WIDTH - total_circle_width) // (c.MAX_BALLS * 2) if (c.SCREEN_WIDTH - total_circle_width) > 0 else 0
        y = self.calculate_y(radius, margin)
        x = self.calculate_x(radius, margin, pos_index)

        self.rect.center = (x, y)

    def calculate_y(self, ball_radius, margin):
        y = ball_radius + margin
        return y

    def calculate_x(self, ball_radius, margin, pos_index):
        x = (margin * (1 + pos_index)) + (ball_radius * (1 + (2 * pos_index))) + (margin * pos_index)
        return x
