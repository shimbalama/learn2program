from turtle import *
from math import *

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 3, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 4, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed from random_plan\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

def build_city(plan):

    pass

create_drawing_canvas()


speed('fastest')

tracer(True)

title("gg")
build_city(random_plan()) 
release_drawing_canvas()