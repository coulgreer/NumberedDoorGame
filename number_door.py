import pygame
import constants as c


class NumberDoor(pygame.sprite.Sprite):
    def __init__(self, door_value, image_url):
        pygame.sprite.Sprite.__init__(self)

        self.slots = [c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE,
                      c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE]
        self.is_active = False
        self.door_value = door_value
        self.image_url = image_url

        self.image = pygame.image.load(image_url)
        self.rect = self.image.get_rect()

    def set_slots(self, slots):
        self.slots = slots

    def get_slots(self):
        return self.slots

    def add_ball(self, ball_value):
        if c.DEFAULT_SLOT_VALUE not in self.slots:
            return False
        else:
            for index in range(0, c.MAX_SLOTS):
                if self.slots[index] == c.DEFAULT_SLOT_VALUE:
                    self.slots[index] = ball_value
                    return True

    def remove_ball(self, ball_value):
        try:
            index = self.slots.index(ball_value)
            self.slots[index] = c.DEFAULT_SLOT_VALUE
            return True
        except ValueError:
            return False

    def reset(self):
        self.slots = [c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE,
                      c.DEFAULT_SLOT_VALUE, c.DEFAULT_SLOT_VALUE]

    def has_valid_solution(self):
        digital_root = 0
        if c.MIN_SLOTS > self.slots.count(c.DEFAULT_SLOT_VALUE):
            for value in self.slots:
                digital_root += value
                while digital_root >= 10:
                    digital_root = sum(int(i) for i in str(digital_root))

            if digital_root == self.door_value:
                return True
            else:
                return False
        else:
            return False

    def set_position(self, pos_index, total_siblings):
        x = (pos_index / total_siblings) * c.SCREEN_WIDTH + (c.SCREEN_WIDTH / total_siblings) / 2
        y = c.BALL_DIV_HEIGHT
        self.rect.midtop = (x, y)

    def set_active(self, is_active):
        self.is_active = is_active
        if is_active:
            pygame.draw.rect(self.image, c.WHITE,
                             [(0, 0), (self.rect.width, self.rect.height)], c.DOOR_BORDER_THICKNESS)
        else:
            self.image = pygame.image.load(self.image_url)
