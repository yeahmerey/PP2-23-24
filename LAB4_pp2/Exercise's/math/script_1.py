import math 

def ConToRad(angle):
    return (angle*math.pi)/180

inner=int(input("Input degree: "))

print("Output radian: ",ConToRad(inner))