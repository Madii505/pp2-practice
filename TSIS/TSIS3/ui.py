import pygame
import sys
from persistence import load_scores, load_settings, save_settings

def menu_loop(screen):
    font = pygame.font.SysFont(None, 50)

    while True:
        screen.fill((0,0,0))

        screen.blit(font.render("PLAY (P)", True, (255,255,255)), (200,200))
        screen.blit(font.render("LEADERBOARD (L)", True, (255,255,255)), (200,300))
        screen.blit(font.render("SETTINGS (S)", True, (255,255,255)), (200,400))
        screen.blit(font.render("QUIT (Q)", True, (255,255,255)), (200,500))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p: return "play"
                if e.key == pygame.K_l: return "leaderboard"
                if e.key == pygame.K_s: return "settings"
                if e.key == pygame.K_q: return "quit"


def leaderboard_screen(screen):
    font = pygame.font.SysFont(None, 40)
    scores = load_scores()

    while True:
        screen.fill((0,0,0))

        y = 100
        for i, s in enumerate(scores[:10]):
            text = f"{i+1}. {s['name']} {s['score']} {s['distance']}"
            screen.blit(font.render(text, True, (255,255,255)), (100,y))
            y += 40

        screen.blit(font.render("BACK (ESC)", True, (255,255,255)), (100,600))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return


def settings_screen(screen):
    font = pygame.font.SysFont(None, 40)
    settings = load_settings()

    while True:
        screen.fill((0,0,0))

        screen.blit(font.render(f"Sound: {settings['sound']} (S)", True, (255,255,255)), (100,200))
        screen.blit(font.render(f"Difficulty: {settings['difficulty']} (D)", True, (255,255,255)), (100,300))
        screen.blit(font.render("BACK (ESC)", True, (255,255,255)), (100,500))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s:
                    settings["sound"] = not settings["sound"]
                if e.key == pygame.K_d:
                    settings["difficulty"] = "hard" if settings["difficulty"]=="easy" else "easy"
                if e.key == pygame.K_ESCAPE:
                    save_settings(settings)
                    return