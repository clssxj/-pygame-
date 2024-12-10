import pygame
import random
import Comman
import Draw
import PlayerInput
import Tetrimino
import DangBlock

pygame.init()

# 创建屏幕,为了方便初始碰撞设置，假设开始时最底层是一层方块
screen = pygame.display.set_mode((Comman.SCREEN_WIDTH,Comman.SCREEN_HEIGHT + 1))
pygame.display.set_caption("俄罗斯方块")

# 设置游戏帧率
clock = pygame.time.Clock()

# 随机选择方块
def RDC():
    random.seed()
    return random.randint(0,7)

# 创建玩家
player1 = Tetrimino.tetrimino((4,0),Comman.RED,RDC())
player2 = Tetrimino.tetrimino((12,0),Comman.BLUE,RDC())

# 用于控制方块的自动下落间隔
fall_counter = 0
# 每20帧自动下落1格
fall_speed = 20

running = True
while running:
    # 填充白色背景
    screen.fill(Comman.WHITE)
    # 画格子（测试版方便调试，后续完善可以考虑删除）
    Draw.draw_grid()

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 玩家输入
    key = pygame.key.get_pressed()
    # 玩家一输入
    move_left1, move_right1, move_down1, rotate1 = PlayerInput.Input(key, 1)
    # 玩家二输入
    move_left2, move_right2, move_down2, rotate2 = PlayerInput.Input(key, 2)

    # 存储动作
    act1, act2 = -1, -1
    if move_left1:
        act1 = 0
    elif move_right1:
        act1 = 1
    elif move_down1:
        act1 = 2
    elif rotate1:
        act1 = 3

    if move_left2:
        act2 = 0
    elif move_right2:
        act2 = 1
    elif move_down2:
        act2 = 2
    elif rotate2:
        act2 = 3

    # 先判定悬空方块是否碰撞，在悬空方块碰撞判定完之后判定与左右边界值碰撞，最后判定与下界碰撞
    DangBlock.IsAgainst(player1, player2, act1, act2)

