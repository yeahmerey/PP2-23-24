def Squares(N):
    a = 1
    while a < N:
        yield a**2
        a+=1 

lim = int(input())

for i in Squares(lim):
    print(i)

    



