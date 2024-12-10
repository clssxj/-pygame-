import Comman
import Tetrimino
import Against

"""
本类主要作用为判定悬空中的方块的体积碰撞问题，主要为判定一个主体和一个碰撞体，假设两个物体一起移动，如果主体移动合法，则先移动主体位置，不然就移动碰撞体位置
主要判定方向为左边和上边，规定中心在上面或者中心在左边的方块为主体。
"""
def CertainMain(tetrimino1, tetrimino2):
    crood1 = tetrimino1.get_coordinates()
    crood2 = tetrimino2.get_coordinates()

    # 找到每一个方块的边界值
    left_side1 = (Comman.MAXINT,0)
    right_side1 = (Comman.MININT,0)
    up_side1 = (0, Comman.MININT)
    down_side1 = (0, Comman.MAXINT)
    for i in range(0,len(crood1)):
        if crood1[i][0] < left_side1[0]:
            left_side1 = crood1[i]
        if crood1[i][0] > right_side1[0]:
            right_side1 = crood1[i]
        if crood1[i][1] < down_side1[1]:
            down_side1 = crood1[i]
        if crood1[i][1] > up_side1[1]:
            up_side1 = crood1[i]

    left_side2 = (Comman.MAXINT, 0)
    right_side2 = (Comman.MININT, 0)
    up_side2 = (0, Comman.MININT)
    down_side2 = (0, Comman.MAXINT)
    for i in range(0, len(crood2)):
        if crood2[i][0] < left_side2[0]:
            left_side2 = crood2[i]
        if crood2[i][0] > right_side2[0]:
            right_side2 = crood2[i]
        if crood2[i][1] < down_side2[1]:
            down_side2 = crood2[i]
        if crood2[i][1] > up_side2[1]:
            up_side2 = crood2[i]


    if :
        UnderAgainst(main, minor)
    elif :
        LeftAgainst(main, minor)

def UnderAgainst(main, minor):


def LeftAgainst(main, minor):


def IsAgainst(tetrimino1, tetrimino2, act1, act2):
    CertainMain(tetrimino1, tetrimino2, act1, act2)