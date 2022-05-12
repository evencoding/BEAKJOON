import math
from sys import stdin
input = stdin.readline
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    cnt = 0
    if distance < 4:
        cnt = distance

    num = math.floor(math.sqrt(distance))
    num_square = num ** 2

    if distance == num_square:
        cnt = num * 2 - 1
    elif distance > num_square + num:
        cnt = num * 2 + 1
    else:
        cnt = num * 2
        
    print(cnt)