N = int(input())

A, B, C = 0, 0, 0

A += N // 300
N = N % 300

B += N // 60
N = N % 60

C += N // 10

print(-1 if N % 10 else " ".join(map(str, [A, B, C])))