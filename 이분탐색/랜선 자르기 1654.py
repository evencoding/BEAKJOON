from sys import stdin
input = stdin.readline

K, N = map(int, input().split())
wire = [int(input()) for _ in range(K)]
start, end = 1, max(wire)

while end >= start:
    mid = (start + end) // 2
    sum = 0
    for w in wire:
        if w >= mid:
            sum += w // mid
    if sum >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)