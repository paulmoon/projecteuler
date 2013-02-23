import math
import time

start = time.clock()

n = 1

while True:
    # Every hexagonal number is a triangular number.
    # Thus, we only need to check whether a given hexagonal
    # number is also a pentagonal number.
    x = n*(2*n-1)
    y = ((math.sqrt(24*x+1)+1)/6)
    if y % 1 == 0 and x > 40755:
        print (x)
        print (time.clock() - start)
        break
    n += 1
