def doubleSpaced(char):
    if len(char) == 0:
        return ''
    else:
        return char[0]*2 + ' ' + doubleSpaced(char[1:])

print(doubleSpaced("hello!"))
print(doubleSpaced("wider"))
