#!/usr/bin/env python3

import pygame #import the library
import time
import random

#2do -why does chicken start at same place all the time?
#figure out what resets the chicken when it hits the bottom

def main():

    pygame.init() #initialise the library

    display_width = 1000 #make a variable of type int called display_width
    display_height = 700
    
    black  = (0,0,0) #make a variable of type tuple (a container the holds ints) called black and set it to (0,0,0) - a tuple of 3 ints
    white  = (255,255,255)
    red = (255,0,0)
    colors = (black, white, red)
    
    carImg = pygame.image.load('racecar.jpeg') #use the load function of the image class of the class pygame to laod an image
    car_width = 250# Make a square object - be careful - your car might be a different shape!
    car_height = 250
    car_specs = (carImg, car_width, car_height)

    gameDisplay = pygame.display.set_mode((display_width, display_height)) #Make a varaible called gameDisplay this is pygame object where display has a function 'set_mode' which takes 2 parameters - display_width, display_height - as a tuple.
    pygame.display.set_caption('Speed racer') #set Title of game
    clock = pygame.time.Clock() #Game clock

    display = (gameDisplay, display_width, display_height)
    game_loop(clock, display, colors, car_specs)
    pygame.quit()
    quit()


# Here we define functions to use in the game
def chicken_maker():

    chicken_number = random.randrange(1, 4)
    chickenImg = pygame.image.load('chicken' + str(chicken_number) + '.jpg') #use the load function of the image class of the class pygame to laod an image
    chickenImg = pygame.transform.scale(chickenImg, (100,100))
    w, h = chickenImg.get_size()
    
    return chickenImg, w, h

def blocks(blockx, blocky, blockw, blockh, color):
    
    '''
    Draws rectangular blocks of the given dimensions
    '''
    
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

class Car: #Define a function called 'car' which takes teh parameters x and y
    
    '''
    Displays car
    '''
    
    def __init__(self, gameDisplay,img, x, y, width, height):
        self.img = img
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gameDisplay = gameDisplay

    def blit(self):
        self.gameDisplay.blit(self.img, (self.x, self.y)) #Give 2 parameters to the function blit - carImg and the tuple (x, y).  
    
class Chicken(Car):
    
    no_of_chickens = 0

    def __init__(self, gameDisplay,img, x, y, width, height, speed):
        super().__init__(gameDisplay,img, x, y, width, height)
        self.speed = speed
        
        Chicken.no_of_chickens += 1

def text_objects(text, font, black):
    
    '''
    Sends text to screen
    '''
    
    textSurface = font.render(text, True, black)
    
    return textSurface, textSurface.get_rect()

def message_display(text, size, x_pos, black, display, sleep = 1):

    '''
    Manages the details of the text to screen
    '''
    
    gameDisplay, display_width, display_height = display

    this_text = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, this_text, black)
    TextRect.center = ((display_width/2),(display_height/x_pos))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(sleep)

def crash(black, display, clock, colors, car_specs):
    
    '''
    Handle a crash where the car hits the wall or block
    '''
    
    message_display('You Crashed!!', 111, 2, black, display)# Calls above
    message_display('Any key to start again', 55, 1.1, black, display)# Calls above
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_loop(clock, display, colors, car_specs)#Starts loop over again

#this is the most important bit - it keeps the game running!
def game_loop(clock, display, colors, car_specs):
    
    '''
    The main loop that runs the game
    '''

    gameDisplay, display_width, display_height = display
    black, white, red = colors 
    carImg, car_width, car_height = car_specs

    x_change = 0
    y_change = 0
    chicken_speed = random.randrange(8, 12) 
    
    car = Car(gameDisplay, carImg, display_width * 0.45, display_height * 0.6, car_width, car_height)
    chickenImg, block_width, block_height = chicken_maker()#V2
    gameExit = False
    chicken = None
    while not gameExit:
        chicken_speed +=0.01
        if not chicken or chicken.y > 650.0:#goes back to top once off screen so this catches it if screen at 700 height
            chickenImg, block_width, block_height = chicken_maker()#V2
            chicken = Chicken(gameDisplay,
                chickenImg,
                random.randrange(0, display_width),
                -400,
                block_width,
                block_height,
                chicken_speed)
            message_display(str(Chicken.no_of_chickens-1), 111, 2, black, display, 0.001)# Calls above
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
        car.x += x_change
        car.y += y_change
        
        gameDisplay.fill(white)# Make background white
        
        #V2
        x_direcetion = random.choice([0, 1])
        if x_direcetion == 0:
            chicken.x += 17
        else:
            chicken.x -= 17
        chicken.y += chicken_speed
        #chicken.update(block_startx, block_starty)
        if chicken.y > 633:
            print ('chicken', 'chicken.x',chicken.x,
                    'chicken.y',chicken.y,'chicken.speed',chicken.speed,'no',Chicken.no_of_chickens )
        chicken.blit()
        #print ('car', car.x, car.y)
        #car.update(x, y)
        car.blit()
        #detect wall crash
        if car.x > display_width - car_width or car.x < 0:
            #print ('Wall crash: startx:', block_startx, 'speed:', block_speed, 'width:', block_width, 'height:',block_height)
            crash(black, display, clock, colors, car_specs) #Defined above	
        if chicken.y > display_height:
            chicken.y = 0 - chicken.height
            chicken.x = random.randrange(0, chicken.width)
        
        #detect block crash
        block_y_coordinates = set(list(range(int(chicken.y), int(chicken.y) + int(chicken.height))))
        car_y_coordinates = set(list(range(int(car.y), int(car.y) + car_height)))
        if len(block_y_coordinates.intersection(car_y_coordinates)) > 1:
            block_x_coordinates = set(list(range(chicken.x, chicken.x + chicken.width)))
            car_x_coordinates = set(list(range(int(car.x), int(car.x) + car_width)))
            if len(block_x_coordinates.intersection(car_x_coordinates)) > 1:# Logic - if objects share an x coordinate, they crash
                #print (block_x_coordinates,car_x_coordinates,block_x_coordinates.intersection(car_x_coordinates))
                crash(black, display, clock, colors, car_specs)
        #debug - see outline of car object
        #pygame.draw.rect(gameDisplay, red, (x,y,car_width,car_height), 2)
        #pygame.draw.rect(gameDisplay, red, (block_startx, block_starty, block_width, block_height), 2)
        
        #update!
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
