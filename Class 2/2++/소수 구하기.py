from math import sqrt
m, n = map(int, input().split())

def is_prime(i):
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            return
    print(i)

for i in range(m, n+1):
    if i == 1: continue
    elif i == 2: print(i)
    else:
        is_prime(i)
