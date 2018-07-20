import pygame
import sys
import constants as c
from number_ball import NumberBall
from number_door import NumberDoor
from button import Button

current_stage = 1
door_sprites = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()


def main():
    global screen
    global clock
    pygame.init()

    pygame.display.set_caption('Numbered Door Game')
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    intro_loop()


def intro_loop():
    done = False
    text_font = pygame.font.SysFont('Arial', c.EXTRA_LARGE_TEXT)
    button_font = pygame.font.SysFont('Arial', c.LARGE_TEXT)
    start_button = Button((c.SCREEN_WIDTH / 2 - c.LARGE_BUTTON_WIDTH / 2, c.SCREEN_HEIGHT / 2 + c.EXTRA_LARGE_TEXT,
                           c.LARGE_BUTTON_WIDTH, c.LARGE_BUTTON_HEIGHT),
                          'Start', button_font, c.GRAY, c.HOT_PINK)
    start_button.assign_function(game_loop)
    button_sprites.add(start_button)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            for button in button_sprites:
                button.handle_event(event)

        screen.fill(c.WHITE)
        draw_text(screen, 'Welcome to the Game', text_font, [c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2])

        button_sprites.update()
        button_sprites.draw(screen)

        pygame.display.update()


def exit_game():
    pygame.quit()
    sys.exit()


def draw_text(surf, text, font, coordinates):
    x = coordinates[0]
    y = coordinates[1]
    text_surf = font.render(text, True, c.BLACK)
    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surf, text_rect)


def game_loop():
    done = False

    button_sprites.empty()
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

    create_buttons(stages)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.MOUSEBUTTONUP:
                move_ball(stages[current_stage])

            for button in button_sprites:
                button.handle_event(event)

        door_sprites.empty()
        for x in range(0, len(stages[current_stage])):
            door = stages[current_stage][x]
            door.set_position(x, len(stages[current_stage]))
            door_sprites.add(door)

        ball_sprites.update()
        door_sprites.update()
        button_sprites.update()

        screen.fill(c.BLACK)
        door_sprites.draw(screen)
        ball_sprites.draw(screen)
        button_sprites.draw(screen)

        pygame.display.update()
        clock.tick(60)


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
                for unselected_door in stage:
                    unselected_door.set_active(False)
                door.set_active(True)
                break

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
        game_over_loop()


def game_over_loop():
    button_sprites.empty()

    done = False
    text_font = pygame.font.SysFont('Arial', c.EXTRA_LARGE_TEXT)
    button_font = pygame.font.SysFont('Arial', c.MEDIUM_TEXT)
    retry_button = Button((c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2 + c.LARGE_BUTTON_HEIGHT,
                           c.LARGE_BUTTON_WIDTH, c.LARGE_BUTTON_HEIGHT),
                          'Restart', button_font, c.GRAY, c.LIGHT_STEEL_BLUE)
    retry_button.assign_function(restart_game)
    button_sprites.add(retry_button)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            for button in button_sprites:
                button.handle_event(event)

        screen.fill(c.WHITE)
        draw_text(screen, 'Congrats You Won!!', text_font, (c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2))
        button_sprites.update()
        button_sprites.draw(screen)

        pygame.display.update()


def reset():
    for ball in ball_sprites:
        ball.reset_position()

    for door in door_sprites:
        door.reset()


def restart_game():
    global current_stage
    global ball_sprites

    ball_sprites.empty()
    current_stage = 1

    game_loop()


def create_buttons(stages):
    font = pygame.font.SysFont('Arial', c.SMALL_TEXT)

    margin = 10
    button_area = margin + c.MEDIUM_BUTTON_WIDTH + margin
    y = 300

    x = margin + c.SCREEN_WIDTH / 2 - (button_area * 3) / 2
    check_button = Button((x, y, c.MEDIUM_BUTTON_WIDTH, c.MEDIUM_BUTTON_HEIGHT),
                          'Check', font, c.GRAY, c.TAN)
    check_button.assign_function(progress_to_next_stage, stages)
    button_sprites.add(check_button)

    x += button_area
    clear_button = Button((x, y, c.MEDIUM_BUTTON_WIDTH, c.MEDIUM_BUTTON_HEIGHT),
                          'Clear', font, c.GRAY, c.LIGHT_SKY_BLUE)
    clear_button.assign_function(reset)
    button_sprites.add(clear_button)

    x += button_area
    restart_button = Button((x, y, c.MEDIUM_BUTTON_WIDTH, c.MEDIUM_BUTTON_HEIGHT),
                            'Restart', font, c.GRAY, c.ORCHID)
    restart_button.assign_function(restart_game)
    button_sprites.add(restart_button)


if __name__ == '__main__':
    main()
