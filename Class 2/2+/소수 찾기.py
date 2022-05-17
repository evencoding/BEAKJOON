_ = input()
n = list(map(int, input().split()))
cnt = n.count(2) if 2 in n else 0

def prime(i):
    global cnt
    for j in range(2, i):
        if i % j == 0:
            return
    cnt += 1

for i in n:
    if i > 2:
        prime(i)

print(cnt)