import re
txt = input()
x = re.findall("ab*", txt)
print(x)
