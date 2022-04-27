from collections import deque
from sys import stdin
input = stdin.readline

N, goal = map(int, input().split())
queue = deque([(N, 1)])

res = -1
while queue:
    num, i = queue.popleft()
    if num == goal:
        res = i
        break
    if num * 2 <= goal:
        queue.append((num * 2, i+1))
    if int(str(num) + '1') <= goal:
        queue.append((int(str(num) + '1'), i+1))

print(res)

