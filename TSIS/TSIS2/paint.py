import pygame
import sys
from datetime import datetime
from tools import flood_fill

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# colors
color = (0, 0, 0)

# tools
tool = "pencil"
brush_size = 2

drawing = False
start_pos = None
last_pos = None

# text
font = pygame.font.SysFont(None, 30)
typing = False
text = ""
text_pos = (0, 0)

def save_canvas():
    filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
    pygame.image.save(canvas, filename)
    print("Saved:", filename)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_f:
                tool = "fill"
            if event.key == pygame.K_t:
                tool = "text"

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()

            if typing:
                if event.key == pygame.K_RETURN:
                    rendered = font.render(text, True, color)
                    canvas.blit(rendered, text_pos)
                    typing = False
                    text = ""
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text = ""
                else:
                    text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if tool == "fill":
                flood_fill(canvas, event.pos, color)

            elif tool == "text":
                typing = True
                text_pos = event.pos
                text = ""

            else:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if tool == "line" and drawing:
                pygame.draw.line(canvas, color, start_pos, event.pos, brush_size)
            drawing = False

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))

    # preview line
    if drawing and tool == "line":
        temp = canvas.copy()
        pygame.draw.line(temp, color, start_pos, pygame.mouse.get_pos(), brush_size)
        screen.blit(temp, (0, 0))

    # typing preview
    if typing:
        preview = font.render(text, True, color)
        screen.blit(preview, text_pos)

    pygame.display.flip()
    clock.tick(60)