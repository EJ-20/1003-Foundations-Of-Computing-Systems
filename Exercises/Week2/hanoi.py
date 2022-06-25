# massively reduced version of code found on the booksite
# look at the return statement and notice that the final
# output is going to be a palindrome...
import sys

def hanoi(n, left):
    if n == 0: return " "
    move = str(n)
    move += "L" if left else "R"
    return hanoi(n-1, not(left)) + move + hanoi(n-1, not(left))

def main():
    n = int(sys.argv[1])
    print(hanoi(n, False))

main()
