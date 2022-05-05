from sys import stdin
from collections import deque
input = stdin.readline

M, N = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

print(matrix)