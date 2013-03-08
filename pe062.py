import time

def num_digits(number):
    digits = [0]*10
    number = str(number)
    for char in number:
        digits[int(char)] += 1
    return ''.join([str(d) for d in digits])

start = time.clock()
digits_cubes = {}
number = 1

while True:
    digits = num_digits(number**3)

    if digits not in digits_cubes:
        digits_cubes[digits] = [1, number]
    else:
        digits_cubes[digits][0] += 1
    if digits_cubes[digits][0] == 5:
        print (digits_cubes[digits][1]**3)
        print (time.clock() - start)
        break
    number += 1
