def unique(dupl):
    newlist = []
    for n in dupl:
        if n not in newlist:
            newlist.append(n)
    return newlist
    
dupl = []
a = int(input())
for i in range(a):
    dupl.append(int(input()))

print(unique(dupl))