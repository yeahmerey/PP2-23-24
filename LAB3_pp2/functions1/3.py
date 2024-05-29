def solve(numheads, numlegs):
    chicken = 0
    rabbit = 0
    rabbit = (numlegs - 2 * numheads) / 2
    chicken = numheads - rabbit 
    return int(chicken), int(rabbit)

"""
x + y = 35 => x = 35- y => 2x + 2y = 70
2y = 70 - 2x 
4x + 2y = 94 => 
4x + 70 - 2x = 94
2x = 94 -70
"""

print(solve(int(input()), int(input())))