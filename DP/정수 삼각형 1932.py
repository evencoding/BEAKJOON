from sys import stdin
input = stdin.readline
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
    for j in range(len(dp[i])):
        if j > 0 and dp[i][j] >= dp[i][j-1] or j == 0:
            dp[i+1][j] += dp[i][j]
        if j < len(dp[i])-1 and dp[i][j] > dp[i][j+1] or j == len(dp[i])-1:
            dp[i+1][j+1] += dp[i][j]

print(max(dp[n-1]))



