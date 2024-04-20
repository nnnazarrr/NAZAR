import pygame 
import os 

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 800
HEIGHT = 600
CENTER = (WIDTH / 2, HEIGHT / 2)

BUTTON = 50
 
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption('Binary')
bg_image = pygame.image.load(os.path.normpath('bg.png'))

bg_mus = pygame.image.load('skr.png')
bg_x = WIDTH - 835
bg_y = 0

play_button = pygame.transform.scale(pygame.image.load('start.png'), (BUTTON, BUTTON))
pause_button = pygame.transform.scale(pygame.image.load('pause.png'), (BUTTON, BUTTON))

current_song_index = 0
SONGS = ['mus/1.mp3', 'mus/2.mp3', 'mus/3.mp3']
pygame.mixer.music.load(os.path.normpath(SONGS[current_song_index]))
pygame.mixer.music.play()

SIZE_OF_ALBOM = 250
album_cover = pygame.transform.scale(pygame.image.load('skr.png'), (SIZE_OF_ALBOM, SIZE_OF_ALBOM))

play = True 
x = 0
font = pygame.font.SysFont('arial', 40)

runnng = True 
while runnng: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnng = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        play = not play 
        if play: 
            pygame.mixer.music.unpause()
        else: 
            pygame.mixer.music.pause()
    
    if pressed[pygame.K_LEFT]:
        current_song_index = (current_song_index - 1)%len(SONGS)
        pygame.mixer.music.load(SONGS[current_song_index])
        pygame.mixer.music.play()
        play = True
        x = 0
        album_cover = pygame.transform.scale(pygame.image.load('skr.png'), (SIZE_OF_ALBOM, SIZE_OF_ALBOM))

    if pressed[pygame.K_RIGHT]:
        current_song_index = (current_song_index + 1)%len(SONGS)
        pygame.mixer.music.load(SONGS[current_song_index])
        pygame.mixer.music.play()
        play = True
        x = 0
        album_cover = pygame.transform.scale(pygame.image.load('skr.png'), (SIZE_OF_ALBOM, SIZE_OF_ALBOM))

    game_display.fill(WHITE)
    game_display.blit(bg_image, (bg_x, bg_y))
    text = font.render(SONGS[current_song_index][6:-4], True, BLACK)
    game_display.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    game_display.blit(album_cover, (WIDTH // 2 -  SIZE_OF_ALBOM // 2, 65))

    pygame.draw.rect(game_display, (192, 192, 192), (WIDTH // 2 - SIZE_OF_ALBOM // 2, 342, SIZE_OF_ALBOM , 11))
    if play:
        x += 0.1
        if x > SIZE_OF_ALBOM:
            x = 0
    pygame.draw.rect(game_display, (0, 0, 255), (WIDTH // 2 - SIZE_OF_ALBOM // 2, 342, x, 11))
    
    BUTTON_X = 367
    BUTTON_Y = WIDTH - 350

    if play:
        game_display.blit(pause_button, (BUTTON_X, BUTTON_Y))
    else:
        game_display.blit(play_button, (BUTTON_X, BUTTON_Y))
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()