from math import tan, pi

def CalcAreaPolygon(n,length):
    return  n * (length ** 2) / (4 * tan(pi / n))
        

#magic

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

print("The area of the polygon is: ",CalcAreaPolygon(n,s))