import pygame
import constants as c
from number_ball import NumberBall
from number_door import NumberDoor
from button import Button

current_stage = 1
door_sprites = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()


def main():
    pygame.init()

    pygame.display.set_caption('Numbered Door Game')
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    done = False

    initialize_balls()

    door_images = ('images/Doors/Door-1.png', 'images/Doors/Door-2.png', 'images/Doors/Door-3.png',
                   'images/Doors/Door-4.png', 'images/Doors/Door-5.png', 'images/Doors/Door-6.png',
                   'images/Doors/Door-7.png', 'images/Doors/Door-8.png', 'images/Doors/Door-9-Small.png',
                   'images/Doors/Door-9-Big.png')

    stages = (None,
              (NumberDoor(4, door_images[3]), NumberDoor(5, door_images[4])),
              (NumberDoor(3, door_images[2]), NumberDoor(7, door_images[6]), NumberDoor(8, door_images[7])),
              (NumberDoor(1, door_images[0]), NumberDoor(6, door_images[5]), NumberDoor(2, door_images[1])),
              (NumberDoor(9, door_images[8]), NumberDoor(9, door_images[9])))

    stages[current_stage][0].set_active(True)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONUP:
                move_ball(stages[current_stage])

        door_sprites.empty()
        for x in range(0, len(stages[current_stage])):
            door = stages[current_stage][x]
            door.set_position(x, len(stages[current_stage]))
            door_sprites.add(door)

        create_buttons(event, stages)

        ball_sprites.update()
        door_sprites.update()
        button_sprites.update()

        screen.fill(c.BLACK)
        door_sprites.draw(screen)
        ball_sprites.draw(screen)
        button_sprites.draw(screen)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()


def initialize_balls():
    ball_images = ('images/Balls/Ball-1.png', 'images/Balls/Ball-2.png', 'images/Balls/Ball-3.png',
                   'images/Balls/Ball-4.png', 'images/Balls/Ball-5.png', 'images/Balls/Ball-6.png',
                   'images/Balls/Ball-7.png', 'images/Balls/Ball-8.png', 'images/Balls/Ball-9.png')

    for i in range(0, c.MAX_BALLS):
        ball = NumberBall(i + 1, ball_images[i])
        ball.set_default_position_index(i)
        ball_sprites.add(ball)


def move_ball(stage):
    mouse_position = pygame.mouse.get_pos()
    mouse_y = mouse_position[1]
    if c.BALL_DIV_HEIGHT < mouse_y:
        for door in stage:
            if door.rect.collidepoint(mouse_position):
                door.set_active(True)
            else:
                door.set_active(False)

    for ball in ball_sprites:
        if ball.rect.collidepoint(mouse_position) and c.BALL_DIV_HEIGHT < mouse_y:
            ball.reset_position()
            for door in stage:
                if door.remove_ball(ball.value):
                    break
        elif ball.rect.collidepoint(mouse_position) and c.BALL_DIV_HEIGHT > mouse_y:
            for door in stage:
                if door.is_active and door.add_ball(ball.value):
                    slots = door.get_slots()
                    ball.move_to_door(slots.index(ball.value), door.rect)


def remove_unused_balls(stage):
    temp_balls = pygame.sprite.Group()
    for ball in ball_sprites:
        for door in stage:
            if ball.value in door.get_slots() and door.has_valid_solution():
                temp_balls.add(ball)
    return temp_balls


def reset():
    for ball in ball_sprites:
        ball.reset_position()

    for door in door_sprites:
        door.reset()


def progress_to_next_stage(stages):
    global current_stage
    global ball_sprites

    solutions = []
    for door in stages[current_stage]:
        solution = door.has_valid_solution()
        solutions.append(solution)

    if True in solutions and current_stage < 4:
        ball_sprites = remove_unused_balls(stages[current_stage])
        reset()
        current_stage += 1
        stages[current_stage][0].set_active(True)
    elif True in solutions and current_stage == 4:
        reset()

        # Give the user some fanfare and tell them they won
        current_stage = 1


def restart_game():
    global current_stage
    global ball_sprites

    ball_sprites.empty()
    current_stage = 1

    initialize_balls()
    reset()


def create_buttons(event, stages):
    margin = 10
    button_length = 80
    button_area = margin + button_length + margin
    y = 300

    x = margin + c.SCREEN_WIDTH / 2 - (button_area * 3) / 2
    check_button = Button((x, y, 80, 40), 'Check', c.GRAY, c.TAN)
    check_button.assign_function(event, progress_to_next_stage, stages)
    button_sprites.add(check_button)

    x += button_area
    clear_button = Button((x, y, 80, 40), 'Clear', c.GRAY, c.LIGHT_SKY_BLUE)
    clear_button.assign_function(event, reset)
    button_sprites.add(clear_button)

    x += button_area
    restart_button = Button((x, y, 80, 40), 'Restart', c.GRAY, c.ORCHID)
    restart_button.assign_function(event, restart_game)
    button_sprites.add(restart_button)


if __name__ == '__main__':
    main()
