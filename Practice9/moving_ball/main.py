import pygame
import sys
from ball import Ball

# Инициализация Pygame
pygame.init()

# Параметры окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Moving Ball Game")
clock = pygame.time.Clock()

# Создание мяча
ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, radius=25)
ball.set_boundaries(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

# Главный игровой цикл
running = True
while running:
    clock.tick(FPS)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move(0, -20)
            elif event.key == pygame.K_DOWN:
                ball.move(0, 20)
            elif event.key == pygame.K_LEFT:
                ball.move(-20, 0)
            elif event.key == pygame.K_RIGHT:
                ball.move(20, 0)
            elif event.key == pygame.K_q:
                running = False
    
    # Очистка экрана (белый фон)
    screen.fill((255, 255, 255))
    
    # Отрисовка мяча
    ball.draw(screen)
    
    # Отрисовка подсказок
    font = pygame.font.Font(None, 24)
    hint_text = font.render("Use arrow keys to move | Q to quit", True, (0, 0, 0))
    screen.blit(hint_text, (10, 10))
    
    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()