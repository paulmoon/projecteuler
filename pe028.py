# Notice the pattern:
# 1x1 grid: 1
# 3x3 grid: 3 5 7 9 
# 5x5 grid: 13 17 21 25
# 7x7 grid: 31 37 43 49...
# The differences are 1, 2, 4, 6, 8, 10 and so on.

import time

start = time.clock()

difference = 2
# Starting with 3x3 grid
grid_number = 3
solution = 1
# The starting number in the four corners of a 3x3 grid: 3, 5, 7, 9
starting_number = 3

while grid_number <= 1001:
    # For example, 3, 5, 7, 9 = 3 + (3+2) + (3+4) + (3+6) = 3*4 + 2*6
    solution += (starting_number*4) + (difference*6)
    grid_number += 2
    starting_number += 4*difference + 2
    difference += 2

print (solution)
print (time.clock() - start)
