import pygame
import random


pygame.init()


window = pygame.display.set_mode((1280, 600))
screen = pygame.Surface((1280, 600))
color = 255, 255, 255
pygame.display.set_caption("click")

coord = random.randint(200, 600)
coord2 = random.randint(0, 500)
rect1 = pygame.draw.rect(window, color, pygame.Rect(coord, coord2, 60, 60))
points = 0


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if rect1.collidepoint(pos):
                points += 1
                print(points)
                coord = random.randint(100, 1000)
                coord2 = random.randint(0, 550)
                rect1.move(coord, coord2)




    window.fill((0, 0, 0))
    rect1 = pygame.draw.rect(window, color, pygame.Rect(coord, coord2, 60, 60))
    pygame.display.update()
