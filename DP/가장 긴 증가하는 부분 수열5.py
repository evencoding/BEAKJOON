from bisect import bisect_left
from sys import stdin
input = stdin.readline
n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
LIS = [-1000000001]
for i in range(1, n+1):
    if nums[i] > LIS[-1]:
        LIS.append(nums[i])
        dp[i] = len(LIS)-1
    else:
        dp[i] = bisect_left(LIS, nums[i])
        LIS[dp[i]] = nums[i]
print(len(LIS)-1)

max_idx = dp.index(max(dp))
ans = [nums[max_idx]]
cur = max_idx
for i in range(max_idx-1, 0, -1):
    if dp[i] == dp[cur]-1 and nums[i] < nums[cur]:
        ans.append(nums[i])
        cur = i
print(*ans[::-1])

# max_idx = max(dp)+1
# ans = []
# for i in range(n, 0, -1):
#     if dp[i] == max_idx-1:
#         ans.append(nums[i])
#         max_idx = dp[i]
# print(*ans[::-1])