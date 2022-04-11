# 빙판이 물로 녹는 BFS와, 백조가 이동하는 BFS를 따로 나눈다.
# 물을 위한 큐는 wq1, wq2가 있고, 백조를 위한 큐는 sq1, sq2가 있다.
# 입력으로 주어지는 호수 맵에서 물('.')의 좌표를 wq1에 모두 넣는다.
# 호수 맵에서 백조('L')의 좌표를 sq1에 하나 넣고, 다른 하나의 백조 위치는 도착 위치(ex, ey)로 저장한다.
#
# 우선, 빙판을 먼저 녹이고, 백조를 이동시켜야 한다.
# 물 BFS에서 맵을 이동하면서, 빙판('X')을 물('.')로 녹인다.
# 다음 위치가 물('.')인 경우, sq1에 좌표를 넣는다.
# 다음 위치가 빙판('X')인 경우, sq2에 좌표를 넣는다.
#
# 백조 BFS에서 맵을 이동하면서, 도착 위치에 있는 백조를 만날 수 있는지 확인한다.
# 다음 위치가 물('.')인 경우, wq1에 좌표를 넣는다.
# 다음 위치가 빙판('X')인 경우, wq2에 좌표를 넣는다.
#
# 현재 wq2에는 빙판의 위치가 들어있다. 다음 이동을 위해 wq1를 wq2로 대체한다.
# 현재 sq2에는 빙판의 위치가 들어있다. 다음 이동을 위해 sq1를 sq2로 대체한다.
# wq2와 sq2를 초기화한다.
# 백조가 만날 때까지, 위 과정을 반복한다.

from collections import deque
from sys import stdin
input = stdin.readline

ex, ey, ans = 0, 0, 0
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
R, C = map(int, input().split())

lack = [list(input().strip()) for _ in range(R)]
wc = [[False] * C for _ in range(R)]
sc = [[False] * C for _ in range(R)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

for i in range(R):
    for j in range(C):
        # 첫번째로 찾은 백조의 위치 기억
        if lack[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                sc[i][j] = True
            else:
                ex, ey = i, j
            lack[i][j] = '.'
        if lack[i][j] == '.':
            wq1.append((i, j))
            wc[i][j] = True


def water():
    while wq1:
        x, y = wq1.popleft()
        lack[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or wc[nx][ny]:
                continue
            if lack[nx][ny] == '.':
                wq1.append((nx, ny))
            else:
                wq2.append((nx, ny))
            wc[nx][ny] = True


def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or sc[nx][ny]:
                continue
            if lack[nx][ny] == '.':
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            sc[nx][ny] = True
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
