import pygame
from datetime import datetime #для получение текущего времени

pygame.init() #Инициализация Pygame
screen = pygame.display.set_mode((1400, 1050)) #Screen settings

bg_image = pygame.image.load('images/mainclock.png') #loading background
sec_img = pygame.image.load('images/leftarm.png') #loading leftarm-second arm
min_img = pygame.image.load('images/rightarm.png') #loading rightarm-minute arm


rect = bg_image.get_rect(center=(700, 525)) #определение центра часов

process = True
while process :
    screen.blit(bg_image, (0, 0))
    #exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False

    time = datetime.now().time() #для получение текущего времени
    angle_sec = -(time.second * 6) #360/60 = 6 бұрышты алу үшін
    sec_in_img = pygame.transform.rotate(sec_img, angle_sec)
    sec_rect = sec_in_img.get_rect(center=rect.center) #центрді реттеу
    screen.blit(sec_in_img, sec_rect.topleft)

    min_angle = -(time.minute * 6) #min_angle
    nmin_img = pygame.transform.rotate(min_img, min_angle) #для поворота изображение на заданный угол
    min_rect = nmin_img.get_rect(center=rect.center)  #центрді реттеу
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()





#sec - min , min - hour


#time = datetime.now().time()
    #hour_angle = -(time.minute * 6)  # Поворачиваем часовую стрелку на количество минут
    #hour_in_img = pygame.transform.rotate(hour_img, hour_angle)
    #hour_rect = hour_in_img.get_rect(center=rect.center)
    #screen.blit(hour_in_img, hour_rect.topleft)

    #min_angle = -(time.second * 6)  # Поворачиваем минутную стрелку на количество секунд
    #min_in_img = pygame.transform.rotate(min_img, min_angle)
    #min_rect = min_in_img.get_rect(center=rect.center)
    #screen.blit(min_in_img, min_rect.topleft)