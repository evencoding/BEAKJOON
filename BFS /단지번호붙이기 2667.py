from collections import deque
from sys import stdin

input = stdin.readline

N = int(input())
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

complex = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

total_complex = 0
house = deque()
answer = []


def bfs():
    cnt = 1
    while house:
        x, y = house.popleft()
        for i in range(4):
            ex, ey = x + dx[i], y + dy[i]
            if ex < 0 or ex >= N or ey < 0 or ey >= N or visited[ex][ey]:
                continue
            if int(complex[ex][ey]) == 1:
                house.append((ex, ey))
                visited[ex][ey] = True
                cnt += 1
    return cnt


for i in range(N):
    for j in range(N):
        if int(complex[i][j]) == 1 and not visited[i][j]:
            house.append((i, j))
            total_complex += 1
            visited[i][j] = True
            point = bfs()
            answer.append(point)

answer.sort()

print(total_complex)
for num in answer:
    print(num)
