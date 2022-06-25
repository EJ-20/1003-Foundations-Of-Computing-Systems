# A Queue object is a first-in-first-out container.
# by Sedgewick & Wayne, with slight adaptation
import fileinput
import sys

class Queue:
    class _Node:  # private nested class
        def __init__(self, item = None, nextNode = None):
            self._nextNode = nextNode
            self._item = item
    
    # Construct an empty queue.
    def __init__(self):
        self._first = None  # Reference to first _Node
        self._last = None   # Reference to last _Node
        self._length = 0    # Number of items

    # Return True if self is empty, and False otherwise.
    def isEmpty(self):
        return self._first is None

    # Add item to the end of self.
    def enqueue(self, item):
        oldLast = self._last
        self._last = self._Node(item, None)
        if self.isEmpty():
            self._first = self._last
        else:
            oldLast._nextNode = self._last
        self._length += 1

    # Remove the first item of self and return it.
    def dequeue(self):
        item = self._first._item
        self._first = self._first._nextNode
        if self.isEmpty():
            self._last = None
        self._length -= 1
        return item

    # Return the number of items in self.
    def __len__(self):
        return self._length

    # Return a string representation of self.
    def __str__(self):
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur._item) + ", "
            cur = cur._nextNode
        return s[0:-2]

# Test client, reads a text file, one line at a time.
# Parses each space-separated string,
# and adds it to a queue using enqueue().
# '-' is interpreted as a call to the dequeue() command.
def main():
    queue = Queue()
    output = "" # to record items removed from the queue
    for line in fileinput.input(sys.argv[1:]): #read each line in file
        items = line.split(' ') # read each (space-separated) item in line
        for item in items:
            item = item.strip() # removes any leading and trailing spaces
            if item != '-':
                queue.enqueue(item)
            else:
                output += queue.dequeue() + " "
        print(output)

if __name__ == '__main__':
    main()

# tobe.txt
# to be or not to - be - - that - - - is

# python linkedqueue.py < tobe.txt
# to be or not to be
