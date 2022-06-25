# simple tester for factors.py module
# @author mhatcher 2020
#
# run example: python3 factor.py 6 42
#
#-----------------------------------
import sys
import factors

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Is", a, "prime? A.",factors.prime(a))
print("Is", b, "prime? A.",factors.prime(b))

print("\nQ. Is", a, "a factor of", b, "? A.",factors.is_factor(a,b))

print("\nGreatest common divisor of",a, "and", b, ":", factors.gcd(a,b))

print("\nFactors of", a, ":", factors.factor_list(a))
print("Factors of", b, ":", factors.factor_list(b))

print("\nQ. Is", a, "perfect? A.",factors.perfect(a))
print("Q. Is", b, "perfect? A.",factors.perfect(b))
print("\n")
