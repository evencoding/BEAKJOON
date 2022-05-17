import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()
for _ in range(n):
    s = input().split()
    if s[0] == 'push_front': 
        deq.appendleft(s[1])
    if s[0] == 'push_back': 
        deq.append(s[1])
    if s[0] == 'pop_front': 
        print(deq.popleft() if deq else -1)
    if s[0] == 'pop_back': 
        print(deq.pop() if deq else -1)
    if s[0] == 'size': 
        print(len(deq))
    if s[0] == 'empty':
        print(0 if deq else 1) 
    if s[0] == 'front': 
        print(deq[0] if deq else -1)
    if s[0] == 'back': 
        print(deq[-1] if deq else -1)