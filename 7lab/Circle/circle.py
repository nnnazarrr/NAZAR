import pygame 

WIDTH = 600
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SPEED = 20
RADIUS = 25
X = 100
Y = 100

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (103, 235, 158)


clock = pygame.time.Clock()

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        Y = max(RADIUS, Y - SPEED)
    if pressed[pygame.K_DOWN]:
        Y = min(HEIGHT - RADIUS, Y + SPEED)
    if pressed[pygame.K_LEFT]: 
        X = max(RADIUS, X - SPEED)
    if pressed[pygame.K_RIGHT]:
        X = min(WIDTH - RADIUS, X + SPEED)
    else: 
        color =  BLACK
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (X, Y), RADIUS)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()