def is_palindrome(num):
    return str(num) == str(num)[::-1]

sol = 0

for x in range(999, 100, -1):
    for y in range(999, x, -1):
        if x*y < sol: break
        if is_palindrome(x*y) and x*y > sol:
            sol = x*y

print (sol)
