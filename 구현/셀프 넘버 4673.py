arr = [True] * 10001
arr[0] = False

for i in range(10001):
    for j in str(i):
        i += int(j)
    if i < 10001:
        arr[i] = False

for i, n in enumerate(arr):
    if n:
        print(i)
