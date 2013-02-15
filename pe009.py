# In a Pythagoras triangle, a + b > c. If a + b + c = 1000, then it must be that c < 500,
# otherwise a + b can never be greater than c since a + b = 1000 - c.
# In addition, a < b < c implies that c > 334 since if c <= 334, then any choice of
# b < c and a < b would give a + b + c < 1000.

import math
import time

start = time.clock()

for c in range(334,500):
    for a in range(1, (1000-c)//2):
        b = 1000 - a - c
        if a**2 + b**2 == c**2:
            print (a*b*c)
            print (time.clock() - start)
