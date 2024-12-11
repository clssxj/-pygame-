import pygame


def Input(keys, pid):
    move_left = keys[pygame.K_LEFT] if pid == 1 else keys[pygame.K_a]
    move_right = keys[pygame.K_RIGHT] if pid == 1 else keys[pygame.K_d]
    move_down = keys[pygame.K_DOWN] if pid == 1 else keys[pygame.K_s]
    rotate = keys[pygame.K_UP] if pid == 1 else keys[pygame.K_w]

    if move_left or move_right or move_down or rotate:
        print(f"PID: {pid}, Left: {move_left}, Right: {move_right}, Down: {move_down}, Rotate: {rotate}")
    return move_left, move_right, move_down, rotate