from sys import stdin
input = stdin.readline

N = int(input())
students = []
ranks = []
for _ in range(N):
    students.append(list(map(int, input().split())))

for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    ranks.append(str(rank))

print(" ".join(ranks))
            