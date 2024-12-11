import pygame
import Comman
import Draw
import DangBlock
import Border

'''
方块类
悬空方块判定：
两个方块都是两个独立的个体，当两个方块碰撞，操作无效
方块设定：
方块选择使用random.choice，保证每次刷新出来的方块不同
用字典映射每种方块
对于每种方块，采取用数组存储其旋转的形状
每次方块固定完之后，依据玩家id重新生成方块
旋转时中心旋转
'''
class tetrimino:
    # 初始化方块，初始位置，颜色，形状
    def __init__(self, stp, clr, sid):
        self.clr = clr
        self.x, self.y = stp
        self.sid = sid
        self.shape = Comman.SHAPES.get(sid)
        self.rid = 0
        self.cx = self.x + len(self.shape[0]) // 2  # 计算旋转中心x坐标
        self.cy = self.y + len(self.shape) // 2  # 计算旋转中心y坐标
        self.isMain = -1

    # 旋转方块
    def rotate(self):
        # 旋转前，获取当前形状
        new_shape = Comman.ROTATE_SHAPE[self.sid][(self.rid + 1) % len(Comman.ROTATE_SHAPE[self.sid])]

        # 更新方块的形状和旋转状态
        self.rid = (self.rid + 1) % len(Comman.ROTATE_SHAPE[self.sid])  # 更新旋转次数
        self.shape = new_shape  # 更新方块形状


    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # 获取这个方块每个格子的左上角坐标
    def get_coordinates(self):
        coords = []
        # 获得一个二维数组
        now_shape = Comman.ROTATE_SHAPE[self.sid][self.rid]
        for i in range(len(now_shape)):
            for j in range(len(now_shape[i])):
                if now_shape[i][j] == 1:
                    coords.append((i + self.x, j + self.y))

        return coords