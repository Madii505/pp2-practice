import pygame
import sys
from racer import game_loop
from ui import menu_loop, leaderboard_screen, settings_screen

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

while True:
    action = menu_loop(screen)

    if action == "play":
        game_loop(screen)
    elif action == "leaderboard":
        leaderboard_screen(screen)
    elif action == "settings":
        settings_screen(screen)
    elif action == "quit":
        pygame.quit()
        sys.exit()