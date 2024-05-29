def PrintDef(N):
    for i in range(N):
        if i%2 == 0:
            yield i

List = [x for x in range(1,9)]
print(List)

# generator expression 
PrintDefver2 = (i for i in range(4) if i%2==0)

for i in PrintDef(4):
    print(i,end=",")

print()

for i in PrintDefver2:
    print(i,end=",")