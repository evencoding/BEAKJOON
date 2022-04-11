from sys import stdin
import math
input = stdin.readline

case = int(input())

for _ in range(case):
    H, W, N = map(int, input().split())

    dis = str(math.ceil(N / H))
    if int(dis) < 10: dis = '0'+dis

    floor = str((N-1) % H + 1)

    print(floor+dis, sep="")