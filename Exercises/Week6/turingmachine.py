from tape import *
class TM:
#There is no error checking of the description of the TM given as input!
#The input string to test for membership includes symbols in the alphabet only

    def __init__(self, fileObj): #Reads the description of the machine
        def readToken(fileobj):
            for line in fileobj:
                for token in line.split():
                    yield token
        self._nextState = dict() #given a state and symbol give the next state
        self._action = dict() #type of state: accept or reject
        self._out = dict() #given a state and a symbol, give output symbol
        self._alphabet = []
        f = open(fileObj, "r")
        x = readToken(f)
        self._numStates = next(x)
        alphSym = next(x)
        while alphSym != "#":
            self._alphabet.append(alphSym)
            alphSym = next(x)
        self._alphabet.append("#")
        self._initState = next(x)
        for i in range(int(self._numStates)):
            self._action.update({str(i):next(x)})
            for alphSym in self._alphabet:
                self._nextState.update({(str(i),alphSym):next(x)})
            for alphSym in self._alphabet:
                self._out.update({(str(i), alphSym):next(x)})
        return

    def simulate(self, inputStr):
        currentState = self._initState
        TMtape = Tape(inputStr)
        while self._action[currentState] in {"L","R"}:
            inSymbol = TMtape.read()
            TMtape.write(self._out[(currentState, inSymbol)])
            currentState = self._nextState[(currentState, inSymbol)]
            if self._action[currentState] == "L": TMtape.moveLeft()
            if self._action[currentState] == "R": TMtape.moveRight()
        return self._action[currentState], TMtape
            
    
    def __str__(self): #To show the description of the machine
        x = "\nThe machine includes the following: \n"
        x += "Num of states: " + self._numStates + "\n"
        x += "Start state: " + self._initState +"\n"
        for state in self._action:
            x += "The state " +  state + " is a " + self._action[state] + " state \n"
        x += "The state transition function is given by the table: \n"
        for pair in self._nextState:
            x += "(" + pair[0]+ ", " + pair[1] + ")" + " ---> " + self._nextState[pair] + "\n"
        x +=  "The output for each state and symbol combination is given by the table: \n"
        for pair in self._out:
            x += "(" + pair[0]+ ", " + pair[1] + ")" + " ---> " + self._out[pair] + "\n"
        return x
                
        
def main():
    #The input includes a file name containing a description of a Turing Machine
    # and a number of input strings to give as input to the described machine.
    # The input strings are terminated by the string "end".
    inputFile = input("Name of the file describing the machine: ")
    machine = TM(inputFile) 
    print(machine)
    # Input string of symbols from the alphabet only
    testString = input("Enter string to test: ")
    while testString!= "end":
        resultOfSimulation = machine.simulate(testString)
        print("State reached: ", resultOfSimulation[0],
              " and the tape contents is: ", resultOfSimulation[1])
        testString = input("Enter string to test: ")
        
    return
main()



