def generator(n):
    iterator = n
    while(iterator):
        yield iterator
        iterator -= 1
    yield 0


for i in generator(7):
    print(i)