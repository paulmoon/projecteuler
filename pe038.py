import time
import sys

def check(num):
    digits = {}
    answer = []

    for i in range(1, 10):
        value = num*i
        for digit in str(value):
            if digit in digits or '0' in digits:
                return False
            else:
                digits[digit] = True
                answer.append(digit)
        if len(answer) == 9:
            return int(''.join(answer))

start = time.clock()

for i in range(9876, 1, -1):
    solution = check(i)
    if solution != False:
        print (solution)
        print (time.clock() - start)
        sys.exit()
