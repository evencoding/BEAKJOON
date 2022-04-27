from sys import stdin
input = stdin.readline

N = int(input())
meeting = []
for _ in range(N):
    a, b = map(int, input().split())
    meeting.append((a, b))

meeting.sort(key=lambda x:(x[1], x[0]))

cnt = 1
end_time = meeting[0][1]
for i in range(1, N):
    if meeting[i][0] >= end_time:
        cnt += 1
        end_time = meeting[i][1]

print(cnt)