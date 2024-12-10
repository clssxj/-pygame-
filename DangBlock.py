import copy

import Act
import Comman
import Tetrimino
import Against

"""
本类主要作用为判定悬空中的方块的体积碰撞问题，主要为判定一个主体和一个碰撞体，假设两个物体一起移动，如果主体移动合法，则先移动主体位置，不然就移动碰撞体位置
主要判定方向为左边和上边，规定中心在上面或者中心在左边的方块为主体。
"""
# 判断坐标有没有重合
def IsSame(tetrimino1, tetrimino2):
    coord1 = tetrimino1.get_coordinates()
    coord2 = tetrimino2.get_coordinates()
    for coord in coord1:
        if coord in coord2:
            return True
    return False



def CalcSide(tetrimino):
    # 找到每一个方块的边界值
    crood = tetrimino.get_coordinates()
    left_side = (Comman.MAXINT, 0)
    right_side = (Comman.MININT, 0)
    up_side = (0, Comman.MININT)
    down_side = (0, Comman.MAXINT)
    for i in range(0, len(crood)):
        if crood[i][0] < left_side[0]:
            left_side = crood[i]
        if crood[i][0] > right_side[0]:
            right_side = crood[i]
        if crood[i][1] < down_side[1]:
            down_side = crood[i]
        if crood[i][1] > up_side[1]:
            up_side = crood[i]
    return left_side, right_side, up_side, down_side

def CertainMain(main, minor, act):
    temp = copy.deepcopy(main)
    temp = Act.tetrimino_move(temp, act)
    return IsSame(temp, minor)


def IsAgainst(main, minor, act):
    return CertainMain(main, minor, act)