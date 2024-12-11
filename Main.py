import pygame
import random

import Act
import Against
import Border
import Comman
import Draw
import PlayerInput
import Tetrimino
import DangBlock

pygame.init()

# 创建屏幕,为了方便初始碰撞设置，假设开始时最底层是一层方块
screen = pygame.display.set_mode((Comman.SCREEN_WIDTH,Comman.SCREEN_HEIGHT + Comman.BLOCK_SIZE))
pygame.display.set_caption("俄罗斯方块")

# 设置游戏帧率
clock = pygame.time.Clock()

# 随机选择方块
def RDC():
    random.seed()
    return random.randint(0,7)

def tetrimino_act(main, minor, act, border):
    if DangBlock.IsAgainst(main, minor, act):
        return border, main, False
    else :
        if Against.LRAgainst(main, act):
            return border, main, False
        else :
            return Against.UnderAgainst(main, act, border)
# 创建玩家
player1 = Tetrimino.tetrimino((4,1), Comman.RED, RDC())
player2 = Tetrimino.tetrimino((12,1), Comman.BLUE, RDC())

# print(player1.shape)
# print(player1.get_coordinates())
# print(player2.shape)
# print(player2.get_coordinates())

# 用于控制方块的自动下落间隔
fall_counter = 0
# 每20帧自动下落1格
fall_speed = 20

# 创建已有方块类
border = Border.border()


print(border.get_coordinates())
running = True
while running:
    # 填充白色背景
    screen.fill(Comman.WHITE)
    # 画格子（测试版方便调试，后续完善可以考虑删除）
    Draw.draw_grid(screen)
    Draw.draw_border(border, screen)  # 绘制固定方块

    Draw.draw_tetrimino(player1, screen)  # 绘制玩家1的方块
    Draw.draw_tetrimino(player2, screen)  # 绘制玩家2的方块

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # 检测按键按下
            if event.key == pygame.K_LEFT:  # 玩家1左移
                player1 = Act.tetrimino_move(player1, 0)
            elif event.key == pygame.K_RIGHT:  # 玩家1右移
                player1 = Act.tetrimino_move(player1, 1)
            elif event.key == pygame.K_DOWN:  # 玩家1下落
                player1 = Act.tetrimino_move(player1, 2)
            elif event.key == pygame.K_UP:  # 玩家1旋转
                player1 = Act.tetrimino_move(player1, 3)
            elif event.key == pygame.K_a:  # 玩家2左移
                player2 = Act.tetrimino_move(player2, 0)
            elif event.key == pygame.K_d:  # 玩家2右移
                player2 = Act.tetrimino_move(player2, 1)
            elif event.key == pygame.K_s:  # 玩家2下落
                player2 = Act.tetrimino_move(player2, 2)
            elif event.key == pygame.K_w:  # 玩家2旋转
                player2 = Act.tetrimino_move(player2, 3)

    # 自动下落逻辑
    fall_counter += 1
    if fall_counter >= fall_speed:
        fall_counter = 0
        border, player1, IsFix1 = tetrimino_act(player1, player2, 2, border)  # 玩家1下落
        if IsFix1:
            player1 = Tetrimino.tetrimino((4, 1), Comman.RED, RDC())

        border, player2, IsFix2 = tetrimino_act(player2, player1, 2, border)  # 玩家2下落
        if IsFix2:
            player2 = Tetrimino.tetrimino((12, 1), Comman.BLUE, RDC())

    pygame.display.update()
    clock.tick(Comman.FPS)
    # running = False

print("ENDING")