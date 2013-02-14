def calculate_namescore(s):
    score = 0
    for char in s:
        if char.isalpha():
            score += ord(char)-64
    return score

with open("names.txt", "r") as f:
    names = []
    for line in f:
        names.extend([x for x in line.strip().split(',')])

names.sort()
solution = []

for i in range(len(names)):
    solution.append(calculate_namescore(names[i])*(i+1))

print (sum(solution))
