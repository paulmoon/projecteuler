curr = 1
prev = 1
next = 0
solution = 2

while len(str(curr)) < 1000:
    next = curr + prev
    prev = curr
    curr = next
    solution += 1

print solution