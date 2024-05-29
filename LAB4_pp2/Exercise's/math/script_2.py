def AreaofTpz(Height,BaseDown,BaseUp):
    return Height*(BaseDown+BaseUp)/2

height = int(input("Height: "))
baseFirst = int(input("Base, first value: "))
baseSecond = int(input("Base, second value: ")) 

print("Area is :",AreaofTpz(height,baseFirst,baseSecond))