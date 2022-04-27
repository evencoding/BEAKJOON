from sys import stdin
from collections import Counter
input = stdin.readline

_ = input()
N = input().split()
_ = input()
M = input().split()

cnt = Counter(N)
print(' '.join(f'{cnt[m]}' if m in cnt else '0' for m in M))