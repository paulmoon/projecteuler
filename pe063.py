import time

start = time.clock()

# 10^(n-1) < x^n < 10^n
# x must be 1 to 9, otherwise x^n will have > n+1 digits.
digits = list(range(9, 0, -1))
power, solution = 1, 0

while digits:
    for digit in digits:
        num = len(str(digit**power))
        if num == power:
            solution += 1
        # Again, 10^(n-1) < x^n < 10^n.
        # Since x is from 9 to 1, if the number of digits in, say 4^3 = 64,
        # is less than the power, then it's also the case that the digits of
        # 4^4 is less than 4, digits of 4^5 is less than 5, and so on. Therefore
        # we do not need to consider 4^6, 4^7, 4^8, and 4^9.
        elif num < power:
            digits.pop()
            break
    power += 1

print (solution)
print (time.clock() - start)
