import pygame
import time
import math
import os

class MickeyClock:
    """Класс для отображения часов с руками Микки Мауса"""
    
    def __init__(self, x, y, radius=150):
        """
        Инициализация часов
        
        Args:
            x: X координата центра часов
            y: Y координата центра часов
            radius: Радиус циферблата
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.hand_color = (0, 0, 0)
        self.circle_color = (200, 200, 200)
        
        # Загрузка изображения руки Микки
        self.hand_image = None
        self.load_hand_image()
        
    def load_hand_image(self):
        """Загрузка и масштабирование изображения руки"""
        try:
            # Папка где находится этот скрипт
            script_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(script_dir, "images", "mickey_hand.png")
            
            if os.path.exists(image_path):
                self.hand_image = pygame.image.load(image_path).convert_alpha()
                # Масштабируем изображение до размера 60x100 пикселей
                self.hand_image = pygame.transform.scale(self.hand_image, (60, 100))
                print(f"✓ Изображение загружено: {image_path}")
            else:
                print(f"✗ Файл не найден: {image_path}")
                self.hand_image = None
        except Exception as e:
            print(f"✗ Ошибка загрузки изображения: {e}")
            self.hand_image = None
    
    def get_hand_position(self, angle, hand_length):
        """
        Вычисляет конечную позицию стрелки на основе угла
        
        Args:
            angle: Угол в градусах (0 = вверх, по часовой стрелке)
            hand_length: Длина стрелки
            
        Returns:
            Кортеж (x, y) конечной позиции
        """
        # Преобразование градусов в радианы
        radians = math.radians(angle)
        
        # Вычисление конечной позиции
        end_x = self.x + hand_length * math.sin(radians)
        end_y = self.y - hand_length * math.cos(radians)
        
        return (end_x, end_y)
    
    def update(self):
        """Обновление времени"""
        # Получение текущего времени
        current_time = time.localtime()
        self.minutes = current_time.tm_min
        self.seconds = current_time.tm_sec
    
    def draw(self, surface):
        """
        Отрисовка часов на поверхность
        
        Args:
            surface: pygame.Surface для отрисовки
        """
        # Отрисовка циферблата
        pygame.draw.circle(surface, self.circle_color, (self.x, self.y), self.radius, 3)
        pygame.draw.circle(surface, (0, 0, 0), (self.x, self.y), 8)
        
        # Отрисовка отметок часов
        for i in range(12):
            angle = (i * 30)  # 360 / 12 = 30 градусов на час
            radians = math.radians(angle)
            
            # Длинные отметки
            start_x = self.x + (self.radius - 20) * math.sin(radians)
            start_y = self.y - (self.radius - 20) * math.cos(radians)
            end_x = self.x + (self.radius - 5) * math.sin(radians)
            end_y = self.y - (self.radius - 5) * math.cos(radians)
            
            pygame.draw.line(surface, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)
        
        # Расчет углов для стрелок
        # Минутная стрелка (правая рука) - полный оборот за 60 минут
        minutes_angle = (self.minutes * 6)  # 360 / 60 = 6 градусов на минуту
        
        # Секундная стрелка (левая рука) - полный оборот за 60 секунд
        seconds_angle = (self.seconds * 6)  # 360 / 60 = 6 градусов на секунду
        
        # Если изображение загружено - рисуем его вместо линий
        if self.hand_image:
            self._draw_rotated_image(surface, self.hand_image, minutes_angle, 
                                    self.radius - 50, (255, 0, 0))  # Минутная (красная)
            self._draw_rotated_image(surface, self.hand_image, seconds_angle, 
                                    self.radius - 60, (0, 0, 255))  # Секундная (синяя)
        else:
            # Если нет изображения - рисуем линии
            minutes_end = self.get_hand_position(minutes_angle, self.radius - 30)
            seconds_end = self.get_hand_position(seconds_angle, self.radius - 40)
            
            pygame.draw.line(surface, (255, 0, 0), (self.x, self.y), minutes_end, 4)
            pygame.draw.line(surface, (0, 0, 255), (self.x, self.y), seconds_end, 2)
        
        # Отрисовка времени текстом
        font = pygame.font.Font(None, 36)
        time_text = font.render(f"{self.minutes:02d}:{self.seconds:02d}", True, (0, 0, 0))
        surface.blit(time_text, (self.x - 50, self.y + self.radius + 20))
    
    def _draw_rotated_image(self, surface, image, angle, distance, color_tint=None):
        """
        Рисует повернутое изображение
        
        Args:
            surface: Поверхность для отрисовки
            image: Изображение для отрисовки
            angle: Угол поворота
            distance: Расстояние от центра
            color_tint: Цвет для тонирования (опционально)
        """
        # Поворот изображения
        rotated_image = pygame.transform.rotate(image, -angle)  # Минус потому что pygame поворачивает против часовой
        
        # Получение размеров повернутого изображения
        rect = rotated_image.get_rect()
        
        # Вычисление позиции (конец стрелки)
        end_pos = self.get_hand_position(angle, distance)
        
        # Центрируем изображение в конечной позиции
        rect.center = (int(end_pos[0]), int(end_pos[1]))
        
        # Отрисовка изображения
        surface.blit(rotated_image, rect)