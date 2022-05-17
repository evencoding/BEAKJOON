n, r, c = map(int, input().split())
cnt = 0
while n > 0:
    n = n-1
    # 1 사분면
    if r < (2**(n+1)) // 2 and c < (2**(n+1)) // 2:
        pass
    # 2 사분면
    if r < (2**(n+1)) // 2 and c >= (2**(n+1)) // 2:
        cnt += (2**n) * (2**n) * 1
        c = c - (2**n)
    # 3 사분면
    if r >= (2**(n+1)) // 2 and c < (2**(n+1)) // 2:
        cnt += (2**n) * (2**n) * 2
        r = r - (2**n)
    # 4 사분면
    if r >= (2**(n+1)) // 2 and c >= (2**(n+1)) // 2:
        cnt += (2**n) * (2**n) * 3
        r = r - (2**n)
        c = c - (2**n)
print(cnt)