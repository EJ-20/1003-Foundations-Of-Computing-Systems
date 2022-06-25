# simple methods on the theme of factors
# @author mhatcher 2020

# determines if x is a factor of y
def is_factor(x,y):
    return (y % x == 0)

# returns the greatest common divisor of x and y
def gcd(x,y):
    stop_at = x + 1 if x < y else y + 1
    greatest = 1
    for divisor in range(2,stop_at):
        if (x % divisor == 0) and (y% divisor == 0):
            greatest = divisor
    return greatest

# determines if x is prime
def prime(x):
    for divisor in range(2,x):
       if (x % divisor == 0):
          return False
    return True

# returns list of factors of x, including itself
def factor_list(x):
    list = []
    for divisor in range(1,x+1):
        if is_factor(divisor,x):
            list.append(divisor)
    return list

# determines if x is perfect
def perfect(x):
    list = factor_list(x)
    sum = 0
    for item in list:
        sum += item
    return sum == 2 * x

