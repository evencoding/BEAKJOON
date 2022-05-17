# from collections import deque
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     cnt = 1
#     importance = deque(list(map(int, input().split())))
#     idx = deque([i for i in range(n)])

#     while idx:
#         i, o = idx[0], importance[0]
#         if o >= max(importance):
#             if i == m:
#                 break
#             idx.popleft()
#             importance.popleft()
#             cnt += 1
#         else:
#             idx.append(idx.popleft())
#             importance.append(importance.popleft())

#     print(cnt)

from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    que = deque(i for i in enumerate(map(int, input().split())))
    cnt = 1
    while que:
        i, o = que.popleft()
        if not que or o >= max(map(lambda p: p[1], que)):
            if i == m:
                break
            cnt += 1
        else:
            que.append((i, o))
    print(cnt)