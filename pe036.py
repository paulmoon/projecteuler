import time

def is_palindrome(s):
    return s == s[::-1]

start = time.clock()
solution = 0

for i in range(10**6):
    si = str(i)
    # Preliminary checking
    if si[0] != si[-1]:
        continue
    if not is_palindrome(si):
        continue
    if is_palindrome(bin(i)[2:]):
        solution += i

print (solution)
print (time.clock() - start)
