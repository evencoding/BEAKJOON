from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
stuff = [0]
for _ in range(N):
    W, V = map(int, input().split())
    stuff.append((W, V))

DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    weight = stuff[i][0]
    value = stuff[i][1]
    for j in range(1, K+1):
        if j < weight:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-weight] + value)

print(DP[N][K])