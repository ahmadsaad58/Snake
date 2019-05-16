import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object): 
	row = 0
	column = 0

	def __init__(self, start, dirnx = 1, dirny = 0, color = (255, 0, 0)):
		pass
	
	def move(self, dirnx, dirny):
		pass
	
	def draw(self, surface, eyes = False): 
		pass

class snake(object):

	def __init__(self, color, pos):
		pass
	
	def move(self):
		pass
	
	def reset(self):
		pass
	
	def addCube(self):
		pass

	def draw(self):
		pass
	
def drawGrid(column, row, surface):
	pass

def redrawWindow(surface):
	win.fill(0,0,0)
	drawGrid(surface)
	pygame.display.update()

def randomSnack(row, items):
	pass

def message_box(subject, content):
	messagebox(subject, content)

def main(): 
	#create the board
	width = 500
	height = 500
	rows = 20
	#surface
	window = pygame.display.set_mode(width, height)
	
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



