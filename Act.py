# 用来移动的函数
def tetrimino_move(tetrimino, act):
    # 向左
    if act == 0:
        tetrimino.move(-1, 0)
    # 向右
    elif act == 1:
        tetrimino.move(1, 0)
    # 向下
    elif act == 2:
        tetrimino.move(0, 1)
    # 旋转
    elif act == 3:
        tetrimino.rotate()
    return tetrimino

def map_act(move_left, move_right, move_down, rotate):
    act = -1
    if move_left:
        act2 = 0
    elif move_right:
        act2 = 1
    elif move_down:
        act2 = 2
    elif rotate:
        act2 = 3
    return act