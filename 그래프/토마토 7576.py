from sys import stdin
from collections import deque
input = stdin.readline
n, m = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(m)]
visit = [[False] * n for _ in range(m)]
queue1, queue2 = deque(), deque()
cnt = 0
dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)

for i in range(m):
    for j in range(n):
        if farm[i][j] == 1:
            queue1.append((i, j))
            visit[i][j] = True
        elif farm[i][j] == -1:
            visit[i][j] = True

def dfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:
                if farm[nx][ny] == 0:
                    farm[nx][ny] = 1
                    visit[nx][ny] = True
                    queue2.append((nx, ny))

def allok(arr):
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                return False
    return True


while True:
    dfs(queue1)
    if not queue2:
        if allok(farm):
            print(cnt)
            break
        else:
            print(-1)
            break
    else:
        cnt += 1
        queue1 = queue2
        queue2 = deque()