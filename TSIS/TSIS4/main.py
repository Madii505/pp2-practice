import pygame
import sys
from game import game_loop
from db import init_db, get_top10

pygame.init()
init_db()

screen = pygame.display.set_mode((600,600))
font = pygame.font.SysFont(None,40)

def input_name():
    name = ""
    while True:
        screen.fill((0,0,0))
        screen.blit(font.render("Enter name:",True,(255,255,255)),(150,200))
        screen.blit(font.render(name,True,(0,255,0)),(150,250))
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return name
                elif e.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += e.unicode

def leaderboard():
    data = get_top10()
    y = 100
    while True:
        screen.fill((0,0,0))
        for d in data:
            text = f"{d[0]} {d[1]} {d[2]}"
            screen.blit(font.render(text,True,(255,255,255)),(100,y))
            y+=40
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                return

while True:
    screen.fill((0,0,0))
    screen.blit(font.render("Play (P)",True,(255,255,255)),(200,200))
    screen.blit(font.render("Leaderboard (L)",True,(255,255,255)),(200,300))
    screen.blit(font.render("Quit (Q)",True,(255,255,255)),(200,400))
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_p:
                name = input_name()
                game_loop(screen, name)
            if e.key == pygame.K_l:
                leaderboard()
            if e.key == pygame.K_q:
                pygame.quit()
                sys.exit()