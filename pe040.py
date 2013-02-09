numbers = range(1, 10)
i = 10

while len(numbers) <= 1000000:
    for s in str(i):
        numbers.append(int(s))
    i += 1

print(numbers[0]*numbers[9]*numbers[99]*numbers[999]*numbers[9999]*numbers[99999]*numbers[999999])
