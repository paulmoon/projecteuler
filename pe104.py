import math
import time

def is_pandigital(num):
    if '0' in num or len(num) != 9:
        return False
    digits = {}
    for digit in num:
        if digit not in digits:
            digits[digit] = 1
        else:
            return False
    return True

start = time.clock()
five_sqrt = math.log(math.sqrt(5), 10)
Phi = math.log((1+math.sqrt(5))/2, 10)
curr = 1
prev = 0
next = 0
n = 1

while True:
    if is_pandigital(str(curr)[-9:]):
        """ http://en.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding
        Fib(n) = Phi^n / sqrt(5) => log (Fib(n)) = n*log(Phi) - log(sqrt(5))
        If we want the first 9 digits of Fib(n), then since
        log (Fib(n)) = d = digits of Fib(n), 10^(d-int(d)+8) will be
        what we're looking for. """
        digits = n*Phi - five_sqrt
        temp = 10**(digits - int(digits) + 8)

        if is_pandigital(str(temp)[:9]):
            print (n)
            print (time.clock() - start)
            break
    next = curr + prev % 10**9
    prev = curr
    curr = next
    n += 1
