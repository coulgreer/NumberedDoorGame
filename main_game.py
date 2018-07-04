import pygame
import constants as c
import number_ball


def main():
    pygame.init()

    pygame.display.set_caption('Numbered Door Game')
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    done = False

    images = ('images/Balls/Ball-1.png', 'images/Balls/Ball-2.png', 'images/Balls/Ball-3.png',
              'images/Balls/Ball-4.png', 'images/Balls/Ball-5.png', 'images/Balls/Ball-6.png',
              'images/Balls/Ball-7.png', 'images/Balls/Ball-8.png', 'images/Balls/Ball-9.png')

    ball_sprites = pygame.sprite.Group()
    for i in range(0, c.MAX_BALLS):
        ball_sprites.add(number_ball.NumberBall(i, images[i]))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        ball_sprites.update()

        screen.fill(c.BLACK)
        ball_sprites.draw(screen)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
