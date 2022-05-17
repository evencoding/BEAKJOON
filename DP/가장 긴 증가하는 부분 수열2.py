from bisect import bisect_left
from sys import stdin
input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))
LIS = [nums[0]]
for i in range(1, n):
    if nums[i] > LIS[-1]:
        LIS.append(nums[i])
    else:
        LIS[bisect_left(LIS, nums[i])] = nums[i]
print(len(LIS))
