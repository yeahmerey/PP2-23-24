from math import sqrt
def is_prime(a):
    i=2
    while i <= sqrt(a):
     if a % i == 0:
        return False
        break
    i += 1
    return True

b=list(map(int,input().split()))
for i in  range(len(b)):
    if is_prime(b[i])==1:
        print (b[i]," ")
