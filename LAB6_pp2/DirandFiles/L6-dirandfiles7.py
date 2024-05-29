import os
with open('lab6/examplefile.txt', 'r') as r:
    with open('lab6/examplefile_copy.txt', 'w') as w:
        for line in r:
            w.write(line)
