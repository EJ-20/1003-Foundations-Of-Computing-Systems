
def sums(n, lst):

    if len(lst) == 0:
        lst.append(n)
    if n == 1:
        return lst
    else:
        a = int(lst[0]) - n
        lst.append(str(n) + " - " + )

    return sums(n-1, lst)

def main():
    print(sums(4, []))
main()