import pygame
import random
import json
from persistence import load_settings, save_score

WIDTH, HEIGHT = 600, 800

def game_loop(screen):
    settings = load_settings()

    player = pygame.Rect(250, 650, 50, 80)
    speed = 5
    coins = 0
    distance = 0

    traffic = []
    obstacles = []
    powerups = []

    active_power = None
    power_timer = 0

    font = pygame.font.SysFont(None, 30)
    clock = pygame.time.Clock()

    username = input("Enter name: ")

    running = True
    while running:
        screen.fill((30,30,30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed

        # spawn traffic
        if random.random() < 0.02:
            x = random.choice([100, 250, 400])
            if abs(x - player.x) > 80:
                traffic.append(pygame.Rect(x, -100, 50, 80))

        # spawn obstacles
        if random.random() < 0.02:
            x = random.choice([100, 250, 400])
            obstacles.append(pygame.Rect(x, -50, 50, 50))

        # spawn powerups
        if random.random() < 0.01:
            x = random.choice([100, 250, 400])
            t = random.choice(["nitro", "shield", "repair"])
            powerups.append((pygame.Rect(x, -50, 40, 40), t))

        # move objects
        for t in traffic:
            t.y += speed + 2
        for o in obstacles:
            o.y += speed
        for p in powerups:
            p[0].y += speed

        # collisions
        for t in traffic:
            if player.colliderect(t):
                if active_power == "shield":
                    active_power = None
                else:
                    running = False

        for o in obstacles:
            if player.colliderect(o):
                running = False

        for p in powerups:
            rect, typ = p
            if player.colliderect(rect):
                active_power = typ
                power_timer = 300
                powerups.remove(p)

        # power effects
        if active_power == "nitro":
            speed = 10
        else:
            speed = 5

        if power_timer > 0:
            power_timer -= 1
        else:
            active_power = None

        distance += speed
        coins += 1

        # draw
        pygame.draw.rect(screen, (0,255,0), player)

        for t in traffic:
            pygame.draw.rect(screen, (255,0,0), t)
        for o in obstacles:
            pygame.draw.rect(screen, (100,100,100), o)
        for p in powerups:
            pygame.draw.rect(screen, (0,0,255), p[0])

        screen.blit(font.render(f"Coins: {coins}", True, (255,255,255)), (10,10))
        screen.blit(font.render(f"Dist: {distance}", True, (255,255,255)), (10,40))

        if active_power:
            screen.blit(font.render(f"Power: {active_power}", True, (255,255,0)), (10,70))

        pygame.display.flip()
        clock.tick(60)

    score = coins + distance // 10
    save_score(username, score, distance)