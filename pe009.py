import math
import sys

for a in range(1, 999):
    for b in range(1, 999):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print int(a*b*c)
            sys.exit()