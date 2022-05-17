n = int(input())
r, m = 31, 1234567891
s = input()
ans = 0

for i in range(n):
    ans += (ord(s[i])-96) * (r ** i)
print(ans%m)