# recursive fill demonstration using recursion
# @author mhatcher 2020
#
# click anywhere to begin a fill
# the fill colour cycles through the rainbow
#
# because graphics.py doesn't let you natively set and get pixel colours
# a virtual canvas is created, which can be magnified
#
# to run: python3 fillDemo.py x y m
# x = width, y = height, m = pixel magnification

import sys
import random
from graphics import *
win = 0
magnification = 0

# flood fills an area of the canvas
def flood_fill(canvas, x, y, new_colour):
    old_colour = canvas[x][y]
    canvas[x][y] = new_colour
    drawPixel(x, y, canvas[x][y])
    win.update()
    
    if x > 0 and canvas[x - 1][y] == old_colour:
        flood_fill(canvas, x - 1, y, new_colour)
    if y > 0 and canvas[x][y-1] == old_colour:
        flood_fill(canvas, x, y - 1, new_colour)
    if x < len(canvas) - 1 and canvas[x + 1][y] == old_colour:
        flood_fill(canvas, x + 1, y, new_colour)
    if y < len(canvas[0]) - 1 and canvas[x][y + 1] == old_colour:
        flood_fill(canvas, x, y + 1, new_colour)

# draw the canvas in the window
def drawCanvas(canvas):
    for y in range(len(canvas[0])):
        for x in range(len(canvas)):
            drawPixel(x, y, canvas[x][y])
    win.update()

# draw a magnified pixel
def drawPixel(x, y, colour):
    upperLeft = Point(x * magnification, y * magnification)
    bottomRight = Point((x + 1) * magnification, (y + 1) * magnification)
    pixel = Rectangle(upperLeft, bottomRight)
    pixel.setFill(colour)
    pixel.draw(win)

# setup and run demo
def main():
    global win
    global magnification
    
    # get canvas height and width
    width = 900 #int(sys.argv[1])
    height = 900 #int(sys.argv[2])
    magnification = 100 #int(sys.argv[3])
    fill_palette = ['red', 'orange', 'yellow', 'green', 'blue', 'blue violet', 'dark magenta']
    
    # reset Python's recursion limit to match the size of the canvas
    sys.setrecursionlimit(width*height)
    
    # create representation of canvas
    canvas = [['white'] * height for i in range(width)]
    
    # add lines to the canvas to partition into regions
    horizontal = random.randint(1,height-2)
    vertical = random.randint(1,width-2)
    diagonal = random.randint(0,width-2)
    gap = random.randint(0,width-1)
    for i in range(width):
        if i != gap:
            canvas[i][horizontal] = 'black'
        canvas[i][(i + diagonal) % height] = 'black'
    
    for j in range(height):
        canvas[vertical][j] = 'black'
        canvas[(j + diagonal) % width][height - j - 1] = 'black'
    
    # create the graphics window
    win = GraphWin("Recursive Fill", width*magnification, height*magnification, autoflush=False)
    
    # display the canvas
    drawCanvas(canvas)
    
    index = 0
    while (True):
        try:
            # let the user click a pixel to begin the fill
            point = win.getMouse()
            x = int(point.getX()/magnification)
            y = int(point.getY()/magnification)
            
            # fill the region around the chosen pixel
            flood_fill(canvas, x, y, fill_palette[index % len(fill_palette)])
            index += 1
            
            # display the canvas
            drawCanvas(canvas)

        except GraphicsError: break # catch if user closes the window
     
    win.close()

main()
