from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for n in tree:
        if n > mid:
            sum += n - mid
    if M <= sum:
        start = mid + 1
    else:
        end = mid - 1

print(end)