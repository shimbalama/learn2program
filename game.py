#!/usr/bin/env python3

import pygame #import the library
import time
import random
#2do - make a module to see the dimensions of objects and understand interactions
pygame.init() #initialise the library

display_width = 1000 #make a variable of type int called display_width and set it to 800
display_height = 700

black  = (0,0,0) #make a variable of type tuple (a container the holds ints) called black and set it to (0,0,0) - a tuple of 3 ints
white  = (255,255,255)
red = (255,0,0)

car_width = 250# Make a square object - be careful - your car might be a different shape!
car_height = 250

gameDisplay = pygame.display.set_mode((display_width, display_height)) #Make a varaible called gameDisplay this is pygame object where display has a function 'set_mode' which takes 2 parameters - display_width, display_height - as a tuple.
pygame.display.set_caption('Speed racer') #set Title of game
clock = pygame.time.Clock() #Game clock

carImg = pygame.image.load('racecar.jpeg') #use the load function of the image class of the class pygame to laod an image 

# Here we define functions to use in the game

def blocks(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

def car(x, y): #Define a function called 'car' which takes teh parameters x and y
    gameDisplay.blit(carImg, (x, y)) #Give 2 parameters to the function blit - carImg and the tuple (x, y).  

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, size, x_pos):

    this_text = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, this_text)
    TextRect.center = ((display_width/2),(display_height/x_pos))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)

def crash():
    message_display('You Crashed!!', 111, 2)# Calls above
    message_display('Any key to start again', 55, 1.1)# Calls above
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_loop()#Starts loop over again

#this is the most important bit - it keeps the game running!
def game_loop():
    x = (display_width * 0.45) #set x to be a variable of type float which equals the existing variable 'display_width' times (*) 0.55
    y = (display_height * 0.6)
    x_change = 0
    y_change = 0
    
    #blocks
    block_startx = random.randrange(0, display_width)
    block_starty = -600
    block_speed = random.randrange(8, 12)
    block_width = random.randrange(33,99)
    block_height = random.randrange(33,99)
    #print ('Block: startx:', block_startx, 'speed:', block_speed, 'width:', block_width, 'height:',block_height)
    
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            #Exit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
           
           #change position - up down left right
            if event.type == pygame.KEYDOWN:	
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7
                elif event.key == pygame.K_UP:
                    y_change = -7
                elif event.key == pygame.K_DOWN:
                    y_change = 7
            
            # stop change of position
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
        x += x_change
        y += y_change
        
        gameDisplay.fill(white)# Make background white
        
        # blocks - call previoulsy defined functions
        blocks(block_startx, block_starty, block_width, block_height, black)
        block_starty += block_speed
        car(x,y)

        #detect wall crash
        if x > display_width - car_width or x < 0:
            #print ('Wall crash: startx:', block_startx, 'speed:', block_speed, 'width:', block_width, 'height:',block_height)
            crash() #Defined above	
        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0,display_width)
        
        #detect block crash
        if y < block_starty + block_height:
            block_x_coordinates = set(list(range(block_startx,block_startx + block_width)))
            car_x_coordinates = set(list(range(int(x), int(x) + car_width)))
            
            if len(block_x_coordinates.intersection(car_x_coordinates)) > 1:# Logic - if objects share an x coordinate, they crash
                #print (block_x_coordinates,car_x_coordinates,block_x_coordinates.intersection(car_x_coordinates))
                crash()
        #debug - see outline of car object
        #pygame.draw.rect(gameDisplay, red, (x,y,car_width,car_height), 2)
        
        #update!
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
