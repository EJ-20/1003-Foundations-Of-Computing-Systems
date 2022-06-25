# make sure that graphics.py and complex.py are in the same
# folder as this file

# based on original code by Sedgewick & Wayne
# adapted by Mark H to work with graphics.py and provide
# some simple (non-fractal!) magnification
from graphics import *
from complex import *
win = 0
magnification = 0

# return black if the candidate value is likely to be in the set
# otherwise return red
def mandelbrot(candidate, limit):
    z = candidate
    for t in range(limit):
        if abs(z) > 2.0: return "red"
        z = z * z
        z = z + candidate
    return "black"

# draw a magnified pixel
def drawPixel(x, y, colour):
    upperLeft = Point(x * magnification, y * magnification)
    bottomRight = Point((x + 1) * magnification, (y + 1) * magnification)
    pixel = Rectangle(upperLeft, bottomRight)
    pixel.setFill(colour)
    pixel.setOutline(colour)
    pixel.draw(win)

def main():
    global win
    global magnification
    n = int(80)      # try 80
    if n > 800: n = 800
    xc = float(-0.5)   # try -0.5
    yc = float(0)   # try 0
    size = float(2) # try 2
    magnification = 800 / n
    max = 255
    win = GraphWin("Mandelbrot Set", 800, 800)
    
    for column in range(n):
        for row in range(n):
            x0 = xc - (size / 2) + (size * column) / n
            y0 = yc - (size / 2) + (size * row) / n
            z0 = Complex(x0, y0)
            colour = mandelbrot(z0, max)
            drawPixel(column, n - 1 - row, colour)
            win.update()
    
    win.getMouse()
    win.close()

if __name__ == '__main__': main()
