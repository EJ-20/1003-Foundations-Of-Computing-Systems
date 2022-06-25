import re
import fileinput
import sys

# Searches a text file for matches to the regular expression
# Prints out the required part of any matching sequences
def parseNCBI(textFile):
    regexpr = "[ ]*[0-9]+[ ]([actg ]*).*"
    
    for line in textFile: # read each line in the file
        x = re.match(regexpr, line)
        if x is not None:
            # print the part of the line that matches
            # the part of the RE in parentheses: [actg ]+
            print (x.group(1))

def main():
    textFile = fileinput.input(sys.argv[1:])
    parseNCBI(textFile)

if __name__ == '__main__':
    main()
