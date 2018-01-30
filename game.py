#!/usr/bin/env python3

import pygame #import the library
import time
import random
#2do - make a module to see the dimensions of objects and understand interactions
pygame.init() #initialise the library

display_width = 1200 #make a variable of type int called display_width and set it to 800
display_height = 800

black  = (0,0,0) #make a variable of type tuple (a container the holds ints) called black and set it to (0,0,0) - a tuple of 3 ints
white  = (255,255,255)
red = (255,0,0)

car_width = 250

gameDisplay = pygame.display.set_mode((display_width, display_height)) #Make a varaible called gameDisplay this is pygame object where display has a function 'set_mode' which takes 2 parameters - display_width, display_height - as a tuple.
pygame.display.set_caption('speed racer') #set Title of game
clock = pygame.time.Clock() #Game clock

carImg = pygame.image.load('racecar.jpeg') #use the load function of the image class of the class pygame to laod an image 

#blocks
def blocks(blockx, blocky, blockw, blockh, color):
	pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

#car and crash
def car(x, y): #Define a function called 'car' which takes teh parameters x and y
	gameDisplay.blit(carImg, (x, y)) #Give 2 parameters to the function blit - carImg and the tuple (x, y).  
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash():
	message_display('You Crashed!!')



def game_loop():
	x = (display_width * 0.45) #set x to be a variable of type float which equals the existing variable 'display_width' times (*) 0.55
	y = (display_height * 0.6)
	x_change = 0
	y_change = 0
	#blocks
	block_startx = random.randrange(0, display_width)
	block_starty = -600
	block_speed = random.randrange(11, 33)
	block_width = random.randrange(33,99)
	block_height = random.randrange(33,99)

	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			#change position - up down left right
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_LEFT:
					x_change = -10
				elif event.key == pygame.K_RIGHT:
					x_change = 10
				elif event.key == pygame.K_UP:
					y_change = -10
				elif event.key == pygame.K_DOWN:
					y_change = 10
			# stop change of position 
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0
		x += x_change
		y += y_change
		gameDisplay.fill(white)
		# blocks
		blocks(block_startx, block_starty, block_width, block_height, black)
		block_starty += block_speed
		car(x,y)
	
		if x > display_width - car_width or x < 0:
			crash() #Defined above	
		if block_starty > display_height:
			block_starty = 0 - block_height
			block_startx = random.randrange(0,display_width)
		#detect crash
		if y < block_starty + block_height:
			print('y crossover')
			if x > block_startx and x < block_startx + block_width or x+car_width > block_startx and x + car_width < block_startx + block_width:
				print('x crossover')
				crash()
		pygame.display.update()
		clock.tick(60)
game_loop()
pygame.quit()
quit()
