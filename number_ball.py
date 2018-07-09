import pygame
import constants as c


class NumberBall(pygame.sprite.Sprite):
    def __init__(self, value, image):
        pygame.sprite.Sprite.__init__(self)

        self.pos_index = -1
        self.value = value
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def set_default_position_index(self, pos_index):
        self.pos_index = pos_index
        x = (self.pos_index / c.MAX_BALLS) * c.SCREEN_WIDTH + (c.SCREEN_WIDTH / c.MAX_BALLS) / 2
        y = c.SCREEN_BORDER_THICKNESS
        self.rect.midtop = (x, y)

    def reset_position(self):
        x = (self.pos_index / c.MAX_BALLS) * c.SCREEN_WIDTH + (c.SCREEN_WIDTH / c.MAX_BALLS) / 2
        y = c.SCREEN_BORDER_THICKNESS
        self.rect.midtop = (x, y)

    def move_to_door(self, door_index, rect):
        if not (door_index + 1) % 2 == 0:
            x = (rect.width / 3) / 2 + rect.x
        else:
            x = (rect.width - self.rect.width / 2) + rect.x - c.DOOR_BORDER_THICKNESS

        y = (60 * (door_index // 2) + c.DOOR_BORDER_THICKNESS) + rect.y
        self.rect.midtop = (x, y)

