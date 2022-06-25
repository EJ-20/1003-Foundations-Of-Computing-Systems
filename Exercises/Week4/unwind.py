from linkedlist import *

# use unwind recursion to traverse a list in reverse order
def unwind(node):
    if node._nextNode is not None: # traverse up to the head...
        unwind(node._nextNode)
    if node._item is not None: # (because the head has no item)
        print(node._item) # ...and now print out in reverse

def main():
    l = LinkedList()
    for i in range(13): l.insert(i)
    
    print("List in order of first to last:")
    for i in l: print(i)
    
    print("List in reverse order:")
    unwind(l._head)

if __name__ == '__main__':
    main()
