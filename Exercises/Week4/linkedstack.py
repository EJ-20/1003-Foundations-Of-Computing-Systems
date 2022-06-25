# A Stack object is a last-in-first-out collection.
# Implemented here as a linked-list of Node objects
class Stack:
    class _Node:  # private nested class
        def __init__(self, item = None, nextNode = None):
            self._nextNode = nextNode
            self._item = item

    # Construct an empty Stack object.
    def __init__(self):
        self._first = None  # Reference to first _Node

    # Return True if stack is empty, False otherwise.
    def isEmpty(self):
        return self._first is None

    # Push item onto the top of stack.
    def push(self, item):
        self._first = self._Node(item, self._first)

    # Pop the top item from the stack and return it.
    def pop(self):
        if self._first is None:
            return None
        else:
            item = self._first._item
            self._first = self._first._nextNode
            return item

    # Return a string representation of stack. (Not in the API.)
    def __str__(self):
        s = ""
        cur = self._first
        while cur is not None:
            s += str(cur._item) + ", "
            cur = cur._nextNode
        return s[0:-2]

# test client
def main():
    s = Stack()
    for i in range(13): s.push(i)
    
    print("Stack contents:")
    print(str(s))
    
    s.push(20)
    print("Stack contents:")
    print(str(s))
    
    print("Removed:",str(s.pop()))
    print("Removed:",str(s.pop()))
    
    print("Stack contents:")
    print(str(s))

if __name__ == '__main__':
    main()
