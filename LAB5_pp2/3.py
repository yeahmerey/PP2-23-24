import re
txt = input()
x = re.findall(r"[a-z]+_[a-z]+", txt)
print(x)