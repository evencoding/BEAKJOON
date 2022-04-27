from sys import stdin
input = stdin.readline

N, C = map(int, input().split())
home = [int(input()) for _ in range(N)]
home.sort()

start = 1
end = home[-1] - home[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = home[0]
    for k in home[1:]:
        if k >= current + mid:
            cnt += 1
            current = k
    if cnt < C:
        end = mid - 1
    else:
        start = mid + 1

print(end)
