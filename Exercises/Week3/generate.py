def generateInOrder(n):
    try:
        n + 1   
    #Generate retained list for maximum entries
        lst1 = [""] * 2**n
        def isgenerated(n):
    #return empty list if 0 is reached recursively
            if n == 0:
                return []
    #Create a multiplier equivalent to the number of combinations of 0 and 1 for n spaces
            else: 
                multiplier = (2**n)//2
    #Add zero for half of the possible combinations and one for the other half recursively
                a,b,c = 0, multiplier, multiplier + multiplier
                while c <= len(lst1):
                    for i in range(a,b):
                        lst1[i] = lst1[i] + "0"
                    for i in range(b,c):
                        lst1[i] = lst1[i] + "1"
                    a,b,c = a + multiplier + multiplier, b + multiplier + multiplier, c + multiplier + multiplier
                isgenerated(n-1) 
            return lst1
        lst1 = isgenerated(n)
        return lst1
    except:
        print("Enter a positive integer")
#Tester file for generateInOrder
def main():
    print(generateInOrder(2))
    print(generateInOrder(3))
    print(generateInOrder(4))
    print(generateInOrder(1))
    print(generateInOrder(5))
    print(generateInOrder("what"))
if __name__ == "__main__":
    main()