from sys import stdin
input = stdin.readline
n = int(input())
TP = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    day, pay = TP[i][0], TP[i][1]
    if i + day <= n:
        dp[i] = max(dp[i+1], pay + dp[i+day])
    else:
        dp[i] = dp[i+1]

print(dp[0])

