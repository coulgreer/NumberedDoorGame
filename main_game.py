import pygame
import constants as c
from number_ball import NumberBall
from number_door import NumberDoor


def main():
    pygame.init()

    pygame.display.set_caption('Numbered Door Game')
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    done = False
    current_stage = 1

    ball_images = ('images/Balls/Ball-1.png', 'images/Balls/Ball-2.png', 'images/Balls/Ball-3.png',
                   'images/Balls/Ball-4.png', 'images/Balls/Ball-5.png', 'images/Balls/Ball-6.png',
                   'images/Balls/Ball-7.png', 'images/Balls/Ball-8.png', 'images/Balls/Ball-9.png')

    ball_sprites = pygame.sprite.Group()
    for i in range(0, c.MAX_BALLS):
        ball = NumberBall(i + 1, ball_images[i])
        ball.set_default_position_index(i)
        ball_sprites.add(ball)

    door_images = ('images/Doors/Door-1.png', 'images/Doors/Door-2.png', 'images/Doors/Door-3.png',
                   'images/Doors/Door-4.png', 'images/Doors/Door-5.png', 'images/Doors/Door-6.png',
                   'images/Doors/Door-7.png', 'images/Doors/Door-8.png', 'images/Doors/Door-9-Big.png')

    stages = (None,
              (NumberDoor(4, door_images[3]), NumberDoor(5, door_images[4])),
              (NumberDoor(3, door_images[2]), NumberDoor(7, door_images[6]), NumberDoor(8, door_images[7])),
              (NumberDoor(1, door_images[0]), NumberDoor(6, door_images[5]), NumberDoor(2, door_images[1])),
              (NumberDoor(9, door_images[8]), NumberDoor(9, door_images[8])))

    door_sprites = pygame.sprite.Group()
    stages[current_stage][0].set_active(True)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                mouse_x = mouse_position[1]
                if c.BALL_DIV_HEIGHT < mouse_x:
                    for door in stages[current_stage]:
                        if door.rect.collidepoint(mouse_position):
                            door.set_active(True)
                        else:
                            door.set_active(False)
                for ball in ball_sprites:
                    if ball.rect.collidepoint(mouse_position) and c.BALL_DIV_HEIGHT < mouse_x:
                        ball.reset_position()
                        for door in stages[current_stage]:
                            if door.remove_ball(ball.value):
                                break
                    elif ball.rect.collidepoint(mouse_position) and c.BALL_DIV_HEIGHT > mouse_x:
                        for door in stages[current_stage]:
                            if door.is_active and door.add_ball(ball.value):
                                ball.move_to_door(door.slots.index(ball.value), door.rect)

        door_sprites.empty()
        for x in range(0, len(stages[current_stage])):
            door = stages[current_stage][x]
            door.set_position(x, len(stages[current_stage]))
            door_sprites.add(door)

        ball_sprites.update()
        door_sprites.update()

        screen.fill(c.BLACK)
        door_sprites.draw(screen)
        ball_sprites.draw(screen)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
