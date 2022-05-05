from collections import deque

n, m = map(int, input().split())
idx = deque(list(map(int, input().split())))
queue = deque([i for i in range(1, n+1)])

cnt = 0
while idx:
    if queue[0] == idx[0]:
        queue.popleft()
        idx.popleft()
    else:
        mid = len(queue) // 2
        if queue.index(idx[0]) > mid:
            while queue[0] != idx[0]:
                queue.appendleft(queue.pop())
                cnt += 1
        else:
            while queue[0] != idx[0]:
                queue.append(queue.popleft())
                cnt += 1
print(cnt)

