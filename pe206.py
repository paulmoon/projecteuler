# If a number's last digit is 0, its square will have 00 as the last digits.
# If the square ends with 900, then the original integer must have 30 or 70 as
# its last digits.

import time

start = time.clock()
i = 1000000030

while True:
    if str(i*i)[::2] == "1234567890":
        break
    i += 40
    if str(i*i)[::2] == "1234567890":
        break
    i += 60

print (i)
print (time.clock() - start)
