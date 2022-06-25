# A Stack object is a last-in-first-out collection.
# Implemented here as a list
class Stack:
    # Construct an empty Stack object.
    def __init__(self):
        self._contents = []
    
    # Return True if stack is empty, False otherwise.
    def isEmpty(self):
        return len(self._contents) == 0
    
    # Push item onto the top of stack.
    def push(self, item):
        self._contents.insert(0,item)
    
    # Pop the top item from the stack and return it.
    def pop(self):
        item = self._contents[0]
        self._contents = self._contents[1:]
        return item
    
    # Return a string representation of stack. (Not in the API.)
    def __str__(self):
        s = ""
        for item in self._contents:
            s += str(item) + ", "
        return s[0:-2]

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
