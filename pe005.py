from fractions import gcd

sol = 1

for x in range(1, 21):
    sol = sol * x / gcd(sol, x)

print sol