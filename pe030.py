solution = []

# Upper limit for such numbers
for i in range(2, 354295):
    temp = 0
    for char in str(i):
        temp += int(char)**5
    if temp == i:
        solution.append(temp)

print sum(solution)