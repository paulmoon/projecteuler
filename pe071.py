import fractions
import time
import sys

start = time.clock()
sentinel = fractions.Fraction(str(3/7)).limit_denominator(10**6)

for i in range(10, 0, -1):
    for j in range(1, 10):
        challenger = fractions.Fraction(str((3/7)-(j*10**(-i)))).limit_denominator(10**6)
        if challenger != sentinel:
            print (challenger.numerator)
            print (time.clock() - start)
            sys.exit()
