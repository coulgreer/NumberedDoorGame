import pygame
import constants as c


class Button(pygame.sprite.Sprite):
    def __init__(self,  rect, text, font, inactive_color, active_color):
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

        self.text_surf = font.render(text, True, c.BLACK)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = [rect_width / 2, rect_height / 2]
        self.image.blit(self.text_surf, self.text_rect)

        self.func = None
        self.func_args = None

    def assign_function(self, func, *args):
        self.func = func
        self.func_args = args

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image.fill(self.active_color)
                self.image.blit(self.text_surf, self.text_rect)
            else:
                self.image.fill(self.inactive_color)
                self.image.blit(self.text_surf, self.text_rect)

        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            self.func(*self.func_args)
