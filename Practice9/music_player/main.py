import pygame
import sys
from player import MusicPlayer

# Инициализация Pygame
pygame.init()

# Параметры окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

# Создание плеера
player = MusicPlayer("music")

# Главный игровой цикл
running = True
while running:
    clock.tick(FPS)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                player.play()
            elif event.key == pygame.K_s:  # Stop
                player.stop()
            elif event.key == pygame.K_n:  # Next
                player.next_track()
            elif event.key == pygame.K_b:  # Back/Previous
                player.previous_track()
            elif event.key == pygame.K_q:  # Quit
                running = False
    
    # Очистка экрана
    screen.fill((30, 30, 30))
    
    # Отрисовка информации плеера
    player.draw(screen)
    
    # Обновление экрана
    pygame.display.flip()

player.stop()
pygame.quit()
sys.exit()