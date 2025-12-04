import random
import pygame
import sys

ROWS, COLS = 64, 64
COLS_OFFSET = COLS // 2
TILE_SIZE = 8
FPS = 24
MAX_HEAT_VALUE = 24

pygame.init()
pygame.display.set_caption("Fire Simulation by lmToT27")
screen = pygame.display.set_mode((COLS * TILE_SIZE, ROWS * TILE_SIZE))
clock = pygame.time.Clock()

def GetFireGradient(steps):
    palette = []
    
    color0 = pygame.Color(183, 232, 235)
    color1 = pygame.Color(17, 101, 193)
    color2 = pygame.Color(4, 63, 152)
    color3 = pygame.Color(0, 0, 0)
    
    part = steps // 3
    
    for i in range(part):
        palette.append(color0.lerp(color1, i / part))
        
    for i in range(part):
        palette.append(color1.lerp(color2, i / part))
        
    part = steps - 2 * part
    for i in range(part + 1):
        palette.append(color2.lerp(color3, i / part))
        
    return palette[::-1]

color = GetFireGradient(MAX_HEAT_VALUE)
heat_value = [[0] * (COLS + COLS_OFFSET) for _ in range(ROWS)]

def DisplayFire():
    for i in range(ROWS):
        for j in range(COLS + COLS_OFFSET):
            rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color[heat_value[i][j]], rect)

def SpreadFire(x, y):
    cur_hval = heat_value[x][y]

    if cur_hval == 0: 
        heat_value[x - 1][y] = 0
    else:
        rd = random.randint(0, 3)
        nxt_x = x - 1
        nxt_y = y - rd + 1
        if 0 <= nxt_y < COLS + COLS_OFFSET:
            heat_value[nxt_x][nxt_y] = max(0, cur_hval - (rd & 1))

def SimulatingFire():
    for x in range(1, ROWS):
        for y in range(COLS + COLS_OFFSET):
            SpreadFire(x, y)

running = True
heat_value[ROWS - 1] = [MAX_HEAT_VALUE for _ in range(COLS + COLS_OFFSET)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SimulatingFire()
    screen.fill((0, 0, 0))
    DisplayFire()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()