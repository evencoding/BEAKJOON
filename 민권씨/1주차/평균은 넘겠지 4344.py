from sys import stdin
input = stdin.readline

C = int(input())

for _ in range(C):
    arr = list(map(int, input().split()))
    aver = sum(arr[1:]) / arr[0]

    cnt = 0
    for s in arr[1:]:
        if s > aver:
            cnt += 1
    print(f'{cnt / arr[0] * 100:.3f}%')