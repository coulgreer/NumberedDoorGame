import pygame

pygame.init()
pygame.display.set_caption('Numbered Door Game')
pygame.display.set_mode((600, 600))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
