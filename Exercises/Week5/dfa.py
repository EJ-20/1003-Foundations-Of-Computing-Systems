# Simulates a DFA
#
# There is no error checking of the input machine.
# So the format has to be correct.
#
# The input string must only includes symbols in the alphabet.
# This string is also not validated.
#
# @author Manrique Mata-Montero
class DFA:
    def __init__(self, fileObj):
        
        self._nextState = {} #transition function
        self._action = {} #type of state: accept or reject
        
        f = open(fileObj, "r")
        x = self.readToken(f)
        self._numStates = next(x)
        self._initState = next(x) 
        for i in range(int(self._numStates)):
            self._action.update({next(x):next(x)})
        
        token = next(x,"end")
        while token != "end":
            self._nextState.update({(token,next(x)):next(x)})
            token = next(x, "end")
        
        return
    # Reads the description of the machine from the given file in fileObj
    def readToken(self, fileobj):
        for line in fileobj:
            for token in line.split():
                yield token
    
    # Decides if the input string is in the languages
    def recognizes(self, inputStr):
        currentState = self._initState
        
        for ch in inputStr:
            currentState = self._nextState[currentState, ch]
        
        return self._action[currentState]
    
    # Provides the description of the machine.
    def __str__(self):
        x = "\nThe machine includes the following: \n"
        x = x + "Num of states: " + self._numStates + "\n"
        x = x + "Start state: " + self._initState +"\n"
       
        for state in self._action:
            x = x + "The state " +  state + " is a (an) " + self._action[state] + " state \n"
        
        x = x + "The transition function is given by the table: \n"
        for pair in self._nextState:
            x = x + "(" + str(pair[0])+ ", " + str(pair[1]) + ")" + " ---> " + str(self._nextState[pair]) + "\n"
        
        return x

def main():
    # Input the DFA machine description from a file
    inputFile = input("Name of the file describing the machine: ")
    machine = DFA(inputFile) 
    print(machine)
    
    # Input the string to be tested for membership in the language of the DFA
    testString = input("Enter string to test: ")
    
    # Test if the string is in the language
    if machine.recognizes(testString) == "accept":
        print("The string: ", testString, " is in the language")
    else: print("The string: ", testString, " is not in the language")
    return

main()



