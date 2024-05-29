import pygame
import os
from random import randrange

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))  # set screen


# draw text restart
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


# draw button restart
def draw_button(x, y, width, height, text):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    font = pygame.font.Font(None, 36)
    draw_text(text, font, (255, 255, 255), screen, x + width / 2, y + height / 2)


# restart game
def restart_game():
    # variables
    res, size = 800, 50  # размер окно квадрата, размер квадратика
    x, y = randrange(0, res, size), randrange(0, res, size)  # рандомный нач. положение для snake
    apple = randrange(0, res, size), randrange(0, res, size)
    dirs = {'UP': True, 'DOWN': True, 'RIGHT': True, 'LEFT': True}

    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    fps = 10
    score = 0
    count = 0
    level = 1

    # big apple variables
    big_apple = ()
    big_apple_timer = 0
    big_apple_duration = 3000
    big_apple_cooldown = 5000

    # font to write score
    font_score = pygame.font.SysFont('Arial', 26, bold=True)
    font_end = pygame.font.SysFont('Arial', 66, bold=True)

    # phon
    back_image = pygame.image.load('background.jpg')
    background = pygame.transform.scale(back_image, (res, res))

    # main part
    process = True
    while process:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))

        # draw snake
        [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, size - 2, size - 2))) for i, j in snake]
        # draw apple
        pygame.draw.rect(screen, pygame.Color('blue'), (*apple, size - 5, size - 5))

        # center wall
        pygame.draw.rect(screen, pygame.Color('black'), (res // 3+ size, res // 3 + size, res // 3 - size * 2, res // 3 - size * 2))

        # big apple generation
        current_time = pygame.time.get_ticks()
        if current_time - big_apple_timer >= big_apple_cooldown:
            big_apple_timer = current_time
            big_apple = randrange(0, res, size), randrange(0, res, size)

        if big_apple:
            if current_time - big_apple_timer < big_apple_duration:
                pygame.draw.rect(screen, pygame.Color('red'), (*big_apple, size + 5, size + 5))
                if snake[-1] == big_apple:
                    length += 2
                    score += 2
                    count += 2
                    big_apple = ()
                    # fps += 0.2

            else:
                big_apple = ()

        # drawing score and level
        render_score = font_score.render(f'SCORE:{count}', 1, pygame.Color('white'))
        screen.blit(render_score, (5, 5))
        render_level = font_score.render(f'LEVEL {level}', 1, pygame.Color('white'))
        screen.blit(render_level, (5, 30))

        # update position
        x += dx * size
        y += dy * size
        snake.append((x, y))
        snake = snake[-length:]

        # eat aplle
        if snake[-1] == apple:
            apple = randrange(0, res, size), randrange(0, res, size)
            length += 1
            score += 1
            count += 1
            # fps += 0.2

        # increase speed
        if score % 5 >= 0 and score > 4:
            level += 1
            score = score - 5
            fps += 1

        # condition to collisions
        if x < 0 or x >= res or y < 0 or y >= res or len(snake) != len(set(snake)) or (res // 3 <= x < res * 2 // 3 and res // 3 <= y < res * 2 // 3):
            while True:
                render_end = font_end.render('GAME OVER', 1, pygame.Color('white'))
                screen.blit(render_end, (res // 2 - 200, res // 3))
                render_score = font_score.render(f'SCORE: {count}', 1, pygame.Color('white'))
                # render_level = font_score.render(f'LEVEL {level}', 1 , pygame.Color('white'))
                screen.blit(render_score, ((res // 2) - 75, (res // 3) + 70))
                # screen.blit(render_level,((res //2) - 75, (res//3) + 70))

                draw_button(800 / 2 - 125, 800 / 2 - 30, 200, 50, 'RESTART')

                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 700 / 2 - 50 <= mouse_pos[0] <= 800 / 2 + 50 and 800 / 2 - 125 <= mouse_pos[1] <= 800 / 2 + 125:
                            restart_game()
        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process = False

        # snake's moving
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dirs['UP']:
            dx, dy = 0, -1
            dirs = {'UP': False, 'DOWN': False, 'RIGHT': True, 'LEFT': True}
        if keys[pygame.K_DOWN] and dirs['DOWN']:
            dx, dy = 0, 1
            dirs = {'UP': False, 'DOWN': False, 'RIGHT': True, 'LEFT': True}
        if keys[pygame.K_LEFT] and dirs['LEFT']:
            dx, dy = -1, 0
            dirs = {'UP': True, 'DOWN': True, 'RIGHT': False, 'LEFT': False}
        if keys[pygame.K_RIGHT] and dirs['RIGHT']:
            dx, dy = 1, 0
            dirs = {'UP': True, 'DOWN': True, 'RIGHT': False, 'LEFT': False}


restart_game()
