# 边界类,每一行都有一个set存储该位置是否有块
import Comman

# 已有方块类
class border:
    def __init__(self):
        self.brd = [set() for _ in range(20)]
        self.brd[0] = set([(x, Comman.SCREEN_HEIGHT) for x in range(0,Comman.SCREEN_WIDTH,Comman.BLOCK_SIZE)])

    def add(self, tetrimino):


    def check(self):
