import copy

import Comman
import Tetrimino
import pygame
import Border
import Act

# 判断与底线碰撞判定
def UnderAgainst(tetrimino, act, border):
    tetrimino = Act.tetrimino_move(tetrimino, act)
    coords = tetrimino.get_coordinates()
    for coord in coords:
        x = coord[0]
        y = coord[1]
        if border.brd[x][y] == 1:
            # 这里面主要是为了更改border
            border.add(tetrimino)
            return border, tetrimino, True

    return border, tetrimino, False

# 判断与边界碰撞判定
def LRAgainst(tetrimino, act):
    temp = copy.deepcopy(tetrimino)
    Act.tetrimino_move(temp, act)
    coords = temp.get_coordinates()
    for coord in coords:
        # 判定左边界
        if coord[0] < 0 or coord[0] >= Comman.SCREEN_WIDTH:
            return True
    return False
