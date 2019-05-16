import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class cube(object):
    row = 20
    width = 500

    def __init__(self, start, dirnx = 1, dirny = 0, color = RED):
        self.pos = start
		self.dirnx = 1
		self.dirny = 0
		self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
		self.dirny = dirny
		self.pos(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.width // self.rows
		i = self.pos[0]
		j = self.pos[1]

		pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))

		if eyes: 
			center = dis // 2
			radius = 3 
			circleMiddle = (i*dis+center-radius, j*dis+8)
			circleMiddle2 = (i*dis+ dis -radius*2, j*dis+8)
			pygame.draw.circle(surface, BLACK, circleMiddle, radius)
			pygame.draw.circle(surface, BLACK, circleMiddle2, radius)

# snake object made of cube objects
class snake(object):
    body = []
    turns = {}

    # initializes the snake
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        # body is made of cubes
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    # moves the snake with turns
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # gets the keys pressed
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # for the slither effect
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                # move with x and y
                c.move(turn[0], turn[1])
                # remove last turn
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                # reaching the edges of the screen
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
					#just move
                    c.move(c.dirnx, c.dirny)

    # resets the snake
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        pass

    def draw(self):
        for i, c in enumerate(self.body):
            # draw eyes if head
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(width, rows, surface):
    # creates the size of the grid blocks
    sizeOfBlock = width // rows
    x = 0
    y = 0
    for i in range(rows):
        # update where the lines will be drawn
        x = x + sizeOfBlock
        y = y + sizeOfBlock

        # draw 2 lines each time (surface, color, start, end)
        pygame.draw.line(surface, WHITE, (x, 0), (x, width))
        pygame.draw.line(surface, WHITE, (0, y), (width, y))


def redrawWindow(surface):
    global rows, width, s
    # fills the grid with black
    surface.fill(BLACK)
    # draw snake
    s.draw(surface)
    # draw grid
    drawGrid(width, rows, surface)
    # update display
    pygame.display.update()


def randomSnack(row, items):
    pass


def message_box(subject, content):
    #messagebox(subject, content)
    pass


def main():
    global width, rows, s
    # create the board
    width = 500
    rows = 20
    # surface
    window = pygame.display.set_mode((width, width))

    # create the snake object
    s = snake(RED, (10, 10))

    # create the clock
    clock = pygame.time.Clock()

    # create the while loop
    flag = True
    while flag:
        # speed at which the snake moves

        # lower delay = faster
        pygame.time.delay(50)
        # lower tick = slower
        clock.tick(10)

        redrawWindow(window)

    pass


main()
