n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
ans = []
num = k-1
while arr:
    num %= len(arr)
    ans.append(str(arr[num]))
    arr.pop(num)
    num += k-1
print(f"<{', '.join(ans)}>")