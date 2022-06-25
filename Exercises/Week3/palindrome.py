# determine if the provided text is a palindrome
def palindrome(text):
    if len(text) <= 1: return True
    return (text[0] == text[-1]) and palindrome(text[1:-1])

def main():
    print("noon:", palindrome("noon"))
    print("wasitaratisaw:", palindrome("wasitaratisaw"))
    print("neveroddoreven:", palindrome("neveroddoreven"))
    print("nope:", palindrome("nope"))

main()
