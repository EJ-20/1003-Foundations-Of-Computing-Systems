# stopwatch.py
# by Sedgewick and Wayne, from online booksite section 3.2
# lightly adapted by Mark H

import sys
import time

class Stopwatch:

    # Construct self and start it running.
    def __init__(self):
        self.start = time.time()  # creation time
        self.end = None           # end time if stopped

    # Return the elapsed time since creation of self, in seconds.
    def elapsedTime(self):
        if self.end: return self.end - self.start
        return time.time() - self.start



# test client
# takes integer n as an argument from the command line
# compares the performance of squaring integers using
# i**2 versus i*i for the task of computing the
# sum of the squares of the integers from 1 to n
def main():

    n = int(50)
    
    total1 = 0.0
    watch1 = Stopwatch()
    for i in range(1, n+1):
        total1 += i**2
    time1 = watch1.elapsedTime()
    
    total2 = 0.0
    watch2 = Stopwatch()
    for i in range(1, n+1):
        total2 += i*i
    time2 = watch2.elapsedTime()
    
    print("using i**2: ", time1, "seconds")
    print("using i*i:  ", time2, "seconds")

if __name__ == '__main__':
    main()
