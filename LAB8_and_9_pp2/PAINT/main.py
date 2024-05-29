import sys
import math
import pygame
pygame.init() #Initialize pygame

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MENU_GRAY = (224, 224, 224)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

painting = []
Leftmouse = False
right_triangle = False
romb = False

clock = pygame.time.Clock() #for use fps
FPS = 60 #Set Frames per second

main_color = (0, 0, 0)
active_figure = 0
eraser_image = pygame.image.load("Eraser.png")
main_icon = pygame.image.load("paint.png")


#Set SCREEN
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("PAINT")

Add_SCREEN = pygame.Surface((WIDTH, HEIGHT))

def drawMENU():
    pygame.draw.rect(SCREEN, MENU_GRAY, [0, 0, WIDTH, 120])
    pygame.draw.line(SCREEN, 'gray', [0, 120], [WIDTH, 120])

    # Figure menu:
    rect_back = [pygame.draw.rect(SCREEN, WHITE, [10, 10, 80, 80]), 0]
    pygame.draw.rect(SCREEN, "GRAY", [20, 20, 60, 60])
    circle_back = [pygame.draw.rect(SCREEN, WHITE, [100, 10, 80, 80]), 1]
    pygame.draw.circle(SCREEN, 'GRAY', [140, 50], 30)
    triangle_back = [pygame.draw.rect(SCREEN, WHITE, [200, 10, 80, 80]), 2]
    pygame.draw.polygon(SCREEN, 'GRAY', [(240, 15), (270, 75), (210, 75)], 10)


    figure_menu = [rect_back, circle_back, triangle_back]

    # Color menu: / draw each color
    blue = [pygame.draw.rect(SCREEN, BLUE, [WIDTH - 60, 35, 25, 25]), BLUE]
    red = [pygame.draw.rect(SCREEN, RED, [WIDTH - 85, 10, 25, 25]), RED]
    green = [pygame.draw.rect(SCREEN, GREEN, [WIDTH - 85, 35, 25, 25]), GREEN]
    yellow = [pygame.draw.rect(SCREEN, YELLOW, [WIDTH - 35, 10, 25, 25]), YELLOW]
    black = [pygame.draw.rect(SCREEN, BLACK, [WIDTH - 35, 35, 25, 25]), BLACK]
    purple = [pygame.draw.rect(SCREEN, PURPLE, [WIDTH - 60, 10, 25, 25]), PURPLE]

    # Eraser
    eraser = [pygame.draw.rect(SCREEN, WHITE, [WIDTH - 200, 10, 55, 55]), WHITE]
    color_menu = [blue, red, green, yellow, black, purple, eraser]
    return color_menu, figure_menu

def tikburyshty_triangle(x1,y1,x2,y2):
    sol_zhak = [x1,y1]
    on_zhak = [x1-(x2-x1),y1+(x2-x1)*math.sqrt(3)]
    asty = [x2,y1+(x2-x1)*math.sqrt(3),]
    points = [sol_zhak,on_zhak,asty]
    return points
# romb
def rombFunction(x1, y1, x2, y2):
    sol_zhak = [x1,y1]
    on_zhak = [x2,y2]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    diagonal = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 / 2
    asty = [x -diagonal, y]
    en_asty = [x + diagonal, y]
    points = [sol_zhak, asty, on_zhak, en_asty]
    return points

def draw_PAINT(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(SCREEN, paint[0], paint[1], 15)  # Draw Paint
        if paint[2] == 0:
            pygame.draw.rect(SCREEN, paint[0], [paint[1][0] - 15, paint[1][1] - 15, 30, 30])  # Draw Paint
        if paint[2] == 2:
            pygame.draw.polygon(SCREEN, paint[0], (
                (paint[1][0] - 10, paint[1][1] + 10), (paint[1][0], paint[1][1] - 10),
                (paint[1][0] + 10, paint[1][1] + 10)))

def draw():
    global main_color, active_figure, mouse
    if mouse[1] > 125 and active_figure !=0:
        if active_figure == 0:
            pygame.draw.rect(SCREEN, main_color, [mouse[0] - 15, mouse[1] - 15, 30, 30])  # Draw
        if active_figure == 1:
            pygame.draw.circle(SCREEN, main_color, mouse, 15)
        if active_figure == 2:
            pygame.draw.polygon(SCREEN, main_color, ((mouse[0] - 10, mouse[1] + 10), (mouse[0], mouse[1] - 10), (mouse[0] + 10, mouse[1] + 10)))

process = True
while process:
    clock.tick(FPS)
    SCREEN.fill(WHITE)
    colors , figure = drawMENU()
    mouse = pygame.mouse.get_pos()
    SCREEN.blit(eraser_image, (605, 15))
    SCREEN.blit(main_icon, (400, 20))
    draw()


    click = pygame.mouse.get_pressed()[0]
    if click and mouse[1] > 100:
        painting.append((main_color, mouse, active_figure))
    draw_PAINT(painting)

    for event in pygame.event.get():  # Set quit event
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:  # Set quit event
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYDOWN:  # Set quit event
            if event.key == pygame.K_SPACE:
                painting = []

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Leftmouse = True
            prevx = event.pos[0]
            prevy = event.pos[1]
        # last point
        if Leftmouse:
            currx = event.pos[0]
            curry = event.pos[1]

        if event.type == pygame.KEYDOWN: #addition figures
            if event.key == pygame.K_1:
                right_triangle =  True
                romb = False
            if event.key == pygame.K_2:
                right_triangle = False
                romb = True
            if event.type == pygame.K_q:
                main_color = BLACK
            if event.key == pygame.K_b:
                main_color = BLUE
            if event.key == pygame.K_y:
                main_colorcolor = YELLOW
            if event.key == pygame.K_r:
                main_color = RED
            if event.key == pygame.K_g:
                main_color = GREEN
            if event.key == pygame.K_p:
                main_color = PURPLE
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            Leftmouse = False
            if right_triangle:
                points = tikburyshty_triangle(prevx , prevy , currx , curry)
                pygame.draw.polygon(SCREEN, main_color , points, 2)
            if romb:
                points = rombFunction(prevx , prevy, currx, curry)
                pygame.draw.polygon(SCREEN, main_color, points, 2)


        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    main_color = i[1]
            for i in figure:
                if i[0].collidepoint(event.pos):
                    active_figure = i[1]

    pygame.display.flip()