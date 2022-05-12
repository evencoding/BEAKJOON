from sys import stdin
from math import factorial
input = stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // factorial(n) // factorial(m-n))