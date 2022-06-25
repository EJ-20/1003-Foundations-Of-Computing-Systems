def convert(N): #N is a positive integer
    if (N == 1): return "1"
    else: return convert(N // 2) + str(N % 2)

def main():
    N = int(input("Enter decimal positive integer to convert:\n"))
    print(convert(N))

main()