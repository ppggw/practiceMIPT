import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (250, 245, 240), (0, 0, 500, 500))

#создание тела
circle(screen, (255, 255, 30), (250, 250), 100)

#создание глаз
circle(screen, (255, 0, 0), (215, 230), 19, 11) #левый
circle(screen, (255, 0, 0), (285, 230), 19, 11) #правый
circle(screen, (0, 0, 0), (215, 230), 8)
circle(screen, (0, 0, 0), (285, 230), 8)

#создание рта
rect(screen, (0, 0, 0), (210, 290, 80, 20))

#создание бровей
polygon(screen, (0, 0, 0), [(255, 210), (310, 160), (320, 170), (265, 220)]) #правая бровь
polygon(screen, (0, 0, 0), [(235, 220), (170, 170), (180, 160), (245, 210)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
