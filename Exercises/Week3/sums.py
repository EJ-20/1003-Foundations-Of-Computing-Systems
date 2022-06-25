def sums(n,max_sum=0,count=0):
    try:
        n + 0
    #Add one to the counter variable for eah recursive call. This is to prevent the maximum sum from changing
        count += 1
        if count == 1:
            max_sum = n
    #Return once the recursive stack is complete or if 0 is inputted
        if n == 0:
            return  
    #Create a list of the base partition for any number, that is [1,1,1] for 3 or [1,1,1,1] for 4 
    #lst3 is the uniquely created copy of lst1 to prevent aliasing. lst2 is the returned list for recursion
        if n == 1:
            lst2 = []
            calc_list = [1]*max_sum
            lst3 = [str(x) for x in calc_list]
        #Replace each instance of a comma with an addition symbol
            lst2.append(' + '.join(lst3))
            return lst2
        else:
            calc_list = []
            lst2 = []
        #Return the number if maximum sum is the same as n
            if max_sum == n:
                calc_list = [max_sum]
                lst3 = [str(x) for x in calc_list]
                lst2.append(' + '.join(lst3))
                return lst2 + sums(n-1,max_sum,count)
        #If it isn't divide the max sum into a sum of the recursive n and the difference betweeen n and max sum
            else:
                calc_list = [n]
                second_part = max_sum - n
        #Just return this second part if it's one
                if second_part == 1:
                    calc_list.append(second_part)
                    lst3 = [str(x) for x in calc_list]
                    lst2.append(' + '.join(lst3))
                    return lst2 + sums(n-1,max_sum,count)
        #Keep reducing the second index of our calculated list by 1 until our second index is one.
                elif second_part > 1:
                    calc_list.append(second_part)
                    while calc_list[1] >= 1:
                #Only return our results if the second index is less than or equals to the first. This is to retain uniqueness of sums
                        if calc_list[1] <= calc_list[0]:
                            lst3 = [str(x) for x in calc_list]
                            lst2.append(' + '.join(lst3))
                        second_part = calc_list[1] - 1
                        calc_list[1] = second_part
                        calc_list.append(1)
                    return lst2 + sums(n-1,max_sum,count)
    except:
        print("Only positive integers, not other type")
                
def main():
    print(sums(4))
    print(sums(6))
    print(sums(8))
    print(sums(0))
    print(sums("wrong"))

if __name__ == "__main__":
    main()

                    





        