import re
txt = input()
x = re.findall("[A-Z][^A-Z]*",txt)
slova = ' '.join(x)
print(slova)
