from linkedstack import *

class Tape:
    def __init__(self, inputStr):
        self._left = Stack()
        self._right = Stack()
        self._right.push("#") 
        for ch in inputStr[::-1]:
            self._right.push(ch)
        self._current = self._right.pop()

    def read(self):
        return self._current

    def write(self, symbol):
        self._current = symbol

    def moveLeft(self):
        self._right.push(self._current)
        if self._left.isEmpty(): self._left.push("#")
        self._current = self._left.pop()

    def moveRight(self):
        self._left.push(self._current)
        if self._right.isEmpty(): self._right.push("#")
        self._current = self._right.pop()

    def __str__(self):
        def listStackBtoT(stackStore):
            if stackStore.isEmpty(): return ""
            else:
                t = stackStore.pop()
                toReturn = listStackBtoT(stackStore) + t
                stackStore.push(t)
                return toReturn
            
        def listStackTtoB(stackStore):
            if stackStore.isEmpty(): return ""
            else:
                t = stackStore.pop()
                toReturn = t + listStackTtoB(stackStore)
                stackStore.push(t)
                return toReturn
        listToReturn = listStackBtoT(self._left) + self._current +  listStackTtoB(self._right)
        return listToReturn
            
        

            
    
