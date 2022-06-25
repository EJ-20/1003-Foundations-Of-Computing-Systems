# adapted by Mark H, from the original by Sedgewick & Wayne

import sys

class Rectangle:

    # Construct self with top-left corner (x, y), width w, and height h.
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w;
        self.h = h;

    # Return the area of self.
    def area(self):
        return self.w * self.h

    # Return the perimeter of self.
    def perimeter(self):
        ...

    # Return True if self overlaps other, otherwise False.
    def overlaps(self, other):
        ...

    # Return True if other is completely inside of self, otherwise False.
    def contains(self, other):
        ...
    
    # Return rectangle as a string (replace x, y, w, h with actual values):
    # "top-left = [x, y], width = w, height = h
    def __str__(self):
        return "top-left = [" + str(self.x) + ", " + str(self.y) + "], width = " + str(self.w) + ", height = " + str(self.h)

# test client
# takes x, y, w and h as arguments from the command line
def main():
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    w = int(sys.argv[3])
    h = int(sys.argv[4])
    
    r1 = Rectangle(x, y, w, h)
    
    print("r1 is:", str(r1))
    print("area:", r1.area())
    print("perimeter:", r1.perimeter())
    
    # 3 other rectangles for comparison:
    # r2 is contained within but does not overlap r1
    r2 = Rectangle(x + 1, y + 1, w - 2, h - 2)
    
    # r3 overlaps r1
    r3 = Rectangle(x - 1, y - 1, w, h)
    
    # r4 neither overlaps nor is contained within r1
    r4 = Rectangle(x + w + 1, y + h + 1, w, h)
    
    rectangles = [r2, r3, r4]
    for rectangle in rectangles:
        print("\nComparison of r1 with rectangle:", str(rectangle))
        print("r1 contains this:", r1.contains(rectangle))
        print("r1 overlaps this:", r1.overlaps(rectangle))

if __name__ == '__main__':
    main()
