import re
x = input()
txt = re.sub("[ ,.]",":",x)
print(txt)
