from collections import deque
from sys import stdin
input = stdin.readline

dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
ex, ey, ans = 0, 0, 0

R, C = map(int, input().split())
lack = [list(input().strip()) for _ in range(R)]
wv = [[False] * C for _ in range(R)]
sv = [[False] * C for _ in range(R)]

wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

for i in range(R):
    for j in range(C):
        if lack[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                sv[i][j] = True
            else:
                ex, ey = i, j
            lack[i][j] = '.'
        if lack[i][j] == '.':
            wq1.append((i, j))
            wv[i][j] = True


def water():
    while wq1:
        x, y = wq1.popleft()
        lack[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or wv[nx][ny]:
                continue
            if lack[nx][ny] == '.':
                wq1.append((nx, ny))
            else:
                wq2.append((nx, ny))
            wv[nx][ny] = True


def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or sv[nx][ny]:
                continue
            if lack[nx][ny] == '.':
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            sv[nx][ny] = True
    return False


while True:
    water()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1

print(ans)
