import bindec

# A function that takes an argument as a string and converts and returns it's base64 representation
def charToBin(c):
    decimal = ord(c)

    if decimal == 43:
        binary = bindec.decToBin(62)

    elif decimal == 47:
        binary = bindec.decToBin(63)

    elif 48 <= decimal <= 57:
        binary = bindec.decToBin(decimal + 4)

    elif 65 <= decimal <= 90:
        binary = bindec.decToBin(decimal - 65)

    elif 97 <= decimal <= 122:
        binary = bindec.decToBin(decimal - 71)

    return binary

# A function that takes the base64 representation of characters as a list of 1's and 0's and computes and returns the character it represents
def binToChar(b):
    decimal = bindec.binToDec(b)

    if decimal == 62:
        char = chr(decimal + 19)

    elif decimal == 63:
        char = chr(decimal + 16)

    elif decimal >= 52 and decimal <= 61:
        char = chr(decimal - 4)

    elif decimal >= 0 and decimal <= 25:
        char = chr(decimal + 65)

    elif decimal >= 26 and decimal <= 51:
        char = chr(decimal + 71)

    return char

# A function that takes an input as a string and uses the function charToBin to convert a piece of text to base64 encoding
def strToBin(s):
    code = []
    for i in s:
        code += charToBin(i)

    return code

# A function that takes a base64 encoding input as a list of 1's and 0's and computes and returns the text as a string
def binToStr(b_list):
    output = ''

    for i in range(len(b_list)//6):

        bin = b_list[:6]
        output += binToChar(bin)
        b_list = b_list[6:]

    return output

# A function that takes a seed as a list, tap position and the length of the sequence as integers and generates a list of random binary numbers
def generatePad(seed, k, l):
    random = []
    for i in range(l):

        if seed[0] == seed[len(seed)-k]:
            random.append(0)
            seed.append(0)
        else:
            random.append(1)
            seed.append(1)
        seed = seed[1:]

    return random

# a function that uses the above functions to encrypt a text, taken as a string, a seed as a list and a tap position
def encrypt(message, seed, k):
    binary = strToBin(message)
    random = generatePad(seed, k, len(binary))
    enc = []
    for i in range(len(binary)):
        if binary[0] == random[0]:
            enc.append(0)
        else:
            enc.append(1)
        binary = binary[1:]
        random = random[1:]
    cipher = binToStr(enc)
    return cipher


