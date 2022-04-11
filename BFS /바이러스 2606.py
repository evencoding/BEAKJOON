from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
C = int(input())
check = [0] * (N + 1)
connection = [[] for _ in range(N+1)]

for _ in range(C):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)


def dfs(array):
    for num in array:
        if not check[num]:
            check[num] = 1
            dfs(connection[num])

dfs(connection[1])
print(sum(check)-1)
