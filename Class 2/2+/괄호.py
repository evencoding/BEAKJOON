import sys
input = sys.stdin.readline
T = int(input())

def check(s, l, r):
    for c in s:
        if c == '(':
            l += 1
        else:
            r += 1
        if r > l: return 0
    if l == r: return 1
    else: return 0

for _ in range(T):
    s = input().rstrip()
    l_bracket = 0
    r_bracket = 0
    print('YES' if check(s, l_bracket, r_bracket) else 'NO')