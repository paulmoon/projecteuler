import time

start = time.clock()
solution = 0

# Anything to the power of 1 probably wouldn't give the maximum digit sums,
# but for the sake of completeness I will include it.
# a, b > 80 would be my guess without looking at the answer.
for a in range(1, 100):
    for b in range(1, 100):
        sum_digits = 0
        for digit in str(a**b):
            sum_digits += int(digit)
        if sum_digits > solution:
            solution = sum_digits

print (solution)
print (time.clock() - start)
