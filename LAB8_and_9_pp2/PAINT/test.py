import pygame
import sys
import math

pygame.init()

WIDTH = 960
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
done = False
eraser = False
Leftmouse = False
rectangle = False
circle = False
square = False
triangle = False
diamond = False
tenqabyrgaly = False
romb = False

# Colors
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorRed = (255, 0, 0)
colorGreen = (0, 255, 0)
colorBlue = (0, 0, 255)
colorYellow = (255, 255, 0)
color = colorWhite


# rect
def rectFunction(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


# circle radius
def circleFunction(x1, y1, x2, y2):
    radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return radius


# eraser
def eraserFunction(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


# square
def squareFunction(x1, y1, x2, y2):
    size = max(abs(x2 - x1), abs(y2 - y1))
    return pygame.Rect(min(x1, x2), min(y1, y2), size, size)


# tenqabyrgaly_triangle
def tenqabyrgaly_triangle(x1, y1, x2, y2):
    sol_zhak = [x1, y1]
    on_zhak = [x2, y2]
    asty = [x1, y2]
    points = [sol_zhak, on_zhak, asty]
    return points


# triangle
def tikburyshty_triangle(x1, y1, x2, y2):
    sol_zhak = [x1, y1]
    on_zhak = [x1 - (x2 - x1), y1 + (x2 - x1) * math.sqrt(3)]
    asty = [x2, y1 + (x2 - x1) * math.sqrt(3), ]
    points = [sol_zhak, on_zhak, asty]
    return points


# romb
def rombFunction(x1, y1, x2, y2):
    sol_zhak = [x1, y1]
    on_zhak = [x2, y2]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    diagonal = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 / 2
    asty = [x - diagonal, y]
    en_asty = [x + diagonal, y]
    points = [sol_zhak, asty, on_zhak, en_asty]
    return points


# main part
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # first point
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Leftmouse = True
            prevx = event.pos[0]
            prevy = event.pos[1]
        # last point
        if Leftmouse:
            currx = event.pos[0]
            curry = event.pos[1]
        if event.type == pygame.KEYDOWN:
            # Eraser
            if event.key == pygame.K_e:
                eraser = True
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                tenqabyrgaly = False
                romb = False
            # Rect
            if event.key == pygame.K_1:
                rectangle = True
                eraser = False
                circle = False
                square = False
                triangle = False
                diamond = False
                tenqabyrgaly = False
                romb = False
            # донгелек
            if event.key == pygame.K_2:
                circle = True
                eraser = False
                rectangle = False
                square = False
                triangle = False
                diamond = False
                tenqabyrgaly = False
                romb = False
            # квадрат
            if event.key == pygame.K_3:
                square = True
                eraser = False
                rectangle = False
                circle = False
                triangle = False
                diamond = False
                tenqabyrgaly = False
                romb = False
            # ушбурыш
            if event.key == pygame.K_4:
                triangle = True
                eraser = False
                rectangle = False
                circle = False
                square = False
                diamond = False
                tenqabyrgaly = False
                romb = False
            # тен ушбырыш
            if event.key == pygame.K_5:
                tenqabyrgaly = True
                eraser = False
                Leftmouse = False
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                romb = False
            # ромб
            if event.key == pygame.K_6:
                romb = True
                eraser = False
                Leftmouse = False
                rectangle = False
                circle = False
                square = False
                triangle = False
                diamond = False
                tenqabyrgaly = False
            if event.key == pygame.K_b:
                color = colorBlue
            if event.key == pygame.K_y:
                color = colorYellow
            if event.key == pygame.K_r:
                color = colorRed
            if event.key == pygame.K_g:
                color = colorGreen
        # мышканы жібергенде
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            Leftmouse = False
            if eraser:
                pygame.draw.rect(screen, colorBlack, eraserFunction(prevx, prevy, currx, curry))
            if rectangle:
                pygame.draw.rect(screen, color, rectFunction(prevx, prevy, currx, curry), 2)
            if circle:
                radius = circleFunction(prevx, prevy, currx, curry)
                pygame.draw.circle(screen, color, (prevx, prevy), radius, 2)
            if square:
                pygame.draw.rect(screen, color, squareFunction(prevx, prevy, currx, curry), 2)
            base_layer.blit(screen, (0, 0))
            if triangle:
                points = tenqabyrgaly_triangle(prevx, prevy, currx, curry)
                pygame.draw.polygon(screen, color, points, 2)
            if tenqabyrgaly:
                points = tikburyshty_triangle(prevx, prevy, currx, curry)
                pygame.draw.polygon(screen, color, points, 2)
            if romb:
                points = rombFunction(prevx, prevy, currx, curry)
                pygame.draw.polygon(screen, color, points, 2)

    if Leftmouse:
        screen.blit(base_layer, (0, 0))
        if eraser:
            pygame.draw.rect(screen, colorYellow, eraserFunction(prevx, prevy, currx, curry), 2)
        if rectangle:
            pygame.draw.rect(screen, color, rectFunction(prevx, prevy, currx, curry), 2)
        if circle:
            radius = circleFunction(prevx, prevy, currx, curry)
            pygame.draw.circle(screen, color, (prevx, prevy), radius, 2)
        if square:
            pygame.draw.rect(screen, color, squareFunction(prevx, prevy, currx, curry), 2)
        if triangle:
            points = tenqabyrgaly_triangle(prevx, prevy, currx, curry)
            pygame.draw.polygon(screen, color, points, 2)
        if tenqabyrgaly:
            points = tikburyshty_triangle(prevx, prevy, currx, curry)
            pygame.draw.polygon(screen, color, points, 2)
        if romb:
            points = rombFunction(prevx, prevy, currx, curry)
            pygame.draw.polygon(screen, color, points, 2)
    pygame.display.flip()