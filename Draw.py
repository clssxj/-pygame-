import pygame
import Comman

# 游戏网格
def draw_grid(screen):
    for x in range(Comman.BLOCK_SIZE, Comman.SCREEN_WIDTH, Comman.BLOCK_SIZE):
        pygame.draw.line(screen, Comman.BLACK, (x, 0), (x, Comman.SCREEN_HEIGHT))
    for y in range(0, Comman.SCREEN_HEIGHT + Comman.BLOCK_SIZE, Comman.BLOCK_SIZE):
        pygame.draw.line(screen, Comman.BLACK, (0, y), (Comman.SCREEN_WIDTH, y))

# 绘制Tetrimino
def draw_tetrimino(tetrimino, screen):
    for coord in tetrimino.get_coordinates():
        x = coord[0]
        y = coord[1]
        pygame.draw.rect(screen, tetrimino.clr, pygame.Rect(x * Comman.BLOCK_SIZE, y * Comman.BLOCK_SIZE, Comman.BLOCK_SIZE, Comman.BLOCK_SIZE))

# 绘制已有方块类
def draw_border(border, screen):
    for coord in border.get_coordinates():
        x = coord[0]
        y = coord[1]
        pygame.draw.rect(screen, Comman.CYAN, pygame.Rect(y * Comman.BLOCK_SIZE, x * Comman.BLOCK_SIZE, Comman.BLOCK_SIZE, Comman.BLOCK_SIZE))