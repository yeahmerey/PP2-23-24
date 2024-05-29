def Squares(a,b):
    for i in range(a,b):
        yield i*i

for i in Squares(10,20):
    print(i)