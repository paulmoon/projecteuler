factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
solution = []

# Switch the upper bound to 45000, and the program runs in 0.145 seconds vs 11 s
for i in range(3, 2540160):
    temp = 0
    for char in str(i):
        temp += factorial[(int(char))]
    if temp == i:
        solution.append(temp)

print sum(solution)
