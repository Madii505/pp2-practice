import pygame
import random
import json
from db import save_game, get_best

WIDTH, HEIGHT = 600, 600
CELL = 20

def load_settings():
    try:
        with open("settings.json") as f:
            return json.load(f)
    except:
        return {"color":[0,255,0],"grid":True,"sound":True}

def save_settings(s):
    with open("settings.json","w") as f:
        json.dump(s,f,indent=4)


def game_loop(screen, username):
    settings = load_settings()

    snake = [(5,5)]
    direction = (1,0)
    food = (10,10)
    poison = None
    power = None

    speed = 10
    score = 0
    level = 1

    best = get_best(username)

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None,30)

    running = True
    while running:
        screen.fill((0,0,0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: direction=(0,-1)
        if keys[pygame.K_DOWN]: direction=(0,1)
        if keys[pygame.K_LEFT]: direction=(-1,0)
        if keys[pygame.K_RIGHT]: direction=(1,0)

        head = (snake[0][0]+direction[0], snake[0][1]+direction[1])

        # collision
        if head in snake or head[0]<0 or head[1]<0 or head[0]>=30 or head[1]>=30:
            save_game(username, score, level)
            return

        snake.insert(0, head)

        # food
        if head == food:
            score += 10
            food = (random.randint(0,29), random.randint(0,29))
        else:
            snake.pop()

        # poison
        if not poison and random.random()<0.02:
            poison = (random.randint(0,29), random.randint(0,29))

        if poison and head == poison:
            snake = snake[:-2]
            poison = None
            if len(snake) <= 1:
                save_game(username, score, level)
                return

        # powerups
        if not power and random.random()<0.01:
            power = {"pos":(random.randint(0,29),random.randint(0,29)),"type":random.choice(["fast","slow","shield"]),"time":pygame.time.get_ticks()}

        if power and head == power["pos"]:
            if power["type"]=="fast":
                speed = 20
            elif power["type"]=="slow":
                speed = 5
            power["time"] = pygame.time.get_ticks()
        
        if power and pygame.time.get_ticks()-power["time"]>5000:
            speed = 10
            power = None

        # draw
        for s in snake:
            pygame.draw.rect(screen, settings["color"], (s[0]*CELL, s[1]*CELL, CELL, CELL))

        pygame.draw.rect(screen,(255,0,0),(food[0]*CELL,food[1]*CELL,CELL,CELL))

        if poison:
            pygame.draw.rect(screen,(150,0,0),(poison[0]*CELL,poison[1]*CELL,CELL,CELL))

        if power:
            pygame.draw.rect(screen,(0,0,255),(power["pos"][0]*CELL,power["pos"][1]*CELL,CELL,CELL))

        screen.blit(font.render(f"Score:{score}",True,(255,255,255)),(10,10))
        screen.blit(font.render(f"Best:{best}",True,(255,255,0)),(10,40))

        pygame.display.flip()
        clock.tick(speed)