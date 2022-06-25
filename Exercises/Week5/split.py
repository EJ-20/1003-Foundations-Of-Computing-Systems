import re

# Splits a string into a list at each match of the R.E.
# In this case: split whenever whitespace is found.
def main():
    text = "I'd like to be somebody else and not know where I've been"
    
    # \s denotes whitespace
    # \ prefix required as escape character
    splitOn = "\\s"
    result = re.split(splitOn, text)

    print("Input string to split at whitespaces:\n", text)
    print("\nList generated:\n", result)

main()
