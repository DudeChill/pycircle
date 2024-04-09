import pygame
from pygame.locals import *
import sys
import math
import random

pygame.init()
fps = 144
fpsclock = pygame.time.Clock()
res = w, h = (500, 500)
center = w1, h1 = (250,250)
dimensions = 500
flags = pygame.NOFRAME
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 0, 255
color = 0
Pi = math.pi
circles = []
pointsinCircle = 0
pointsoutsideCircle = 0
screen = pygame.display.set_mode(res, flags, vsync=1)
def addDot(x):
    for i in range(x):
        circles.append((random.uniform(0,500),random.uniform(0,500)))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill('white')
    pygame.draw.circle(screen, black, center, 250, 1)
    for c in circles:
        if math.sqrt((c[0]-250)**2 + (c[1]-250)**2) <= 250:
            color = red
            pointsinCircle += 1
        if math.sqrt((c[0]-250)**2 + (c[1]-250)**2) >= 250:
            color = blue
            pointsoutsideCircle += 1
        pygame.draw.circle(screen, color, (c[0],c[1]), 1, 0)
    key_input = pygame.key.get_pressed()
    if key_input[K_a]:
        addDot(10)
        if pointsinCircle != 0 and pointsoutsideCircle != 0:
            print((pointsinCircle/(pointsinCircle+pointsoutsideCircle))*4)
    pygame.display.update()
    fpsclock.tick(fps)

