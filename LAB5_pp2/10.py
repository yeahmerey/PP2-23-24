import re
txt = input()
x = re.findall(r"[A-Z][a-z0-9]*",txt)
slova = '_'.join(i.lower() for i in x)
print(slova)