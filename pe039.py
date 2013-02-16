"""
From http://en.wikipedia.org/wiki/Pythagorean_triple,
In a Pythagorean triple, m > n,
a = m^2 - n^2
b = 2mn
c = m^2 + n^2.
If p = a + b + c, then p = 2m^2 + 2mn.
If the maximum value of p is 1000, then the max value for m is 22 (quadratic formula).
"""

import fractions
import time

start = time.clock()

array = [0]*1001

for m in range(1, 22):
    for n in range(1, m):
        # Need only the primitive Pythagorean triples.
        if bool(m % 2 == 1) != bool(n % 2 == 1) and fractions.gcd(m, n) == 1:
            p = 2*m*m + 2*m*n
            if p > 1000:
                break
            # Cross off multiples.
            for x in range(p, 1001, p):
                array[x] += 1

print (array.index(max(array)))
print (time.clock() - start)
