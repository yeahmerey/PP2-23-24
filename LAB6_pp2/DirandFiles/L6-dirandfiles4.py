import os
with open('lab6/examplefile.txt', 'r') as file:
    x = sum(1 for line in file)
print(x)
