import re
txt = input()
str = txt.split('_')
x = str[0] + ''.join(i.title() for i in str[1:])
print(x)