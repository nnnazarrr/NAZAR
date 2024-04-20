import pygame
from datetime import datetime 
import math

RES = WIDTH, HEIGHT = 900, 800
H_WIDTH, H_HEIGHT = WIDTH//2, HEIGHT//2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS-85}
pygame.init()
bg = pygame.image.load('cl.png')
surface = pygame.display.set_mode((RES))
pygame.display.set_caption("Clock")

clock = pygame.time.Clock()

clock12 = dict(zip(range(12), range(0, 360, 30)))  
clock60 = dict(zip(range(60), range(0, 360, 6))) 

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand])-math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand])-math.pi / 2)
    return x, y
font = pygame.font.SysFont('Verdana', 60)


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()
    
    surface.fill(pygame.Color('black'))
    t = datetime.now()
    hour, minute, second = t.hour%12, t.minute, t.second
    surface.blit(bg,(128,72))
    pygame.draw.line(surface, pygame.Color('red'),  (H_WIDTH, H_HEIGHT), get_clock_pos(clock12, hour, 'hour'), 10)
    pygame.draw.line(surface, pygame.Color('orange'),  (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 6)
    pygame.draw.line(surface, pygame.Color('blue'),  (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 3)
    pygame.draw.circle(surface, pygame.Color('White'), (H_WIDTH, H_HEIGHT), 8)
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('green'), pygame.Color('orange'))
    surface.blit(time_render, (0,0))
    pygame.display.flip()
    clock.tick(20)
