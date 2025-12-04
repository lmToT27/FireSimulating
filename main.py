import random
import pygame
import sys

SCREEN_SIZE = (600, 400) # WIDTH / HEIGHT
TILE_SIZE = 20
ROWS, COLS = (SCREEN_SIZE[1] + TILE_SIZE - 1) // TILE_SIZE, (SCREEN_SIZE[0] + TILE_SIZE - 1) // TILE_SIZE
print(ROWS, COLS)
FPS = 24

MAX_HEAT_VALUE = 36
MAX_HEAT_INDEX = 12

pygame.init()
pygame.display.set_caption("Fire Simulation by lmToT27")
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

def GetFireGradient(steps):
    palette = []
    
    white = pygame.Color(255, 255, 255)
    yellow = pygame.Color(255, 255, 0)
    red = pygame.Color(255, 0, 0)
    black = pygame.Color(0, 0, 0)
    
    part = steps // 3
    
    for i in range(part):
        palette.append(white.lerp(yellow, i / part))
        
    for i in range(part):
        palette.append(yellow.lerp(red, i / part))
        
    part = steps - 2 * part
    for i in range(part):
        palette.append(red.lerp(black, i / part))
        
    return palette

color = GetFireGradient(MAX_HEAT_INDEX)

def DisplayFire():
    for i in range(ROWS):
        for j in range(COLS):
            x = (COLS - j - 1) * TILE_SIZE
            y = (ROWS - i - 1) * TILE_SIZE
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color[heat_value[i][j] // MAX_HEAT_VALUE], rect)
            
heat_value = [[15] * COLS] * ROWS

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#000000")
    DisplayFire()
    pygame.display.update()

pygame.quit()
sys.exit()