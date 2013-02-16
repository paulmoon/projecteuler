import fractions
import time

start = time.clock()
num_product = 1
den_product = 1

for num in range(10, 100):
    for den in range(num, 100):
        # We only care about ax and xb numbers.
        if num == den or str(num)[1] != str(den)[0]:
            continue
        original = float(num)/den
        new = (float(str(num)[0]))
        new_den = (int(str(den)[1]))
        # Can't divide by 0
        if new_den == 0:
            continue
        new /= new_den
        if original == new:
            num_product *= num
            den_product *= den

f = fractions.Fraction(num_product, den_product)
print (f.denominator)
print (time.clock() - start)
