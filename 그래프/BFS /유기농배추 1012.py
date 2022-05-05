from sys import stdin
from collections import deque

input = stdin.readline

T = int(input())
dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
queue = deque()

def bfs(matrix, visited, M, N):
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            ex, ey = x + dx[i], y + dy[i]
            if ex < 0 or ex >= M or ey < 0 or ey >= N or visited[ey][ex]:
                continue
            if matrix[y][x] == 1:
                queue.append((ey, ex))
                visited[ey][ex] = True
    return visited


for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0
    matrix = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and not visited[i][j]:
                cnt += 1
                queue.append((i, j))
                visited = bfs(matrix, visited, M, N)
    print(cnt)