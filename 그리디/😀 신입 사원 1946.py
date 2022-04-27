from sys import stdin
input = stdin.readline

N = int(input())

for _ in range(N):
    people = sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x:x[0])
    cnt = 1
    end = people[0][1]
    for paper, interview in people[1:]:
        if interview < end:
            cnt += 1
            end = interview
    print(cnt)
    