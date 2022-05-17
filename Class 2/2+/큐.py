import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()
def push(num:int):
    queue.append(num)

def pop():
    print(queue.popleft() if queue else -1)

def size():
    print(len(queue))

def empty():
    print(0 if queue else 1)

def front():
    print(queue[0] if queue else -1)

def back():
    print(queue[-1] if queue else -1)

for _ in range(n):
    c = input().split()
    if c[0] == 'push': push(c[1])
    if c[0] == 'pop': pop()
    if c[0] == 'size': size()
    if c[0] == 'empty': empty()
    if c[0] == 'front': front()
    if c[0] == 'back': back()