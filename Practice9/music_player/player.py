import pygame
import os
from pathlib import Path

class MusicPlayer:
    """Класс музыкального плеера с управлением с клавиатуры"""
    
    def __init__(self, music_folder="music"):
        """
        Инициализация плеера
        
        Args:
            music_folder: Папка с музыкальными файлами (относительная или абсолютная)
        """
        pygame.mixer.init()
        
        # Получение полного пути к папке с музыкой
        if os.path.isabs(music_folder):
            self.music_folder = music_folder
        else:
            # Если путь относительный - ищем от папки где находится этот скрипт
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.music_folder = os.path.join(script_dir, music_folder)
        
        print(f"Папка с музыкой: {self.music_folder}")
        print(f"Папка существует: {os.path.exists(self.music_folder)}")
        
        self.playlist = self._load_playlist()
        self.current_track_index = 0
        self.is_playing = False
        
        if self.playlist:
            print(f"✓ Найдено {len(self.playlist)} треков")
            for i, track in enumerate(self.playlist):
                print(f"  {i+1}. {os.path.basename(track)}")
            pygame.mixer.music.load(self.playlist[0])
        else:
            print("✗ Треки не найдены!")
    
    def _load_playlist(self):
        """
        Загрузка списка треков из папки
        
        Returns:
            Список путей к аудиофайлам
        """
        if not os.path.exists(self.music_folder):
            print(f"✗ Папка не существует: {self.music_folder}")
            os.makedirs(self.music_folder)
            return []
        
        # Поддерживаемые форматы
        supported_formats = ('.mp3', '.wav', '.ogg', '.flac')
        
        tracks = []
        try:
            for file in sorted(os.listdir(self.music_folder)):
                full_path = os.path.join(self.music_folder, file)
                
                # Проверяем что это файл (не папка)
                if os.path.isfile(full_path):
                    if file.lower().endswith(supported_formats):
                        tracks.append(full_path)
                        print(f"  Найден трек: {file}")
        except Exception as e:
            print(f"✗ Ошибка при чтении папки: {e}")
        
        return tracks
    
    def play(self):
        """Воспроизведение текущего трека"""
        if not self.playlist:
            print("✗ Плейлист пуст!")
            return
        
        if not self.is_playing:
            try:
                pygame.mixer.music.load(self.playlist[self.current_track_index])
                pygame.mixer.music.play()
                self.is_playing = True
                print(f"▶ Воспроизведение: {os.path.basename(self.playlist[self.current_track_index])}")
            except Exception as e:
                print(f"✗ Ошибка воспроизведения: {e}")
        else:
            # Возобновление воспроизведения
            pygame.mixer.music.unpause()
            print("▶ Возобновлено")
    
    def stop(self):
        """Остановка воспроизведения"""
        pygame.mixer.music.pause()
        self.is_playing = False
        print("⏸ Остановлено")
    
    def next_track(self):
        """Переход на следующий трек"""
        if not self.playlist:
            return
        
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        
        if self.is_playing:
            try:
                pygame.mixer.music.load(self.playlist[self.current_track_index])
                pygame.mixer.music.play()
                print(f"⏭ Следующий: {os.path.basename(self.playlist[self.current_track_index])}")
            except Exception as e:
                print(f"✗ Ошибка: {e}")
    
    def previous_track(self):
        """Переход на предыдущий трек"""
        if not self.playlist:
            return
        
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        
        if self.is_playing:
            try:
                pygame.mixer.music.load(self.playlist[self.current_track_index])
                pygame.mixer.music.play()
                print(f"⏮ Предыдущий: {os.path.basename(self.playlist[self.current_track_index])}")
            except Exception as e:
                print(f"✗ Ошибка: {e}")
    
    def draw(self, surface):
        """
        Отрисовка информации плеера
        
        Args:
            surface: pygame.Surface для отрисовки
        """
        # Шрифты
        title_font = pygame.font.Font(None, 48)
        info_font = pygame.font.Font(None, 32)
        controls_font = pygame.font.Font(None, 24)
        
        # Заголовок
        title = title_font.render("Music Player", True, (255, 255, 255))
        surface.blit(title, (150, 50))
        
        # Информация о треке
        if self.playlist:
            track_name = os.path.basename(self.playlist[self.current_track_index])
            track_info = info_font.render(f"Track {self.current_track_index + 1}/{len(self.playlist)}", 
                                         True, (100, 200, 255))
            track_display = info_font.render(track_name, True, (200, 255, 100))
            
            surface.blit(track_info, (150, 150))
            surface.blit(track_display, (150, 200))
        else:
            no_tracks = info_font.render("No tracks found in music folder", True, (255, 100, 100))
            surface.blit(no_tracks, (150, 150))
        
        # Статус
        status = "▶ PLAYING" if self.is_playing else "⏸ STOPPED"
        status_color = (100, 255, 100) if self.is_playing else (255, 100, 100)
        status_text = info_font.render(status, True, status_color)
        surface.blit(status_text, (150, 300))
        
        # Управление
        controls = [
            "P - Play/Resume",
            "S - Stop",
            "N - Next Track",
            "B - Previous Track",
            "Q - Quit"
        ]
        
        y_offset = 400
        for control in controls:
            control_text = controls_font.render(control, True, (200, 200, 200))
            surface.blit(control_text, (150, y_offset))
            y_offset += 35