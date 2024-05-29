import math
str = str(input())

def permutation(str):
    a = len(str)
    return math.factorial(a)

print(permutation(str))