import fractions
import operator

solution = []

for num in range(10, 100):
    for den in range(num, 100):
        # We only care about ax and xb numbers.
        if num == den or str(num)[1] != str(den)[0]:
            continue
        original = float(num)/den
        new = (float(str(num)[0]))
        new_den = (int(str(den)[-1]))
        # Can't divide by 0
        if new_den == 0:
            continue
        new /= new_den
        if original == new:
            solution.append((num, den))

# zip(*) is unzipping
num, den = zip(*solution)
f = fractions.Fraction(reduce(operator.mul, num), reduce(operator.mul, den))
print (f.denominator)
