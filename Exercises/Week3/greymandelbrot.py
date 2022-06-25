# make sure that graphics.py and complex.py are in the same
# folder as this file

# based on original code by Sedgewick & Wayne
# adapted by Mark H to work with graphics.py and provide
# some simple (non-fractal!) magnification
from graphics import *
from complex import *

class GreyMandelbrot:
    'Plots shades of grey te represent likelihood of a complex number being in the set.'
    
    max = 255
    window_size = 800
    
    def __init__(self, n, xc, yc, size):
        if n > GreyMandelbrot.window_size: n = GreyMandelbrot.window_size
        self.n = n
        self.magnification = GreyMandelbrot.window_size / self.n
        self.xc = xc
        self.yc = yc
        self.size = size
    
    # draw the set
    def drawSet(self):
        self.win = GraphWin("Mandelbrot Set", GreyMandelbrot.window_size, GreyMandelbrot.window_size)
        for column in range(self.n):
            for row in range(self.n):
                x0 = self.xc - (self.size / 2) + (self.size * column) / self.n
                y0 = self.yc - (self.size / 2) + (self.size * row) / self.n
                z0 = Complex(x0, y0)
                grey = self.max - GreyMandelbrot.mandelbrot(z0, self.max)
                colour = color_rgb(grey, grey, grey)
                self.drawPixel(column, self.n - 1 - row, colour)
                self.win.update()
        
        self.win.getMouse()
        self.win.close()

    # draw a magnified pixel
    def drawPixel(self, x, y, colour):
        upperLeft = Point(x * self.magnification, y * self.magnification)
        bottomRight = Point((x + 1) * self.magnification, (y + 1) * self.magnification)
        pixel = Rectangle(upperLeft, bottomRight)
        pixel.setFill(colour)
        pixel.setOutline(colour)
        pixel.draw(self.win)

    # return a value from 0 to limit based on how long it takes
    # to determine that a point is not in the set
    # 0 = immediately apparent the point is not in set
    # 255 = point likely to be in set
    @staticmethod
    def mandelbrot(candidate, limit):
        z = candidate
        for t in range(limit):
            if abs(z) > 2.0: return t
            z = z * z
            z = z + candidate
        return limit

# test client
def main():
    n = int(80)      # try 80
    xc = float(-0.5)   # try -0.5
    yc = float(0)   # try 0
    size = float(2) # try 2
    
    # create the instance and draw
    mandelbrot = GreyMandelbrot(n, xc, yc, size)
    mandelbrot.drawSet()

if __name__ == '__main__': main()
