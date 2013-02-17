import time

def is_pandigital(num):
    if len(num) != 9 or '0' in num:
        return False
    digits = {}
    for digit in num:
        if digit not in digits:
            digits[digit] = 1
        else:
            return False
    return True

start = time.clock()
solution = {}

for i in range(2, 99):
    # If 10 or 11 divides i, then it's not pandigital (10, 11, 20, 22, 30, 33, ...)
    if i % 10 != 0 and i % 11 != 0:
        # Since we want a 9-digit pandigital number, either
        # i = 1 digit and j = 4 digits, to make up i + j = 4 or 5 digits result.
        # i = 2 digits, and j = 3 digits, to make up i + j = 4 or 5 digits result.
        # Having 10000/i as the upper bound avoids i + j  = 5 digits result,
        # which gives a number with 10 digits and thus cannot be pandigital.
        for j in range(1, 10000//i):
            product = i*j
            if is_pandigital(str(i) + str(j) + str(product)):
                if product not in solution:
                    solution[product] = True

print (sum(solution.keys()))
print (time.clock() - start)
