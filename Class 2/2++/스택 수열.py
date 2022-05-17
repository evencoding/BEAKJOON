import sys
input = sys.stdin.readline
t = int(input())
stk, ans = [], []
cnt = 1
for _ in range(1, t+1):
    n = int(input())
    while n >= cnt:
        stk.append(cnt)
        ans.append('+')
        cnt += 1
    if stk[-1] == n:
        stk.pop()
        ans.append('-')
print("NO" if stk else '\n'.join(ans))