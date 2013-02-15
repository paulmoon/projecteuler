import time

def is_palindrome(num):
    return str(num) == str(num)[::-1]

start = time.clock()
solution = 0

for x in range(999, 100, -1):
    for y in range(999, x, -1):
        if x*y < solution: break
        if is_palindrome(x*y):
            solution = x*y

print (solution)
print (time.clock() - start)
