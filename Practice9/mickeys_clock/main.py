import pygame
import sys
from clock import MickeyClock

# Инициализация Pygame
pygame.init()

# Параметры окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mickey's Clock")
clock = pygame.time.Clock()

# Создание часов
mickey_clock = MickeyClock(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Главный игровой цикл
running = True
while running:
    clock.tick(FPS)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    # Очистка экрана
    screen.fill((255, 255, 255))
    
    # Обновление и отрисовка часов
    mickey_clock.update()
    mickey_clock.draw(screen)
    
    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()