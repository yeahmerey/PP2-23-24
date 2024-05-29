import pygame
pygame.init()

#screen Settings
screen_width , screen_height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game")

#variables
radius_of_ball = 25
x_plane = (screen_width - radius_of_ball * 2) // 2
y_plane = (screen_height - radius_of_ball * 2) // 2
speed_of_ball = 50

process = True
while process:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_plane = max(0, y_plane - speed_of_ball)
            elif event.key == pygame.K_DOWN:
                y_plane = min(screen_height - radius_of_ball * 2, y_plane + speed_of_ball)
            elif event.key == pygame.K_LEFT:
                x_plane = max(0, x_plane - speed_of_ball)
            elif event.key == pygame.K_RIGHT:
                x_plane = min(screen_width - radius_of_ball * 2, x_plane + speed_of_ball)
    screen.fill("white")
    pygame.draw.circle(screen, "red" , (x_plane + radius_of_ball, y_plane + radius_of_ball), radius_of_ball)

    pygame.display.flip()
pygame.quit()
