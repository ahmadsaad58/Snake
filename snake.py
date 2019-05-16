import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object): 
	row = 0
	width = 0

	def __init__(self, start, dirnx = 1, dirny = 0, color = (255, 0, 0)):
		pass
	
	def move(self, dirnx, dirny):
		pass
	
	def draw(self, surface, eyes = False): 
		pass

class snake(object):
	body = []
	turns = {}

	def __init__(self, color, pos):
		self.color = color
		self.head = cube(pos)
		#body is made of cubes
		self.body.append(self.head)
		self.dirnx = 0
		self.dirny = 1
	
	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			#gets the keys pressed
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
			
				

	
	def reset(self):
		pass
	
	def addCube(self):
		self.

	def draw(self):
		pass
	
def drawGrid(width, rows, surface):
	#creates the size of the grid blocks
	sizeOfBlock = width // rows
	x = 0
	y = 0 
	for i in range(rows):
		#update where the lines will be drawn
		x = x + sizeOfBlock
		y = y + sizeOfBlock

		#draw 2 lines each time (surface, color, start, end)
		pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
		pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))




def redrawWindow(surface):
	global rows, width
	#fills the grid with black
	surface.fill((0,0,0))
	drawGrid(width, rows, surface)
	pygame.display.update()

def randomSnack(row, items):
	pass

def message_box(subject, content):
	#messagebox(subject, content)
	pass

def main(): 
	global width, rows
	#create the board
	width = 500
	rows = 20
	#surface
	window = pygame.display.set_mode((width, width))
	
	#create the snake object
	s = snake((255, 0, 0), (10, 10))
	
	#create the clock
	clock = pygame.time.Clock()
	
	#create the while loop
	flag = True 
	while flag:
		#speed at which the snake moves
		
		#lower delay = faster 
		pygame.time.delay(50)
		#lower tick = slower 
		clock.tick(10)
		
		redrawWindow(window)
	
	pass




main()
