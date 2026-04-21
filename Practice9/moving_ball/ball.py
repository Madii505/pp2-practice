import pygame

class Ball:
    """Класс для движущегося мяча"""
    
    def __init__(self, x, y, radius=25, color=(255, 0, 0)):
        """
        Инициализация мяча
        
        Args:
            x: X координата центра мяча
            y: Y координата центра мяча
            radius: Радиус мяча
            color: RGB цвет мяча
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
        # Границы экрана (устанавливаются позже)
        self.min_x = 0
        self.min_y = 0
        self.max_x = 800
        self.max_y = 600
    
    def set_boundaries(self, min_x, min_y, max_x, max_y):
        """
        Установка границ экрана
        
        Args:
            min_x: Минимальная X координата
            min_y: Минимальная Y координата
            max_x: Максимальная X координата
            max_y: Максимальная Y координата
        """
        self.min_x = min_x + self.radius
        self.min_y = min_y + self.radius
        self.max_x = max_x - self.radius
        self.max_y = max_y - self.radius
    
    def move(self, dx, dy):
        """
        Движение мяча с проверкой границ
        
        Args:
            dx: Изменение X координаты
            dy: Изменение Y координаты
        """
        # Вычисление новой позиции
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Проверка границ и обновление позиции
        if self.min_x <= new_x <= self.max_x:
            self.x = new_x
        
        if self.min_y <= new_y <= self.max_y:
            self.y = new_y
    
    def draw(self, surface):
        """
        Отрисовка мяча на поверхность
        
        Args:
            surface: pygame.Surface для отрисовки
        """
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        # Отрисовка границы
        pygame.draw.circle(surface, (0, 0, 0), (self.x, self.y), self.radius, 2)
    
    def get_position(self):
        """
        Получение текущей позиции мяча
        
        Returns:
            Кортеж (x, y)
        """
        return (self.x, self.y)