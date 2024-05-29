import pygame
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((900 , 512)) #size of display
pygame.display.set_caption("Player") #the name of display
player = pygame.image.load("ex2/images/player.jpg") #main object
process = True #for cycle "for"
playlist = ["ex2/music/music1.mp3", "ex2/music/music2.mp3" , "ex2/music/music3.mp3"] #list of musics
index_of_playlist = 0
def play_music():
    pygame.mixer.music.load(playlist[index_of_playlist])
    pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.stop()
def next_track():
    global index_of_playlist
    index_of_playlist = (index_of_playlist + 1) % len(playlist)
    play_music()
def previous_track():
    global index_of_playlist
    index_of_playlist = (index_of_playlist - 1) % len(playlist)
    play_music()
while process :
    pygame.display.update()
    screen.blit(player , (0 , 0))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            process = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_TAB:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()

pygame.display.flip()
clock.tick(10)
pygame.quit()