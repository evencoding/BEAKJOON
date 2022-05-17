from re import I


# from math import gcd, lcm

n, m = map(int, input().split())
GCD = 0
LMC = 0
for i in range(min(n, m), 0, -1):
    if n % i == 0 and m % i == 0:
        GCD = i
        break
LMC = n * m // GCD
print(GCD)
print(LMC)