# 边界类,每一行都有一个set存储该位置是否有块
import Comman
import numpy as np

# 已有方块类
class border:
    def __init__(self):
        self.brd = np.zeros((Comman.ROW + 1, Comman.COLUMN), dtype=int)
        self.brd[Comman.ROW, :] = 1

    def add(self, tetrimino):
        coords = tetrimino.get_coordinates()
        idx = -1
        dep = -1
        for i in range(len(coords)):
            x = coords[i][0]
            y = coords[i][1]
            for j in range(6):
                if i - j <= 0:
                    continue
                if self.brd[x-j][y] == 1:
                    if dep < j:
                        dep = j
                        idx = i
        tetrimino.move(0,dep)
        coords = tetrimino.get_coordinates()
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.brd[x][y] = 1
        self.check()


    # 检查这一行是否完整，能否被消除
    def check(self):
        idx = []
        for i in range(len(self.brd)):
            f = False
            for j in range(len(self.brd[0])):
                if self.brd[i][j] == 0:
                    f = True
                    break
            # 跑完之后，表示这一行满足消除的行条件
            if f:
                idx.append(i)

        sz = len(idx)
        l = []
        for i in range(Comman.ROW):
            l.append(i in idx)

        for i in range(Comman.ROW, 0, -1):
            if l[i]:
                j = i - 1
                while l[j] and j > 0:
                    j -= 1
                if j <= 0:
                    self.brd[i, :] = 0
                else:
                    l[j] = 1
                    self.brd[i] = self.brd[j]




    def get_coordinates(self):
        l = []
        for i in range(len(self.brd)):
            for j in range(len(self.brd[0])):
                if self.brd[i][j] == 1:
                    l.append((i, j))
        return l
