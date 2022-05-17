n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] + [1] * n
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i]+1, dp[j])
print(max(dp))

max_idx = dp.index(max(dp))
nums = [arr[max_idx]]
cur = max_idx
for i in range(max_idx-1, 0, -1):
    if dp[i] == dp[cur]-1 and arr[i] < arr[cur]:
        nums.append(arr[i])
        cur = i
print(*nums[::-1])