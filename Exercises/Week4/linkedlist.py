class LinkedList:
    class _Node:  # private nested class
        def __init__(self, item = None, nextNode = None):
            self._nextNode = nextNode
            self._item = item
    
    def __init__(self):
        self._head = None
    
    def insert(self, something):
        self._head = self._Node(something, self._head)
    
    def isEmpty(self):
        return self._head is None
    
    # return item in the head and delete the first node
    def delete(self):
        t = None # in case there's nothing to delete
        if self._head != None:
            t = self._head._item
            self._head = self._head._nextNode
        return t
    
    def __iter__(self):
        pointer = self._head
        while pointer is not None:
            yield pointer._item
            pointer = pointer._nextNode

def main():
    l = LinkedList()
    for i in range(13): l.insert(i)
    
    print("List in order of first to last:")
    for i in l: print(i)

if __name__ == '__main__':
    main()
