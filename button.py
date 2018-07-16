import pygame
import constants as c


class Button(pygame.sprite.Sprite):
    def __init__(self,  rect, text, inactive_color, active_color):
        pygame.sprite.Sprite.__init__(self)

        rect_x = rect[0]
        rect_y = rect[1]
        rect_width = rect[2]
        rect_height = rect[3]

        self.inactive_color = inactive_color
        self.active_color = active_color
        self.image = pygame.Surface((rect_width, rect_height))
        self.image.fill(self.inactive_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (rect_x, rect_y)

        font = pygame.font.SysFont('Arial', 12)
        self.text_surf = font.render(text, True, c.BLACK)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = [rect_width / 2, rect_height / 2]
        self.image.blit(self.text_surf, self.text_rect)

    def assign_function(self, event, funct, *args):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image.fill(self.active_color)
                self.image.blit(self.text_surf, self.text_rect)
            else:
                self.image.fill(self.inactive_color)
                self.image.blit(self.text_surf, self.text_rect)

        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            return funct(*args)
